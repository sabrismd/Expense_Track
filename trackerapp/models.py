from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class Expenses(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.TextField()
    amount = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    mode = models.ForeignKey('Mode', models.DO_NOTHING)
    created_at = models.DateTimeField()
    last_modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'expenses'


class Mode(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mode'


class Users(models.Model):
    userid = models.IntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'