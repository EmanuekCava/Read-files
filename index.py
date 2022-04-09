import re
from sqlite3 import connect
from numpy import float64, int64
import pandas as pd
from tkinter import Tk, filedialog
import os
from tabula import read_pdf

import functions as func

option = func.menu()

typeIndex = None

Tk().withdraw()

def dataDf(df: pd.DataFrame):
    print(df)
    print("Amount of rows: ", len(df.index))
    print("Amount of columns: ", len(df.columns))
    print("Description: ", df.describe())

def showColumns():
    rangeRows = 0

    while rangeRows < 1 or rangeRows > 2:

        print("\n1: Show everything")
        print("2: Range of rows")
        stringRangeRows = input("\nSelect an option: ")

        try:
            rangeRows = int(stringRangeRows)

            if rangeRows < 1 or rangeRows > 2:
                func.availble(rangeRows)
        except:
            func.availble(stringRangeRows)

        return rangeRows

def rangeRows():
    fromRow = 0
    untilRow = 0

    stringFromRow = input("\nFrom: ")
    stringUntilRow = input("Until: ")

    try:
        fromRow = int(stringFromRow)
        untilRow = int(stringUntilRow)
    except:
        print("One option is not availble. Please try again")

    return fromRow, untilRow

def runOptions():
    if option == 1:
        file.optionOne()
    elif option == 2:
        file.optionTwo()
    elif option == 3:
        file.optionThree()
    elif option == 4:
        file.optionFour()
    elif option == 5:
        file.optionFive()
    elif option == 6:
        file.optionSix()
    else:
        file.optionSeven()


def runData(option, df: pd.DataFrame, typeIndexData, newDf):

    if(type(df) == str):
        df = pd.DataFrame([x.split(r"\s\s+") for x in df.split('\n')])

    if option == 1:
        print(df.columns)

    elif option == 2:

        print("\nColumns: ", df.columns)
        column = input("\nWrite a column name: ")

        optionRows = showColumns()

        if optionRows == 1:
            newDf = df[column].to_string()
        else:
            fromRow, untilRow = rangeRows()

            newDf = df[column][fromRow:untilRow+1].to_string()

    elif option == 3:
        
        stringAmountColumns = input("\nAmount of columns: ")
        amountColumns = int(stringAmountColumns)

        print(df.columns)

        columns = []

        for i in range(0, amountColumns):
            column = input("\nWrite a column name: ")
            columns.append(column)

        optionRows = showColumns()

        if optionRows == 1:
            newDf = df[columns].to_string()
        else:
            fromRow, untilRow = rangeRows()

            newDf = df[columns][fromRow:untilRow+1].to_string()

    elif option == 4:
        print("\nColumns: ", df.columns)
        column = input("\nWrite a column name: ")

        newDf = df.sort_values(column).to_string()

    elif option == 5:

        stringIndex = input("\nWrite an index value: ")

        if typeIndexData == str:
            newDf = df.loc[stringIndex]     
        elif typeIndexData == int64:
            index = int(stringIndex)
            newDf = df.iloc[index]
        elif typeIndexData == float64:
            index = float(stringIndex)
            newDf = df.loc[index]
        else:
            index = bool(stringIndex)
            newDf = df.loc[index]

    elif option == 6:

        stringAmountOfIndexValue = input("\nAmount of indices values: ")
        amountOfIndexValue = int(stringAmountOfIndexValue)

        indices = []

        for i in range(0, amountOfIndexValue):
            index = input("Write an index value: ")
            indices.append(index)

        if typeIndexData == str:
            newDf = df.loc[indices]
        elif typeIndexData == int64:
            indices = [int(x) for x in indices]
            newDf = df.loc[indices]
        elif typeIndexData == float64:
            indices = [float(x) for x in indices]
            newDf = df.loc[indices]
        else:
            indices = [bool(x) for x in indices]
            newDf = df.loc[indices]

    elif option == 7:

        stringAmountOfIndices = input("\nAmount of indices values: ")
        amountOfIndices = int(stringAmountOfIndices)

        indices = []

        for i in range(0, amountOfIndices):
            index = input("Write an index value: ")
            indices.append(index)

        stringAmountOfColumns = input("\nAmount of columns: ")
        amountOfColumns = int(stringAmountOfColumns)

        columns = []

        for i in range(0, amountOfColumns):
            column = input("Write an index value: ")
            columns.append(column)
        
        if typeIndexData == str:
            newDf = df.loc[indices, columns]
        elif typeIndexData == int64:
            indices = [int(x) for x in indices]
            newDf = df.loc[indices, columns]
        elif typeIndexData == float64:
            indices = [float(x) for x in indices]
            newDf = df.loc[indices, columns]
        else:
            indices = [bool(x) for x in indices ]
            newDf = df.loc[indices, columns]

    elif option == 8:

        optionConditional = 0

        while optionConditional < 1 or optionConditional > 6:

            print("\n.::Choose a conditional option::.")
            print("\n1: Major")
            print("2: Minor")
            print("3: Major or equal")
            print("4: Minor or equal")
            print("5: Equal")
            print("6: Different")
            optionConditionalString = input("Choose an option: ")

            try:

                optionConditional = int(optionConditionalString)

                if optionConditional < 1 or optionConditional > 6:
                    func.availble(optionConditional)

            except:
                func.availble(optionConditionalString)

            try:

                print(df.columns)

                if optionConditional == 1:
                    column, rowInt = func.inputsConditionals()
                    newDf = df[df[column] > rowInt].to_string()
                elif optionConditional == 2:
                    column, rowInt = func.inputsConditionals()
                    newDf = df[df[column] < rowInt].to_string()
                elif optionConditional == 3:
                    column, rowInt = func.inputsConditionals()
                    newDf = df[df[column] >= rowInt].to_string()
                elif optionConditional == 4:
                    column, rowInt = func.inputsConditionals()
                    newDf = df[df[column] <= rowInt].to_string()
                elif optionConditional == 5:
                    column, rowInt = func.inputsConditionals()
                    newDf = df.loc[df[column] == rowInt].to_string()
                else:
                    column, rowInt = func.inputsConditionals()
                    newDf = df.loc[df[column] != rowInt].to_string()

            except:
                print("Error. Probably the row value is not a number value")

    elif option == 9:

        print(df.columns)
        column = input("\nWrite a column name: ")
        row = input("Write a value: ")

        newDf = df[df[column].str.contains(row, regex=True, flags=re.I)]

    elif option == 10:

        print(df.columns)
        column = input("\nWrite a column name: ")
        row = input("Write a value to replace: ")
        rowReplaced = input("Write a new value: ")
        rowValue = row.lower()
        rowReplaced = rowReplaced.lower()

        df.loc[df[column] == rowValue, column] = rowReplaced

        newDf = df.to_string()

    elif option == 11:

        valuesString = input("Amount of first values: ")
        values = int(valuesString)
        newDf = df.head(values).to_string()
        
    elif option == 12:
        
        valuesString = input("Amount of last values: ")
        values = int(valuesString)
        print(values)
        newDf = df.tail(values).to_string()
    
    print(newDf)

    return newDf

class File:

    filename = filedialog.askopenfilename()
    formatFile = os.path.splitext(filename)
    newDataFrame = pd.DataFrame()

    def optionOne(self):
        try:

            index = func.filterColumn()        
            dfIndex = pd.read_excel(self.filename)
            typeIndex = type(dfIndex[index][0])
            df = pd.read_excel(self.filename, index_col=index)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            print(
                f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

        dataDf(df)
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionTwo(self):
        try:
            index = func.filterColumn()
            dfIndex = pd.read_csv(self.filename)
            typeIndex = type(dfIndex[index][0])
            df = pd.read_csv(self.filename, index_col=index)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            print(
                f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

        dataDf(df)
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionThree(self):
        try:
            df = pd.read_json(self.filename)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            print(
                f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

        dataDf(df)
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionFour(self):
        try:
            index = func.filterColumn()
            connection = connect(self.filename)
            tableName = input("\nWrite a table name: ")
            dfIndex = pd.read_sql(f"SELECT * FROM {tableName}", connection)
            typeIndex = type(dfIndex[index][0])
            df = pd.read_sql(f"SELECT * FROM {tableName}", connection, index_col=index)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            if self.formatFile[1] == ".sql":
                print(
                    f"\nError format. You have to select a database.")
            else:
                print(
                    f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

        dataDf(df)
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionFive(self):
        if(self.formatFile[1] != ".txt" and self.formatFile[1] != ".xml"):
            print(
                f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")
        else:
            try:
                index = func.filterColumn()
                dfIndex = pd.read_table(self.filename)
                typeIndex = type(dfIndex[index][0])
                df = pd.read_table(self.filename, index_col=index)
                df = df.apply(lambda x: x.astype(str).str.lower())
                df.fillna("")
                newDf = df
            except:
                print(
                    f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

            dataDf(df)
            optionMenu = func.menuOption()
            self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionSix(self):
        try:
            index = func.filterColumn()
            dfIndex = pd.read_html(self.filename)
            typeIndex = type(dfIndex[index][0])
            df = pd.read_html(self.filename, index_col=index)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            if self.formatFile[1] == ".html":
                print(
                    f"\nFile error. Check if you html file has a table")
            else:
                print(
                    f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

            dataDf(df)
            optionMenu = func.menuOption()
            self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def optionSeven(self):
        try:
            stringPages = input("Pages: ")
            pages = int(stringPages)
            df = read_pdf(self.filename, pages=pages)
            df = df.apply(lambda x: x.astype(str).str.lower())
            df.fillna("")
            newDf = df
        except:
            if self.formatFile[1] == ".pdf":
                print(
                    f"\nFile error. Check if you pdf file has a table")
            else:
                print(
                    f"\nError format. {self.formatFile[1]} is not availble in this case. Please try to choose another option.")

        dataDf(df)
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, df, typeIndex, newDf)

    def stepOne(self):
        os.system('python index.py')
        
    def stepTwo(self):
        runOptions()

    def stepThree(self):
        newDf = self.newDataFrame
        optionMenu = func.menuOption()
        self.newDataFrame = runData(optionMenu, self.newDataFrame, typeIndex, newDf)

file = File()

runOptions()

optionStep = -1

while optionStep != 0:
    optionStep = func.nextStep()

    if optionStep == 1:
        os.system('python index.py')
    elif optionStep == 2:
        runOptions()
    elif optionStep == 3:
        file.stepThree()

