from django.contrib import admin

from .models import BlogTip, Offer, Partner


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "valid_from", "valid_until", "active")
    list_filter = ("active", "valid_from", "valid_until")
    search_fields = ("name", "description")
    list_editable = ("active",)
    date_hierarchy = "valid_from"


@admin.register(BlogTip)
class BlogTipAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published", "created_at")
    list_filter = ("published", "category", "created_at")
    search_fields = ("title", "summary", "content")
    list_editable = ("published",)
    date_hierarchy = "created_at"


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "active")
    list_filter = ("active", "category")
    search_fields = ("name", "category")
    list_editable = ("active",)
