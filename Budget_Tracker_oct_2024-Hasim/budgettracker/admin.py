from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import InputSave, Category, Income, Expense, Budget, EMI, User, UserProfile

# Custom User Admin
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff'),
        }),
    )

# Register the custom user admin
admin.site.register(User, UserAdmin)

# Admin configuration for UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'date_of_birth')
    search_fields = ('user__username', 'phone_number', 'address')

# Admin configuration for InputSave model
@admin.register(InputSave)
class InputSaveAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    search_fields = ('name',)

# Admin configuration for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')

# Admin configuration for Income model
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date')
    list_filter = ('date', 'category')
    search_fields = ('user__username', 'category__name')

# Admin configuration for Expense model
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'description')
    list_filter = ('date', 'category')
    search_fields = ('user__username', 'category__name', 'description')

# Admin configuration for Budget model
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'limit', 'period')
    list_filter = ('period',)
    search_fields = ('user__username', 'category__name')

# Admin configuration for EMI model
@admin.register(EMI)
class EMIAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'due_date', 'description')
    list_filter = ('due_date',)
    search_fields = ('user__username', 'description')
