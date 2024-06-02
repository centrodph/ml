**This notebook is an exercise in the [Data Cleaning](https://www.kaggle.com/learn/data-cleaning) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/handling-missing-values).**

---


In this exercise, you'll apply what you learned in the **Handling missing values** tutorial.

# Setup

The questions below will give you feedback on your work. Run the following cell to set up the feedback system.


```python
from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex1 import *
print("Setup Complete")
```

    /opt/conda/lib/python3.10/site-packages/learntools/data_cleaning/ex1.py:6: DtypeWarning: Columns (22,32) have mixed types. Specify dtype option on import or set low_memory=False.
      sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")
    /tmp/ipykernel_33/3419995878.py:3: DeprecationWarning: `product` is deprecated as of NumPy 1.25.0, and will be removed in NumPy 2.0. Please use `prod` instead.
      from learntools.data_cleaning.ex1 import *
    /opt/conda/lib/python3.10/site-packages/learntools/data_cleaning/ex1.py:69: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
      _expected = sf_permits.fillna(method='bfill', axis=0).fillna(0)


    Setup Complete


# 1) Take a first look at the data

Run the next code cell to load in the libraries and dataset you'll use to complete the exercise.


```python
# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("./Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 
```

    /tmp/ipykernel_33/3534875831.py:6: DtypeWarning: Columns (22,32) have mixed types. Specify dtype option on import or set low_memory=False.
      sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")


Use the code cell below to print the first five rows of the `sf_permits` DataFrame.


```python
# TODO: Your code here!
sf_permits.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Permit Number</th>
      <th>Permit Type</th>
      <th>Permit Type Definition</th>
      <th>Permit Creation Date</th>
      <th>Block</th>
      <th>Lot</th>
      <th>Street Number</th>
      <th>Street Number Suffix</th>
      <th>Street Name</th>
      <th>Street Suffix</th>
      <th>...</th>
      <th>Existing Construction Type</th>
      <th>Existing Construction Type Description</th>
      <th>Proposed Construction Type</th>
      <th>Proposed Construction Type Description</th>
      <th>Site Permit</th>
      <th>Supervisor District</th>
      <th>Neighborhoods - Analysis Boundaries</th>
      <th>Zipcode</th>
      <th>Location</th>
      <th>Record ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>201505065519</td>
      <td>4</td>
      <td>sign - erect</td>
      <td>05/06/2015</td>
      <td>0326</td>
      <td>023</td>
      <td>140</td>
      <td>NaN</td>
      <td>Ellis</td>
      <td>St</td>
      <td>...</td>
      <td>3.0</td>
      <td>constr type 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>Tenderloin</td>
      <td>94102.0</td>
      <td>(37.785719256680785, -122.40852313194863)</td>
      <td>1380611233945</td>
    </tr>
    <tr>
      <th>1</th>
      <td>201604195146</td>
      <td>4</td>
      <td>sign - erect</td>
      <td>04/19/2016</td>
      <td>0306</td>
      <td>007</td>
      <td>440</td>
      <td>NaN</td>
      <td>Geary</td>
      <td>St</td>
      <td>...</td>
      <td>3.0</td>
      <td>constr type 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>Tenderloin</td>
      <td>94102.0</td>
      <td>(37.78733980600732, -122.41063199757738)</td>
      <td>1420164406718</td>
    </tr>
    <tr>
      <th>2</th>
      <td>201605278609</td>
      <td>3</td>
      <td>additions alterations or repairs</td>
      <td>05/27/2016</td>
      <td>0595</td>
      <td>203</td>
      <td>1647</td>
      <td>NaN</td>
      <td>Pacific</td>
      <td>Av</td>
      <td>...</td>
      <td>1.0</td>
      <td>constr type 1</td>
      <td>1.0</td>
      <td>constr type 1</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>Russian Hill</td>
      <td>94109.0</td>
      <td>(37.7946573324287, -122.42232562979227)</td>
      <td>1424856504716</td>
    </tr>
    <tr>
      <th>3</th>
      <td>201611072166</td>
      <td>8</td>
      <td>otc alterations permit</td>
      <td>11/07/2016</td>
      <td>0156</td>
      <td>011</td>
      <td>1230</td>
      <td>NaN</td>
      <td>Pacific</td>
      <td>Av</td>
      <td>...</td>
      <td>5.0</td>
      <td>wood frame (5)</td>
      <td>5.0</td>
      <td>wood frame (5)</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>Nob Hill</td>
      <td>94109.0</td>
      <td>(37.79595867909168, -122.41557405519474)</td>
      <td>1443574295566</td>
    </tr>
    <tr>
      <th>4</th>
      <td>201611283529</td>
      <td>6</td>
      <td>demolitions</td>
      <td>11/28/2016</td>
      <td>0342</td>
      <td>001</td>
      <td>950</td>
      <td>NaN</td>
      <td>Market</td>
      <td>St</td>
      <td>...</td>
      <td>3.0</td>
      <td>constr type 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>Tenderloin</td>
      <td>94102.0</td>
      <td>(37.78315261897309, -122.40950883997789)</td>
      <td>144548169992</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 43 columns</p>
</div>



Does the dataset have any missing values?  Once you have an answer, run the code cell below to get credit for your work.


```python
# Check your answer (Run this code cell to receive credit!)
q1.check()
```


    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct:</span> 

The first five rows of the data does show that several columns have missing values.  You can see this in the "Street Number Suffix", "Proposed Construction Type" and "Site Permit" columns, among others.



```python
# Line below will give you a hint
#q1.hint()
```

# 2) How many missing data points do we have?

What percentage of the values in the dataset are missing?  Your answer should be a number between 0 and 100.  (If 1/4 of the values in the dataset are missing, the answer is 25.)


```python
# TODO: Your code here!
total_cells = np.product(sf_permits.shape)
missing_values_count = sf_permits.isnull().sum();

total_missing_cells = missing_values_count.sum();

# print("shape", sf_permits.shape)
print('total cells', total_cells)
# print('total missing per column', missing_values_count)
print('total missing cells', total_missing_cells)

percent_missing = (total_missing_cells / total_cells) * 100

print('percent missing', percent_missing)
# Check your answer
q2.check()
```

    total cells 8552700
    total missing cells 2245941
    percent missing 26.26002315058403



    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct</span>



```python
# Lines below will give you a hint or solution code
# q2.hint()
# q2.solution()
```

# 3) Figure out why the data is missing

Look at the columns **"Street Number Suffix"** and **"Zipcode"** from the [San Francisco Building Permits dataset](https://www.kaggle.com/aparnashastry/building-permit-applications-data). Both of these contain missing values. 
- Which, if either, are missing because they don't exist? 
- Which, if either, are missing because they weren't recorded?  

Once you have an answer, run the code cell below.


```python
# Check your answer (Run this code cell to receive credit!)
q3.check()
```


    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct:</span> 

If a value in the "Street Number Suffix" column is missing, it is likely because it does not exist. If a value in the "Zipcode" column is missing, it was not recorded.



```python
# Line below will give you a hint
#q3.hint()
```

# 4) Drop missing values: rows

If you removed all of the rows of `sf_permits` with missing values, how many rows are left?

**Note**: Do not change the value of `sf_permits` when checking this.  


```python
# TODO: Your code here!
total_rows = sf_permits.shape[0]
total_rows_after_drop= sf_permits.dropna().shape[0]

print(total_rows)
print(total_rows_after_drop) # no rows
```

    198900
    0


Once you have an answer, run the code cell below.


```python
# Check your answer (Run this code cell to receive credit!)
q4.check()
```


    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct:</span> 

There are no rows remaining in the dataset!



```python
# Line below will give you a hint
#q4.hint()
```

# 5) Drop missing values: columns

Now try removing all the columns with empty values.  
- Create a new DataFrame called `sf_permits_with_na_dropped` that has all of the columns with empty values removed.  
- How many columns were removed from the original `sf_permits` DataFrame? Use this number to set the value of the `dropped_columns` variable below.


```python
# TODO: Your code here
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

dropped_columns = sf_permits.shape[1] - sf_permits_with_na_dropped.shape[1]

# Check your answer
q5.check()
```


    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct</span>



```python
# Lines below will give you a hint or solution code
#q5.hint()
#q5.solution()
```

# 6) Fill in missing values automatically

Try replacing all the NaN's in the `sf_permits` data with the one that comes directly after it and then replacing any remaining NaN's with 0.  Set the result to a new DataFrame `sf_permits_with_na_imputed`.


```python
# TODO: Your code here
sf_permits_with_na_imputed = sf_permits.bfill(axis=0).fillna(0)

# Check your answer
q6.check()
```


    <IPython.core.display.Javascript object>



<span style="color:#33cc33">Correct</span>



```python
# Lines below will give you a hint or solution code
#q6.hint()
#q6.solution()
```

# More practice

If you're looking for more practice handling missing values:

* Check out [this noteboook](https://www.kaggle.com/alexisbcook/missing-values) on handling missing values using scikit-learn's imputer. 
* Look back at the "Zipcode" column in the `sf_permits` dataset, which has some missing values. How would you go about figuring out what the actual zipcode of each address should be? (You might try using another dataset. You can search for datasets about San Fransisco on the [Datasets listing](https://www.kaggle.com/datasets).) 

# Keep going

In the next lesson, learn how to [**apply scaling and normalization**](https://www.kaggle.com/alexisbcook/scaling-and-normalization) to transform your data.

---




*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/data-cleaning/discussion) to chat with other learners.*
