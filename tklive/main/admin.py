from django.contrib import admin
import main.models as M

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(M.UserProfile, UserProfileAdmin)
