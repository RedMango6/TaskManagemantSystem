from django.db import models

# Create your models here.
# Each model corresponds to a table.
# There is a one to many relationship from ToDoList to Item.
class ToDoList(models.Model):   
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Item (models.Model):
    # Belows todolist field is a foreign-key field that references a todolist.
    todolist = models.ForeignKey(ToDoList, on_delete= models.CASCADE)

    text= models.CharField(max_length=300)
    complete= models.BooleanField()

    def __str__(self):
        return self.text




