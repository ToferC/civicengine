from django.db import models
from django.utils import timezone
from django.db.models import F
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import random

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    short_text = models.TextField()
    detail_text = models.TextField()
    sponsoring_departments = models.ManyToManyField('Department')
    submitted_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/project_images/%Y/%m/%d')
    tags = models.ManyToManyField('Tag')
    geo_x = models.FloatField()
    geo_y = models.FloatField()
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Sprint(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    work = models.ManyToManyField('Work')
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=64)
    task = models.CharField(max_length=256)
    duration = models.FloatField()
    member = models.ForeignKey('Member')
    resources = models.ManyToManyField('Resource', blank=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Member(models.Model):
    name = models.CharField(max_length=128)
    department = models.ForeignKey("Department", null=True, blank=True) # Turn this into a radial menu
    branch = models.CharField(max_length=128)
    email = models.EmailField(max_length=128) # validate email
    phone = models.CharField(max_length=10) # validate numbers only
    profile = models.URLField(max_length=128) # validate GCconnex profile
    image = models.ImageField(upload_to='images/user_images/%Y/%m/%d')
    geo_x = models.FloatField()
    geo_y = models.FloatField()
    salary = models.IntegerField()
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Member, self).save(*args, **kwargs)


class Role(models.Model):

    PM = "Project Manager"
    DS = "Designer"
    DV = "Developer"
    AN = "Analyst"
    CM = "Communications"
    PL = "Project Lead"
    CH = "Champion"
    SP = "Project Support"
    ST = "Project Strategy"

    ROLES = (
        (PM, "Project Manager"),
        (DS, "Designer"),
        (DV, "Developer"),
        (AN, "Analyst"),
        (CM, "Communications"),
        (PL, "Project Lead"),
        (CH, "Champion"),
        (SP, "Project Support"),
        (ST, "Project Strategy"),
        )

    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=64, choices=ROLES)
    hrs_per_week = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} - {} - {}".format(self.person, self.role, self.project)


class Resource(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    cost = models.FloatField()
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Resource, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Department(models.Model):
    name = models.CharField(max_length=128)
    name_fr = models.CharField(max_length=128)
    acronym = models.CharField(max_length=128)
    acronym_fr = models.CharField(max_length=128)
    website = models.URLField(max_length=128)
    image = models.ImageField(upload_to='images/department_images/%Y/%m/%d')
    tags = models.ManyToManyField("Tag")
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

