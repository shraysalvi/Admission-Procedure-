# Admission Procedure

The Program is designed to streamline the admission process based on student performance and departmental priorities. The program utilizes the "application_list_*" files, which contains crucial student information in structured columns.

#### File Structure

Column 1: Student Name
Column 2: Student Surname
Column 3: Physics Marks
Column 4: Chemistry Marks
Column 5: Mathematics Marks
Column 6: Computer Marks
Column 7: First Priority Department
Column 8: Second Priority Department
Column 9: Third Priority Department

#### Functionality

- The program aims to assign students to departments based on their mean scores in relevant subjects and the priorities specified by the departments.
- Mean scores are calculated based on specific subject combinations for each department.
- If a student's mean score aligns with the requirements of their first priority department, they are assigned there. Otherwise, the program checks if their scores meet the criteria for other priority departments.
- Users input the number of students required for each department.
- Only students meeting departmental criteria are allotted positions.

Output Format:
Students meeting departmental criteria are listed in separate files named after each department (e.g., physics.txt).
Each file contains student names along with their mean scores.
This program streamlines the admission process, ensuring that students are assigned to departments based on their academic performance and departmental priorities, **resulting in efficient and fair admissions**.
