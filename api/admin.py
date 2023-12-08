from django.contrib import admin

# Register your models here.


from api.models import Task
# Register your models here..

# class TaskAdmin(admin.ModelAdmin):
#     list_display=( "title","description","due_date","status" )
#     search_fields=('title',)   
     

admin.site.register(Task)

