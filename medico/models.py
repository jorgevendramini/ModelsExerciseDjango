from django.db import models

# Create your models here.
class Especialidade(models.Model): #JorgeEnrique
    id_especialidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
#JorgeEnrique