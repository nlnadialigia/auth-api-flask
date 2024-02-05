from sqlalchemy import UUID, text
from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # id (int), username (text), pasword (text)
    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   server_default=text("uuid_generate_v4()"))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
