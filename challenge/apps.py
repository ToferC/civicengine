from django.apps import AppConfig

class ChallengeConfig(AppConfig):
	name = 'challenge'

	def ready(self):

		from actstream import registry

		registry.register(self.get_model('Member'))
		registry.register(self.get_model('Team'))
		registry.register(self.get_model('Project'))
		registry.register(self.get_model('Organization'))
		registry.register(self.get_model('Tag'))
		registry.register(self.get_model('Issue'))
		registry.register(self.get_model('Story'))