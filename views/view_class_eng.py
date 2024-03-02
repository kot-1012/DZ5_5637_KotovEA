# views/view_class_eng.py

class ViewClassEng:
    """Класс представления на английском языке."""

    def __init__(self, teacher, student_list):
        """Инициализация представления."""
        self.teacher = teacher
        self.student_list = student_list

    def get_view(self):
        """Получает представление в виде строки."""
        view = "Teacher: {}\nStudents: {}".format(self.teacher, ", ".join(self.student_list))
        return view