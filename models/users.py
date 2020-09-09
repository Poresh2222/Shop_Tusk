import sqlalchemy



metadata = sqlalchemy.MetaData()


users_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String(30), unique=True, index=True),
    sqlalchemy.Column('name', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String(20)),
)