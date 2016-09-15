class Issue(models.Model):

	STATUS = ()
	()

	name = models.CharField(max_length=64)
	description = models.TextField(null=True, blank=True)
	creator = models.ForeignKey('User')
	status = models.ChoiceField(choices=STATUS)
	ideal_state = models.TextField(null=True, blank=True)
	current_state = models.TextField(null=True, blank=True)
	stories = models.ManyToManyField("Story")
	rating = models.IntegerField(default=0)
	priority = models.IntegerField(default=1)
	date_created = models.DateField(auto_now=True)
	date_edited = models.DateField(auto_now=True)
	followers = models.ManyToManyField("User", blank=True)
	published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/issue_images/%Y/%m/%d/%H_%M_%S', default='images/issue_images/nothing.jpg')
    tags = models.ManyToManyField('Tag', blank=True)
    geo_x = models.FloatField(null=True, blank=True)
    geo_y = models.FloatField(null=True, blank=True)
	slug = models.SlugField(unique=True, max_length=255)


class Story(models.Model):
	name = models.CharField(max_length=64)
	creator = models.ForeignKey('User')
	impact_statement = models.TextField(max_length=1000)
	priority = models.IntegerField(default=1)
	date_created = models.DateField(auto_now=True)
	date_edited = models.DateField(auto_now=True)
	followers = models.ManyToManyField("User", blank=True)
	published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/story_images/%Y/%m/%d/%H_%M_%S', default='images/story_images/nothing.jpg')
    tags = models.ManyToManyField('Tag', blank=True)
    geo_x = models.FloatField(null=True, blank=True)
    geo_y = models.FloatField(null=True, blank=True)
	slug = models.SlugField(unique=True, max_length=255)


class Response(models.Model):
    issue = models.ForeignKey("Issue")
    project = models.ForeignKey("Project")
    objective = models.TextField(max_length=255)
    start_date = (models.DateField(auto_now=True))


class Vote(models.Model):
	project = models.ForeignKey("Project")
	positive = models.IntegerField(default=0)
	negative = models.IntegerField(default=0)
	neutral = models.IntegerField(default=0)

