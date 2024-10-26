import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Advanced_ecommerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
    RATELIMIT_DEFAULT = "100 per day"
    DEBUG = True

class ProductionConfig:
    DATABASE_URl = os.environ.get('DATABASE_URL') or 'sqlite:///Advanced_ecommerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False