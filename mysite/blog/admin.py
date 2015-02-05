import models
from django.contrib import admin


#class UserAdmin(admin.ModelAdmin):
#    list_display = ('id' , 'name', 'age')
    

#class PostAdmin(admin.ModelAdmin):
#    list_display = ('title' , 'author', 'id')
#    search_fields = ('title', 'author')
    #list_filter = ('name',)
    #date_hierarchy = 'name'



#admin.site.register(models.User , UserAdmin)
#admin.site.register(models.Post , PostAdmin)
admin.site.register(models.User )
admin.site.register(models.Article )
admin.site.register(models.FAQ)