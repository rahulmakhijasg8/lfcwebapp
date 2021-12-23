from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_nested import routers
from pprint import pprint

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('carts',views.CartViewSet)

products_router = routers.NestedDefaultRouter(router,'products',lookup = 'products')
products_router.register('reviews',views.ReviewsViewSet,basename='product-reviews')

carts_router= routers.NestedDefaultRouter(router, 'carts', lookup = 'cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', views.home, name = 'home'),
    path('store/', views.store, name = 'store'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('articles', views.articles, name = 'articles'),
    path('fixtures', views.fixtures, name = 'fixtures'),
    path('update_item/', views.updateitem, name = 'updateitem'),
    path('process_order/', views.processOrder, name='processOrder'),
    path('',include(router.urls)),
    path('',include(products_router.urls)),
    path('<int:pk>/',include(router.urls)),
    path('',include(carts_router.urls)),

]