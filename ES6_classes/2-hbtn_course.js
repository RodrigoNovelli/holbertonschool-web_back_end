class HolbertonCourse {
  constructor(name, lenght, students) {
    this.name = name;
    this.lenght = lenght;
    this.students = students;
  }

  /**
   * @param {String} name
   */
  set name(name) {
    if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
    }
    this._name = name;
  }

  get name() {
    return this._name;
  }

  /**
   * @param {Number} length
   */
  set lenght(lenght) {
    if (typeof lenght !== 'number') {
        throw new TypeError('Length must be a number')
    }
    this._length = lenght;
  }

  get lenght() {
    return this._length;
  }

  /**
   * @param {Array} students
   */
  set students(students) {
    if (students instanceof Array) {
          this._students = students;
        } else {
            throw new TypeError('Students must be an Array');
        }
      }
      
  get students() {
    return this._students;
      }
    }
    
    export default HolbertonCourse;
