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
    end_date = models.DateField(null=True, blank=True)
    short_text = models.TextField()
    detail_text = models.TextField(null=True, blank=True)
    sponsoring_organizations = models.ManyToManyField('Organization', null=True, blank=True)
    teams = models.ManyToManyField('Team', null=True, blank=True)
    submitted_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/project_images/%Y/%m/%d', default='images/project_images/nothing.jpg')
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    geo_x = models.FloatField(null=True, blank=True)
    geo_y = models.FloatField(null=True, blank=True)
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
    user = models.OneToOneField(User)
    organization = models.ForeignKey("Organization", null=True, blank=True) # Turn this into a radial menu
    teams = models.ManyToManyField("Team", null=True, blank=True)
    email = models.EmailField(max_length=128, blank=True, null=True) # validate email
    phone = models.CharField(max_length=10, blank=True, null=True) # validate numbers only
    profile = models.URLField(max_length=128, blank=True, null=True) # validate GCconnex profile
    image = models.ImageField(upload_to='images/user_images/%Y/%m/%d/%H_%M_%S', default='images/user_images/nothing.jpg')
    bio = models.TextField(blank=True, null=True)
    geo_x = models.FloatField(blank=True, null=True)
    geo_y = models.FloatField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
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
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    role = models.CharField(max_length=64, choices=ROLES)
    hrs_per_week = models.FloatField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.person, self.role, self.team)


class Resource(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    description = models.TextField()
    cost = models.FloatField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
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
        null=True, blank=True, default='images/tag_images/nothing.jpg')

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
    acronym = models.CharField(max_length=128, null=True, blank=True)
    acronym_fr = models.CharField(max_length=128, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='images/organization_images/%Y/%m/%d',
        default='images/organization_images/nothing.jpg')
    tags = models.ManyToManyField("Tag", null=True, blank=True)
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
    acronym = models.CharField(max_length=128, null=True, blank=True)
    acronym_fr = models.CharField(max_length=128, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='images/team_images/%Y/%m/%d',
        default='images/team_images/nothing.jpg')
    tags = models.ManyToManyField("Tag", null=True, blank=True)
    geo_x = models.FloatField(blank=True, null=True)
    geo_y = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)
