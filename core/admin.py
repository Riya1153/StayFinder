from django.contrib import admin
from .models import Owner, Hostel, House, BoysHostel, GirlsHostel


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'rent', 'rooms', 'owner')


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month', 'gender', 'stars', 'owner')
    list_filter = ('gender', 'stars')
    search_fields = ('title', 'location')


@admin.register(BoysHostel)
class BoysHostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month', 'stars', 'owner')
    search_fields = ('title', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(gender='B')

    def save_model(self, request, obj, form, change):
        obj.gender = 'B'
        super().save_model(request, obj, form, change)


@admin.register(GirlsHostel)
class GirlsHostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_month', 'stars', 'owner')
    search_fields = ('title', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(gender='G')

    def save_model(self, request, obj, form, change):
        obj.gender = 'G'
        super().save_model(request, obj, form, change)