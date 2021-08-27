# Co-Relation Program 

The problem is to calculate the relation between two sets of data on a scale ranging from -1 to +1.

Positive value refers to direct proportionality, the increase in one leads to the increase in the other and vice versa. Negative value refers to inverse proportionality, the increase in one leads to the decrease in the other and vice versa. +1 and -1 refer to perfect correlation where one can predict the output of one set perfectly knowing the other.

From the data provided to you, you are required to compute the relation between the 2 quantities using the formula given.

Ν Σxy – Σx Σy/√(NΣx² - (Σx) ²) (NΣy² - (Σy)²)
N is equal to the number of pairs of values in the data
x and y are a given pair of values
Σxy is the sum of the products of paired scores
Σx the sum of the scores of one data set
Σy the sum of the scores of the other data set
Σx² is the sum of the squares of the scores of one data set
Σy² is the sum of the squares of the scores of the other data set


**Input Format**

x, contains the number of states,
n, the name of the state,
y, percentage of cigaretter smokers,
z, number of lung cancer cases per thousand
Constraints

x is an integer such that 1 ≤ x ≤ 10,
n is a string containing the name of the state,
y and z for each state are float values with a single decimal point

**Output Format**

At the end of the test case, your code should output the relation between the two quantities given. Make sure to print the first 2 places after decimal without rounding off

For example,
`0.69`


**Sample Input 0**

```
5
alabama
23.3
75.2
arkansas
23.7
77.7
california
14.9
51.6
colorado
17.9
48.4
Connecticut
17
68.3
```

**Sample Output 0**
`
0.80
`

**Sample Input 1**

```
5
iowa
21.5
67.1
kansas
20
68.4
kentucky
28.6
97.2
maine
20.9
80.1
michigan
22.4
72
```
**Sample Output 1**

`0.88`
