from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class usr_info_tbl(Base):
    __tablename__ = "usr_info_tbl"

    usr_id = Column(Integer, primary_key=True, increment=1)
    birth_date = Column(String)
    full_name = Column(String)
    usr_email = Column(String, unique=True, index=True)
    usr_pass = Column(String)
    usr_favcolor = Column(String)

   


class cloths_top_tbl(Base):
    __tablename__ = "cloths_top_tbl"

    cloths_top_id = Column(Integer, primary_key=True,increment=1)
    img_path = Column(String)
    cloth_color=Column(String)
    cloth_type = Column(String)
    usr_id = Column(Integer, ForeignKey("usr_info_tbl.usr_id"))
    

class cloths_bottom_tbl(Base):
    __tablename__ = "cloths_bottom_tbl"

    cloths_bottom_id = Column(Integer, primary_key=True,increment=1)
    img_path = Column(String)
    cloth_color=Column(String)
    cloth_type = Column(String)
    usr_id = Column(Integer, ForeignKey("usr_info_tbl.usr_id"))
    
    
class closet_tbl(Base):
    __tablename__ = "closet_tbl"

    closet_id = Column(Integer, primary_key=True,increment=1)
    img_path = Column(String)
    likes=Column(String)
    dislikes = Column(String)
    date_worn = Column(String)
    usr_id = Column(Integer, ForeignKey("usr_info_tbl.usr_id"))
    cloths_top_id = Column(Integer, ForeignKey("cloths_top_tbl.cloths_top_id"))
    cloths_bottom_id = Column(Integer, ForeignKey("cloths_bottom_tbl.cloths_bottom_id"))
  
