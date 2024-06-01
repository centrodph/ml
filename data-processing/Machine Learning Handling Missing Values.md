## we need to import the libraries


```python
import numpy as np
import pandas as pd
```

trying to read the data, I we see that there are mixed types.


```python
data = pd.read_csv("./NFLPlayByPlay2009-2017_v4.csv")
```

    /tmp/ipykernel_23803/1150844578.py:1: DtypeWarning: Columns (25,51) have mixed types. Specify dtype option on import or set low_memory=False.
      data = pd.read_csv("./NFLPlayByPlay2009-2017_v4.csv")


trying to impect the head of the data frame to have a overview of the data-format


```python
data.head()
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
      <th>Date</th>
      <th>GameID</th>
      <th>Drive</th>
      <th>qtr</th>
      <th>down</th>
      <th>time</th>
      <th>TimeUnder</th>
      <th>TimeSecs</th>
      <th>PlayTimeDiff</th>
      <th>SideofField</th>
      <th>...</th>
      <th>yacEPA</th>
      <th>Home_WP_pre</th>
      <th>Away_WP_pre</th>
      <th>Home_WP_post</th>
      <th>Away_WP_post</th>
      <th>Win_Prob</th>
      <th>WPA</th>
      <th>airWPA</th>
      <th>yacWPA</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>15:00</td>
      <td>15</td>
      <td>3600.0</td>
      <td>0.0</td>
      <td>TEN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.485675</td>
      <td>0.514325</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.485675</td>
      <td>0.060758</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>14:53</td>
      <td>15</td>
      <td>3593.0</td>
      <td>7.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>1.146076</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.546433</td>
      <td>0.004655</td>
      <td>-0.032244</td>
      <td>0.036899</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>14:16</td>
      <td>15</td>
      <td>3556.0</td>
      <td>37.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.551088</td>
      <td>-0.040295</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>13:35</td>
      <td>14</td>
      <td>3515.0</td>
      <td>41.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>-5.031425</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.510793</td>
      <td>-0.049576</td>
      <td>0.106663</td>
      <td>-0.156239</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>13:27</td>
      <td>14</td>
      <td>3507.0</td>
      <td>8.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.558929</td>
      <td>0.441071</td>
      <td>0.461217</td>
      <td>0.097712</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 102 columns</p>
</div>




```python

# count how many missing values we have per column
missing_values_per_column = data.isnull().sum()

missing_values_per_column[0:10] # taking the first then columns
```




    Date                0
    GameID              0
    Drive               0
    qtr                 0
    down            61154
    time              224
    TimeUnder           0
    TimeSecs          224
    PlayTimeDiff      444
    SideofField       528
    dtype: int64



how calculate to total of cell in a data frame


```python
total_cells = np.product(data.shape)
total_missing = missing_values_per_column.sum()

print('total_missing', total_missing)

print('total_cells', total_cells)

print('percentaje missing', (total_missing / total_cells) * 100)
```

    total_missing 11505187
    total_cells 41584176
    percentaje missing 27.66722370547874



```python
data[:].count()
```




    Date        407688
    GameID      407688
    Drive       407688
    qtr         407688
    down        346534
                 ...  
    Win_Prob    382679
    WPA         402147
    airWPA      159187
    yacWPA      158926
    Season      407688
    Length: 102, dtype: int64




```python
# remove all row without value this is not recomended
removed_rows_empty_data= data.dropna() 

print(removed_rows_empty_data)
```

    Empty DataFrame
    Columns: [Date, GameID, Drive, qtr, down, time, TimeUnder, TimeSecs, PlayTimeDiff, SideofField, yrdln, yrdline100, ydstogo, ydsnet, GoalToGo, FirstDown, posteam, DefensiveTeam, desc, PlayAttempted, Yards.Gained, sp, Touchdown, ExPointResult, TwoPointConv, DefTwoPoint, Safety, Onsidekick, PuntResult, PlayType, Passer, Passer_ID, PassAttempt, PassOutcome, PassLength, AirYards, YardsAfterCatch, QBHit, PassLocation, InterceptionThrown, Interceptor, Rusher, Rusher_ID, RushAttempt, RunLocation, RunGap, Receiver, Receiver_ID, Reception, ReturnResult, Returner, BlockingPlayer, Tackler1, Tackler2, FieldGoalResult, FieldGoalDistance, Fumble, RecFumbTeam, RecFumbPlayer, Sack, Challenge.Replay, ChalReplayResult, Accepted.Penalty, PenalizedTeam, PenaltyType, PenalizedPlayer, Penalty.Yards, PosTeamScore, DefTeamScore, ScoreDiff, AbsScoreDiff, HomeTeam, AwayTeam, Timeout_Indicator, Timeout_Team, posteam_timeouts_pre, HomeTimeouts_Remaining_Pre, AwayTimeouts_Remaining_Pre, HomeTimeouts_Remaining_Post, AwayTimeouts_Remaining_Post, No_Score_Prob, Opp_Field_Goal_Prob, Opp_Safety_Prob, Opp_Touchdown_Prob, Field_Goal_Prob, Safety_Prob, Touchdown_Prob, ExPoint_Prob, TwoPoint_Prob, ExpPts, EPA, airEPA, yacEPA, Home_WP_pre, Away_WP_pre, Home_WP_post, Away_WP_post, Win_Prob, WPA, airWPA, ...]
    Index: []
    
    [0 rows x 102 columns]



```python
# remove columns with empty values
removed_columns_empty_data= data.dropna(axis=1)

print(removed_columns_empty_data)
```

                  Date      GameID  Drive  qtr  TimeUnder  ydstogo  ydsnet  \
    0       2009-09-10  2009091000      1    1         15        0       0   
    1       2009-09-10  2009091000      1    1         15       10       5   
    2       2009-09-10  2009091000      1    1         15        5       2   
    3       2009-09-10  2009091000      1    1         14        8       2   
    4       2009-09-10  2009091000      1    1         14        8       2   
    ...            ...         ...    ...  ...        ...      ...     ...   
    407683  2017-12-31  2017123101     29    4          1        0      -4   
    407684  2017-12-31  2017123101     29    4          1       14      -4   
    407685  2017-12-31  2017123101     29    4          1       14       9   
    407686  2017-12-31  2017123101     30    4          1       10      -1   
    407687  2017-12-31  2017123101     30    4          0        0      -1   
    
            PlayAttempted  Yards.Gained  sp  ...  AwayTeam  Timeout_Indicator  \
    0                   1            39   0  ...       TEN                  0   
    1                   1             5   0  ...       TEN                  0   
    2                   1            -3   0  ...       TEN                  0   
    3                   1             0   0  ...       TEN                  0   
    4                   1             0   0  ...       TEN                  0   
    ...               ...           ...  ..  ...       ...                ...   
    407683              1             0   0  ...       CIN                  1   
    407684              1             0   0  ...       CIN                  0   
    407685              1            13   0  ...       CIN                  0   
    407686              1            -1   0  ...       CIN                  0   
    407687              1             0   0  ...       CIN                  0   
    
            posteam_timeouts_pre HomeTimeouts_Remaining_Pre  \
    0                          3                          3   
    1                          3                          3   
    2                          3                          3   
    3                          3                          3   
    4                          3                          3   
    ...                      ...                        ...   
    407683                     0                          3   
    407684                     2                          2   
    407685                     2                          2   
    407686                     0                          2   
    407687                     0                          2   
    
            AwayTimeouts_Remaining_Pre  HomeTimeouts_Remaining_Post  \
    0                                3                            3   
    1                                3                            3   
    2                                3                            3   
    3                                3                            3   
    4                                3                            3   
    ...                            ...                          ...   
    407683                           0                            2   
    407684                           0                            2   
    407685                           0                            2   
    407686                           0                            2   
    407687                           0                            2   
    
            AwayTimeouts_Remaining_Post  ExPoint_Prob  TwoPoint_Prob  Season  
    0                                 3           0.0            0.0    2009  
    1                                 3           0.0            0.0    2009  
    2                                 3           0.0            0.0    2009  
    3                                 3           0.0            0.0    2009  
    4                                 3           0.0            0.0    2009  
    ...                             ...           ...            ...     ...  
    407683                            0           0.0            0.0    2017  
    407684                            0           0.0            0.0    2017  
    407685                            0           0.0            0.0    2017  
    407686                            0           0.0            0.0    2017  
    407687                            0           0.0            0.0    2017  
    
    [407688 rows x 37 columns]



```python
# how much data we lost

print("original columns: %d \n" % data.shape[1])

print("cleaned columns: %d \n" % removed_columns_empty_data.shape[1])
```

    original columns: 102 
    
    cleaned columns: 37 
    



```python
# get a small subset of the NFL dataset
subset_nfl_data = data.loc[:, 'EPA':'Season'].head()
subset_nfl_data
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
      <th>EPA</th>
      <th>airEPA</th>
      <th>yacEPA</th>
      <th>Home_WP_pre</th>
      <th>Away_WP_pre</th>
      <th>Home_WP_post</th>
      <th>Away_WP_post</th>
      <th>Win_Prob</th>
      <th>WPA</th>
      <th>airWPA</th>
      <th>yacWPA</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.014474</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.485675</td>
      <td>0.514325</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.485675</td>
      <td>0.060758</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.077907</td>
      <td>-1.068169</td>
      <td>1.146076</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.546433</td>
      <td>0.004655</td>
      <td>-0.032244</td>
      <td>0.036899</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.402760</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.551088</td>
      <td>-0.040295</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.712583</td>
      <td>3.318841</td>
      <td>-5.031425</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.510793</td>
      <td>-0.049576</td>
      <td>0.106663</td>
      <td>-0.156239</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.097796</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.558929</td>
      <td>0.441071</td>
      <td>0.461217</td>
      <td>0.097712</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2009</td>
    </tr>
  </tbody>
</table>
</div>




```python
# basic fill

filled_basic_data = data.fillna(0)


filled_basic_data.head()
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
      <th>Date</th>
      <th>GameID</th>
      <th>Drive</th>
      <th>qtr</th>
      <th>down</th>
      <th>time</th>
      <th>TimeUnder</th>
      <th>TimeSecs</th>
      <th>PlayTimeDiff</th>
      <th>SideofField</th>
      <th>...</th>
      <th>yacEPA</th>
      <th>Home_WP_pre</th>
      <th>Away_WP_pre</th>
      <th>Home_WP_post</th>
      <th>Away_WP_post</th>
      <th>Win_Prob</th>
      <th>WPA</th>
      <th>airWPA</th>
      <th>yacWPA</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>0.0</td>
      <td>15:00</td>
      <td>15</td>
      <td>3600.0</td>
      <td>0.0</td>
      <td>TEN</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.485675</td>
      <td>0.514325</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.485675</td>
      <td>0.060758</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>14:53</td>
      <td>15</td>
      <td>3593.0</td>
      <td>7.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>1.146076</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.546433</td>
      <td>0.004655</td>
      <td>-0.032244</td>
      <td>0.036899</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>14:16</td>
      <td>15</td>
      <td>3556.0</td>
      <td>37.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.551088</td>
      <td>-0.040295</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>13:35</td>
      <td>14</td>
      <td>3515.0</td>
      <td>41.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>-5.031425</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.510793</td>
      <td>-0.049576</td>
      <td>0.106663</td>
      <td>-0.156239</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>13:27</td>
      <td>14</td>
      <td>3507.0</td>
      <td>8.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.558929</td>
      <td>0.441071</td>
      <td>0.461217</td>
      <td>0.097712</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2009</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 102 columns</p>
</div>




```python
# fill with the first value that comes after in the column the remaining one with 0

column_based_fill = data.bfill(axis=0).fillna(0)

column_based_fill.head()
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
      <th>Date</th>
      <th>GameID</th>
      <th>Drive</th>
      <th>qtr</th>
      <th>down</th>
      <th>time</th>
      <th>TimeUnder</th>
      <th>TimeSecs</th>
      <th>PlayTimeDiff</th>
      <th>SideofField</th>
      <th>...</th>
      <th>yacEPA</th>
      <th>Home_WP_pre</th>
      <th>Away_WP_pre</th>
      <th>Home_WP_post</th>
      <th>Away_WP_post</th>
      <th>Win_Prob</th>
      <th>WPA</th>
      <th>airWPA</th>
      <th>yacWPA</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>15:00</td>
      <td>15</td>
      <td>3600.0</td>
      <td>0.0</td>
      <td>TEN</td>
      <td>...</td>
      <td>1.146076</td>
      <td>0.485675</td>
      <td>0.514325</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.485675</td>
      <td>0.060758</td>
      <td>-0.032244</td>
      <td>0.036899</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>14:53</td>
      <td>15</td>
      <td>3593.0</td>
      <td>7.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>1.146076</td>
      <td>0.546433</td>
      <td>0.453567</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.546433</td>
      <td>0.004655</td>
      <td>-0.032244</td>
      <td>0.036899</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>14:16</td>
      <td>15</td>
      <td>3556.0</td>
      <td>37.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>-5.031425</td>
      <td>0.551088</td>
      <td>0.448912</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.551088</td>
      <td>-0.040295</td>
      <td>0.106663</td>
      <td>-0.156239</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>13:35</td>
      <td>14</td>
      <td>3515.0</td>
      <td>41.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>-5.031425</td>
      <td>0.510793</td>
      <td>0.489207</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.510793</td>
      <td>-0.049576</td>
      <td>0.106663</td>
      <td>-0.156239</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2009-09-10</td>
      <td>2009091000</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>13:27</td>
      <td>14</td>
      <td>3507.0</td>
      <td>8.0</td>
      <td>PIT</td>
      <td>...</td>
      <td>0.163935</td>
      <td>0.461217</td>
      <td>0.538783</td>
      <td>0.558929</td>
      <td>0.441071</td>
      <td>0.461217</td>
      <td>0.097712</td>
      <td>-0.010456</td>
      <td>0.006029</td>
      <td>2009</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 102 columns</p>
</div>




```python

```
