from django.contrib.auth.admin import UserAdmin
from thisapp.models import User


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User

    list_display = ('email', 'first_name', 'last_name',
                    'telephone', 'date', 'is_admin', 'is_active',)

    list_filter = ('email', 'date', 'is_admin', 'is_active',)

    fieldsets = (
        (None, {'fields': ('first_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_active')}
         ),
    )

    search_fields = ('email', 'date', )
    ordering = ('email', 'date', )
