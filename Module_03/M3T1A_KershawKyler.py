# coding: utf-8
import pandas as pd
grades = pd.Series([87,100,94])
grades
pd.Series(98.6, range(3))
grades[0]
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()
grades.describe()
grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])
grades
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
grades
grades['Eva']
grades.Wally
grades.dtype
grades.values
hardware = pd.Series(['Hammer','Saw','Wrench'])
hardware
hardware.str.contains('a')
hardware.str.upper()
