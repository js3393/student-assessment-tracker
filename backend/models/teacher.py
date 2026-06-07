class Teacher:
    def __init__(self, teacher_id, first_name, last_name, classroom, username, password):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = classroom
        self.username = username
        self.password = password

    @staticmethod
    def get_teacher_id(self, teacher_id):
        return self.teacher_id

    @staticmethod
    def get_classroom(self, classroom):
        return self.classroom
