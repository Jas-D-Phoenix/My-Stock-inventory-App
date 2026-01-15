# Railway Deployment Guide

This guide will help you deploy the Django Stock Inventory App to Railway.

## Prerequisites

1. A Railway account (sign up at https://railway.app)
2. GitHub account (your code should be on GitHub)

## Deployment Steps

### 1. Connect Your Repository to Railway

1. Log in to Railway (https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Authorize Railway to access your GitHub account
5. Select the `My-Stock-inventory-App` repository

### 2. Add PostgreSQL Database

1. In your Railway project, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway will automatically create a PostgreSQL database
4. The `DATABASE_URL` environment variable will be automatically set

### 3. Configure Environment Variables

Railway will automatically detect and use:
- `DATABASE_URL` (automatically set by PostgreSQL service)
- `PORT` (automatically set)
- `RAILWAY_ENVIRONMENT` (automatically set)

**Required environment variables to add:**
- `SECRET_KEY` - Your Django secret key (from `SECRET_KEY.txt`)
- `DEBUG=False` - Set to False for production
- `ALLOWED_HOSTS` - Your Railway domain (Railway sets this automatically, but you can add `.railway.app`)

### 4. Deploy

1. Railway will automatically detect the Django app
2. It will run:
   - `pip install -r requirements.txt` (installs dependencies including PostgreSQL adapter)
   - `python manage.py migrate` (runs migrations via the release command in Procfile)
   - `gunicorn stock_inventory.wsgi:application --bind 0.0.0.0:$PORT` (starts the server)

### 5. Seed Demo Data (Optional)

After deployment, you can seed the database with demo data:

1. Go to your Railway project dashboard
2. Click on your service
3. Open the "Deploy Logs" or use the Railway CLI
4. Run: `python manage.py seed_data`

Or create a superuser:
```bash
python manage.py createsuperuser
```

### 6. Access Your App

1. Once deployed, Railway will provide you with a public URL
2. Visit the URL to access your app
3. Register a new account or use the demo account (if seeded):
   - Username: `demo`
   - Password: `password123`

## Important Notes

- The app uses PostgreSQL in production (configured in `settings.py`)
- MySQL is used for local development
- Authentication is required to access all features
- Static files are served using WhiteNoise
- The app automatically runs migrations on deployment

## Troubleshooting

If you encounter issues:

1. **Database connection errors**: Ensure PostgreSQL service is added and connected
2. **Migration errors**: Check the Railway logs for migration output
3. **Static files not loading**: WhiteNoise is configured to serve static files
4. **Port binding**: The app uses `$PORT` environment variable (Railway sets this automatically)
5. **Secret key errors**: Make sure `SECRET_KEY` environment variable is set

## Local Development

To run locally (requires Python 3.11+):

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up MySQL database (or use SQLite for simplicity)
# Update settings.py or create .env file

# Run migrations
cd stock_inventory
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Seed demo data (optional)
python manage.py seed_data

# Run server
python manage.py runserver
```

Visit http://localhost:8000
