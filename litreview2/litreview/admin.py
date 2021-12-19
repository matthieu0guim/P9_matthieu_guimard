from django.contrib import admin

from authentication.models import User
from litreview.models import Ticket, Review

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'id')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'answered')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'rating', 'ticket')

admin.site.register(User, UserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
