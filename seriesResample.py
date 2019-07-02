import pandas as pd


def resample_series(data, period_min, agg_fn):
    # resample each time series to the desired period

    period_min = str(period_min) + 'min'
    resampled = data.resample(period_min, on='timestamp').apply(agg_fn)
    return resampled


def merge_by_timestamp(data, agg_fn):
    # merges the matching timestamps in data with agg_fn

    return data.groupby(pd.Grouper(key='timestamp')).agg(agg_fn)
