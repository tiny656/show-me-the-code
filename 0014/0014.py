#coding:utf-8
import xlwt

def write_xls():
    with open('students.txt', 'r') as f:
        data = eval(f.read())
    file = xlwt.Workbook()
    table = file.add_sheet('student')
    row = 0
    for k, v in data.iteritems():
        for col, val in enumerate([k]+v):
            table.write(row, col, val if type(val) != str else val.decode('gbk'))
        row += 1
    file.save('student.xls')

if __name__ == '__main__':
    write_xls()