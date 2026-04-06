import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from scheduler.models import Product

def seed():
    products = [
        {
            'name': 'El Örgüsü Kazak',
            'image': 'products/sweater.png',
            'description': 'Yumuşacık, %100 yün iplerle örülmüş, kış ayları için ideal sıcak tutan tasarım kazak.'
        },
        {
            'name': 'Renkli Atkı & Bere Seti',
            'image': 'products/collection.png',
            'description': 'Canlı renklerle örülmüş, hem şık hem de koruyucu atkı ve bere takımı.'
        },
        {
            'name': 'Amigurumi Ayıcık',
            'image': 'products/collection.png',
            'description': 'Çocuklar için güvenli, uyku arkadaşı olabilecek el yapımı amigurumi ayıcık.'
        },
        {
            'name': 'Bebek Battaniyesi',
            'image': 'products/collection.png',
            'description': 'Hipoalerjenik iplerle, sevgiyle örülmüş yumuşak bebek battaniyesi.'
        }
    ]
    
    for p_data in products:
        Product.objects.get_or_create(
            name=p_data['name'],
            defaults={'image': p_data['image'], 'description': p_data['description']}
        )
    print("Seed data created successfully.")

if __name__ == '__main__':
    seed()
