from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from abstracts.models import AbstractDateTime
from django.db.models import QuerySet
# Create your models here.

class StudentQuerySet(QuerySet):
    ADULT_AGE = 18

    def get_adult_students(self) -> QuerySet:
        return self.filter(
            age_gte=self.ADULT_AGE
    )

class AccountQuerySet(QuerySet):

    def get_superusers(self) -> QuerySet:
        return self.filter(
            user__is_superuser=True
        )

class GroupQuerySet(QuerySet):
    HIGH_GPA_LEVEL = 4.0

    def get_students_with_high_gpa(self) -> QuerySet:
        return self.filter(
            gpa_gt=self.HIGH_GPA_LEVEL
    )

objects = AccountQuerySet().as_manager()
    
class Group(AbstractDateTime):
    GROUP_NAME_MAX_LENGTH = 10
    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH
    )

    def __str__(self) -> str:
        return f'Group {self.name}'
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    objects = GroupQuerySet().as_manager()
    
class Account (AbstractDateTime):
    ACCOUNT_FULL_NAME_MAX_LENTGTH = 20
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=ACCOUNT_FULL_NAME_MAX_LENTGTH)
    description = models.TextField()

    def __str__(self) -> str:
        return f'Account {self.user.id} / {self.full_name}'

    objects = AccountQuerySet().as_manager()

    class Meta:
        ordering = ('full_name',)
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

class Student(AbstractDateTime):
    
    MAX_AGE = 27
    # 1 Account = много Студентов
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        on_delete = models.PROTECT
    )
    age = models.IntegerField(
        'Возраст студента'
    )
    GPA = models.FloatField(
        'Среднее значение GPA'
    )
    
    def __str__(self) -> str:
        return f'Student: {self.account} \
        age: {self.age} group: {self.group} GPA: {self.GPA}'

    objects = StudentQuerySet().as_manager()

    def save (
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None: 
        if self.age > self.MAX_AGE:
            self.age =  self.MAX_AGE
            raise ValidationError(
                f'Допустимый возраст: {self.MAX_AGE}'
            )
        super().save(*args, **kwargs) 

    

    class Meta:
        ordering = (
            'account',
            'age',
            'group',
            'GPA'
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Professor(AbstractDateTime):
    FULL_NAME_MAX_LENGTH = 20
    TOPIC_MAX_LENGTH  = 10
    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_TS = 'typescript'
    TOPIC_JS = 'javascript'
    TOPIC_RUBY  = 'ruby'
    TOPIC_GO  = 'golang'
    TOPIC_SQL = 'sql'
    TOPIC_SWIFT =  'swift'
    TOPIC_PHP  = 'php'
    TOPIC_DEPLHI = 'dephli'
    TOPIC_PERL  = 'perl'
    TOPIC_CHOICES = (
        (TOPIC_JAVA,'Java'),
        (TOPIC_PYTHON,'Python'),
        (TOPIC_TS, 'Typescript'),
        (TOPIC_JS,'Javascript'),
        (TOPIC_RUBY, 'Ruby'),
        (TOPIC_GO, 'GoLong'),
        (TOPIC_SQL, 'SQL'),
        (TOPIC_SWIFT, 'Swift'),
        (TOPIC_PHP, 'PHP'),
        (TOPIC_DEPLHI, 'Dephli'),
        (TOPIC_PERL, 'Perl'),
    )
    full_name = models.CharField(
        verbose_name = 'полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    topic = models.CharField(
        verbose_name='предмет',
        max_length=TOPIC_MAX_LENGTH,
        choices=TOPIC_CHOICES,
        default=TOPIC_JAVA
    )
    students = models.ManyToManyField(
        Student
    )

    def __str__(self) -> str:
        return f'Профессор: {self.full_name}/ Топик: {self.topic}'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        super().save(*args, **kwargs)

    class Meta:
        ordering = (
            'topic',
        )
        verbose_name = 'Профессор'
        verbose_name_plural = 'Профессор'

    