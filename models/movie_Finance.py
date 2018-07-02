#coding=utf-8
import tushare as tu
import numpy as nu
import pandas as pa
import matplotlib
import matplotlib.pyplot as mmplot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
type=sys.getfilesystemencoding()

def movie():
    df = tu.realtime_boxoffice()
    df_data = nu.array(df)
    df_list = df_data.tolist()
    send_df_list = []
    for i in df_list:
        send_df_list.append('-'.join(i[:-1]))
    send_df_list.insert(0, u"实时票房(万)-票房排名-影片名称-票房占比-上映天数-累计票房(万)")
    str_send_df_list = '\n'.join(send_df_list)
    return str_send_df_list

def cinema():
    dd = tu.day_cinema()
    dd_data = nu.array(dd)
    dd_list = dd_data.tolist()
    send_dd_list = []
    for i in dd_list[:10]:
        send_dd_list.append('-'.join(i))
    send_dd_list.insert(0,u"上座率-场均人次-影院名称-排名-今日观众-今日票房-今日场次-场均票价")
    str_send_dd_list = '\n'.join(send_dd_list)
    return str_send_dd_list


#感觉好水啊。。。。
def history_data(str):    #财经历史数据
    str_list=str.split('#')
    if str_list[0]==str_list[-1]:
        tu_data = tu.get_hist_data(str)
        pa_data = pa.DataFrame(tu_data)
        #mmplot.show()
        ax = pa_data.plot()
        fig = ax.get_figure()
        fig.savefig(str + '-'+'all'+'.png')
        return str + '-'+'all'+'.png'
    else:
        tu_data = tu.get_hist_data(str(str_list[0]), ktype=str(str_list[-1]))
        pa_data = pa.DataFrame(tu_data)
        # mmplot.show()
        ax = pa_data.plot()
        fig = ax.get_figure()
        fig.savefig(str + '-' + str(str_list[-1]) + '.png')
        return str + '-' + str(str_list[-1]) + '.png'




