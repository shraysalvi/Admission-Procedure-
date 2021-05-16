file = open(r'F:\Python material\pycharm\applicant_list.txt', 'r')  #Opening file "I used my PC locatio for this file you can use your's"
x = file.readlines()
file.close()
applications = []
for _ in x:
    n = _.split()
    applications.append(n)
applications.sort(key=lambda x: (-float(x[2]), x[0], x[1]))  # sort file according to student gpa

Biotech = []
Chemistry = []
Mathematics = []
Physics = []
Engineering = []

till = int(input())
already = []

# the loops below is the main concept of the program which will decide department of student (I used list you can use disctionary instead, to short the program)
for sub in [3, 4, 5]:
    for applicant in applications:
        if applicant[sub] == "Biotech" and len(Biotech) < till and applicant not in already:
            Biotech.append(applicant)
            already.append(applicant)

        elif applicant[sub] == "Chemistry" and len(Chemistry) < till and applicant not in already:
            Chemistry.append(applicant)
            already.append(applicant)

        elif applicant[sub] == "Engineering" and len(Engineering) < till and applicant not in already:
            Engineering.append(applicant)
            already.append(applicant)

        elif applicant[sub] == "Mathematics" and len(Mathematics) < till and applicant not in already:
            Mathematics.append(applicant)
            already.append(applicant)

        elif applicant[sub] == "Physics" and len(Physics) < till and applicant not in already:
            Physics.append(applicant)
            already.append(applicant)

# Again sorting department files for clearification

Biotech.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
Chemistry.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
Engineering.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
Mathematics.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
Physics.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

result = {'Biotech':Biotech, 'Chemistry':Chemistry, 'Engineering':Engineering, 'Mathematics':Mathematics, 'Physics':Physics}

for _ in result:
    print(_)
    for _1 in result[_]:
        print(_1[0], _1[1], _1[2])
    print()
