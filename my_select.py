from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher
from sqlalchemy.orm import sessionmaker
from models import engine

Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade'))\
            .limit(5).all()


def select_2(subject_id):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id == subject_id)\
            .group_by(Student.id)\
        .order_by(desc('avg_grade')).first()


def select_3(subject_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id == subject_id)\
            .group_by(Student.group_id).all()


def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).first()


def select_5(teacher_id):
    return session.query(Teacher.fullname, Subject.name)\
        .select_from(Teacher).join(Grade).join(Subject)\
        .filter(Teacher.id == teacher_id).group_by(Teacher.fullname, Subject.name).all()


def select_6(group_id):
    return session.query(Student.fullname)\
        .select_from(Student).filter(Student.group_id == group_id).all()


def select_7(group_id, subject_id):
    return session.query(Student.fullname, Grade.grade)\
        .select_from(Student).join(Grade).join(Subject)\
        .filter(Student.group_id == group_id, Subject.id == subject_id).all()


def select_8(teacher_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Teacher).join(Subject)\
        .filter(Teacher.id == teacher_id).group_by(Teacher.fullname).first()


def select_9(student_id):
    return session.query(Subject.name)\
        .select_from(Subject).join(Grade).join(Student)\
        .filter(Student.id == student_id).group_by(Subject.name).all()


def select_10(student_id, teacher_id):
    return session.query(Subject.name)\
        .select_from(Subject).join(Grade).join(Student).join(Teacher)\
        .filter(Student.id == student_id, Teacher.id == teacher_id).group_by(Subject.name).all()


def select_avg_grade_for_student_by_teacher(student_id, teacher_id):
    return session.query(func.avg(Grade.grade)).select_from(Grade).join(Student).join(Teacher)\
        .filter(Student.id == student_id, Teacher.id == teacher_id).scalar()


def select_grades_for_student_in_group_by_subject(student_id, group_id, subject_id):
    return session.query(Grade.grade)\
        .select_from(Grade).join(Student).join(Subject)\
        .filter(Student.id == student_id, Student.group_id == group_id, Subject.id == subject_id)\
        .order_by(Grade.date.desc()).limit(1).scalar()


if __name__ == "__main__":
    print(select_1())  
