from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
                  path('user-signup/', views.Signup, name='user_signup'),
                  path('user-login/', views.Login, name='user_login'),
                  path('profile/', views.Profile, name='profile'),
                  path('logout/', views.logout_user, name='logout')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
