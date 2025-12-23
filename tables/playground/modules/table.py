import copy
from aggregationFunction import aggregationFunction


# A table is a list A of lists B, where A is interpreted as the list of columns and the Bs are interpreted as the rows.
# Row indices are named i
# Column indices are named j

#Currently there are side-effects respectively no side effects resulting from the internal data structure
# list(list,list,...)
# for instance:
# table.getRow(i=0) returns a pointer to the row
# table.getColumn(j=0) returns a new list, where the entries are the objects from table[*,0]

class Table:
    rows: list

    def __init__(self):
        self.rows = []

    def getRows(self):
        return self.rows

    def setRows(self, rows: list):
        self.rows = rows
        return

    def isEmpty(self):
        return self.getRows() == []

    def getRow(self, i: int):
        return self.getRows()[i]

    def setRow(self, i: int, row: list):
        self.getRows()[i] = row
        return

    def pushRow(self, row: list):
        self.getRows().append(row)

    def popRow(self):
        self.getRows().pop()

    # def removeRowByIndex(self, index: int):
    #     self.getRows().pop(index)
    #
    # def removeRowByIdentity(self, row: list):
    #     self.getRows().remove(row)

    def getNumberOfRows(self):
        return len(self.getRows())

    def getNumberOfColumns(self):
        return len(self.getRows()[0])

    def getEntry(self, i: int, j: int):
        return self.getRow(i=i)[j]

    def setEntry(self, i: int, j: int, entry):
        self.getRow(i=i)[j] = entry
        return

    # To improve
    # Problem: In contrast to getRow, the return value does not point to the column but is a new list
    def getColumn(self, j: int):
        result = []
        for row in self.getRows():
            result.append(row[j])
        return result

    # To improve
    def setColumn(self, j: int, column: list):
        k = 0
        for row in self.getRows():
            row[j] = column[k]
            k += 1
        return

    def print(self, numberOfRows=-1):
        counter = 0
        for row in self.getRows():
            print(row)
            counter += 1
            if counter == numberOfRows:
                break
        return

    def deepcopy(self):
        result = Table()
        localRows = copy.deepcopy(self.getRows())
        result.setRows(rows=localRows)
        return result

    # To improve
    def filter(self, filter, headers=False):
        aList = []
        for i in range(0,self.getNumberOfRows()):
            if i == 0 and headers:
                row = self.getRow(i=i)
                aList.append(row)
                next
            else:
                row = self.getRow(i=i)
                if filter(row=row):
                    aList.append(row)
        self.setRows(aList)
        # localCopy = self.deepcopy()
        # for row in localCopy.getRows():
        #     if not filter(row):
        #         self.getRows().remove(row)

    def createFilteredTable(self, filter, headers=False):
        result = self.deepcopy()
        result.filter(filter=filter, headers=headers)
        return result

    def removeRowsByFilter(self, filter):
        localCopy = self.deepcopy()
        for row in localCopy.getRows():
            if filter(row):
                self.getRows().remove(row)

    def pushColumn(self, column: list):
        if self.getNumberOfRows() == len(column):
            i = 0
            for row in self.getRows():
                row.append(column[i])
                i += 1
        else:
            print('Error: Size does not match' + str(self.getNumberOfRows()) + str(len(column)))
        return

    def insertColumn(self, index: int, column: list):
        if self.getNumberOfRows() == len(column):
            i = 0
            for row in self.getRows():
                row.insert(index, column[i])
                i += 1
        else:
            print('Error: Size does not match' + str(self.getNumberOfRows()) + str(len(column)))
        return

    def convertColumn(self, j: int, targetType):
        for row in self.getRows():
            row[j] = targetType(row[j])

    def createPivot(self, index, values, aggregationFunctions):
        localTable = self.deepcopy()
        result = Table()
        while not localTable.isEmpty():
            # Get current pivot element
            currentRow = localTable.getRow(i=0)

            def filter(row):
                return row[index] == currentRow[index]

            filteredTable = self.createFilteredTable(filter=filter)

            # creating the new pivot row
            newRow = [filteredTable.getRow(i=0)[index]]
            for i in range(len(values)):
                newRow.append(aggregationFunctions[i](filteredTable.getColumn(values[i])))
            result.pushRow(newRow)

            # Remove all rows with the current pivot element
            localTable.removeRowsByFilter(filter=filter)
        return result


if __name__ == '__main__':
    myTable = Table()
    myTable.setRows(rows=[
        ['a', 1, 2],
        ['a', 3, 4],
        ['b', 5, 6]
    ])
    print(myTable.getRows())
    print()
    print(myTable.isEmpty())
    print()
    print(myTable.getRow(i=0))
    print()
    cache = myTable.getRow(i=0)
    myTable.setRow(i=0, row=[0, 0, 0])
    myTable.print()
    print()
    myTable.setRow(i=0, row=cache)
    myTable.print()
    print()
    myTable.pushRow(row=['b', 7, 8])
    myTable.print()
    print()
    myTable.popRow()
    myTable.print()
    print()
    print(myTable.getNumberOfRows())
    print(myTable.getNumberOfColumns())
    print()
    print(myTable.getEntry(i=0, j=0))
    print()
    myTable.setEntry(i=0, j=0, entry='b')
    myTable.print()
    myTable.setEntry(i=0, j=0, entry='a')
    print()
    print(myTable.getColumn(j=0))
    print()
    cache = myTable.getColumn(j=0)
    myTable.setColumn(j=0, column=['x', 'x', 'x'])
    myTable.print()
    myTable.setColumn(j=0, column=cache)
    print()

    print("Filter-Test")
    def myFilter(row):
        return row[0] == 'b'
    myTable.print()
    print("=>")
    myTable.createFilteredTable(filter=myFilter,headers=True).print()

    print()
    myTable.print()
    print("=>")
    myTable.createPivot(index=0, values=[1], aggregationFunctions=[aggregationFunction.sum]).print()



    print("Neuer Test")
    myTable = Table()
    myTable.setRows(rows=[
        ['a', 1, 2],
        ['a', 3, 4],
        ['b', 5, 6]
    ])
    col=myTable.getColumn(j=0)
    col[0]='b'
    myTable.print()
    row = myTable.getRow(i=0)
    row[0] = 'b'
    myTable.print()