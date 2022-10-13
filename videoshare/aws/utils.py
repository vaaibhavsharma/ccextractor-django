from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='videoshare/static')
MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='videoshare/media')