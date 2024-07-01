from sqlalchemy import create_engine, MetaData, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

import json

with open('bars.json', 'r') as j:
    bars = json.load(j)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/krasnodarbars')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BarModel(Base):
    __tablename__ = 'bar'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    inst_url = Column(String, nullable=True)
    vk_url = Column(String, nullable=True)
    tg_url = Column(String, nullable=True)


Base.metadata.create_all(engine)

with session:
    for bar in bars:
        bar_to_add = BarModel(name=bar.get('Заведения'),
                              inst_url=bar.get('Instagram'),
                              vk_url=bar.get('Vk'),
                              tg_url=bar.get('Telegram'))
        session.add(bar_to_add)
        session.commit()