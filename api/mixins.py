from typing import Optional

from django.db import models


class AddressMixin(models.Model):
    """
    Encapsulate functionalities and attributes of an Address Field.

    If inherited, provides these fields to the component class.
    """

    line_1: str = models.CharField(max_length=140, null=False)
    line_2: Optional[str] = models.CharField(max_length=140, null=True)
    line_3: Optional[str] = models.CharField(max_length=140, null=True)
    localty: str = models.CharField(max_length=14, null=False)
    state: Optional[str] = models.CharField(max_length=3, null=True)
    country: str = models.CharField(max_length=2, null=False)

    class Meta:
        """Metadata for AddressMixin."""

        abstract = True
