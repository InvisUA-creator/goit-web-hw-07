from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import datetime
from models import Group, Teacher, Subject, Student, Grade, engine

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()



# Додавання груп
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Додавання викладачів
teachers = [Teacher(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Додавання предметів
subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(5)]
session.add_all(subjects)
session.commit()

# Додавання студентів
students = [Student(first_name=fake.first_name(), last_name=fake.last_name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Додавання оцінок
grades = [
    Grade(
        student=random.choice(students),
        subject=random.choice(subjects),
        grade=random.randint(50, 100),
        date=fake.date_between(start_date="-2y", end_date="today")
    )
    for _ in range(200)
]
session.add_all(grades)
session.commit()

session.close()
