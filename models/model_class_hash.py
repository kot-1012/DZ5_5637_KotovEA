# models/model_class_hash.py
from collections import defaultdict

from models.student import student

class ModelClassHash:
    """Класс модели с хранилищем типа HashMap<int, Student>."""

    def __init__(self):
        """Инициализация модели."""
        self.hash_map = defaultdict(student)

    def add_student(self, student_id, student):
        """Добавляет студента в хранилище."""
        self.hash_map[student_id] = student

    def get_student(self, student_id):
        """Получает студента из хранилища по его ID."""
        return self.hash_map.get(student_id)

    def delete_student(self, student_id):
        """Удаляет студента из хранилища по его ID."""
        if student_id in self.hash_map:
            del self.hash_map[student_id]
            return True
        else:
            return False