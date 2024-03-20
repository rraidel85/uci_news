from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
        
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'phone_number', 'street', 'number', 'zone', 'category', 'is_staff']
    list_filter = ['username', 'email', 'phone_number', 'street', 'number', 'zone', 'category', 'is_staff']
    
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Información adicional',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'phone_number',
                    'street',
                    'number',
                    'zone',
                    'category',
                    'experience'
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)