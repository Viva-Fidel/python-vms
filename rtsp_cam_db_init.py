from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rtsp_cam_list(Base):
    __tablename__ = "rtsp_cam_list"

    #cam_id = Column("cam_id", Integer, primary_key=True)
    cam_name = Column("cam_name", String, primary_key=True)
    cam_link = Column("cam_link", String)

    def __init__(self, cam_name, cam_link):
        #self.cam_id = cam_id
        self.cam_name = cam_name
        self.cam_link = cam_link

    #def __repr__(self):
        #return f'{self.cam_id}, {self.cam_name}, {self.cam_link}'

engine = create_engine('sqlite:///rtsp_cam_list.db', echo=True)
Base.metadata.create_all(bind=engine)