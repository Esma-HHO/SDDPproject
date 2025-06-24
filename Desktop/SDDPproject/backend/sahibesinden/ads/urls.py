from django.urls import path
from . import views



urlpatterns = [
    #path('ads', views.ad_list,name="ad_list"),
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('houses/', views.house_list, name='house_list'),
    path('furniture/', views.furniture_list, name='furniture_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_house/', views.add_house, name='add_house'),
    path('add_furniture/', views.add_furniture, name='add_furniture'),
    path('cars/<int:car_id>/like/', views.like_car, name='like_car'),
    path('houses/<int:house_id>/like/', views.like_house, name='like_house'),
    path('furniture/<int:furniture_id>/like/', views.like_furniture, name='like_furniture'),
    path('car/delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('house/delete/<int:house_id>/', views.delete_house, name='delete_house'),
    path('furniture/delete/<int:furniture_id>/', views.delete_furniture, name='delete_furniture'),
    path('send/<str:model_name>/<int:object_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('reply/<int:receiver_id>/', views.reply_message, name='reply_message'),
    path('<str:model_name>/<int:id>/', views.listing_detail, name='listing_detail'),
    path('<str:model_name>/<int:id>/detail/', views.show_listing_detail, name='show_listing_detail'),
    
    


]
