# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:12:21 2024

@author: PVS
"""
import   pandas               as      pd
import   numpy                as      np

def understand_data(df, target, unwanted = []):
    import   pandas               as    pd
    import   numpy                as    np
    import   matplotlib.pyplot    as    plt
    import   seaborn              as    sns
### 1 Null values
    print("\n(1) Missing values")
    cols                 =  df.columns
    c                    =  df.isnull().sum()
    p                    =  round((df.isnull().sum() * 100) / df.shape[0],2)
    count_df             =  pd.DataFrame({'Column' : cols, 'NA Count' : c, 'NA Percentage' : p })
    print("Presence of Nulls: ",df.isnull().values.any())
    if df.isnull().values.any():
        filtered_df1         =  count_df[(count_df['NA Count'] > 0)]
        filter80_df1         =  count_df[(count_df['NA Percentage'] > 80)]  
        print("\nNull values")
        print(filtered_df1)
        print("\nNull values above 80 & above to be dropped from the data")
        print(filter80_df1)
        cols80              =   filter80_df1['Column'].tolist()
        print(cols80)

        for m in range(len(cols80)):
            colx   =   cols80[m]
            print("\nDrop the column, %s having excessive nulls" % colx)
            df.drop(colx, axis = 1, inplace = True)      
### 2 Zero values
    dfn                  =  df.select_dtypes(include = np.number)
    cols                 =  dfn.columns
    dfmerged             =  pd.DataFrame()
    print("\n\n")
    for col in cols:
        d1     = df[col].value_counts().to_dict()
        dk     =  d1.get(0, 'No Zeros')
        i      =  0
        if  dk != 'No Zeros':
            dicts        =  {'Column': col, 'Zeros' :  d1[0]}
            i            =  i + 1
            df1          =  pd.DataFrame(dicts, index = [0])
            dfmerged     =  pd.concat([dfmerged, df1])
    dfmerged['Slno']     =  range(dfmerged.shape[0])
    dfmerged.set_index('Slno', inplace = True)

    print("\n(2) Zero values")
    print(dfmerged)
### 3 Unique values
    print("\n(3)Unique values")
    k = df.columns
    for i in k:
        unicol  =  df[i].nunique()
        print('\nNumber of Unique values in ',i,'is: ',df[i].nunique())
        if unicol == 1:
           print("Variables having constant values to be removed from the dataset", i)
           df.drop(i, axis = 1, inplace = True)           
### 4 Duplicate values
    print("\n(4)Duplicate values")  
    dups      = df.duplicated()
   # count the number of duplicated rows
    dup_count  = dups.sum()
    print("Number of duplicated rows: ", dup_count)
    if dup_count > 0:
       print("\nDropping duplicates")
       df.drop_duplicates(inplace = True)    
### 5 Remove unwanted columns
    print("\n(5)Remove unwanted columns") 
    print("\nDropping unwanted columns {}".format(unwanted))        
    df.drop(unwanted, axis = 1, inplace = True)         
    print("\n Dataframe has {0} rows and {1}".format(df.shape[0], df.shape[1]))
### 5 Distribution of classes in the Target variable 
    print("\n(5)Classes in the Target variable")     
    counts          =    df[target].value_counts()
    percs           =    df[target].value_counts(normalize = True)
    df_target       =    pd.concat([counts,percs], axis=1, keys=['count', 'percentage'])
    print(df_target)
### Barplot    
    ax    =  sns.countplot(x=df[target],hue = target, legend = True, data = df);
    total =  df[target].count()

    # annotate the bars with fmt from matplotlib v3.7.0
    for c in ax.containers:
        ax.bar_label(c, fmt=lambda x: f'{(x/total)*100:0.1f}%')
   
    # show plot
    plt.show()
###
file = 'G:\DSE-FT-C-May24-G5\Data\Customer-Churn-Records.csv'

df =  pd.read_csv(file, encoding = 'Latin-1')
print(df.shape)
print(df.columns)

print("\n Rows {0} Columns {1}".format(df.shape[0], df.shape[1]))
print(df.info())

X    =  df[['CreditScore', 'Geography','Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',\
             'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Complain', 'Satisfaction Score', 'Card Type', 'Point Earned']]
y   =   df['Exited']               
target = 'Exited'                 
## Remove unwanted columns
unwantedcols = ['RowNumber', 'CustomerId', 'Surname' ]
understand_data(df, target, unwantedcols)
