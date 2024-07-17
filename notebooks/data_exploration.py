import pandas as pd
import os, sys
# change run dir to script path
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

## data import
## in following line change name of file you want to look at
path_file = '../data/raw/imdb/title.akas.tsv.gz'
df = pd.read_csv(path_file, sep = '\t') # for tsv files
#df = pd.read_csv(path_file) # for csv files
## general overview
print('============ overview of data in %s ===========' % path_file.split('/')[-1])
print('====================== .head() ======================')
print(df.head())

print('\n')
print('====================== .info() ======================')
print(df.info())

# calculation of parecentage NaNs: sum of NaN divided by length of df
nan_rate = df.isna().sum()/df.shape[0]
print('\n')
print('================== percentage NaNs ==================')
print(nan_rate)

##individual statistics
print('\n')
print('=============== variable distribution ===============')
# create DataFrame u consisting only of object type variables for counting unique values
u = df.select_dtypes(include=[object])
print('number of unique values for object variables')
# for each column in u print column name and number of unique values
for i in u.columns:
    print('%s:' % i, len(pd.unique(u[i])))

print('\n')
# create DataFrame s consisting only of non-object type variables for basic descriptive statistics
s = df.select_dtypes(exclude=[object])
# for each column in u print column name and number of unique values
for i in s.columns:
    print('basic statistics for %s' % i, '\n', s[i].describe())
    print('\n')