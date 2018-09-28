import pytest
import numpy as np
import pandas
import modin.pandas as pd
import os
from modin.pandas.utils import to_pandas

frame_data = {
    "col1": [0, 1, 2, 3],
    "col2": [4, 5, 6, 7],
    "col3": [8, 9, 0, 1],
    "col4": [2, 4, 5, 6]
}

nan_data = {
    "col1": [np.nan, 1, 2, 3],
    "col2": [4, 5, 6, np.nan],
    "col3": [8, 9, np.nan, 1],
    "col4": [2, np.nan, 5, np.nan]
}

frame_data2 = {"col5": [0], "col6": [1]}

# ray_df = pd.read_csv("~/2017.csv")
ray_df = pd.read_csv("~/Downloads/201710k.csv")
drop_cols = ["Unnamed: " + str(n) for n in [0,4,5,7]]
print(ray_df.columns)
ray_df = ray_df.drop(columns=drop_cols)
# ray_df = pd.read_csv("~/Downloads/googleplaystore.csv")
# ray_df = pd.DataFrame(frame_data)

def test_read_csv(benchmark):
    path = "~/Downloads/201710k.csv"
    result = benchmark(pd.read_csv, path)
    print(result)

def test_sum(benchmark):
    # ray_df = pd.DataFrame(frame_data)
    result = benchmark(pd.DataFrame.sum, ray_df)

def test_fillna(benchmark):
    result = benchmark(pd.DataFrame.fillna, ray_df, 0)

def test_add(benchmark):
    result = benchmark(pd.DataFrame.add, ray_df, 1)
    
def test_add_df(benchmark):
    result = benchmark(pd.DataFrame.add, ray_df, ray_df)

def test_describe(benchmark):
    result = benchmark(pd.DataFrame.describe, ray_df)

def test_isna(benchmark):
    result = benchmark(pd.DataFrame.isna, ray_df)


########################## DEVIN's Tests above

# @pytest.fixture
# def ray_df_equals_pandas(ray_df, pandas_df):
#     return to_pandas(ray_df).equals(pandas_df)

# @pytest.fixture
# def test_inter_df_math(op, simple=False):
#     ray_df = pd.DataFrame(frame_data)
#     return getattr(ray_df, op)(ray_df)

# @pytest.fixture
# def test_operator(op):
#     ray_df = pd.DataFrame(frame_data)
#     return getattr(ray_df, op)(ray_df) 

# def test_add(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.add, ray_df, nan_df)

# def test_mean(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.mean, ray_df)

# def test_sum(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.sum, ray_df)

# def test_mode(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.mode, ray_df)

# def test_sub(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.sub, ray_df, nan_df)

# def test_max(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.max, ray_df)

# def test_le(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.le, ray_df, nan_df)

# def test_count(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.count, ray_df)

# def test_std(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.std, ray_df)

# def test_ne(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.ne, ray_df, nan_df)

# # def test_corr(benchmark):
# #     ray_df = pd.DataFrame(frame_data)
# #     result = benchmark(pd.DataFrame.corr, ray_df)

# def test_median(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.median, ray_df)

# def test_min(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.min, ray_df)

# def test_describe(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.describe, ray_df)

# def test_info(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.info, ray_df)

# def test_keys(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.keys, ray_df)

# def test_items(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.items, ray_df)

# def test_get(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.get, ray_df, 'col1')

# def test_dataframe(benchmark):
#     result = benchmark(pd.DataFrame, frame_data)

# def test_append(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     ray_df2 = pd.DataFrame(frame_data2)
#     result = benchmark(pd.DataFrame.append, ray_df, ray_df2)

# def test_head(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.head, ray_df, 10)

# def test_sort_values(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.sort_values, ray_df, by=['col1'])

# def test_astype(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.astype, ray_df, 'int64')

# def test_fillna(benchmark):
#     ray_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.fillna, ray_df, 0)

# def test_drop(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.drop, ray_df, ['col1', 'col3'], axis=1)

# def test_read_csv(benchmark):
#     path = "~/2017.csv"
#     result = benchmark(pd.read_csv, path)

# def test_to_csv(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     cwd = os.getcwd() + "/out.csv"
#     result = benchmark(pd.DataFrame.to_csv, ray_df, cwd)

# def test_concat(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.concat, [ray_df, nan_df])

# def test_apply(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.apply, ray_df, np.sqrt)

# def test_join(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.join, ray_df, nan_df, lsuffix="other_")

# def test_reset_index(benchmark):
#     ray_df = pd.DataFrame(frame_data)
#     result = benchmark(pd.DataFrame.reset_index, ray_df)

# def test_groupby(benchmark):
#     nan_df = pd.DataFrame(nan_data)
#     result = benchmark(pd.DataFrame.groupby, nan_df, 'col4')
