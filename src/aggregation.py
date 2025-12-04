def calculate_daily_totals(df):
    df_daily = df.resample('D', on='timestamp')['kwh'].sum().reset_index()
    return df_daily

def calculate_weekly_aggregates(df):
    df_weekly = df.resample('W', on='timestamp')['kwh'].sum().reset_index()
    return df_weekly

def building_wise_summary(df):
    summary = df.groupby('building')['kwh'].agg(['mean','min','max','sum'])
    summary.rename(columns={'sum':'total_consumption'}, inplace=True)
    return summary
