from django.db import models


# Data types:
# Full name (a combination of first name and last name)
# Job
# Email
# Domain name
# Phone number
# Company name
# Text (with specified range for a number of sentences)
# Integer (with specified range)
# Address
# Date

# class SchemaColumn(models.Model):
#


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'cul name {self.name} type {self.type} order {self.order}'


class ColumnSet(models.Model):
    name = models.CharField(max_length=50)
    column = models.ManyToManyField(Column)
    download_link = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return f' {self.name}'
