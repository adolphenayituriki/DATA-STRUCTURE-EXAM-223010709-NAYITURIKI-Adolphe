#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

//Struct to hold student data
struct Student {
    char name[30];
    float* grades;
    int nGrades;

    Student() : grades(nullptr), nGrades(0) {}
    ~Student() { delete[] grades; }
};

//This is Dynamic grade functions
void addGrade(Student& student, float newGrade) {
    float* newArray = new float[student.nGrades + 1];
    for (int i = 0; i < student.nGrades; ++i)
        *(newArray + i) = *(student.grades + i);
    *(newArray + student.nGrades) = newGrade;

    delete[] student.grades;
    student.grades = newArray;
    student.nGrades++;
}

void removeGrade(Student& student, int index) {
    if (index < 0 || index >= student.nGrades) {
        cout << "Invalid index!\n";
        return;
    }

    float* newArray = new float[student.nGrades - 1];
    for (int i = 0, j = 0; i < student.nGrades; ++i) {
        if (i != index)
            *(newArray + j++) = *(student.grades + i);
    }

    delete[] student.grades;
    student.grades = newArray;
    student.nGrades--;
}

//Abstract base class
class GradeMetric {
public:
    virtual float compute(const Student* student) = 0;
    virtual ~GradeMetric() {}
};

//This is Derived metric classes
class AverageMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        float sum = 0;
        for (int i = 0; i < student->nGrades; ++i)
            sum += *(student->grades + i);
        return student->nGrades > 0 ? sum / student->nGrades : 0;
    }
};

class MaxMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0;
        float max = *(student->grades);
        for (int i = 1; i < student->nGrades; ++i)
            if (*(student->grades + i) > max)
                max = *(student->grades + i);
        return max;
    }
};

//Class to Display grades
void displayGrades(const Student& student) {
    cout << "\nGrades for " << student.name << ":\n";
    for (int i = 0; i < student.nGrades; ++i)
        cout << " [" << i << "] " << *(student.grades + i) << endl;
    if (student.nGrades == 0)
        cout << " No grades available.\n";
}

//Class to display Menu system,
void menu() {
    vector<Student*> students;
    GradeMetric* metrics[2];
    metrics[0] = new AverageMetric();
    metrics[1] = new MaxMetric();

    int currentIndex = -1;
    int choice;

    do {
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
        cin.ignore();

        switch (choice) {
            case 1: {
                Student* newStudent = new Student();
                cout << "Enter new student names: ";
                cin.getline(newStudent->name, 30);
                students.push_back(newStudent);
                currentIndex = students.size() - 1;
                cout << "Student added and selected.\n";
                break;
            }
            case 2:
                if (students.empty()) {
                    cout << "No students available. Add one first.\n";
                    break;
                }
                cout << "\nAvailable Students:\n";
                for (int i = 0; i < students.size(); ++i)
                    cout << " [" << i << "] " << students[i]->name << endl;
                cout << "Select student index: ";
                cin >> currentIndex;
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
                cout << "\nAverage: " << metrics[0]->compute(students[currentIndex]) << endl;
                cout << "Maximum: " << metrics[1]->compute(students[currentIndex]) << endl;
                break;
            case 7:
                cout << "Exiting system...\n";
                break;
            default:
                cout << "Invalid choice. Try again.\n";
        }

    } while (choice != 7);

    // Cleanup
    delete metrics[0];
    delete metrics[1];
    for (Student* s : students)
        delete s;
}

//The nain function
int main() {
    menu();
    return 0;
}
