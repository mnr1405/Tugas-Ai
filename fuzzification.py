import xlrd
import pandas as pd
import matplotlib.pyplot as plt


def readExcel(loc):
    mahasiswa = []
    ex = xlrd.open_workbook(loc)
    sheet = ex.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        mahasiswa.append(sheet.row_values(i))
    return mahasiswa


def fuzzificationLowIncome(income):
    if(income <= 3):
        low = 1
    elif(income >= 5):
        low = 0
    else:
        low = round((5-income)/(5-3), 3)
    return low, "low"


def fuzzificationAvarageIncome(income):
    if(income >= 6 and income <= 8):
        avarage = 1
    elif(income <= 3 or income >= 10):
        avarage = 0
    elif(income > 3 and income < 6):
        avarage = round((income-3)/(6-3), 3)
    else:
        avarage = round(-(income-10)/(10-8), 3)
    return avarage, "avarage"


def fuzzificationHighIncome(income):
    if(income >= 12):
        high = 1
    elif(income < 8):
        high = 0
    else:
        high = round((income-8)/(12-8), 3)
    return high, "high"


def fuzzificationLowExpense(expense):
    if(expense <= 3 and expense > 0):
        low = 1
    elif(expense >= 4):
        low = 0
    else:
        low = round((4-expense) / (4-3), 3)
    return low, "low"


def fuzzificationAvaregeExpense(expense):
    if(expense >= 5 and expense <= 8):
        avarage = 1
    elif(expense <= 3 or expense >= 9):
        avarage = 0
    elif(expense > 3 and expense < 5):
        avarage = round((expense - 3)/(5-3), 3)
    else:
        avarage = round(-(expense - 9)/(9-8), 3)
    return avarage, "avarage"


def fuzzificationHighExpense(expense):
    if(expense >= 10):
        high = 1
    elif(expense <= 8):
        high = 0
    else:
        high = round((expense-8)/(10-8), 3)
    return high, "high"


def fuzzyRule(val_inc, val_exp, i):
    output = []
    if(val_inc[i][1][1] == "low" and val_exp[i][1][1] == "low"):
        output.append(["Considered", (val_inc[i][1][0] and val_exp[i][1][0])])
    if(val_inc[i][1][1] == "low" and val_exp[i][2][1] == "avarage"):
        output.append(["Accept", (val_inc[i][1][0] and val_exp[i][2][0])])
    if(val_inc[i][1][1] == "low" and val_exp[i][3][1] == "high"):
        output.append(["Accept", (val_inc[i][1][0] and val_exp[i][3][0])])
    if(val_inc[i][2][1] == "avarage" and val_exp[i][1][1] == "low"):
        output.append(["Reject", (val_inc[i][2][0] and val_exp[i][1][0])])
    if(val_inc[i][2][1] == "avarage" and val_exp[i][2][1] == "avarage"):
        output.append(["Considered", (val_inc[i][2][0] and val_exp[i][2][0])])
    if(val_inc[i][2][1] == "avarage" and val_exp[i][3][1] == "high"):
        output.append(["Accept", (val_inc[i][2][0] and val_exp[i][3][0])])
    if(val_inc[i][3][1] == "high" and val_exp[i][1][1] == "low"):
        output.append(["Reject", (val_inc[i][3][0] and val_exp[i][1][0])])
    if(val_inc[i][3][1] == "high" and val_exp[i][2][1] == "avarage"):
        output.append(["Reject", (val_inc[i][3][0] and val_exp[i][2][0])])
    if(val_inc[i][3][1] == "high" and val_exp[i][3][1] == "high"):
        output.append(["Reject", (val_inc[i][3][0] and val_exp[i][3][0])])
    return output


def disjunctionRule(accept, reject, considered, inf, i):
    result = []
    for j in range(len(inf[i])):
        if(inf[i][j][0] == "Accept"):
            accept.append(inf[i][j][1])
        if(inf[i][j][0] == "Considered"):
            considered.append(inf[i][j][1])
        if(inf[i][j][0] == "Reject"):
            reject.append(inf[i][j][1])

    result.append(max(accept[0], accept[1], accept[2]))
    result.append(max(considered[0], considered[1]))
    result.append(max(reject[0], reject[1], reject[2], reject[3]))
    return result


def defuzzification(disj):
    return ((disj[2]*50)+(disj[0]*100)+(disj[1]*70))/(disj[0]+disj[1]+disj[2])


def ResultFuzzy(defuzz):
    result = []
    for i in range(20):
        result.append(defuzz[i][1])
    return result


# Income Membership Function
d1 = [0, 3, 5, 8, 10, 20]
x1 = [0, 3, 5, 20]
y1 = [1, 1, 0, 0]
x2 = [0, 3, 6, 8, 10, 20]
y2 = [0, 0, 1, 1, 0, 0]
x3 = [0, 8, 12, 20]
y3 = [0, 0, 1, 1]


plt.plot(x1, y1, label="Low Income")
plt.plot(x2, y2, label="Avarage Income")
plt.plot(x3, y3, label="High Income")
plt.legend()
plt.show()
# Expense Membership Function
ex1 = [0, 3, 4, 20]
ey1 = [1, 1, 0, 0]
ex2 = [0, 3, 5, 8, 9, 20]
ey2 = [0, 0, 1, 1, 0, 0]
ex3 = [0, 8, 10, 20]
ey3 = [0, 0, 1, 1]
plt.plot(ex1, ey1, label="Low Expense")
plt.plot(ex2, ey2, label="Avarage Expense")
plt.plot(ex3, ey3, label="High Expense")
plt.legend()
plt.show()


# Defuzzification Plot
plt.axvline(x=50, color="red", label="Reject")
plt.axvline(x=70, color="blue", label="Considered")
plt.axvline(x=100, color="green", label="Accept")
plt.legend()
plt.show()

# Main Program
loc = ("D:\Project\AI\Tupro\Tupro 2\Mahasiswa.xls")
mahasiswa = readExcel(loc)
x = len(mahasiswa)
val_inc = []
val_exp = []
inf = []
defuzz = []
for i in range(x):
    income = mahasiswa[i][1]
    expense = mahasiswa[i][2]
    val_inc.append([i+1, fuzzificationLowIncome(income), fuzzificationAvarageIncome(
        income), fuzzificationHighIncome(income)])
    val_exp.append([i+1, fuzzificationLowExpense(expense), fuzzificationAvaregeExpense(
        expense), fuzzificationHighExpense(expense)])
    rule = fuzzyRule(val_inc, val_exp, i)
    inf.append(rule)
    accept = []
    reject = []
    considered = []
    disj = disjunctionRule(accept, reject, considered, inf, i)
    defuzz.append([defuzzification(disj), i+1])

defuzz.sort(reverse=True)
print(defuzz)
result = ResultFuzzy(defuzz)
result.sort()
print(result)
 excel = pd.DataFrame({'Id Mahasiswa': result})
 writer = pd.ExcelWriter('Bantuan.xlsx', engine='xlsxwriter')
 excel.to_excel(writer, sheet_name='Sheet1')
 writer.save()


# print(mahasiswa)
# income = mahasiswa[0][1]
# expense = mahasiswa[0][2]
# print(income)
# print(expense)
# val_inc = []
# val_exp = []
# val_inc.append([1, fuzzificationLowIncome(income), fuzzificationAvarageIncome(
#     income), fuzzificationHighIncome(income)])
# val_exp.append([1, fuzzificationLowExpense(expense), fuzzificationAvaregeExpense(
#     expense), fuzzificationHighExpense(expense)])
# # val_inc.append([fuzzificationLowIncome(income), fuzzificationAvarageIncome(
# #     income), fuzzificationHighIncome(income)])
# # val_exp.append([fuzzificationLowExpense(expense), fuzzificationAvaregeExpense(
# #     expense), fuzzificationHighExpense(expense)])
# print(val_inc)
# print(val_exp)
# print(val_inc[0][0])
# print(val_exp[0][0])
# rule = fuzzyRule(val_inc, val_exp, 0)
# print(rule)
# HighIncome = fuzzificationHighIncome(coba)
# AvarageIncome = fuzzificationAvarageIncome(coba)
# LowIncome = fuzzificationLowIncome(coba)
# print(col)
# print(col[0][0][1])
# print(AvarageIncome)
# print(LowIncome)
# xdwq = mahasiswa[73][2]
# asdas = fuzzificationLowExpense(xdwq)
# print(xdwq)
# print(asdas)
# print(defuzz)
# print(len(defuzz))
# print(len(defuzz))
# print(val_inc[97])
# print(val_exp[97])
# print(inf[98])
# print(inf[97])
# print(defuzz[97])
# print(result)
# print(disj)
# print(inf)
# print(len(inf[i]))
# result = []
# for j in range(len(inf[i])):
#     if(inf[i][j][0] == "Accept"):
#         accept.append(inf[i][j][1])
#     if(inf[i][j][0] == "Reject"):
#         reject.append(inf[i][j][1])

# # print(len(accept))
# # print(len(reject))
# result.append(accept[0] or accept[1] or accept[2]
#               or accept[3] or accept[4])
# result.append(reject[0] or reject[1] or reject[2] or reject[3])


# print(inf[0][1][0])
