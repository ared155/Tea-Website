from django.urls import path,re_path
# from django.conf.urls import urls
from . import views

app_name='shop'

urlpatterns = [
    path('<str:title>/',views.product,name="product_list"),
    path('', views.categories_list,name="categories"),
    path('<str:title>/<slug:slug>/',views.product_detail,name="product_detail")
    # re_path(r'^(?P<slug>[\w-]+)/$',views.product_detail,name="product_detail"),
    # re_path(r'^(?P<slug>[\w-]+)/$',views.recipe_detail,name="recipe_detail"),
    # re_path(r'^(?P<title>[\w-]+\s[\w.-]+)/$',views.product_list,name="product_list")
] 