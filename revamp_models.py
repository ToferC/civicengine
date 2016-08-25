class Issue(models.Model):
	name = CharField()
	description = TextField()
	creator = ForeignKey('User')
	image = ImageField()
	ideal_state = TextField()
	current_state = TextField()
	stories = ManyToManyField("Story")
	rating = IntegerField()



class Story(models.Model):
	creator = ForeignKey('User')
	impact_statement = TextField()
	priority = IntegerField()