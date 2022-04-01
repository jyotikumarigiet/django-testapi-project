from django.db import models

# Create your models here.
class Singer(models.Model):
    singer_name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.id) + " | " + self.singer_name

class SongList(models.Model):
    title = models.CharField(max_length=50)
    
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song_list")     
    duration = models.FloatField()
    
    def __str__(self):
        return str(self.id) + " | " + str(self.title) + " | " + str(self.singer.singer_name)


        #password of cacoo( MUMRU&-5Vym5/QZ )