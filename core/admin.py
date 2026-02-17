from django.contrib import admin
from core.models import Comment
# # from unfold.admin import ModelAdmin as unfoldModelAdmin

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
# from django.contrib.auth.models import User, Group

# from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
# from unfold.admin import ModelAdmin

# # Register your models here.

# admin.site.site_header = "Hello"
#     # "SITE_SUBHEADER": "Hello",

@admin.register(Comment)
# class CommeentAdmin(ModelAdmin):
class CommeentAdmin(admin.ModelAdmin):
    list_display=['id','message']
# admin.site.unregister(User)
# admin.site.unregister(Group)


# @admin.register(User)
# class UserAdmin(BaseUserAdmin, ModelAdmin):
#     # Forms loaded from `unfold.forms`
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm


# @admin.register(Group)
# class GroupAdmin(BaseGroupAdmin, ModelAdmin):
#     pass