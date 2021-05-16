file = open(r'F:\Python material\pycharm\applicant_list_6.txt', 'r')
x = file.readlines()
file.close()
new_list = []
for _ in x:
    n = _.split()
    new_list.append(n)

applications = []
for _ in new_list:
    applications.append([_[0], _[1], _[6], _[7], _[8], int(_[2])/2+int(_[4])/2, float(_[3]), float(_[4]), int(_[4])/2+int(_[5])/2, int(_[2])/2+int(_[3])/2])

Biotech = []
Chemistry = []
Mathematics = []
Engineering = []
Physics = []
already = []

till = int(input())

for check in [2, 3, 4]:
    for sub in range(5, 10):
        applications.sort(key=lambda x: (-float(x[sub]), x[0], x[1]))
        for applicant in applications:
            if sub == 9 and applicant[check] == "Biotech" and len(Biotech) < till and applicant not in already:
                Biotech.append(applicant)
                already.append(applicant)

            elif sub == 6 and applicant[check] == "Chemistry" and len(Chemistry) < till and applicant not in already:
                Chemistry.append(applicant)
                already.append(applicant)

            elif sub == 8 and applicant[check] == "Engineering" and len(Engineering) < till and applicant not in already:
                Engineering.append(applicant)
                already.append(applicant)

            elif sub == 7 and applicant[check] == "Mathematics" and len(Mathematics) < till and applicant not in already:
                Mathematics.append(applicant)
                already.append(applicant)

            elif sub == 5 and applicant[check] == "Physics" and len(Physics) < till and applicant not in already:
                Physics.append(applicant)
                already.append(applicant)

Biotech.sort(key=lambda x: (-float(x[9]), x[0], x[1]))
Chemistry.sort(key=lambda x: (-float(x[6]), x[0], x[1]))
Engineering.sort(key=lambda x: (-float(x[8]), x[0], x[1]))
Mathematics.sort(key=lambda x: (-float(x[7]), x[0], x[1]))
Physics.sort(key=lambda x: (-float(x[5]), x[0], x[1]))

bio_file = open(r'biotech.txt', 'w', encoding='utf-8')
for _ in Biotech:
    bio_file.write(_[0] + " " + _[1] + " " + str(_[9]) + "\n")
bio_file.close()

che_file = open(r'chemistry.txt', 'w', encoding='utf-8')
for _ in Chemistry:
    che_file.write(_[0] + " " + _[1] + " " + str(_[6]) + "\n")
che_file.close()

eng_file = open(r'engineering.txt', 'w', encoding='utf-8')
for _ in Engineering:
    eng_file.write(_[0] + " " + _[1] + " " + str(_[8]) + "\n")
eng_file.close()

math_file = open(r'mathematics.txt', 'w', encoding='utf-8')
for _ in Mathematics:
    math_file.write(_[0] + " " + _[1] + " " + str(_[7]) + "\n")
math_file.close()

phy_file = open(r'physics.txt', 'w', encoding='utf-8')
for _ in Physics:
    phy_file.write(_[0] + " " + _[1] + " " + str(_[5]) + "\n")
phy_file.close()
