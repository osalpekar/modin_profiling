Instructions to Run:

-1. download the dataset with this: `wget http://noaa-ghcn-pds.s3.amazonaws.com/csv/2017.csv`

0. run `pip install pytest-benchmark` and `pip install gitpython`

1. change the path to the modin repo in prof.py line 6 

2. copy the python notebook and test\_modin.py file to the parent directory of
   your local modin repo

3. copy prof.py into the root directory of the modin repo

4. checkout the modin repo to the rewrite\_backend branch and run prof.py

5. Once it has prof.py has finished, run the python notebook.
