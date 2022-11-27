
cancer_data_list = [[0, 12, 41, 1],[1, 20, 44, 0],[0, 8, 30, 0],[0, 0, 25, 1],[0, 15, 36, 1],[1, 17, 42, 0],[0, 22, 40, 1],[0, 0, 61, 1],[1, 2, 64, 0],[1, 0, 60, 0],[0, 0, 78, 0],[0, 28, 60, 1],[0, 41, 72, 1],[0, 43, 62, 1],[1, 4, 72, 0],[0, 0, 81, 0],[1, 0, 59, 0],[0, 26, 55, 1],[1, 33, 59, 0],[0, 30, 48, 1],[1, 0, 56, 0],[0, 0, 61, 0],[0, 0, 64, 1],[0, 0, 73, 0],[0, 28, 64, 1],[0, 41, 61, 1],[1, 26, 46, 1],[0, 41, 62, 0],[1, 15, 38, 1],[1, 0, 25, 0],[1, 0, 28, 0],[0, 0, 82, 0],[1, 3, 24, 1],[1, 8, 29, 0],[0, 4, 22, 1],[1, 0, 17, 0],[1, 0, 75, 0],[1, 0, 71, 0],[0, 0, 72, 0],[0, 11, 38, 1],[0, 8, 32, 0],[0, 28, 54, 1],[0, 37, 65, 1],[0, 11, 30, 0],[1, 0, 87, 0],[1, 0, 82, 0],[1, 0, 49, 1],[1, 14, 40, 0],[1, 20, 50, 0],[0, 5, 25, 0]]

#Row 1 
def get_cancer_lst_1(cancer_data_list):
    lst = []
    for row in cancer_data_list:
        Veg = row[0]
        years_smoking = row[1]
        age = row[2]
        cancer_incident = row [3]
        if (Veg == 1) and (years_smoking <= 4) and (age <= 40):       
            lst.append(cancer_incident)
    return lst 

def get_risk(cancer_lst):
    cancer_count = 0 
    for i in cancer_lst:
        cancer_count += i
    risk = cancer_count / len(cancer_lst) * 100
    return risk

def make_string(risk):
    srisk = ""
    if risk <= 25:
        srisk += "LOW"
    elif 25 < risk < 75:
        srisk += "MEDIUM"
    elif risk >= 75:
        srisk +="HIGHT"
    return srisk

def row_1():
    cancer_lst = get_cancer_lst_1(cancer_data_list)
    risk = get_risk(cancer_lst)
    string = make_string(risk)
    print(f"Vegetraian: Yes, Years Smoking: 0-4, Age: <=40 then risk is {string}")

#Row 2
def get_cancer_lst_2(cancer_data_list):
    lst = []
    for row in cancer_data_list:
        Veg = row[0]
        years_smoking = row[1]
        age = row[2]
        cancer_incident = row [3]
        if (Veg == 1) and (years_smoking <= 4) and (age > 40):       
            lst.append(cancer_incident)
    return lst 

def row_2():
    cancer_lst = get_cancer_lst_2(cancer_data_list)
    risk = get_risk(cancer_lst)
    string = make_string(risk)
    print(f"Vegetraian: Yes, Years Smoking: 0-4, Age: > 40 then risk is {string}")

#Row 3
def get_cancer_lst_3(cancer_data_list):
    lst = []
    for row in cancer_data_list:
        Veg = row[0]
        years_smoking = row[1]
        age = row[2]
        cancer_incident = row [3]
        if (Veg == 1) and (years_smoking > 5) and (age <= 40):       
            lst.append(cancer_incident)
    return lst 

def row_3():
    cancer_lst = get_cancer_lst_3(cancer_data_list)
    risk = get_risk(cancer_lst)
    string = make_string(risk)
    print(f"Vegetraian: Yes, Years Smoking: 5+, Age: <= 40 then risk is {string}")

#Row 4...
#TODO define get_cancer_list_4 then def row_4()

def main():
    return row_1(), row_2(), row_3()

x = main()
print(x)





 
