import os
from pathlib import Path

# Base directory definition, useful if you're initializing the project from scratch
BASE_DIR = Path(__file__).resolve().parent.parent

# Cloudflare R2 Storage Configuration for S3Boto3Storage
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

# Configure django-storages to use boto3 for Cloudflare R2
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
