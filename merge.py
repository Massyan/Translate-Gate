import xlrd
import csv
import os

dirname = './output'

#merge all the xlsx files in output into one csv

def csv_from_excel():
    nrows_id = 0
    for fn in os.listdir(dirname):
        wb = xlrd.open_workbook('./output/' + fn)
        sh = wb.sheet_by_name('Sheet')
        csv_file = open('csv_merge.csv', 'a', encoding="utf-8")
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        nrows_id += rownum
        csv_file.close()

    print('rows merged: ' + str(nrows_id))

csv_from_excel()