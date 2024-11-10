from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="имя",
    )
    password = models.CharField(
        max_length=256,
        verbose_name="пароль",
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.name


class Roommate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        verbose_name="комната",
    )
    dept = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="долг",
    )

    class Meta:
        verbose_name = "участник"
        verbose_name_plural = "участники"

    def __str__(self):
        return self.user.name


class Room(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="комната",
    )
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="админ",
    )
    roommates = models.ManyToManyField(
        User,
        through=Roommate,
        related_name="rooms",
        verbose_name="участники",
    )

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"

    def __str__(self):
        return self.name
