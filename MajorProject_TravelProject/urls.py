"""from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('mood/', views.mood, name='mood'),
    path('explore/',views.explore,name='explore'),
    path('login/',views.login,name='login'),
    path('gallery/',views.gallery,name='gallery'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('bookings/',views.bookings,name='bookings'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('map/',views.map,name='map'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),

]"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
