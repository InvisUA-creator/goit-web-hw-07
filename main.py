import argparse
from models import Teacher, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    first_name, last_name = name.split()
    teacher = Teacher(first_name=first_name, last_name=last_name)
    session.add(teacher)
    session.commit()

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"{teacher.id}: {teacher.first_name} {teacher.last_name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', '-a', required=True)
    parser.add_argument('--model', '-m', required=True)
    parser.add_argument('--name', '-n', required=False)
    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create':
            create_teacher(args.name)
        elif args.action == 'list':
            list_teachers()

if __name__ == "__main__":
    main()
