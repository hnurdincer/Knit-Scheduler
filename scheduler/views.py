from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Order
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    products = Product.objects.all()
    return render(request, 'scheduler/home.html', {'products': products})

def calendar_view(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id) if product_id else None
    return render(request, 'scheduler/calendar.html', {'product': product})

def get_booked_days(request):
    from django.db.models import Count
    orders_by_date = Order.objects.values('date').annotate(count=Count('id'))
    data = []
    for entry in orders_by_date:
        products = list(Order.objects.filter(date=entry['date']).values_list('product__name', flat=True))
        data.append({
            'date': entry['date'].strftime('%Y-%m-%d'),
            'count': entry['count'],
            'product_names': products
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def book_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = get_object_or_404(Product, id=data.get('product_id'))
            date_str = data.get('date')
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            if Order.objects.filter(date=date_obj).count() >= 2:
                return JsonResponse({'status': 'error', 'message': 'Bu günün kontenjanı (2 sipariş) dolmuştur!'}, status=400)
                
            Order.objects.create(
                product=product,
                date=date_obj,
                contact_type=data.get('contact_type'),
                contact_handle=data.get('contact_handle'),
                client_identifier=data.get('client_identifier')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Geçersiz istek'}, status=400)
