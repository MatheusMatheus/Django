from django.db import models

# Esta classe vai virar uma tabela no banco de dados
# Cada variável será uma coluna da tabela
class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title