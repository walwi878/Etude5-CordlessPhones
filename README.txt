Group names + student ID

Brodie Bosecke, 5471718
Meggie Morrison, 7777435
Julian Fawcett, 3861924
William Wallace, 1216661

Download the attached files into a folder and to run the program type into your command line "Python3 telephones.py < test.txt"

The output of the program prints the maximum radius enclosing no more than 11 points, from the list of input 'coordinates'

Submission 2: 
We have removed the duplicates from the list of telephone sites. 

Install pip3 install -U numpy scikit-learn scipy


Test cases we ran listed below

Telephone sites
125.13  122.56
 68.17  104.66
 72.25   85.75
 56.68  103.83
118.09  101.65
 60.41  123.10
107.10   86.17
 83.42  121.16
 85.85  100.11
 99.99   99.80
 30.30   45.45
 21.21   40.40
120.11   20.20

Output: 61.25473304849097

Telephone sites
123.45 678.96
876.54 765.32
123.65 765.34
34.50 68.90
67.89 87.09
435.77 557.18
66.18 56.78
990.60 55.43
66.50 143.76
345.67 897.65
354.68 875.89
5674.88 765.89
127.90 99999.87

Output: 2841.6404419146693

Telephone sites
123.45 678.96
876.54 765.32
123.65 765.34
34.50 68.90
67.89 87.09
435.77 557.18
66.18 56.78
990.60 55.43
66.50 143.76
345.67 897.65
354.68 875.89
400.02 765.89
127.90 120.22
30.0 40.0
10.0 20.0

Output: 469.8254653060006

Fix the following two issues, we finish the etude

Telephone sites
100.000000 0.000000
88.545603 46.472317
56.806475 82.298387
12.053668 99.270887
-35.460489 93.501624
-74.851075 66.312266
-97.094182 23.931566
-97.094182 -23.931566
-74.851075 -66.312266
-35.460489 -93.501624
12.053668 -99.270887
56.806475 -82.298387
88.545603 -46.472317

Currently outputting: RecursionError: maximum recursion depth exceeded while calling a Python object
RESUB: Now outputs 100.00000037410115


Telephone sites
010.00     010.00
020.00     010.00
030.00     010.00
040.00     010.00
050.00     010.00
060.00     010.00
070.00     010.00
080.00     010.00
090.00     010.00
100.00     010.00
110.00     010.00
120.00     010.00
130.00     010.00

Currently outputting: TypeError: 'NoneType' object is not subscriptable
RESUB: Now outputs 55.0

Telephone sites
010.00     060.00
020.00     060.00
010.00     050.00
020.00     050.00
050.00     100.00
060.00     100.00
050.00     090.00
090.00     060.00
100.00     060.00
100.00     050.00
060.00     020.00
060.00     010.00
050.00     010.00

Outputs: 48.5912657903775