from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class UserProfile(models.Model):
    user_image = models.FileField(null=True, verbose_name='User Image', blank=True, upload_to='uploads/')
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number = models.CharField(max_length=20, verbose_name= 'Founder Number')
    user_email = models.EmailField(max_length=150, verbose_name= 'Founder Email')

    def __str__(self):
        return self.user_name

    def post_img(self):
        if self.user_image:
          return self.user_image.url

class Music(models.Model):
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    pst_music = models.FileField(null=True, verbose_name='Music', blank=True, upload_to='uploads/')

    def __str__(self):
        return self.song

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url


    class Meta():
        verbose_name_plural = 'Music'

class Artiste(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
    artiste8 = models.CharField(max_length=100, verbose_name= 'Artiste8')
    song8 = models.CharField(max_length=30, verbose_name= 'Song Title8')
    pst_music8 = models.FileField(null=True, verbose_name='Music8', blank=True, upload_to='uploads/')
    
    artiste9 = models.CharField(max_length=100, verbose_name= 'Artiste9')
    song9 = models.CharField(max_length=30, verbose_name= 'Song Title9')
    pst_music9 = models.FileField(null=True, verbose_name='Music9', blank=True, upload_to='uploads/')
    
    artiste10 = models.CharField(max_length=100, verbose_name= 'Artiste10')
    song10 = models.CharField(max_length=30, verbose_name= 'Song Title10')
    pst_music10 = models.FileField(null=True, verbose_name='Music10', blank=True, upload_to='uploads/')
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
    def post_music8(self):
        if self.pst_music8:
            return self.pst_music8.url
    def post_music9(self):
        if self.pst_music9:
            return self.pst_music9.url
    def post_music10(self):
        if self.pst_music10:
            return self.pst_music10.url


    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Artiste'


class Wizkid(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
    artiste8 = models.CharField(max_length=100, verbose_name= 'Artiste8')
    song8 = models.CharField(max_length=30, verbose_name= 'Song Title8')
    pst_music8 = models.FileField(null=True, verbose_name='Music8', blank=True, upload_to='uploads/')
    
    artiste9 = models.CharField(max_length=100, verbose_name= 'Artiste9')
    song9 = models.CharField(max_length=30, verbose_name= 'Song Title9')
    pst_music9 = models.FileField(null=True, verbose_name='Music9', blank=True, upload_to='uploads/')
    
    artiste10 = models.CharField(max_length=100, verbose_name= 'Artiste10')
    song10 = models.CharField(max_length=30, verbose_name= 'Song Title10')
    pst_music10 = models.FileField(null=True, verbose_name='Music10', blank=True, upload_to='uploads/')
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
    def post_music8(self):
        if self.pst_music8:
            return self.pst_music8.url
    def post_music9(self):
        if self.pst_music9:
            return self.pst_music9.url
    def post_music10(self):
        if self.pst_music10:
            return self.pst_music10.url


    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Wizkid'


class Simi(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
    artiste8 = models.CharField(max_length=100, verbose_name= 'Artiste8')
    song8 = models.CharField(max_length=30, verbose_name= 'Song Title8')
    pst_music8 = models.FileField(null=True, verbose_name='Music8', blank=True, upload_to='uploads/')
    
    artiste9 = models.CharField(max_length=100, verbose_name= 'Artiste9')
    song9 = models.CharField(max_length=30, verbose_name= 'Song Title9')
    pst_music9 = models.FileField(null=True, verbose_name='Music9', blank=True, upload_to='uploads/')
    
    artiste10 = models.CharField(max_length=100, verbose_name= 'Artiste10')
    song10 = models.CharField(max_length=30, verbose_name= 'Song Title10')
    pst_music10 = models.FileField(null=True, verbose_name='Music10', blank=True, upload_to='uploads/')
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
    def post_music8(self):
        if self.pst_music8:
            return self.pst_music8.url
    def post_music9(self):
        if self.pst_music9:
            return self.pst_music9.url
    def post_music10(self):
        if self.pst_music10:
            return self.pst_music10.url


    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Simi'


class Drake(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
    
    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Drake'


class Joefire(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
    artiste8 = models.CharField(max_length=100, verbose_name= 'Artiste8')
    song8 = models.CharField(max_length=30, verbose_name= 'Song Title8')
    pst_music8 = models.FileField(null=True, verbose_name='Music8', blank=True, upload_to='uploads/')
    
    artiste9 = models.CharField(max_length=100, verbose_name= 'Artiste9')
    song9 = models.CharField(max_length=30, verbose_name= 'Song Title9')
    pst_music9 = models.FileField(null=True, verbose_name='Music9', blank=True, upload_to='uploads/')
    
    artiste10 = models.CharField(max_length=100, verbose_name= 'Artiste10')
    song10 = models.CharField(max_length=30, verbose_name= 'Song Title10')
    pst_music10 = models.FileField(null=True, verbose_name='Music10', blank=True, upload_to='uploads/')
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
    def post_music8(self):
        if self.pst_music8:
            return self.pst_music8.url
    def post_music9(self):
        if self.pst_music9:
            return self.pst_music9.url
    def post_music10(self):
        if self.pst_music10:
            return self.pst_music10.url


    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Joefire'


class Nicki(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    
    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Nicki'

class AllMar(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
   
    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'AllMar'

class Gyke(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')

    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')

    artiste8 = models.CharField(max_length=100, verbose_name= 'Artiste8')
    song8 = models.CharField(max_length=30, verbose_name= 'Song Title8')
    pst_music8 = models.FileField(null=True, verbose_name='Music8', blank=True, upload_to='uploads/')

    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url

    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url

    def post_music8(self):
        if self.pst_music8:
            return self.pst_music8.url


    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Gyke'

class Burna(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
   

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Burna'

class Fire(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
   

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Fire'

class Teni(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
   

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Teni'

class Cuppy(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    artiste = models.CharField(max_length=50, verbose_name= 'Artiste')
    song = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music1', blank=True, upload_to='uploads/')
    
    artiste2 = models.CharField(max_length=100, verbose_name= 'Artiste2')
    song2 = models.CharField(max_length=30, verbose_name= 'Song Title2')
    pst_music2 = models.FileField(null=True, verbose_name='Music2', blank=True, upload_to='uploads/')
    
    artiste3 = models.CharField(max_length=100, verbose_name= 'Artiste3')
    song3 = models.CharField(max_length=30, verbose_name= 'Song Title3')
    pst_music3 = models.FileField(null=True, verbose_name='Music3', blank=True, upload_to='uploads/')
    
    artiste4 = models.CharField(max_length=100, verbose_name= 'Artiste4')
    song4 = models.CharField(max_length=30, verbose_name= 'Song Title4')
    pst_music4 = models.FileField(null=True, verbose_name='Music4', blank=True, upload_to='uploads/')
    
    artiste5 = models.CharField(max_length=100, verbose_name= 'Artiste5')
    song5 = models.CharField(max_length=30, verbose_name= 'Song Title5')
    pst_music5 = models.FileField(null=True, verbose_name='Music5', blank=True, upload_to='uploads/')
    
    artiste6 = models.CharField(max_length=100, verbose_name= 'Artiste6')
    song6 = models.CharField(max_length=30, verbose_name= 'Song Title6')
    pst_music6 = models.FileField(null=True, verbose_name='Music6', blank=True, upload_to='uploads/')
    
    artiste7 = models.CharField(max_length=100, verbose_name= 'Artiste7')
    song7 = models.CharField(max_length=30, verbose_name= 'Song Title7')
    pst_music7 = models.FileField(null=True, verbose_name='Music7', blank=True, upload_to='uploads/')
    
   
    def __str__(self):
        return self.artiste

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url
    def post_music1(self):
        if self.pst_music1:
          return self.pst_music1.url
    def post_music2(self):
        if self.pst_music2:
          return self.pst_music2.url
    def post_music3(self):
        if self.pst_music3:
            return self.pst_music3.url
    def post_music4(self):
        if self.pst_music4:
            return self.pst_music4.url
    def post_music5(self):
        if self.pst_music5:
            return self.pst_music5.url
    def post_music6(self):
        if self.pst_music6:
            return self.pst_music6.url
    def post_music7(self):
        if self.pst_music7:
            return self.pst_music7.url
   

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Cuppy'

class Songs(models.Model):
    name = models.CharField(max_length=30, verbose_name= 'Song Title')
    pst_music = models.FileField(null=True, verbose_name='Music', blank=True, upload_to='uploads/')
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    def __str__(self):
        return self.name

    def post_music(self):
        if self.pst_music:
          return self.pst_music.url

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'Songs'


class About(models.Model):
    name = models.CharField(max_length=30, verbose_name= 'Founder Name')
    pst_image = models.FileField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')
    inst = models.CharField(max_length=30, verbose_name= 'Instrument Skill')

    def __str__(self):
        return self.name

    def post_image(self):
        if self.pst_image:
          return self.pst_image.url


    class Meta():
        verbose_name_plural = 'About'

