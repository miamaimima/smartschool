import sqlalchemy as db

engine = db.create_engine('sqlite:///new.db')
metadata = db.MetaData()



user = db.Table('users', metadata,
    db.Column('user_id', db.Integer, primary_key=True),
    db.Column('name', db.Text),
    db.Column('lastname', db.Text),
    db.Column('role', db.Text),
    db.Column('orgid', db.Integer),
    db.Column('tgid', db.Integer),
    db.Column('inshcool', db.Integer, default=0),
    db.Column('zuchenik', db.Integer),
    db.Column('idcard', db.Text)
)


telegram = db.Table('tgus', metadata,
                    db.Column("tgid", db.Integer, primary_key = True))


familyshcool = db.Table('uchan', metadata,
    db.Column('orgcode', db.Integer, primary_key=True),
    db.Column('name', db.Text),
    db.Column('lastname', db.Integer),
    db.Column('role', db.Text),
    db.Column('prychenforrod', db.Integer)
)



# Create the table
metadata.create_all(engine)

# Connect to the database
connection = engine.connect()

# Insert data into the table


