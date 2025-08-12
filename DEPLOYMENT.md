# Vercel Deployment Guide

## Prerequisites

1. **GitHub Repository**: Ensure your code is pushed to a GitHub repository
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **External PostgreSQL Database**: Vercel doesn't provide PostgreSQL, you'll need:
   - [Supabase](https://supabase.com) (recommended, free tier available)
   - [Neon](https://neon.tech) (PostgreSQL-compatible, free tier)
   - [Railway](https://railway.app) (PostgreSQL hosting)
   - [AWS RDS](https://aws.amazon.com/rds/) (production-grade)

## Environment Variables Setup

In your Vercel project dashboard, add these environment variables:

```bash
# Database Configuration
DATABASE_URL=postgresql://username:password@host:5432/database_name
TEST_DATABASE_URL=postgresql://username:password@host:5432/test_database_name

# Google AI API Key (for LangChain integration)
GOOGLE_API_KEY=your_google_api_key_here

# JWT Secret Key (generate a secure random string)
SECRET_KEY=your_super_secret_jwt_key_here

# Environment
ENVIRONMENT=production

# Vercel Environment (automatically set by Vercel)
VERCEL=1
```

## Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### 2. Connect to Vercel
1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect it as a Python project

### 3. Configure Build Settings
- **Framework Preset**: Other
- **Build Command**: Leave empty (Vercel will use requirements.txt)
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### 4. Add Environment Variables
In the Vercel dashboard:
1. Go to Project Settings → Environment Variables
2. Add all the variables listed above
3. Make sure to set them for Production, Preview, and Development

### 5. Deploy
Click "Deploy" - Vercel will:
1. Install dependencies from `requirements.txt`
2. Build your FastAPI application
3. Deploy using the `index.py` entry point

## Database Setup

### Option 1: Supabase (Recommended)
1. Create account at [supabase.com](https://supabase.com)
2. Create new project
3. Go to Settings → Database
4. Copy the connection string
5. Add to Vercel as `DATABASE_URL`

### Option 2: Neon
1. Create account at [neon.tech](https://neon.tech)
2. Create new project
3. Copy the connection string
4. Add to Vercel as `DATABASE_URL`

## Google AI API Key Setup
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create new API key
3. Add to Vercel as `GOOGLE_API_KEY`

## CORS Configuration
The app is configured to allow:
- `http://localhost:5173` (local development)
- `http://127.0.0.1:5173` (local development)

For production, update the CORS origins in `app/main.py`:
```python
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://your-frontend-domain.vercel.app",  # Add your frontend URL
    # Add other allowed origins here
]
```

## Testing Deployment

After deployment, test these endpoints:
- `https://your-app.vercel.app/` - Should return welcome message
- `https://your-app.vercel.app/docs` - FastAPI documentation
- `https://your-app.vercel.app/welcome` - Additional test endpoint

## Troubleshooting

### Common Issues:

1. **Database Connection Errors**
   - Verify `DATABASE_URL` is correct
   - Ensure database allows external connections
   - Check if database requires SSL (add `?sslmode=require` to URL)

2. **Import Errors**
   - Verify all dependencies are in `requirements.txt`
   - Check Python path configuration in `vercel.json`

3. **Environment Variable Issues**
   - Ensure all required env vars are set in Vercel dashboard
   - Check variable names match exactly

4. **Timeout Issues**
   - AI operations might take time, consider increasing function timeout
   - Current max duration is set to 30 seconds in `vercel.json`

## Database Migration

Since Vercel is serverless, database migrations should be handled separately:

1. **Local Migration** (before deployment):
   ```bash
   alembic upgrade head
   ```

2. **Production Migration**:
   - Run migrations from your local machine pointing to production DB
   - Or use a separate migration service/script

## Monitoring

- Check Vercel Function logs in the dashboard
- Monitor database connections and performance
- Set up Sentry for error tracking (already configured in dependencies)

## Security Notes

- Never commit `.env` files to Git (already in `.gitignore`)
- Use strong, unique `SECRET_KEY`
- Regularly rotate API keys
- Enable database connection encryption
- Consider rate limiting for production use
