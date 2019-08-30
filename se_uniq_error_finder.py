from bs4 import BeautifulSoup
from re import compile
import xlrd

# create a BeautifulSoup object with the htm file of students so we can iterate through and make a list of all the students that appear in the advisor's "My Students" view
f = open("students.htm",'rb')
soup = BeautifulSoup(f, features="html.parser", from_encoding='ascii')
f.close()

# create a list of uniqnames from the BeautifulSoup object of all the students that appear in the advisor's "My Students" view--these will be all the valid uniqnames that did not cause an error
valid_stus = []
for stu in soup.findAll('a', attrs={'href': compile("^/students/[a-z]+/$")}):
    link = stu.get('href')
    uniq = link.split("/")[2]
    if uniq is not 'nothappen': valid_stus.append(uniq)
valid_stus = set(valid_stus)

# create a list of uniqnames of students that were uploaded in the cohort so we can compare it to the other list and see which students uploaded in the cohort are not showing up in the "My Students" view--those are our errors
book = xlrd.open_workbook('cohort.xls')
sheet = book.sheet_by_index(0)
cohort_stus = []
for row in range(sheet.nrows):
    cohort_stus.append(sheet.cell_value(rowx=row,colx=0))

errors = []
for stu in cohort_stus:
    if stu not in valid_stus:
        errors.append(stu)
        print(stu)
print('There were {} errors'.format(len(errors)))
