from sqlalchemy import Column, String, Boolean
from sqlalchemy.util.preloaded import orm

Base = orm.declarative_base()

class Cam_list(Base):
    __tablename__ = "cam_list"

    cam_id = Column("cam_id", String, primary_key=True)
    cam_name = Column("cam_name", String)
    cam_link = Column("cam_link", String)
    cam_position_in_grid = Column('cam_position_in_grid', String)
    cam_status = Column('cam_status', Boolean)
    analytics_status = Column('analytics_status', Boolean)


    def __init__(self, cam_id, cam_name, cam_link, cam_position_in_grid, cam_status, analytics_status):
        self.cam_id = cam_id
        self.cam_name = cam_name
        self.cam_link = cam_link
        self.cam_position_in_grid = cam_position_in_grid
        self.cam_status = cam_status
        self.analytics_status = analytics_status


    def __repr__(self):
        return f'{self.cam_id}, {self.cam_name}, {self.cam_link}, {self.cam_position_in_grid}'
