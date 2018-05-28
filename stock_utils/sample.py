import stock_utils.utils as sutils

stock_pd = sutils.get_stock_info_tencent(["600340", "600341"])
shiyinglv = stock_pd.loc['600340']
print(shiyinglv['市净率'])