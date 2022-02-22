# -*- coding: utf-8 -*-
"""JBrokaw-PughMatrix-RadarPlot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fSgB4GOZadHlM1HEIIuRlXSVncbeyNCY
"""

import pandas as pd
import math 

AA = pd.DataFrame(columns=['criteria', 'weight', 'ratingA', 'ratingB', 'scoreA', 'scoreB'])
print(AA)


AA['criteria'] = ['risk', 'ROI', 'customerSatisfaction', 'Feasibility', 'strategicAlignment']

AA['weight'] = [.2, .15, .3, .05, .3]

AA['ratingA'] = [5, 1, 2, 1, 3]
AA['ratingB'] = [2, 1, 2, 1, 2]

for index, row in AA.iterrows():
  AA['scoreA'][index] = row['ratingA']*row['weight']
  AA['scoreB'][index] = row['ratingB']*row['weight']


print(AA)


totalScoreA = 0
totalScoreB = 0

for index, row in AA.iterrows():
  totalScoreA += row['scoreA']
  totalScoreB += row['scoreB']

print('---------------------------------')
print('The total score for A is: {:.2f}'.format(totalScoreA))
print('The total score for B is: {:.2f}'.format(totalScoreB))

import numpy as np
import matplotlib.pyplot as plt


axisLocations = np.linspace(start=0, stop=2*np.pi, num=len(AA['ratingA']), endpoint=False)
axisLocations = np.concatenate((axisLocations, [axisLocations[0]]))

ratingsA = AA['ratingA']
ratingsB = AA['ratingB']

ratingsACircular = np.concatenate((ratingsA, [ratingsA[0]]))
ratingsBCircular = np.concatenate((ratingsB, [ratingsB[0]]))

plt.figure(figsize=(8,8))
plt.subplot(polar=True)

plt.plot(axisLocations, ratingsACircular, 'o-', linewidth=2, label='In-house development')
plt.plot(axisLocations, ratingsBCircular, 'd-', linewidth=2, label='Outsource')

plt.title('Project Options Comparisons', size=20)
lines,labels = plt.thetagrids(np.degrees(axisLocations), labels=AA['criteria'])
plt.legend(['In House Development', 'Outsourced Development'], loc='lower left', borderaxespad = -5)
plt.show()