from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer

Base = declarative_base()

class Kunde(Base):
	__tablename__ = "kunder"
	id = Column(Integer, primary_key=True)
	efternavn = Column(String)
	kontakt = Column(String)
	auth = Column(Integer)

	def __repr__(self):
		return f"Kunde({self.id=}    {self.efternavn=}    {self.kontakt=}    {self.auth=})"

	def convert_to_tuple(self):
		return self.id, self.efternavn, self.kontakt, self.auth

	def valid(self):
		try:
			value = int(self.auth)
		except ValueError:
			return False
		return value >= 0

class Rejse(Base):
	__tablename__ = "rejser"
	id = Column(Integer, primary_key=True)
	rute = Column(String)
	dato = Column(String)
	pladskapacitet = Column(Integer)

	def __repr__(self):
		return f"Rejse({self.id=}    {self.rute=}    {self.dato=}    {self.pladskapacitet=})"

	def convert_to_tuple(self):
		return self.id, self.rute, self.dato, self.pladskapacitet

	def valid(self):
		try:
			value = int(self.pladskapacitet)
		except ValueError:
			return False
		return value >= 0

class Booking(Base):
	__tablename__ = "bookinger"
	id = Column(Integer, primary_key=True)
	kundeid = Column(Integer, ForeignKey("kunder.id"), nullable=False)
	rejseid = Column(Integer, ForeignKey("rejser.id"), nullable=False)
	pladser = Column(Integer)

	def __repr__(self):
		return f"Booking({self.id=}    {self.rejseid=}    {self.kundeid=}    {self.pladser=})"

	def convert_to_tuple(self):
		return self.id, self.rejseid, self.kundeid, self.pladser

	def valid(self):
		try:
			value = int(self.pladser)
		except ValueError:
			return False
		return value >= 0

class PermissionLevel:
	LOW = 0
	HIGH = 1