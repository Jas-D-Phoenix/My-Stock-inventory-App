# Stock Inventory Management System

A Django-based web application for managing stock inventory with user authentication, CRUD operations, and a responsive Bootstrap interface.

## Features

- User authentication (register/login/logout)
- Stock item management (Create, Read, Update, Delete)
- Stock details tracking
- Responsive Bootstrap 5 UI
- MySQL database support
- Production-ready deployment configurations

## Tech Stack

- **Backend**: Django 5.0.6
- **Database**: MySQL
- **Frontend**: Bootstrap 5, jQuery
- **Deployment**: Docker, Gunicorn, WhiteNoise

## Local Development Setup

### Prerequisites

- Python 3.11+
- MySQL Server
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jas-D-Phoenix/My-Stock-inventory-App.git
   cd My-Stock-inventory-App
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Create a MySQL database named `stock_inventory`
   - Update database credentials in `stock_inventory/settings.py` or create a `.env` file

5. **Run migrations:**
   ```bash
   cd stock_inventory
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Main app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Production Deployment

### Option 1: Docker Compose (Recommended)

1. **Clone and navigate to the project:**
   ```bash
   git clone https://github.com/Jas-D-Phoenix/My-Stock-inventory-App.git
   cd My-Stock-inventory-App
   ```

2. **Create environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your production values
   ```

3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up -d --build
   ```

4. **Run database migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

The application will be available at http://localhost:8000

### Option 2: Manual Deployment

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   Create a `.env` file with production settings

3. **Run migrations and collect static files:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

4. **Run with Gunicorn:**
   ```bash
   gunicorn stock_inventory.wsgi:application --bind 0.0.0.0:8000
   ```

### Environment Variables

Create a `.env` file in the project root:

```env
# Django settings
SECRET_KEY=your-very-long-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database settings
DB_NAME=stock_inventory
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

## Project Structure

```
My-Stock-inventory-App/
├── stock_inventory/          # Main Django project
│   ├── stock_inventory/      # Project settings
│   ├── stock_app/           # Main application
│   ├── manage.py
│   └── db.sqlite3
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .dockerignore
└── README.md
```

## API Endpoints

- `/` - Home page
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/add_stock/` - Add new stock item
- `/stock_info/` - View all stock items
- `/stock_details/<id>/` - View specific stock details
- `/update_stock/<id>/` - Update stock item
- `/delete_stock/<id>/` - Delete stock item
- `/admin/` - Django admin panel

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Author

**Miriam Musa**
- GitHub: [@Jas-D-Phoenix](https://github.com/Jas-D-Phoenix)
