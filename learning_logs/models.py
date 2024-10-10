from django.db import models

# Create your models here.
class Topic(models.Model):
    #um assunto sobre o user
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        #MOSTA O PAINEL ADM E DEVOLVE UMA  APRESNETACAO
        return self.text
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Entradas"
    def __str__(self):
        #MOSTA O PAINEL ADM E DEVOLVE UMA  APRESNETACAO
        return self.text[:50] + "..."