from django.contrib import admin
from .models import Owner, Hostel, House, BoysHostel, GirlsHostel,Student,Application


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'rent', 'rooms', 'owner')


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month', 'gender',  'owner')
    list_filter = ('gender', )
    search_fields = ('title', 'location')


@admin.register(BoysHostel)
class BoysHostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month',  'owner')
    search_fields = ('title', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(gender='B')

    def save_model(self, request, obj, form, change):
        obj.gender = 'B'
        super().save_model(request, obj, form, change)


@admin.register(GirlsHostel)
class GirlsHostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month',  'owner')
    search_fields = ('title', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(gender='G')

    def save_model(self, request, obj, form, change):
        obj.gender = 'G'
        super().save_model(request, obj, form, change)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # This adds the columns to your admin list view
    list_display = ('name', 'email', 'phone', 'password')




@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'get_property',
        'phone_number',
        'own_phone',
        'guardian_phone',
        'nid_number',
        'current_address',
        'check_in_date',
        'applied_on'
    )


    search_fields = ('full_name', 'email', 'nid_number', 'phone_number')


    list_filter = ('check_in_date', 'applied_on')


    def get_property(self, obj):
        if obj.house:
            return f"House: {obj.house.title}"
        if obj.hostel:
            return f"Hostel: {obj.hostel.title}"
        return "No Property"

    get_property.short_description = 'Property'
