import csv
import pandas as pd
import math
from table import Table
from abc import ABC

class TableTool(ABC):
    def readCsv(filename: str, delimiter=','):
        myTable=Table()
        with open(filename) as fileHandler:
            csvReaderObject = csv.reader(fileHandler, delimiter=delimiter)
            for row in csvReaderObject:
                myTable.pushRow(row=row)
        return myTable

    def writeCsv(table:Table, filename: str):
        with open(filename, 'w', newline='') as fileHandler:
            csvWriterObject = csv.writer(fileHandler)
            for row in table.getRows():
                csvWriterObject.writerow(row)
        return

    def readExcelWorksheet(filename:str,worksheet = 0):
        myTable = Table()
        dataframe = pd.read_excel(io=filename,sheet_name=worksheet)
        #extract headers
        myTable.pushRow(list(dataframe.columns))
        #extract rows
        for index, row in dataframe.iterrows():
            myTable.pushRow(list(row))
        #nan to None casting
        for i in range(0,myTable.getNumberOfRows()):
            for j in range(0,myTable.getNumberOfColumns()):
                if type(myTable.getEntry(i=i,j=j)) is float and math.isnan(myTable.getEntry(i=i,j=j)):
                    myTable.setEntry(i=i,j=j,entry = None)
        return myTable

    def writeExcelWorksheet(table:Table, filename:str,worksheet="Sheet"):
        if table.getRows() == []:
            print("!!!writeExcelWorksheet: empty table!!!")
            return
        dataframe= pd.DataFrame(columns=table.getRow(i=0))
        for i in range(0,table.getNumberOfRows()):
            dataframe.loc[i] = table.getRow(i=i)
        dataframe = dataframe.reset_index(drop=True)
        dataframe.to_excel(excel_writer=filename,sheet_name=worksheet, header = False, index = False)
        return