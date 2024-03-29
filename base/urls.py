from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),

    # authentications
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

    path('profile/',views.profile,name='profile'),
    path('post/<int:post_id>/like_comment',views.like_comment,name='post_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
regex in url is better , more efficient ! gott learn
'''
