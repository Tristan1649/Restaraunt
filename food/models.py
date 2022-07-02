from django.db import models


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Название блюда')

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name= "навзвание")
    category= models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    img = models.ImageField(upload_to='foods')
    desc = models.TextField(verbose_name='описание'),
    price = models.IntegerField(verbose_name='цена'),

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BookTable(models.Model):
    name = models.CharField(max_length=255)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(),
    persons = models.IntegerField()
    message = models.TextField()


    def __str__(self):
        return f'клиент {self.name} забронировал столие {self.table} на {self.date}'


class Response(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    subjects = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='events')
    index = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)
    text2= models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name