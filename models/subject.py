from sqlalchemy import Column, String, Integer, ForeignKey,Table

from sqlalchemy.orm import relationship
from .database import Base


table_relationship = Table(
    "relationship_between_tables",
    Base.metadata, Column("subject_id", Integer, ForeignKey("subjects.id")),
    Column("group_id", Integer, ForeignKey("groups.id"))

)


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    groups = relationship("Group", secondary=table_relationship, backref="group_subject")

    def __repr__(self):
        return f"Subject ID - {self.id} with Name - {self.title}"