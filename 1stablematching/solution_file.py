import sys
import time

def remove_student_pairing(company_students, company_nr, new_student, students):
    students.append(company_students[company_nr - 1])
    company_students[company_nr - 1] = new_student


def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))



    # Number of companies and students, taking account to possibly weird data
    N = int(input_lines[0].split()[0])
    proper_data = []
    
    # Restructure data thas has weird line breaks
    new_list = " ".join(input_lines).split()[1:] #disregeard linebreaks
    # each row should have N+1 elements after resutructuring, append N+1 long segments
    for i in range(len(new_list)//(N + 1)):
        proper_data.append((new_list[(N + 1) * i: (N + 1) * i + N + 1]))

    # For handling input, to see if first number represents company_i or student_i
    company_parsed = [False for _ in range(N)]

    # Preference list of companies where i is student and value is how much valued student is 1 is best
    companies_preference = [[] for _ in range(N)]

    # Students preferences with ID
    students_preference = [[] for _ in range(N)]

    # student dedicated to company_i. default to -1
    company_students = [[-1] for _ in range(N)]

    for i, line in enumerate(proper_data):
        # unit can be both student and company
        unit_i = int(line[0]) - 1
        if not company_parsed[unit_i]:
            # change the list to mean index is student_i and value of index i is how much the company wants student_i
            companies_preference[unit_i] = [0 for _ in range(N)]
            for n in range(N):
                companies_preference[unit_i][ int( line[n+1] ) - 1 ] = n+1 #index magic
            company_parsed[unit_i] = True
        else:
            students_preference[unit_i] = line

    while len(students_preference) > 0:
        # Remove student from list and try to apply
        student = students_preference.pop(0)
        # Remove company index in student pref list to indicate that student has applied to company
        best_company = int(student.pop(1))

        #Best company has no student
        if company_students[best_company - 1] == [-1]:
            company_students[best_company - 1] = student

        #best company elrady has student, need to compare
        else:
            comp = companies_preference[best_company - 1]
            company_preference_for_new_student = comp[int(student[0]) - 1]
            company_preference_for_old_student = comp[int(company_students[best_company - 1][0]) - 1]

            #compare if new student is better fit for company than its current student
            if company_preference_for_new_student < company_preference_for_old_student:
                remove_student_pairing(company_students, best_company, student, students_preference)

            else:
                students_preference.append(student)

    for i in company_students:
        print(i[0])


if __name__ == "__main__":
    main()
