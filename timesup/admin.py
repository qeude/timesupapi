from django.contrib import admin
from .models import Card, Game, Category, CardGame


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "category")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "state")
    list_filter = ("state",)


@admin.register(CardGame)
class CardGameAdmin(admin.ModelAdmin):
    list_display = ("id", "card", "game", "found_this_round")
