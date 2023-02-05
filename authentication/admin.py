from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, nav_settings, nav_settingsAdmin

admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.register(nav_settings, nav_settingsAdmin)
