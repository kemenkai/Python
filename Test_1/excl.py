import openpyxl

wb = openpyxl.Workbook()
filePath = "d:\\tmp\\tmp.xlsx"
ws1 = wb.active
ws1.title = "range name"
list1 = ['A', 'B', 'C', 'D']

for tmp1 in range(1, 5):
    for tmp2 in list1:
        print("{0}{1}".format(tmp2, tmp1))
        ws1['{0}{1}'.format(tmp2, tmp1)] = "{0}{1}".format(tmp2, tmp1)

wb.save(filePath)
wb.close()
