class BaseConfig(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'zay1634hevgerf78r5'
	DEBUG = False
	TESTING = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	TESTING = True

class TestingConfig
	DEBUG = False
	TESTING = True