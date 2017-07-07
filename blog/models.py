from django.db import models  # başka yerlerden bir şeyleri projemize dahil eder
from django.utils import timezone


class Post(models.Model): #bu satır modelimizi tanımlar , post modelimizin ismi
    yazar = models.ForeignKey('auth.User')  #başka bir model ile bağlantı içerir.
    baslik = models.CharField(max_length=200)  #kısıtlı uzunlukta metin tanımlamak için kullanılır.
    yazi = models.TextField() #uzun metinleri tanımlar
    yaratilma_tarihi = models.DateTimeField( #gün ve saati tanımlamada kullanılır.
           default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
           blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik