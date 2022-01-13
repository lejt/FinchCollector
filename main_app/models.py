from django.db import models
from django.urls import reverse

# Choice tuple for dropdown
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class BirdAcc(models.Model):
    item = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('INSERT PATH HERE', kwargs={})

class Finch(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    fav_food = models.CharField(max_length=150)
    weight = models.IntegerField()

    # M:M
    birdacc = models.ManyToManyField(BirdAcc)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})


# one finch to many feeding
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default = MEALS[0][0]
    )
    # Create Finch foreign key
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # method for obtaining Field.choice data
        return f'{self.get_meal_display()} on {self.date}'
    
    # change default sort to recent dates first
    class Meta:
        ordering = ['-date']