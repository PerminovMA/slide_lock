from django.contrib import admin
from .models import UserProfile, City, Country, Token, Error, VKImageCategory, VKAlbum

admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Token)
admin.site.register(Error)
admin.site.register(VKImageCategory)
admin.site.register(VKAlbum)
