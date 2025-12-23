import unittest

import pandas as pd
from IPython import display


class tableTestCase(unittest.TestCase):

    def setUp(self) -> None:
        return



    def test_filter(self):
        localTable = self.myTable.deepcopy()
        def filter(row):
            return row[0] == 'a'
        localTable.filter(filter=filter)
        expectedResult = [['a',1,2],['a',5,6]]
        result = localTable.getRows()
        self.assertEqual(expectedResult, result)

    def test_pivot(self):
        expectedResult = [['a',8],['b',4]]
        result = self.myTable.createPivot(index=0, sumColumn=2).getRows()
        self.assertEqual(expectedResult, result)

    def test_pivot2(self):
        #expectedResult = [['a', 8], ['b', 4]]
        result = self.myPivotTable.createPivot2(pivotColumns=[0,2], sumColumn=4)
        result.print()
        #self.assertEqual(expectedResult, result)

    def test_pandas(self):
        dataframe = pd.read_csv('input.csv',sep=',')
        pivot = pd.pivot_table(data=dataframe, index = ['KontrollwertTyp','Tarif'],values=['Anzahl'])
        print(pivot)

if __name__ == '__main__':
    unittest.main()
