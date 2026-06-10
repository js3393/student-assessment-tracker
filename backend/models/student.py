from pydantic import BaseModel
class Student(BaseModel):
    date: str
    student_id: int
    first_name: str
    last_name: str
    grade_level: str
    age: str
    overall_grade: float
    teacher_name: str
    attendance: bool | None = None
    project_progress: float
        
    @staticmethod
    def get_id(self, student_id):
        return self.student_id

    @staticmethod
    def get_overall_grade(self, overall_grade):
        return self.overall_grade

    @staticmethod
    def get_attendance(self, attendance):
        return self.attendance

    @staticmethod
    def get_project_progress(self):
        return self.project_progress




