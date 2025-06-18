#PROJECT NAME: STUDENT GRADE ANALYZER
-------------------------------------

The purpose of this project, STUDENT GRADE ANALYZER, is to provide a simple yet powerful tool to manage and analyze student grades using C++.
It allows users to create multiple student profiles and dynamically add or remove grades without any fixed limit, better to the use of dynamic memory allocation. The program calculates key academic metrics such as the average and maximum grade for each student using object-oriented principles, including inheritance and polymorphism. Through a clear, menu-driven interface, users can easily interact with the system to input data and retrieve meaningful results. This project also emphasizes important programming concepts like memory management using pointers, the use of arrays, structs, and virtual classes. Overall, it serves as a practical educational tool for understanding student performance and deepening knowledge of core C++ features in real-life applications.


ASSIGNED TASK FOR MY PROJECT
----------------------------
The objective was to develop a C++ program that:
a) Allows managing student names and their dynamically-sized grade lists.
b) Computes grade metrics: Average and Maximum.
c) Demonstrates concepts like:
   i) Inheritance & Polymorphism
   ii) Abstract classes
   iii) Pointer arithmetic
   iv) Dynamic memory management
d) Provides a user-friendly, menu-driven interface.

TASK IMPLEMENTATION
--------------------
- Struct `Student` is used to store names and a dynamic array of grades.
- Functions `addGrade()` and `removeGrade()` handle dynamic memory operations.
- Abstract class `GradeMetric` is extended by:
  - `AverageMetric` – computes average.
  - `MaxMetric` – computes highest grade.
- Menu interface supports:
  1. Add student
  2. Switch between students
  3. Add/remove grades
  4. Compute metrics
  5. Exit program
- All memory is properly managed and released before exit.

FEATURES
--------
1. Add & switch between multiple students
2. Dynamically add or remove grades
3. Compute average & max grade
4. Simple, interactive console menu




#include <iostream>    //  I included the input/output stream library to use cin, cout, etc.
#include <cstring>     // I included C-style string functions like strcpy, etc.
#include <vector>      // Includes the STL vector container to dynamically store students
using namespace std;  // Allows us to use standard C++ features without prefixing with 'std::'

// This is Struct to hold student data include names, grades, and the number of grades.
struct Student {
    char name[30];       // A fixed-size character array to store the student's name
    float* grades;       // A pointer that will dynamically point to an array of grades
    int nGrades;         // An integer to track how many grades are stored

    // Constructor initializes the grades pointer to null and grade count to 0
    Student() : grades(nullptr), nGrades(0) {}

    // Destructor releases memory allocated to grades to prevent memory leaks
    ~Student() { delete[] grades; }
};

//This is a function to add a grade to the student, after selecting or adding one.
void addGrade(Student& student, float newGrade) {
    // This code allocate a new array with space for one additional grade
    float* newArray = new float[student.nGrades + 1];

    // This line is to copy the existing grades to the new array, so as to retain origin student's data.
    for (int i = 0; i < student.nGrades; ++i)
        *(newArray + i) = *(student.grades + i);

    // This line add the new grade at the end
    *(newArray + student.nGrades) = newGrade;

    // Free the old grades array to prevent memory leaks
    delete[] student.grades;

    // Point the student to the new array and increment the grade count
    student.grades = newArray;
    student.nGrades++;
}

// This is function to remove a grade from the student by using indexes.
void removeGrade(Student& student, int index) {
    // This line Validate index is within valid range
    if (index < 0 || index >= student.nGrades) {
        cout << "Invalid index!\n";
        return;
    }

    // This line is to create a new array with one less element
    float* newArray = new float[student.nGrades - 1];

    // Copy all grades except the one at the specified index
    for (int i = 0, j = 0; i < student.nGrades; ++i) {
        if (i != index)
            *(newArray + j++) = *(student.grades + i);
    }

    // Free the old array and assign the new one
    delete[] student.grades;
    student.grades = newArray;
    student.nGrades--;
}

// This is an abstract base class for metrics
class GradeMetric {
public:
    // Pure virtual function that must be implemented by derived classes
    virtual float compute(const Student* student) = 0;

    // Virtual destructor to allow proper cleanup when using base class pointers
    virtual ~GradeMetric() {}
};

// This is Derived class to compute average of the grades for selected student.
class AverageMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        float sum = 0;
        // Sum all grades
        for (int i = 0; i < student->nGrades; ++i)
            sum += *(student->grades + i);
        // Return average, or 0 if there are no grades
        return student->nGrades > 0 ? sum / student->nGrades : 0;
    }
};

// Derived class to compute maximum grade from the grades added to any student.
class MaxMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        // This line is to return 0, If no grades exist, 
        if (student->nGrades == 0) return 0;

        // Start by assuming first grade is max
        float max = *(student->grades);
        // Tis is the lines to check each grade and update maximum if needed
        for (int i = 1; i < student->nGrades; ++i)
            if (*(student->grades + i) > max)
                max = *(student->grades + i);
        return max;
    }
};

// This is function to display a student's grades.
void displayGrades(const Student& student) {
    cout << "\nGrades for " << student.name << ":\n";
    for (int i = 0; i < student.nGrades; ++i)
        cout << " [" << i << "] " << *(student.grades + i) << endl;
    if (student.nGrades == 0)
        cout << " No grades available.\n";
}

// This is the main menu system to interact with user. it includes the list of choices.
void menu() {
    vector<Student*> students;  // A list of dynamically created students
    GradeMetric* metrics[2];    // Array of metric pointers (average and max)
    metrics[0] = new AverageMetric();
    metrics[1] = new MaxMetric();

    int currentIndex = -1;  // Tracks the currently selected student
    int choice;             // User's menu choice

    do {
        // Display current status and menu options
        cout << "\nSTUDENT GRADE ANALYSER MENU\n___________________________\n";
        if (currentIndex != -1)
            cout << "Current student: " << students[currentIndex]->name << "\n";
        else
            cout << "Status: No student selected. Please select of add one student\n";

        cout << "1. Add New Student\n";
        cout << "2. Switch Student\n";
        cout << "3. Add Grade\n";
        cout << "4. Remove Grade by Index\n";
        cout << "5. Show Grades\n";
        cout << "6. Compute Average & Maximum\n";
        cout << "7. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;
        cin.ignore();  // Clear newline character from buffer

        switch (choice) {
            case 1: {
                // This lines adding new student, to the array created as storage
                Student* newStudent = new Student();
                cout << "Enter new student names: ";
                cin.getline(newStudent->name, 30);  // Read full name
                students.push_back(newStudent);     // Store student in list
                currentIndex = students.size() - 1; // Make new student current
                cout << "\xF0\x9F\x93\x8CStudent added and selected.\n";
                break;
            }
            case 2:
                if (students.empty()) {
                    cout << "No students available. Add one first.\n";
                    break;
                }
                // Show all students and let user pick one
                cout << "\nAvailable Students:\n";
                for (int i = 0; i < students.size(); ++i)
                    cout << " [" << i << "] " << students[i]->name << endl;
                cout << "Select student index: ";
                cin >> currentIndex;
                // Validate index
                if (currentIndex < 0 || currentIndex >= students.size()) {
                    cout << "Invalid index!\n";
                    currentIndex = -1;
                }
                break;
            case 3:
                if (currentIndex == -1) {
                    cout << "Please add or select a student first.\n";
                    break;
                }
                float grade;
                cout << "Enter grade to add: ";
                cin >> grade;
                addGrade(*students[currentIndex], grade);
                break;
            case 4:
                if (currentIndex == -1) {
                    cout << "Please add or select a student first.\n";
                    break;
                }
                int index;
                displayGrades(*students[currentIndex]);
                cout << "Enter index to remove: ";
                cin >> index;
                removeGrade(*students[currentIndex], index);
                break;
            case 5:
                if (currentIndex == -1) {
                    cout << "Please add or select a student first.\n";
                    break;
                }
                displayGrades(*students[currentIndex]);
                break;
            case 6:
                if (currentIndex == -1) {
                    cout << "Please add or select a student first.\n";
                    break;
                }
                // Use polymorphism to compute metrics
                cout << "\nAverage: " << metrics[0]->compute(students[currentIndex]) << endl;
                cout << "Maximum: " << metrics[1]->compute(students[currentIndex]) << endl;
                break;
            case 7:
                cout << "Exiting system...\n";
                break;
            default:
                cout << "Invalid choice. Try again.\n";
        }

    } while (choice != 7);  // Repeat until user chooses to exit

    // Below lines cleanup memory to prevent memory leaks
    delete metrics[0];
    delete metrics[1];
    for (Student* s : students)
        delete s;
}

// This is the program entry point.
int main() {
    menu();  // Launch the interactive menu
    return 0;
}

