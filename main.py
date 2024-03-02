# main.py
from controllers.controller import Controller
from models.model_class_hash import ModelClassHash
from models.student import student

def main():
    # Выбор языка
    language = input("Choose language (ENG/RUS): ").upper()

    # Создаем экземпляр контроллера
    controller = Controller()

    # Создаем и добавляем модели в контроллер
    model1 = ModelClassHash()
    model2 = ModelClassHash()
    controller.add_model(model1)
    controller.add_model(model2)

    # Добавляем студентов в модели
    student1 = student("Alice", 20)
    student2 = student("Bob", 21)
    controller.add_student(1, student1)
    controller.add_student(2, student2)

    # Получаем студента по его ID
    if language == "ENG":
     student_id = int(input("Enter student ID: "))
    elif language == "RUS": 
     student_id = int(input("Ведите ID студента: "))
    retrieved_student = controller.get_student(student_id)
    if retrieved_student:
        if language == "ENG":
            print("Student found - Name:", retrieved_student.name, ", Age:", retrieved_student.age)
        elif language == "RUS":
            print("Студент найден - Имя:", retrieved_student.name, ", Возраст:", retrieved_student.age)
        else:
            print("Unsupported language.")
    else:
        if language == "ENG":
            print("Student not found")
        elif language == "RUS":
            print("Студент не найден")
        else:
            print("Unsupported language.")

if __name__ == "__main__":
    main()
