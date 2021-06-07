export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Array.isArray(students)) {
    return students.filter((student) => student.location === city).map((student) => {
      const grade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: grade?.grade || 'N/A',
      };
    });
  }
  return 0;
}
