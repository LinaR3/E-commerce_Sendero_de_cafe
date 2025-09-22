from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load sample data for Sendero de Café'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {
                'name': 'Café Arábica Premium',
                'slug': 'arabica-premium',
                'description': 'Los mejores granos de café arábica, cultivados en las mejores fincas de Colombia.'
            },
            {
                'name': 'Café Especial de Origen',
                'slug': 'especial-origen',
                'description': 'Cafés de origen único con sabores distintivos de cada región.'
            },
            {
                'name': 'Mezclas Artesanales',
                'slug': 'mezclas-artesanales',
                'description': 'Cuidadosas mezclas creadas por nuestros maestros tostadores.'
            },
            {
                'name': 'Café Descafeinado',
                'slug': 'descafeinado',
                'description': 'Todo el sabor del café sin la cafeína, perfecto para cualquier momento.'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'name': 'Café Huila Premium',
                'slug': 'cafe-huila-premium',
                'description': 'Exquisito café arábica del departamento del Huila, con notas florales y frutales. Cultivado a 1800 metros de altura en suelos volcánicos que le otorgan su sabor único.',
                'category': 'arabica-premium',
                'coffee_type': 'arabica',
                'roast_level': 'medium',
                'origin': 'Huila, Colombia',
                'weight': 250,
                'price': 28000,
                'stock': 50
            },
            {
                'name': 'Café Nariño Especial',
                'slug': 'cafe-narino-especial',
                'description': 'Café de altura de Nariño con cuerpo intenso y acidez balanceada. Perfecto para los amantes del café con carácter.',
                'category': 'especial-origen',
                'coffee_type': 'arabica',
                'roast_level': 'dark',
                'origin': 'Nariño, Colombia',
                'weight': 250,
                'price': 32000,
                'stock': 30
            },
            {
                'name': 'Mezcla de la Casa',
                'slug': 'mezcla-casa',
                'description': 'Nuestra mezcla insignia que combina los mejores granos de diferentes regiones colombianas. Un equilibrio perfecto entre sabor y aroma.',
                'category': 'mezclas-artesanales',
                'coffee_type': 'blend',
                'roast_level': 'medium',
                'origin': 'Colombia',
                'weight': 250,
                'price': 25000,
                'stock': 75
            },
            {
                'name': 'Café Eje Cafetero',
                'slug': 'cafe-eje-cafetero',
                'description': 'Tradicional café del Eje Cafetero con sabor suave y aroma intenso. Ideal para preparaciones en prensa francesa.',
                'category': 'arabica-premium',
                'coffee_type': 'arabica',
                'roast_level': 'light',
                'origin': 'Eje Cafetero, Colombia',
                'weight': 250,
                'price': 30000,
                'stock': 40
            },
            {
                'name': 'Café Santander Tostado Oscuro',
                'slug': 'cafe-santander-oscuro',
                'description': 'Café de Santander con tostado oscuro, perfecto para espresso. Notas de chocolate y nueces.',
                'category': 'especial-origen',
                'coffee_type': 'arabica',
                'roast_level': 'dark',
                'origin': 'Santander, Colombia',
                'weight': 250,
                'price': 29000,
                'stock': 25
            },
            {
                'name': 'Descafeinado Suave',
                'slug': 'descafeinado-suave',
                'description': 'Café descafeinado procesado naturalmente, conservando todo el sabor original. Perfecto para disfrutar en cualquier momento del día.',
                'category': 'descafeinado',
                'coffee_type': 'arabica',
                'roast_level': 'medium',
                'origin': 'Valle del Cauca, Colombia',
                'weight': 250,
                'price': 26000,
                'stock': 35
            }
        ]

        for product_data in products_data:
            category_slug = product_data.pop('category')
            product_data['category'] = categories[category_slug]
            product_data['available'] = True
            
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))