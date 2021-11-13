from django.db import models

class cast(models.Model):
    title = models.CharField(max_length=255, unique=True)


class category(models.Model):
    title = models.CharField(max_length=255, unique=True)

class CommonInfo(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(verbose_name="Movie Description")
    production_date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='movie/images')
    Cast = models.ManyToManyField(cast)
    Category = models.ManyToManyField(category)


    def __str__(self):
        return str(self.title)



class movie(CommonInfo):
    pass

class series(CommonInfo):
    pass


