import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render

from .details import *
from .models import *
from .tv import get_tv
from .utils import cookie

movie = Movie()


# Create your views here.
def home(request):
    mtotal = cart_total(request)
    pop_movies = popular_movies(request)
    tv = get_tv(request)

    print('tv:', tv)

    context = {'popular': pop_movies,
               'mtotal': mtotal,
               'tv': tv

               }
    return render(request, 'movies/home.html', context)


def search(request):
    context = {}
    return render(request, 'movies/search.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()

    else:
        cookieData = cookie(request)
        items = cookieData['items']
        order = cookieData['order']

    m_total = cart_total(request)
    price_total = m_total * 40

    context = {'items': items,
               'order': order,
               'mtotal': m_total,
               'price': price_total
               }
    return render(request, 'movies/cart.html', context)


def details(request, pk):
    moovy = movie_details(request, pk)
    reviews = moovy.get('reviews')
    recommendations = get_recommendations(request, pk)


    context = {'moovy': moovy,
               'reviews': reviews,
               'reccs': recommendations,
               }
    return render(request, 'movies/details.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()

    else:
        cookieData = cookie(request)
        items = cookieData['items']
        order = cookieData['order']
    m_total = len(items)
    price_total = m_total * 40

    vendors = Vendor.objects.all()

    context = {'items': items,
               'order': order,
               'mtotal': m_total,
               'price': price_total,
               'vendors': vendors
               }
    return render(request, 'movies/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    movie_id = data['movieId']
    action = data['action']
    print('action:', action)
    print('movie:', movie_id)

    m = movie.details(movie_id)

    customer = request.user.customer
    movie_title = m.title
    year = m.release_date

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    if action == 'add':
        orderItem, created = OrderItem.objects.get_or_create(order=order, year=year, movie=movie_title)
        orderItem.save()
    else:
        orderItem, created = OrderItem.objects.get_or_create(order=order, year=year, movie=movie_title)
        orderItem.delete()

    print(movie_title)

    return JsonResponse(['hello', 'hi'], safe=False)


def cart_total(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()

    else:
        try:
            kart = json.loads(request.COOKIES['cart'])

        except:
            kart = []

        if not kart:
            items = []

        else:
            items = json.loads(request.COOKIES['cart'])

        order = []
    m_total = len(items)

    return m_total


def remove_item(request):
    data = json.loads(request.body)
    movie_title = data['movieId']

    customer = request.user.customer

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, movie=movie_title)
    orderItem.delete()

    return JsonResponse(['deleted', movie_title], safe=False)


def process_order(request):
    txn_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    vendor_chsn = data['order']['vendor']
    vendors = Vendor.objects.all()

    for v in vendors:

        if vendor_chsn == v.name:
            vendor = v.vendor.vendor

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.txn_id = txn_id
        order.vendor = vendor

        order.location = 'mombasa'
        order.town = 'likoni'
        order.complete = True

        order.save()
    else:
        town = data['order']['town']
        name = data['order']['name']
        location = data['order']['location']
        email = data['order']['email']
        cookieData = cookie(request)
        items = cookieData['items']
        customer, created = Customer.objects.get_or_create(email=email)
        customer.name = name
        customer.save()
        order = Order.objects.create(customer=customer,
                                     town=town,
                                     vendor=vendor,
                                     location=location,
                                     complete=False)
        for i in items:
            movie = i['movie']
            year = i['year']

            orderItem = OrderItem.objects.create(
                movie=movie,
                year=year,
                order=order
            )

        order.complete = True

        order.save()

    print(request.body)

    return JsonResponse(['payment complete'], safe=False, )
