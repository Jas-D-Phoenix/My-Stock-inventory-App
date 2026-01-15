# Stock Inventory Management System

A robust and scalable Django-based web application for managing stock inventory with user authentication, CRUD operations, and a responsive Bootstrap interface. Built with modern web technologies and deployed on Railway.

## 🚀 Live Demo

[Add your Railway deployment URL here after deployment]

## ✨ Features

- **User Authentication**: Secure registration, login, and logout functionality
- **Stock Management**: Full CRUD operations (Create, Read, Update, Delete) for stock items
- **Category Organization**: Organize stocks by categories (Grains, Seeds, Consultancy, etc.)
- **Purchase & Sales Tracking**: Record purchases and sales with detailed transaction history
- **Reorder Level Alerts**: Set and monitor reorder levels for inventory management
- **CSV Export**: Export stock data to CSV for reporting and analysis
- **Stock Details**: Comprehensive view of stock information and transaction history
- **Responsive Design**: Bootstrap 5 UI that works on desktop, tablet, and mobile
- **Production Ready**: Configured for deployment on Railway with PostgreSQL

## 🛠️ Technologies Used

- **Backend**: Django 5.0.6
- **Database**: PostgreSQL (Production), MySQL (Development)
- **Frontend**: Bootstrap 5, jQuery, HTML5, CSS3
- **Deployment**: Railway, Gunicorn, WhiteNoise
- **Other**: Django Crispy Forms, Python Decouple

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL (for production) or MySQL (for local development)
- Git
- Railway account (for deployment)

## 🚀 Getting Started

### Local Development Setup

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
   - Update database credentials in `stock_inventory/settings.py` or create a `.env` file:
     ```env
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     DB_NAME=stock_inventory
     DB_USER=root
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=3306
     ```

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

7. **Seed demo data (optional):**
   ```bash
   python manage.py seed_data
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - Main app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Demo Account

After running `python manage.py seed_data`, you can use these credentials:
- **Username**: demo
- **Password**: password123

This account comes with sample categories and stocks pre-loaded.

## 🗄️ Database

- **Development**: MySQL (configurable in settings.py)
- **Production**: PostgreSQL (configured for Railway)

The app automatically detects `DATABASE_URL` environment variable for PostgreSQL in production.

## 🧪 Testing

Run the Django test suite:
```bash
python manage.py test
```

## 🚢 Deployment

This app is configured for deployment on [Railway](https://railway.app).

### Railway Deployment Steps

1. **Connect your GitHub repository to Railway**
2. **Add a PostgreSQL database service**
3. **Add environment variables:**
   - `SECRET_KEY` - Your Django secret key (from `SECRET_KEY.txt`)
   - `DEBUG=False` - Set to False for production
   - `ALLOWED_HOSTS` - Your Railway domain (automatically handled)
4. **Railway will automatically:**
   - Install dependencies
   - Run migrations
   - Start the server with Gunicorn

See [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md) for detailed deployment instructions.

## 📁 Project Structure

```
My-Stock-inventory-App/
├── stock_inventory/          # Main Django project
│   ├── stock_inventory/      # Project settings
│   │   ├── settings.py      # Django settings
│   │   ├── urls.py          # URL configuration
│   │   └── wsgi.py          # WSGI configuration
│   ├── stock_app/           # Main application
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View functions
│   │   ├── forms.py         # Form definitions
│   │   ├── templates/       # HTML templates
│   │   ├── static/          # Static files (CSS, JS, images)
│   │   └── management/      # Management commands
│   │       └── commands/
│   │           └── seed_data.py
│   └── manage.py
├── requirements.txt
├── Procfile                 # Railway deployment config
├── railway.json             # Railway configuration
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose config
└── README.md
```

## 🔐 Security Features

- User authentication with Django's built-in auth system
- Password hashing and validation
- CSRF protection
- Secure session management
- Production security settings (SSL, HSTS, etc.)

## 📝 API Endpoints

- `/` - Home page (requires login)
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/add_stock/` - Add new stock item
- `/stock_list/` - View all stock items
- `/stock_info/<id>/` - View specific stock details
- `/update_stock/<id>/` - Update stock item
- `/delete_stock/<id>/` - Delete stock item
- `/stock_details/` - View stock transaction history
- `/admin/` - Django admin panel

## 🎯 Key Features Explained

### Stock Management
- Add new stock items with category, quantity, and reorder levels
- Update existing stock information
- Delete stock items
- Search and filter stocks by category and name

### Purchase & Sales
- Record stock purchases with supplier information
- Record stock sales with customer details
- Automatic quantity updates on purchase/sale
- Transaction history tracking

### Reports & Export
- View detailed stock information
- Filter stock details by date range
- Export stock data to CSV format

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Miriam Musa / Jas-D-Phoenix**
- GitHub: [@Jas-D-Phoenix](https://github.com/Jas-D-Phoenix)
- Project Link: [https://github.com/Jas-D-Phoenix/My-Stock-inventory-App](https://github.com/Jas-D-Phoenix/My-Stock-inventory-App)

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Styled with [Bootstrap](https://getbootstrap.com/)
- Deployed on [Railway](https://railway.app)
- Icons and UI components from Bootstrap Icons

## 📞 Support

For support, email support@example.com or open an issue in the GitHub repository.
