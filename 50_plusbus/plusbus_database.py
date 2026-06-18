from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update

from plusbus_data import Base, Kunde, Booking, Rejse, PermissionLevel

Database = 'sqlite:///plusbus_database.db'

def select_all(table):
	with Session(engine) as session:
		records = session.scalars(select(table))
		result = []
		for record in records:
			result.append(record)
	return result

def get_all_bookinger(kundeid):
	with Session(engine) as session:
		records = session.scalars(select(Booking).where(Booking.kundeid == kundeid)).all()
	return records

def change_rejse_data(id_, rute, dato, pladskapacitet):
	with Session(engine) as session:
		session.execute(update(Rejse).where(Rejse.id == id_).values(rute=rute, dato=dato, pladskapacitet=pladskapacitet))
		session.commit()

def change_account_data(id_, efternavn, kontaktinfo):
	with Session(engine) as session:
		session.execute(update(Kunde).where(Kunde.id == id_).values(efternavn=efternavn, kontakt=kontaktinfo))
		session.commit()

def get_remaining_slots(id_):
	rejse = get_record(Rejse, id_)
	slots = rejse.pladskapacitet
	for bookinger in get_all_rejse_bookinger(rejse.id):
		if bookinger.valid():
			slots -= (bookinger.pladser if bookinger.pladser > 0 else 0)
	return slots

def get_admin_rejser():
	with Session(engine) as session:
		records = session.scalars(select(Rejse))
		result = []
		for record in records:
			if record.valid():
				record_list = record.convert_to_list()
				record_list.append(get_remaining_slots(record.id))
				result.append(record_list)
	return result

def change_booking_data(id_, pladser):
	with Session(engine) as session:
		session.execute(update(Booking).where(Booking.id == id_).values(pladser=pladser))
		session.commit()

def get_all_rejse_bookinger(rejseid):
	with Session(engine) as session:
		records = session.scalars(select(Booking).where(Booking.rejseid == rejseid)).all()
	return records

def create_test_data():
	with Session(engine) as session:
		test_data = []
		test_data.append(Kunde(efternavn="Petersen(Mig selv ja)", kontakt="Tlf. 27813897"))
		test_data.append(Kunde(efternavn="Hej", kontakt="test@gmail.com"))
		session.add_all(test_data)
		session.commit()

def insert_data(data):
	with Session(engine) as session:
		session.add(data)
		session.flush()
		id_ = data.id
		session.commit()
	return id_

def soft_delete_booking(booking):
	with Session(engine) as session:
		session.execute(update(Booking).where(Booking.id == booking.id).values(pladser=-1))
		session.commit()

def soft_delete_account(kunde):
	with Session(engine) as session:
		session.execute(update(Kunde).where(Kunde.id == kunde.id).values(auth=-1))
		session.commit()

def soft_delete_rejse(rejse):
	with Session(engine) as session:
		session.execute(update(Rejse).where(Rejse.id == rejse.id).values(pladskapacitet=-1))
		session.commit()

def get_record(table, id_):
	with Session(engine) as session:
		record = session.scalars(select(table).where(table.id == id_)).first()
	return record


if __name__ == "__main__":
	engine = create_engine(Database, echo=False, future=True)
	Base.metadata.create_all(engine)
	# create_test_data()
	# insert_data(Kunde(efternavn="Lol", kontakt="Ingen"))
	if get_record(Kunde, 1) is None:
		print("Kunden findes ikke")
	else:
		print(f"#1: {get_record(Kunde, 1)}")
		print(select_all(Kunde))
else:
	engine = create_engine(Database, echo=False, future=True)
	Base.metadata.create_all(engine)
	if get_record(Kunde, 1) is None:
		insert_data(Kunde(efternavn="@admin", kontakt="", auth=PermissionLevel.HIGH))