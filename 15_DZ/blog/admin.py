from django.contrib import admin
from .models import Post

@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
      list_display = ('title', 'created_at')
      search_fields = ('title', 'created_at')

# Register your models here.