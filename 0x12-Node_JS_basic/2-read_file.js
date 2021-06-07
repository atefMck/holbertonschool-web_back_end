const fs = require('fs');

module.exports = function countStudents(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      throw new Error('Cannot load the database');
    }
    const fields = {};
    const students = data.split('\n').map((student) => student.split(','));
    students.shift();

    console.log(`Number of students: ${students.length}`);
    students.forEach((student) => {
      if (!fields[student[3]]) fields[student[3]] = [];
      fields[student[3]].push(student[0]);
    });
    Object.keys(fields).forEach((key) => {
      console.log(`Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`);
    });
  });
};
