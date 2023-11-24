from django.db import models

class Filme(models.Model):
    ftFundo = models.ImageField(upload_to='ft.Fundo')
    descricao = models.TextField(max_length=150)
    genero = models.CharField(max_length=100)
    avaliacao = models.IntegerField()
    ano = models.IntegerField()
    duracao = models.CharField(max_length=50)
    titulo = models.CharField(max_length=80)

    def __str__(self):
        return self.titulo



class Comentarios(models.Model):
    filme = models.ForeignKey(Filme,on_delete=models.PROTECT)
    usuario = models.CharField(max_length=80)
    comentario = models.TextField()

# -------------------------------------------------------------------------------------------------------------------------------------
    regist = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-regist'] # Isso é para que os uma organização para que os comentários sejam registrados na ordem de data no Admin
    def __str__(self):
        return str(f'Filme:  {self.filme} | Com o cometário: {self.comentario}')