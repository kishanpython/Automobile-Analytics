# Automobile-Analytics
This is an automobile analytics project. In this we have analyze the data gathered from the sensors installed on vehicles, using dashboard. The sensors send data in hexadecimal form and we have changes it into decimal form during data pre-processing.Saved the pre-processed data in MySQL database. Then make a dashboard for analyze the the data. Also made a model for demonstration purpose. It contains 40 features which are as follow:- 

```
features_names=['Date','Latitude', 'Longitude', 'Altitude', 'RPM',
        'Driver Demand Torque (%)', 'Engine Load (%)', 'Engine Torque Mode', 'TPS (%)',
        'Percent Load Curret Speed', 'Fuel Rate (L-Hr)', 'Vehicle Speed',
        'Inj Q Cur (mg-st)', 'Inj Q Tor (mg-st)', 'Boost Pressure (mBar)',
        'Atmospheric Pressure (mBar)', 'Coolant Temperature (*C)',
        'Oil Temperature (*C)', 'Boost Temperature (*C)', 'Oil Pressure (mBar)',
        'Battery Voltage (V)', 'Cam Speed (rpm)', 'Rail Pressure (mBar)',
        'Rail Pressure set (mBar)', 'MU PWM (%)', 'MU Vol (mm3-s)',
        'Torque Rat', 'Torque (Nm)', 'TQ Limit Set', 'Main Injection (mg-st)',
        'Pilot Injection (mg-st)', 'Pos 2 Injector (mg-st)', 'EGR Prop (%)',
        'EGR Pos D (%)', 'EGR Pos A (%)', 'Clutch Switch', 'Brake Switch',
        'Engine Grad (rpm)', 'param1', 'param2','col_no'
]

```

### Dashboard Link :- <a href="https://vehicle-dash.herokuapp.com/">click here</a>

![Project Image](https://github.com/kishanpython/Automobile-Tasks/blob/main/Assets/asset_1.png)

This project contains following tasks :- 
## Task A:- Pre-processed the data and save it in database with proper schema.
<ul>
  <li>Dataset in '.xlsx' format :- <a href="https://github.com/kishanpython/Automobile-Tasks/tree/main/Task-1/data_preprocessed">View</a></li>
  <li>Data Preprocessing Notebook :- <a href="https://github.com/kishanpython/Automobile-Tasks/blob/main/Task-1/Data%20Preprocessing.ipynb"> view </a></li>
  <li>Pre-Processed Data in '.csv' format :- <a href="https://github.com/kishanpython/Automobile-Tasks/blob/main/Task-1/db_schema/truck1.csv"> view </a></li>
  <li>Saving Data in MySQL Database :- <a href="https://github.com/kishanpython/Automobile-Tasks/blob/main/Task-1/db_schema/Saving%20data%20in%20database.ipynb"> view </a></li>
</ul>

## Task B:- Make a Dashboard by using pre-processed data to show vehicle location on map and other variables values on graph.
<ul>
  <li>Dashboard formation using 'Dash' :- <a href="https://github.com/kishanpython/Automobile-Tasks/tree/main/Task-2/Dashbord">View</a></li>
  <li>Dashboard deployment link :- <a href="https://vehicle-dash.herokuapp.com/">view</a></li>
</ul>

## Task C:- Building of Model.
<ul>
  <li>Independent Variables are :- 'RPM' and 'TPS %' and Dependent Variable is :- 'Inj Q Tor (mg-st)'</li>
  <li>Model Notebook Link :- <a href="https://github.com/kishanpython/Automobile-Tasks/blob/main/Task-3/Task-3%20Data%20Modelling.ipynb">view</a></li>
</ul>

## Conclusion :- 
In this project I worked on data cleaning, data saving on dbms, dashboard formation and data modelling parts.

