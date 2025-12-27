class Config:
    SECRET_KEY = "secret-key-that-is-never-seen-before"
    JWT_SECRET_KEY = "super-duper-secret-key-that-is-never-seen-before"
    SQLALCHEMY_DATABASE_URI = "sqlite:///ott.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False