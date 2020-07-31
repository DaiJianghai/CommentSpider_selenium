import xlwt

list = []
list.append(["daijiangai", 23, "haiaha"])
list.append(["hailiang","wangmingyang","jiang"])

workbook = xlwt.Workbook(encoding = 'utf-8')
sheet = workbook.add_sheet("first", cell_overwrite_ok=True)
sheet.write(0, 0,  '0')
sheet.write(0, 1,  '1')
sheet.write(0, 2,  '2')



for i in range(len(list)):
    for j in range(len(list[0])):
        sheet.write(i+1, j, list[i][j])

workbook.save("workbook1.xls")


# print(list)