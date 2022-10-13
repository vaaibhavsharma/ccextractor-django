AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH =True
AWS_DEFAULT_ACL =None
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'videoshare.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'videoshare.aws.utils.StaticRootS3BotoStorage'

AWS_STORAGE_BUCKET_NAME = "videosharevaibhav"

AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com"

#static media settings
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

MEDIA_URL = STATIC_URL + "media/"
STATIC_ROOT = "staticfiles"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
STATICFILES_FINDERS = (
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
