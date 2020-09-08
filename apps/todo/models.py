from sqlalchemy import Column, Integer, String
from database import Base


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(250))
    start_date = Column(String(25))
    status = Column(String(25))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date,
            "status": self.status
            }
