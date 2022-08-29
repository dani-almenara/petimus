from django.contrib import admin
from .models import PetimusType, Petimus, Image, Comment, Notification

# admin.site.register(PetimusType)
@admin.register(PetimusType)
class PetimusTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    ordering = ('description',)


admin.site.register(Petimus)

admin.site.register(Image)

admin.site.register(Comment)

admin.site.register(Notification)