from django.test import TestCase

from todo.models import Todo


class TestModel(TestCase):
    def test_todo_model_fields(self):
        obj = Todo(title='test')
        assert obj.title == 'test'

    def test_todo_create(self):
        obj = Todo.objects.create(title='test todo')
        assert obj.id is not None

    def test_todo_create_is_completed(self):
        obj = Todo.objects.create(title='first task')
        assert obj.is_completed is False, 'todo should has is_completed=False as default'

    def test_todo_mark_as_is_completed(self):
        obj = Todo.objects.create(title='first task')
        assert obj.is_completed is False, 'todo should has is_completed=False as default'

        obj.mark_as_completed()
        assert obj.is_completed is True, 'todo should change is_completed=True'

        obj.mark_as_uncompleted()
        assert obj.is_completed is False, 'todo should change is_completed=False'