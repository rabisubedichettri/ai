import pandas as pd


def feature_data(df):
    feature_dict = {"Columns": [], "unique": [], "Is_misssing": [], "Dtypes": []}
    for col in df.columns:
        feature_dict["Columns"].append(col)
        feature_dict["unique"].append(df[col].unique().shape[0])
        feature_dict["Is_misssing"].append(df[col].isna().sum())
        feature_dict["Dtypes"].append(df[col].dtypes)
    feature_df = pd.DataFrame.from_dict(feature_dict)
    des_df = pd.DataFrame(df.describe().T)
    merged_feature_df = pd.concat([feature_df.set_index('Columns'), des_df], axis=1)
    return merged_feature_df


def cate_to_num(df, feature_df):
    string_type_col = []
    num_type_col = []
    for col in df.columns:
        if df[col].dtypes in ['int', 'float']:
            df[col].astype('float')
            num_type_col.append(col)
        else:
            try:
                df[col].astype('float')
                num_type_col.append(col)
            except:
                if feature_df.loc['unique', col] in range(2, 11):
                    string_type_col.append(col)
    return string_type_col, num_type_col


def estimate(df):
    feature_df = feature_data(df).T
    target_col = df.columns[-1]
    input_data = df.drop(columns=target_col)
    str_col_lis, cate_col_lis = cate_to_num(input_data, feature_df)
    return print('{} are numerical columns \n\n  {} are categorical columns'.format(str_col_lis, cate_col_lis))
