from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
