from django.db import models


class Avaliation(models.Model):
    contributor = models.ForeignKey(
        to='accounts.Contributor',
        on_delete=models.CASCADE,
        related_name='avaliations'
    )
    service = models.ForeignKey(
        to='services.Service',
        on_delete=models.CASCADE,
        related_name='avaliations'
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField()
    comment = models.CharField(max_length=50)

    class Meta:
        ordering = ('contributor__points',)


class AvaliationFeedbacks(models.Model):
    contributor = models.ForeignKey(
        to='accounts.Contributor',
        on_delete=models.CASCADE,
        related_name='avaliation_feedbacks'
    )
    avaliation = models.ForeignKey(
        to=Avaliation,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    is_positive = models.BooleanField()

    class Meta:
        ordering = ('contributor__points',)
