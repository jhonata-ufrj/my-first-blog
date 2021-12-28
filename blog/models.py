from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #criação dos atributos do modelo
    #correspondente às colunas da tabela
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#deleta todos os dados acoplados a ela
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        #método que publica o post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title