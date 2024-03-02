# controllers/controller.py

class Controller:
    """Класс контроллера, управляющий взаимодействием между моделью и представлением."""

    def __init__(self):
        """Инициализация контроллера."""
        self.models = []

    def add_model(self, model):
        """Добавляет модель в список моделей контроллера."""
        self.models.append(model)

    def add_student(self, student_id, student):
        """Добавляет студента во все модели контроллера."""
        for model in self.models:
            model.add_student(student_id, student)

    def get_student(self, student_id):
        """Получает студента по его ID из всех моделей контроллера."""
        for model in self.models:
            student = model.get_student(student_id)
            if student:
                return student
        return None