from django.test import TestCase

from todo.models import Todo


class TestModel(TestCase):
    def test_todo_model_fields(self):
        obj = Todo(title='test')
        assert obj.title == 'test'
