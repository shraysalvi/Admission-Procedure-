file = open(r'F:\Python material\pycharm\applicant_list_5.txt', 'r')
x = file.readlines()
file.close()
applications = []
for _ in x:
    n = _.split()
    applications.append(n)

Biotech = []
Chemistry = []
Mathematics = []
Engineering = []
Physics = []
already = []

till = int(input())

for check in [6, 7, 8]:
    for sub in range(2, 6):
        applications.sort(key=lambda x: (-float(x[sub]), x[0], x[1]))
        for applicant in applications:
            if sub == 3 and applicant[check] == "Biotech" and len(Biotech) < till and applicant not in already:
                Biotech.append(applicant)
                already.append(applicant)

            elif sub == 3 and applicant[check] == "Chemistry" and len(Chemistry) < till and applicant not in already:
                Chemistry.append(applicant)
                already.append(applicant)

            elif sub == 5 and applicant[check] == "Engineering" and len(Engineering) < till and applicant not in already:
                Engineering.append(applicant)
                already.append(applicant)

            elif sub == 4 and applicant[check] == "Mathematics" and len(Mathematics) < till and applicant not in already:
                Mathematics.append(applicant)
                already.append(applicant)

            elif sub == 2 and applicant[check] == "Physics" and len(Physics) < till and applicant not in already:
                Physics.append(applicant)
                already.append(applicant)

Biotech.sort(key=lambda x: (-float(x[3]), x[0], x[1]))
Chemistry.sort(key=lambda x: (-float(x[3]), x[0], x[1]))
Engineering.sort(key=lambda x: (-float(x[5]), x[0], x[1]))
Mathematics.sort(key=lambda x: (-float(x[4]), x[0], x[1]))
Physics.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

result = {'Biotech':Biotech, 'Chemistry':Chemistry, 'Engineering':Engineering, 'Mathematics':Mathematics, 'Physics':Physics}

for _ in result:
    print(_)
    for finals in result[_]:
        if _ == "Physics":
            x = 2
        elif _ == "Chemistry":
            x = 3
        elif _ == "Mathematics":
            x = 4
        elif _ == "Biotech":
            x = 3
        elif _ == "Engineering":
            x = 5
        print(finals[0], finals[1], finals[x])
    print()