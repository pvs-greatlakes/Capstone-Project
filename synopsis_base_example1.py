# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:37:19 2024

@author: PVS
"""
import   pandas               as      pd
import   numpy                as      np
def understand_data(df, target):
    import   pandas               as    pd
    import   numpy                as    np
    import   matplotlib.pyplot    as    plt
    import   seaborn              as    sns
    # importing pipes for making the Pipe flow
    cols                 =  df.columns
    c                    =  df.isnull().sum()
    p                    =  round((df.isnull().sum() * 100) / df.shape[0],2)
    count_df             =  pd.DataFrame({'Column' : cols, 'NA Count' : c, 'NA Percentage' : p })
    filtered_df1         =  count_df[(count_df['NA Count'] > 0)]
    print("\nMissing values")
    print(filtered_df1)

    dfn                  =  df.select_dtypes(include = np.number)
    cols                 =  dfn.columns
    dfmerged             =  pd.DataFrame()
    for col in cols:
        d1     = df[col].value_counts().to_dict()
        ## print(d1)
        dk     =  d1.get(0, 'No Zeros')
        i      =  0
        if  dk != 'No Zeros':
            dicts        =  {'Column': col, 'Zeros' :  d1[0]}
            print(dicts)
            i            =  i + 1
            df1          =  pd.DataFrame(dicts, index = [0])
            dfmerged     =  pd.concat([dfmerged, df1])
    dfmerged['Slno']     =  range(dfmerged.shape[0])
    dfmerged.set_index('Slno', inplace = True)

    print("\nZero values")
    print(dfmerged)

    counts          =    df[target].value_counts()
    percs           =    df[target].value_counts(normalize = True)
    df_target       =    pd.concat([counts,percs], axis=1, keys=['count', 'percentage'])
    print(df_target)
    sns.countplot(x = target,  data = df)
    # show plot
    plt.show()

file   =  r'G:\DSE-FT-B-JUN24-G2\Data\diabetic_data.csv'
df     =  pd.read_csv(file, keep_default_na=False, na_values=['?'])
# create a list of our conditions
conditions = [
        (df['readmitted'] ==  '>30') | (df['readmitted'] == 'NO'),    
        (df['readmitted'] == '<30' )
]

# create a list of the values we want to assign for each condition
values = [0, 1]

# create a new column and use np.select to assign values to it using our lists as arguments
df['Target'] = np.select(conditions, values)

print("\n Rows {0} Columns {1}".format(df.shape[0], df.shape[1]))
print(df.info())

X    =  df[['encounter_id', 'patient_nbr', 'race', 'gender', 'age','admission_type_id', 'discharge_disposition_id',\
             'admission_source_id','time_in_hospital', 'payer_code', 'medical_specialty','num_lab_procedures', 'num_procedures',\
            'num_medications','number_outpatient', 'number_emergency', 'number_inpatient', 'diag_1','diag_2', 'diag_3',\
            'number_diagnoses', 'max_glu_serum', 'A1Cresult','metformin', 'repaglinide', 'nateglinide', 'chlorpropamide',\
            'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide','pioglitazone', 'rosiglitazone', 'acarbose',\
            'miglitol', 'troglitazone','tolazamide', 'examide', 'citoglipton', 'insulin','glyburide-metformin',\
            'glipizide-metformin','glimepiride-pioglitazone', 'metformin-rosiglitazone','metformin-pioglitazone', 'change',\
            'diabetesMed']]
y   =   df['Target']               
target = 'Target'                 
# fitting the data in the pipe
understand_data(df, target)
    
    