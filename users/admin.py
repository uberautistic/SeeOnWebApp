from django.contrib import admin
from .models import User, UserActivityLog, Watchlist, Preference, Recomendations

# Register your models here.

admin.site.register(User)
admin.site.register(UserActivityLog)
admin.site.register(Watchlist)
admin.site.register(Preference)
admin.site.register(Recomendations)
