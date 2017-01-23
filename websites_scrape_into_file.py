#import os
#import csv
import xlwt
import urllib2

class CSVGeneration:

    def __init__(self):
        self.main()


    def get_filenames(self):
        outputFile = "scraped_data_programs.xls"
        return outputFile


    def program_headers(self, data_file):
        headers = ['website', 'e-commerce']
        self.programs_excel_file = xlwt.Workbook(encoding="utf-8")
        self.programs_excel_sheet_hdlr = self.programs_excel_file.add_sheet("sheet1")

        for i, row in enumerate(headers):
                self.programs_excel_sheet_hdlr.write(0, i, row)
        self.prog_row_count = 1
 

    def main(self):
        data_file = self.get_filenames()
        self.program_headers(data_file)
        input_file = open('websites.txt', 'r').readlines()
        count = 0
        for line in input_file:
            line = line.strip('+').strip('\n')
            if 'http:' not in line:
                line = 'http://' + line

            try:
                connection = urllib2.urlopen(line)
                get_responsedata = connection.read()
                ecommerce_value =''
                if 'cart ' in get_responsedata or 'buy' in get_responsedata or 'sell' in get_responsedata or 'shopping' in get_responsedata:
                    ecommerce_value = 'True'
                else:
                    ecommerce_value = 'False'
                connection.close()
            except:
                 ecommerce_value= 'No Response'

            value = [line,ecommerce_value]
            count += 1
            for col_count, data in enumerate(value):
                self.programs_excel_sheet_hdlr.write(self.prog_row_count, col_count, data)
            self.prog_row_count +=  1
    
        self.programs_excel_file.save(data_file)


if __name__ == "__main__":
    CSVGeneration()
