from pandas import concat, DataFrame


def generate_average_rcf(rcf_list: list[dict]) -> DataFrame:
    df_list = []

    for inner_list in rcf_list:
        inner_df_list = []
        for d in inner_list:
            df = DataFrame.from_dict(d, orient='index').T
            inner_df_list.append(df)
        inner_result_df = concat(inner_df_list)
        df_list.append(inner_result_df)

    average_rcf = concat(df_list, axis=0, ignore_index=True)

    average_rcf = average_rcf.groupby('month').sum()

    total = average_rcf.sum().rename('Total')
    average = average_rcf.mean().rename('Average')
    average_rcf = average_rcf.T
    average_rcf = concat((average_rcf, total), axis=1)
    average_rcf = concat((average_rcf, average), axis=1)
    average_rcf = average_rcf.T
    return average_rcf
