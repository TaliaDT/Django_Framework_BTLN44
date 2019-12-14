from django.db import models

# Create your models here.c
class SanPham(models.Model):
    tieude = models.CharField(max_length=100)
    noidung = models.TextField()
    ngaythem = models.DateTimeField(auto_now_add=True)
    anh  = models.ImageField(null= True)
    gia = models.FloatField()
    
    def __str__(self):
        return self.tieude