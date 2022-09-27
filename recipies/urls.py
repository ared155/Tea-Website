from django.urls import path,re_path
# from django.conf.urls import urls
from . import views

app_name='recipes'

urlpatterns = [
    path('', views.recipe_list,name="recipe_list"),
    # re_path(r'^(?P<slug>[\w-]+)/$',views.recipe_detail,name="recipe_detail"),
    path('<slug:slug>/',views.recipe_detail,name="recipe_detail")
] 