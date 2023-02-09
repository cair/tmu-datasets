def preprocess(df):
    df.replace({
        "absent": 0,
        "present": 1
    }, inplace=True)
    return df.astype(int)
