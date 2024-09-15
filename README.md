# EXPERIMENT 3 - Python Data Analysis

This is for my Programming Assignment 3 containing my codes for Experiment 3 - Python Data Analysis

**Problem 1** - Save your file as Surname_Pandas-P1.py

Using knowledge obtained from the experiment and demonstrations:

&emsp; a. Load the corresponding .csv file into a data frame named cars using pandas

&emsp; b. Display the first five and last five rows of the resulting cars

**Problem 2** - Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

&emsp; a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

&emsp; b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

&emsp; c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

&emsp; d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# Codes *(Outputs can be seen in the PA3-Codes.ipynb file)*

## *Problem 1*

```python
import pandas as pd

# load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
cars

# display the first five rows by using .head()
cars.head()

# display the last five rows by using .tail()
cars.tail()
```

## *Problem 2* 

```python
import pandas as pd

# using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations

cars = pd.read_csv('cars.csv')
cars

# a. display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# combine two operations which are slicing and using .head()
# [1::2], so that it will begin at 1 and will increment by 2 to obtain the odd number of rows
# .head() to return the first five rows
cars[1::2].head()

# b. display the row that contains the ‘Model’ of ‘Mazda RX4’.

# use .loc to extract the row and column containing the Model which is Mazda RX4
cars.loc[[0],['Model']]

# c. how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# use .loc to extract the value under 'cyl' and display the name Camaro Z28
cars.loc[[23],['Model','cyl']]

# d. determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# use .loc to extract the values under 'cyl' and 'gear' of the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’
cars.loc[[1,28,18],['Model','cyl','gear']]
```
## How to save the files as .py?

1. Click file
   
2. Select Save and Export Notebook as
   
3. Click Executable Script

## The experiment is focused on the use of Python Data Analysis (PANDAS). If there are any problems, inquiries, or recommendations about the experiment, please to let me know!
# Author
Argamosa, Gabriel Ian E.




