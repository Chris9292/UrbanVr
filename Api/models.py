from django.contrib.gis.db import models
        
class Building(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    kaek = models.BigIntegerField(blank=True, null=True)
    numfloor = models.IntegerField(db_column='numFloor', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(blank=True, null=True)
    landuse = models.CharField(db_column='landUse', max_length=30, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    roof = models.CharField(max_length=30, blank=True, null=True)
    centroid_x = models.FloatField(blank=True, null=True)
    centroid_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Building'
        
        
class Block(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=8, blank=True, null=True)
    sitecoverage = models.FloatField(db_column='siteCoverage', blank=True, null=True)  # Field name made lowercase.
    plotratio = models.FloatField(db_column='plotRatio', blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    centroid_x = models.FloatField(blank=True, null=True)
    centroid_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Block'