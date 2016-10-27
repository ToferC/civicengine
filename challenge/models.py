from django.db import models
from django.utils import timezone
from django.db.models import F
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import random 

from actstream import registry
from actstream.models import following, followers

# Create your models here.

class Project(models.Model):

    PL = "Planning"
    DE = "Recruiting"
    AC = "Active"
    IN = "Inactive"
    CM = "Completed"
    AB = "Aborted"

    STATUS = (
        (PL, "Planning"),
        (DE, "Recruiting"),
        (AC, "Active"),
        (IN, "Inactive"),
        (CM, "Completed"),
        (AB, "Aborted"),
        )

    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    status = models.CharField(max_length=64, choices=STATUS, default="Planning")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    short_text = models.TextField()
    detail_text = models.TextField(null=True, blank=True)
    sponsoring_organizations = models.ManyToManyField('Organization', blank=True)
    submitted_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/project_images/%Y/%m/%d/%H_%M_%S', default='images/project_images/nothing.jpg')
    tags = models.ManyToManyField('Tag', blank=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def set_project_to_planning(self):
        self.status = "Planning"

    def set_project_to_recruit(self):
        self.status = "Recruiting"

    def set_project_to_active(self):
        self.status = "Active"

    def set_project_to_inactive(self):
        self.status = "Inactive"

    def set_project_to_completed(self):
        self.status = "Completed"

    def set_project_to_aborted(self):
        self.status = "Aborted"

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

    AC = "Active"
    IN = "Inactive"

    STATUS = (
        (AC, "Active"),
        (IN, "Inactive"),
        )

    name = models.CharField(max_length=128)
    user = models.OneToOneField(User)
    status = models.CharField(max_length=64, choices=STATUS, default="Active")
    organization = models.ForeignKey("Organization", null=True, blank=True) # Turn this into a radial menu
    email = models.EmailField(max_length=128, blank=True, null=True) # validate email
    phone = models.CharField(max_length=10, blank=True, null=True) # validate numbers only
    profile = models.URLField(max_length=128, blank=True, null=True) # validate GCconnex profile
    image = models.ImageField(upload_to='images/user_images/%Y/%m/%d/%H_%M_%S', default='images/user_images/nothing.jpg')
    bio = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")
    salary = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def set_member_to_active(self):
        self.status = "Active"

    def set_member_to_inactive(self):
        self.status = "Inactive"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Member, self).save(*args, **kwargs)


class Role(models.Model):

    VA = "Vacant"
    AA = "Applied"
    AC = "Active"
    IN = "Inactive"
    RE = "Retired"
    RM = "Removed"

    STATUS = (
        (VA, "Vacant"),
        (AA, "Applied"),
        (AC, "Active"),
        (IN, "Inactive"),
        (RE, "Retired"),
        (RM, "Removed"),
        )

    person = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    role = models.CharField(max_length=64, default="Occupation")
    status = models.CharField(max_length=64, choices=STATUS, default="Vacant")
    hrs_per_week = models.FloatField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def set_role_to_vacant(self):
        self.status = "Vacant"

    def set_role_to_applied(self):
        self.status = "Applied"

    def set_role_to_activate(self):
        self.status = "Active"

    def set_role_to_retired(self):
        self.status = "Retired"

    def set_role_to_removed(self):
        self.status = "Removed"

    def set_role_to_inactive(self):
        self.status = "Inactive"

    def __str__(self):
        return "{} - {} - {}".format(self.person, self.role, self.team)


class Committment(models.Model):
    team = models.ForeignKey("Team")
    project = models.ForeignKey(Project)
    objective = models.TextField(max_length=255)
    start_date = (models.DateField(auto_now=True))
    end_date = (models.DateField(null=True, blank=True))


class Resource(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    description = models.TextField()
    cost = models.FloatField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Resource, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/tag_images/%Y/%m/%d/%H_%M_%S',
        null=True, blank=True, default='images/tag_images/nothing.jpg')

    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

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
    image = models.ImageField(upload_to='images/organization_images/%Y/%m/%d/%H_%M_%S',
        default='images/organization_images/nothing.jpg')
    tags = models.ManyToManyField("Tag", blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

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
    image = models.ImageField(upload_to='images/team_images/%Y/%m/%d/%H_%M_%S',
        default='images/team_images/nothing.jpg')
    tags = models.ManyToManyField("Tag", blank=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)


class Issue(models.Model):

    AC = "Active"
    IN = "Inactive"
    RE = "Resolved"
    IM = "Improving"
    WO = "Worsening"

    STATUS = (
        (AC, "Active"),
        (IN, "Inactive"),
        (RE, "Resolved"),
        (IM, "Improving"),
        (WO, "Worsening"),
        )

    CO = "Community"
    MU = "Municipal"
    RN = "Regional"
    PO = "Provincial/State"
    NA = "National"
    IT = "International"

    SCOPE = (
        (CO, "Community"),
        (MU, "Municipal"),
        (RN, "Regional"),
        (PO, "Provincial/State"),
        (NA, "National"),
        (IT, "International"),
        )

    OP = "Opportunity"
    CH = "Challenge"

    ISSUE_TYPE = (
        (OP, "Opportunity"),
        (CH, "Challenge"),
        )

    name = models.CharField(max_length=64)
    creator = models.ForeignKey(User)
    issue_type = models.CharField(choices=ISSUE_TYPE, max_length=32, default="Challenge")
    summary = models.TextField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default="Active",
        max_length=64)
    scope = models.CharField(choices=SCOPE, default="Municipal",
        max_length=64)
    current_state = models.TextField(null=True, blank=True)
    ideal_state = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)
    followers = models.ManyToManyField(User, blank=True, related_name="issue_followers")
    image = models.ImageField(upload_to='images/issue_images/%Y/%m/%d/%H_%M_%S', default='images/issue_images/nothing.jpg')
    tags = models.ManyToManyField(Tag, blank=True)
    priority = models.IntegerField(default=1)
    rating = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")
    slug = models.SlugField(unique=True, max_length=255)

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Issue, self).save(*args, **kwargs)


class Story(models.Model):
    name = models.CharField(max_length=64)
    creator = models.ForeignKey(User)
    issue = models.ForeignKey(Issue)
    impact_statement = models.TextField(max_length=1000)
    priority = models.IntegerField(default=1)
    rating = models.IntegerField(default=0)
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)
    followers = models.ManyToManyField(User, blank=True, related_name="story_followers")
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/story_images/%Y/%m/%d/%H_%M_%S', default='images/story_images/nothing.jpg')
    tags = models.ManyToManyField(Tag, blank=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")

    def get_number_followers(self):
        return len(followers(self))

    def get_followers(self):
        return followers(self)

    def __str__(self):
        return self.name


class Response(models.Model):
    project = models.ForeignKey(Project)
    issue = models.ForeignKey(Issue)
    objective = models.TextField(max_length=255)
    start_date = (models.DateField(auto_now=True))


class Vote(models.Model):
    project = models.ForeignKey(Project)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Issue, blank=True, null=True)
    story = models.ForeignKey(Story, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    team = models.ForeignKey(Team, blank=True, null=True)
    member = models.ForeignKey(Member, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
