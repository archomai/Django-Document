from django.db import models




class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )

    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.manufacturer.name} | {self.name}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    # 자기 자시을 다대일로 연력하는 필드
    # 비어있어도 무과느 연결된 객체가 삭제되면 함께 삭제되지 않고
    # 해당 필드를 비움
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Type(models.Model):
    type_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type_number} | {self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03} | {self.type} | {self.name}'