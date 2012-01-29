
from django.contrib import admin
import mikroblog.models as M

class PostAdmin(admin.ModelAdmin):
    list_display = ('text','pub_date')
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        user = kwargs['request'].user
        if db_field.name == "author":
            kwargs['initial'] = user
        elif db_field.name == "place":
            if user.get_profile().default_place != None:
                kwargs['initial'] = user.get_profile().default_place
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(M.Post, PostAdmin)
