from preprocessing import feature_data, cate_to_num, Data_normalized
from preprocessing import create_dummies, train_machine


def estimate(df):
    feature_data_ = feature_data(df)
    target_col = 'Salary'
    input_data = df.drop(columns=target_col)
    cate_col_lis = cate_to_num(input_data, feature_data_)
    if len(cate_col_lis) == 0:
        norm_df = Data_normalized(input_data)
    else:
        dummies_df = create_dummies(input_data, cate_col_lis)
        norm_df = Data_normalized(input_data)
    dict_data = train_machine(norm_df, df[target_col])
    return dict_data
