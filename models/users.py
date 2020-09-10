import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID



metadata = sqlalchemy.MetaData()


users_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String(30), unique=True, index=True),
    sqlalchemy.Column('name', sqlalchemy.String(50)),
    sqlalchemy.Column('hashed_password', sqlalchemy.String()),
    sqlalchemy.Column(
        'is_active',
        sqlalchemy.Boolean(),
        server_default=sqlalchemy.sql.expression.true(),
        nullable=False,
        ),
)


tokens_table = sqlalchemy.Table(
    'tokens',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        'token',
        UUID(as_uuid=False),
        unique=True,
        nullable=True,
        index=True,
    ),
    sqlalchemy.Column('expires', sqlalchemy.DateTime()),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id')),
)