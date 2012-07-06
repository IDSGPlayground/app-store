# from sqlalchemy import (
#     Column,
#     Integer,
#     Text,
#     )

# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import (
#     scoped_session,
#     sessionmaker,
#     )

# from zope.sqlalchemy import ZopeTransactionExtension

# DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
# Base = declarative_base()

# class Call(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text, unique=True)
#     state = Column(Text)
#     app_number = Column(Integer)

#     def __init__(self, title = 'default', current = '', app_number = -1):
#         self.name = title
#         self.state = current
#         self.app_number = app_number

# def populate():
#     session=DMSession()
#     model1=status(title='MatLab', current="Not Available",app_number=1)
#     model2=status(title='MatLab + toolbox', current="Not Available", app_number=2)
#     session.add(model1)
#     session.add(model2)
#     session.flush()
#     transaction.commit()


# def initialize_sql(engine):
#     DBSession.configure(bind=engine)
#     Base.metadata.bind = engine
#     Base.metadata.create_all(engine)
#     try:
#         #session = DBSession()
#         #page = Page('FrontPage', 'initial data')
#         #session.add(page)
#         #transaction.commit()
#         populate()
#     except IntegrityError:
#         # already created
#         pass

from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Page(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    data = Column(Text)

    def __init__(self, name, data):
        self.name = name
        self.data = data

