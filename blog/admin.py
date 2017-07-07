#Modelini hazırladığımız yazıları eklemek, 
#düzenlemek ve silmek için Django admin'i kullanacağız.

from django.contrib import admin
from .models import Post

admin.site.register(Post) #Modelimizi admin sayfasında görünür yapmak için modeli belirtmemiz gerekir.



