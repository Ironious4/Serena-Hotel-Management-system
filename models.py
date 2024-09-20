from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    reservations = relationship("Reservation", back_populates="guest")
    inventory_items = relationship("Inventory", back_populates="guest")


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    reservations = relationship("Reservation", back_populates="room")


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    check_in_date = Column(String, nullable=False)
    check_out_date = Column(String, nullable=False)

    guest = relationship("Guest", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")
 

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    guest_id = Column(Integer, ForeignKey('guests.id'))

    guest = relationship("Guest", back_populates="inventory_items")


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position= Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    tasks = relationship('Task', backref='staff')



