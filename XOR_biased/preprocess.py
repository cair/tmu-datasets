def preprocess(df):
    df.replace({
        "F": 0,
        "T": 1
    }, inplace=True)
    return df.astype(int)
