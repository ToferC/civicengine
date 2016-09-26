from django.db import models
from django.utils import timezone
from django.db.models import F
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import random 

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()
    short_text = models.TextField()
    detail_text = models.TextField()
    sponsoring_organizations = models.ManyToManyField('Organization')
    teams = models.ManyToManyField('Team')
    submitted_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/project_images/%Y/%m/%d')
    tags = models.ManyToManyField('Tag')
    latitude = models.FloatField()
    longitude = models.FloatField()
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Sprint(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey('User')
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    task = models.ManyToManyField('Task')
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sprint, self).save(*args, **kwargs)


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    duration = models.FloatField()
    member = models.ForeignKey('Member')
    resources = models.ManyToManyField('Resource', blank=True)
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(unique=True, max_length=255)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)


class Member(models.Model):
    name = models.CharField(max_length=128)
    user = models.OneToOneField(User)
    organization = models.ForeignKey("Organization", null=True, blank=True) # Turn this into a radial menu
    team = models.ForeignKey("Team", null=True, blank=True)
    email = models.EmailField(max_length=128, blank=True, null=True) # validate email
    phone = models.CharField(max_length=10, blank=True, null=True) # validate numbers only
    profile = models.URLField(max_length=128, blank=True, null=True) # validate GCconnex profile
    image = models.ImageField(upload_to='images/user_images/%Y/%m/%d/%H_%M_%S')
    bio = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
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
    creator = models.ForeignKey(User)
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
    creator = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/tag_images/%Y/%m/%d',
        null=True, blank=True)

    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Organization(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    name_fr = models.CharField(max_length=128, blank=True, null=True)
    acronym = models.CharField(max_length=128)
    acronym_fr = models.CharField(max_length=128, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='images/organization_images/%Y/%m/%d')
    tags = models.ManyToManyField("Tag")
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)


class Team(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    name_fr = models.CharField(max_length=128, blank=True, null=True)
    acronym = models.CharField(max_length=128)
    acronym_fr = models.CharField(max_length=128, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='images/team_images/%Y/%m/%d')
    tags = models.ManyToManyField("Tag")
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)
