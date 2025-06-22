from django.db import models

class AboutMe(models.Model):
        short_description=models.TextField(verbose_name="About me")
        discription=models.TextField()
        image=models.ImageField(upload_to="about")

        class Meta: 
            verbose_name = "About Me"
            verbose_name_plural = "About Me"

        def __str__(self):
            return "About Me"


class Services(models.Model):
     title=models.CharField(max_length=100, verbose_name="Service Name")
     discription=models.TextField(verbose_name="about Services")

     def __str__(self):
          return self.title
     
class Clients(models.Model):
     name=models.CharField(max_length=100, verbose_name="Client Name")
     discription=models.TextField(verbose_name="Client Says")
     image=models.ImageField(upload_to='clients', default='default.png')
     def __str__(self):
          return self.name
     
class RecentWork(models.Model):
     discription=models.TextField(verbose_name="About Recent Work")
     image=models.ImageField(upload_to="works")