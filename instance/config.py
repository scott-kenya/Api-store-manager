import os


class Config(object):
	DEBUG = False
	#CSRF_ENABLED - Trues
	SECRET = os.getenv('secret')


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	DEBUG = True
	TESTING = True

class StagingConfig(Config):
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	DEBUG = False
	TESTING = False


app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig				
}
