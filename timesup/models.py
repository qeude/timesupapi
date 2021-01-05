from django.db import models
from uuid import uuid4
from django_fsm import FSMField, transition
from .constants import game_states


class Category(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=128)

    class Meta:
        unique_together = ("name",)

    def __str__(self) -> str:
        return f"{self.name}"


class Card(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=128)

    class Meta:
        unique_together = ("word",)


class Game(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    state = FSMField(default=game_states.created)

    cards = models.ManyToManyField(Card, related_name="game_set", through="CardGame")

    @transition(field=state, source=game_states.created, target=game_states.first_round)
    def start(self):
        ...

    @transition(
        field=state, source=game_states.first_round, target=game_states.second_round
    )
    def start_second_round(self):
        ...

    @transition(
        field=state, source=game_states.second_round, target=game_states.third_round
    )
    def start_third_round(self):
        ...

    @transition(field=state, source="*", target=game_states.finished)
    def finish(self):
        ...


class CardGame(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    found_this_round = models.BooleanField(default=False)
