from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, delete_from_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<product_id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<cart_line_item_id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
]
