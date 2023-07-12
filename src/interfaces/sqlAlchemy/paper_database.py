import os
import uuid

import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

from utils.paper import Paper

Base = declarative_base()


class DataBasePaper(Base):
    __tablename__ = "local_analysis"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = sql.Column(sql.Uuid, primary_key=True)
    name = sql.Column(sql.String)
    url = sql.Column(sql.String)
    publication_date = sql.Column(sql.String)
    authors = sql.Column(sql.String)
    quotations = sql.Column(sql.Integer)
    content = sql.Column(sql.LargeBinary)

    def __init__(self, paper: Paper) -> None:
        self.id = uuid.uuid4()
        self.name = paper.name
        self.url = paper.url
        self.publication_date = paper.publication_date
        self.authors = str(paper.authors)
        self.quotations = paper.quotations
        self.content = paper.content


def generate_database(database_type: str, base, **kwargs):
    engine = None
    if database_type == "sqlite":
        engine = sql.create_engine(
            f'sqlite:///{os.getcwd()}/resources/{kwargs.get("database_name")}',
            echo=True
        )
    elif database_type == "postgresql":
        engine = sql.create_engine(
            f"postgresql+pyscopg2://{kwargs.get('url')}",
            echo=True
        )

    base.metadata.create_all(engine)


# generate_database("sqlite", Base, database_name="test.db")
