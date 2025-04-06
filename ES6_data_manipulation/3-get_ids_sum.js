export default function getStudentIdsSum(students) {
    if (students instanceof Array) {
        return students.reduce(
            (prevSTUDENT, curStudent) => prevStudent.id || prevStudent + curStudent.id,
            0,
        );
    }
    return 0;
}
