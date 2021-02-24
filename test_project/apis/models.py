from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_image(image):
    file_size = image.size
    limit_kb = 200
    if file_size > limit_kb * 1024:
        raise ValidationError("Ensure that the file size is below 200 Kb")


class GeeksModel(models.Model): 
    title = models.CharField(max_length = 50, unique=True)
    image = models.ImageField(upload_to='item_images', validators=[validate_image])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self): 
        return (self.title, self.user)




