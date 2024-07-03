from . import db

class BarModel(db.Model):
    __tablename__ = 'bar'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    inst_url = db.Column(db.String, nullable=True)
    vk_url = db.Column(db.String, nullable=True)
    tg_url = db.Column(db.String, nullable=True)

    def __init__(self, name, inst_url=None, vk_url=None, tg_url=None):
        self.name = name
        self.inst_url = inst_url
        self.vk_url = vk_url
        self.tg_url = tg_url

    @classmethod
    def find_bar_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()