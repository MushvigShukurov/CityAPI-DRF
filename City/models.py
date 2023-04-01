from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    
    image = models.ImageField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Şəhərlər"
    
    def __str__(self):
        return self.name