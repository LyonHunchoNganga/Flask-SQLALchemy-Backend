from app import app
from models import db, Exercise
from datetime import date

with app.app_context():
    print("Seeding database...")

    # clear existing data
    Exercise.query.delete()

    # add sample exercises
    e1 = Exercise(name="Push Ups", category="strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="cardio", equipment_needed=False)
    e3 = Exercise(name="Stretching", category="flexibility", equipment_needed=False)

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print("Done seeding!")