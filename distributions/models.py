from django.db import models

from hashid_field import HashidAutoField
from math import e, log, pi, sqrt

# Create your models here.


class ProbabilityDistribution(models.Model):

    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    xaxis_name = models.CharField(max_length=60)

    lower_bound = models.FloatField()
    upper_bound = models.FloatField()

    def __str__(self):
        return self.name

    def get_sum_of_weights(self):
        weightsum = 0
        for d in self.normal_distributions.all():
            weightsum += d.weight
        # add more if other distributions included
        return weightsum

    def get_weighted_value_at(self, p):
        """returns the weighted value of the distribution at point p"""
        normal_distributions = self.normal_distributions.all()
        # add more here if other distributions available
        value = 0
        for d in normal_distributions:
            value += d.get_unweighted_value_at(p) * d.weight
        return value

    def get_data(self, resolution: int = 200):
        data = []
        weightsum = self.get_sum_of_weights()
        weightsum += not weightsum
        p = self.lower_bound
        while p <= self.upper_bound:
            weighted_value = self.get_weighted_value_at(p)
            normalized_value = weighted_value / weightsum

            data.append([str(p), normalized_value])

            p += (self.upper_bound - self.lower_bound) / resolution
            p = round(p, 3)
        return data


class NormalDist(models.Model):

    id = HashidAutoField(primary_key=True)
    mean = models.FloatField()
    std = models.FloatField()
    weight = models.FloatField()

    probabilitydistribution = models.ForeignKey(
        ProbabilityDistribution,
        on_delete=models.CASCADE,
        related_name="normal_distributions",
    )

    def get_unweighted_value_at(self, p):
        result = (
            1
            / (self.std * sqrt(2 * pi))
            * e ** (-1 / 2 * ((p - self.mean) / self.std) ** 2)
        )
        return result


# class PoissonDist(models.Model):

#     parameter = models.FloatField()
#     weight = models.FloatField()

#     probabilitydistribution = models.ForeignKey(
#         ProbabilityDistribution, on_delete=models.CASCADE
#     )
