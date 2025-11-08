from scipy.stats import zscore

def clean_and_flag_outliers(df, cols):
    z_scores = df[cols].apply(zscore)
    df['Outlier'] = (z_scores.abs() > 3).any(axis=1)
    for col in cols:
        df[col] = df[col].fillna(df[col].median())
    return df[~df['Outlier']]