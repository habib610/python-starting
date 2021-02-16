marks = {1: 45, 2: 56, 3: 67, 4: 45, 5: 78, 6: 98}
# print(marks[1])

final_marks = {"D001": {"Bangla": 56, "English": 45}, "D0002": {"Bangla": 46, "English": 77}}

# print(final_marks["D001"]["Bangla"])
# print(final_marks["D0002"]["English"])

BD_DIVISION_INFO = {}
BD_DIVISION_INFO["Dhaka"] = {"District": 13, "Upozila": 93, "Union": 1833  }
BD_DIVISION_INFO["Barisal"] = {"District": 6, "Upozila": 39, "Union": 333  }
BD_DIVISION_INFO["Chittagong"] = {"District": 11, "Upozila": 97, "Union": 336 }
BD_DIVISION_INFO["Khulna"] = {"District": 10, "Upozila": 59, "Union": 270 }
BD_DIVISION_INFO["Rangpur"] = {"District": 8, "Upozila": 58, "Union": 536 }

print(BD_DIVISION_INFO)
divisions =  BD_DIVISION_INFO.keys()

for divisions in BD_DIVISION_INFO:
    # print(divisions)
    pass


for divisions in BD_DIVISION_INFO:
    print(divisions, BD_DIVISION_INFO[divisions]["Upozila"])