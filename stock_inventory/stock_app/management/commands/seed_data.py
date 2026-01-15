from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from stock_app.models import Category, Stock


class Command(BaseCommand):
    help = 'Seed the database with demo data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        Stock.objects.all().delete()
        Category.objects.all().delete()

        # Create demo user if it doesn't exist
        demo_user, created = User.objects.get_or_create(
            username='demo',
            defaults={
                'email': 'demo@example.com',
                'first_name': 'Demo',
                'last_name': 'User'
            }
        )
        if created:
            demo_user.set_password('password123')
            demo_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created demo user: {demo_user.username}'))
        else:
            self.stdout.write(f'Demo user already exists: {demo_user.username}')

        # Create categories
        self.stdout.write('Creating categories...')
        categories_data = [
            'Grains',
            'Seeds',
            'Consultancy',
            'Fertilizers',
            'Tools'
        ]

        categories = {}
        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(category_name=cat_name)
            categories[cat_name] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat_name}'))

        # Create sample stocks
        self.stdout.write('Creating sample stocks...')
        stocks_data = [
            {
                'category': categories['Grains'],
                'stock_name': 'Wheat',
                'quantity': 500,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier A',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 100
            },
            {
                'category': categories['Grains'],
                'stock_name': 'Rice',
                'quantity': 300,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier B',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 80
            },
            {
                'category': categories['Seeds'],
                'stock_name': 'Corn Seeds',
                'quantity': 200,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier C',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 50
            },
            {
                'category': categories['Seeds'],
                'stock_name': 'Bean Seeds',
                'quantity': 150,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier A',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 40
            },
            {
                'category': categories['Fertilizers'],
                'stock_name': 'NPK Fertilizer',
                'quantity': 100,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier D',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 30
            },
            {
                'category': categories['Tools'],
                'stock_name': 'Garden Hoe',
                'quantity': 75,
                'quantity_purchased': 0,
                'purchased_by': 'Supplier E',
                'quantity_sold': 0,
                'sold_by': '',
                'sold_to': '',
                'reorder_level': 20
            }
        ]

        for stock_data in stocks_data:
            stock, created = Stock.objects.get_or_create(
                stock_name=stock_data['stock_name'],
                defaults=stock_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created stock: {stock.stock_name}'))

        self.stdout.write(self.style.SUCCESS('\nSeed data created successfully!'))
        self.stdout.write('\nDemo user credentials:')
        self.stdout.write('  Username: demo')
        self.stdout.write('  Password: password123')
        self.stdout.write(f'\nTotal categories: {Category.objects.count()}')
        self.stdout.write(f'Total stocks: {Stock.objects.count()}')
