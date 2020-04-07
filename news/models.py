from django.db import models

# Create your models here.


class Story(models.Model):
    HEADING_MAX_LENGTH = 128
    BODY_MAX_LENGTH = 512

    heading = models.CharField(max_length=HEADING_MAX_LENGTH)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='story_images',blank=True)
    body = models.CharField(max_length=BODY_MAX_LENGTH)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.heading
