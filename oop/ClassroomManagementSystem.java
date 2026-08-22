import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

public class ClassroomManagementSystem {
    static class Student {
        private final int studentId;
        private final String name;
        private final String branch;

        Student(int studentId, String name, String branch) {
            this.studentId = studentId;
            this.name = name;
            this.branch = branch;
        }

        @Override
        public boolean equals(Object object) {
            if (this == object) return true;
            if (!(object instanceof Student)) return false;
            Student other = (Student) object;
            return studentId == other.studentId;
        }

        @Override
        public int hashCode() {
            return Objects.hash(studentId);
        }
    }

    static class Classroom {
        private final String classroomId;
        private final String course;
        private final Set<Student> students = new HashSet<>();

        Classroom(String classroomId, String course) {
            this.classroomId = classroomId;
            this.course = course;
        }

        void addStudent(Student student) {
            students.add(student); // Same student ID cannot be added twice.
        }

        int getStudentCount() {
            return students.size();
        }
    }

    private final Map<String, Classroom> classrooms = new HashMap<>();

    public void addClassroom(String classroomId, String course) {
        classrooms.put(classroomId, new Classroom(classroomId, course));
    }

    public void addStudentToClassroom(String classroomId, Student student) {
        Classroom classroom = classrooms.get(classroomId);
        if (classroom == null) {
            throw new IllegalArgumentException("Classroom not found: " + classroomId);
        }
        classroom.addStudent(student);
    }

    public Classroom getClassroomWithMostStudents() {
        return classrooms.values().stream()
                .max(Comparator.comparingInt(Classroom::getStudentCount))
                .orElse(null);
    }
}
