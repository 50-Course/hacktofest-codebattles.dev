from typing import Any, List, Optional

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import UUIDFieldMixin
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel,
)

from api.mixins import AddressMixin


class CBUser(UUIDFieldMixin, AbstractUser):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    email = models.EmailField(unique=True)  # type: ignore
    first_name = models.CharField(max_length=40, null=False)  # type: ignore
    last_name = models.CharField(max_length=40, null=False)  # type: ignore
    preffered_name = models.CharField(max_length=100, null=True, blank=True)  # type: ignore

    REQUIRED_FIELDS: List[str] = ["first_name", "last_name", "email"]
    USERNAME_FIELD: str = "email"

    class Meta:
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username

    def save(
        self,
        *,
        first_name: str,
        last_name: str,
        email: models.EmailField,
        **kwargs: dict[str, Any],
    ) -> None:
        if not kwargs:
            pass
        elif "preffered_name" in kwargs:
            self.preffered_name = kwargs["preferred_name"]

        for arg in kwargs:
            self.kwargs[arg] = kwargs.get(arg)

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        return super(AbstractUser, self).save(
            first_name, last_name, email, **kwargs
        )


class Advocate(AddressMixin, TimeStampedModel, models.Model):
    """
    Model class for Advocates.

    Includes:
        - id (uuid): unique user identifier from `UUIDFieldMixin`.
        - created (date): creation date from `TimeStampedModel`.
        - modified (date): date an instance of this model is modified \
            from `TimeStampedModel`.
    """

    user = models.OneToOneField(
        CBUser, on_delete=models.CASCADE, related_name="user"
    )
    summary: Optional[str] = models.CharField(max_length=120, null=True)
    bio: Optional[str] = models.TextField(blank=True, null=True)
    headshot: Any = models.ImageField(
        to="uploads/", width_field=300, height_field=300
    )
    socials: Optional[dict[str, Any]] = models.JSONField(
        default=dict, blank=True
    )

    class Meta:
        verbose_name = "Advocate"
        verbose_name_plural = "Advocates"

    def __str__(self) -> str:
        return self.user


class Company(TitleSlugDescriptionModel, TimeStampedModel, models.Model):
    """
    Model class for companies.

    Includes:
        - created (date): creation date from `TimeStampedModel`.
        - modified (date): date an instance of this model is modified \
            from `TimeStampedModel`.
    """

    advocates: List[Advocate] = models.ManyToManyField(
        Advocate, related_query_name="advocaates"
    )
    logo: Any = models.ImageField(to="company/%s/".format(super().title))

    class Meta:
        db_table = "tbl_company"
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return f"{super(TitleSlugDescriptionModel, self).title}"