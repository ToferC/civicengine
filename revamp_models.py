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

	name = models.CharField(max_length=64)
	creator = models.ForeignKey('User')
	description = models.TextField(null=True, blank=True)
	status = models.ChoiceField(choices=STATUS, default="Active")
	scope = models.ChoiceField(choices=SCOPE, default="Municipal")
	current_state = models.TextField(null=True, blank=True)
	ideal_state = models.TextField(null=True, blank=True)
	date_created = models.DateField(auto_now=True)
	date_edited = models.DateField(auto_now=True)
	followers = models.ManyToManyField("User", blank=True)
    image = models.ImageField(upload_to='images/issue_images/%Y/%m/%d/%H_%M_%S', default='images/issue_images/nothing.jpg')
	stories = models.ManyToManyField("Story")
    tags = models.ManyToManyField('Tag', blank=True)
	priority = models.IntegerField(default=1)
	rating = models.IntegerField(default=0)
	published = models.BooleanField(default=True)
    geo_x = models.FloatField(null=True, blank=True)
    geo_y = models.FloatField(null=True, blank=True)
	slug = models.SlugField(unique=True, max_length=255)

	def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Issue, self).save(*args, **kwargs)


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

	def __str__(self):
        return self.name


class Response(models.Model):
    project = models.ForeignKey("Project")
    issue = models.ForeignKey("Issue")
    objective = models.TextField(max_length=255)
    start_date = (models.DateField(auto_now=True))


class Vote(models.Model):
	project = models.ForeignKey("Project")
	positive = models.IntegerField(default=0)
	negative = models.IntegerField(default=0)
	neutral = models.IntegerField(default=0)

