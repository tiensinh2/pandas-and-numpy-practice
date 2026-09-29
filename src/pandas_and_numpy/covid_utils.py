def clean_covid_df(filepath):
    df = pd.read_csv(filepath)
    date_cols = df.columns[4:]
    
    # Tính daily
    daily = df[date_cols].diff(axis=1).clip(lower=0)
    
    # Groupby quốc gia
    country_cumulative = df.groupby('Country/Region')[date_cols].sum()
    df_temp = df[['Country/Region']].copy()
    df_temp[date_cols] = daily
    country_daily = df_temp.groupby('Country/Region')[date_cols].sum()
    
    # Chuyển sang datetime
    date_index = pd.to_datetime(date_cols)
    country_cumulative.columns = date_index
    country_daily.columns = date_index
    
    return country_cumulative, country_daily

# Dùng cho cả 3
conf_cum, conf_daily = clean_covid_df('time_series_covid19_confirmed_global.csv')
death_cum, death_daily = clean_covid_df('time_series_covid19_deaths_global.csv')
recov_cum, recov_daily = clean_covid_df('time_series_covid19_recovered_global.csv')