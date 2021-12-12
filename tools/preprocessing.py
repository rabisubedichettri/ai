import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler


def feature_data(df):
    # this function for convert find data features
    feature_dict = {"Columns": [], "unique": [], "Is_misssing": [], "Dtypes": []}
    for col in df.columns:
        feature_dict["Columns"].append(col)
        feature_dict["unique"].append(df[col].unique().shape[0])
        feature_dict["Is_misssing"].append(df[col].isna().sum())
        feature_dict["Dtypes"].append(df[col].dtypes)
    # feature_dict
    feature_df = pd.DataFrame.from_dict(feature_dict)
    des_df = pd.DataFrame(df.describe().T)
    merged_feature_df = pd.concat([feature_df.set_index('Columns'), des_df], axis=1)
    return merged_feature_df


# Now we all are ready to differentiate the numerical and categorical columns
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
                string_type_col.append(col)
    return string_type_col


def create_dummies(df, string_col_name):
    dummies_df = pd.get_dummies(data=df, columns=string_col_name)
    return dummies_df


def Data_normalized(df):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)
    return scaled


def train_machine(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    reg = LinearRegression().fit(X_train, y_train)
    return reg
