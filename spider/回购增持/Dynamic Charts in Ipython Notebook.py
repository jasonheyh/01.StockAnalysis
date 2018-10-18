
# coding: utf-8

# In[76]:


import os
import time
import numpy as np
import pandas as pd
import mof_public


# ## print raw html

# In[77]:


mof_public.print_html("""<h2 style='color: red'>hello, there</h2>""")


# ## print colorful text

# In[78]:


mof_public.print_text(text='Things happen for a reason --- from /Knight and Day/', color='blue')


# ## plot progress bar

# In[24]:


mof_public.print_progressbar(0, initial_bar=True)
for i in range(1, 101):
    mof_public.print_progressbar(i, initial_bar=False)
    time.sleep(np.random.rand() / 3)


# ## plot dataframe in excel format

# In[80]:


from lib import daily_report

### 
file_path = "/Ussers/chenshan/google_driver/github/litaotao.github.io/files"
try: 
    os.listdir(file_path)
except:
    file_path = "http://litaotao.github.io/files/"
    
print 'use data file path: ', file_path


# In[81]:


df1 = pd.read_msgpack('{}/dazong1.msg'.format(file_path))
df2 = pd.read_msgpack('{}/dazong2.msg'.format(file_path))

print 'raw print dataframe'
print df1.head(2)
print df2.head(2)

print '\nprint dataframe with mof_public'
mof_public.print_table(df1.head(2))
mof_public.print_table(df2.head(2))


# ## plot bar/line charts

# In[82]:


get_ipython().run_line_magic('pinfo', 'mof_public.draw')


# In[83]:


### notebook 环境下，如果把 mof_public.draw 运行结果显示的返回给一个变量，则 notebook 不会自动画图
figure = mof_public.draw(df1, x='tradeDate', y=['tradeVal'], type='spline', stock=True,title='大宗交易成交金额')


# In[84]:


### notebook 环境下，如果   没有   把 mof_public.draw 运行结果显示的返回给一个变量，则 notebook 会自动画图
mof_public.draw(df1, x='tradeDate', y=['tradeVal'], type='spline', stock=True,title='大宗交易成交金额')


# In[85]:


mof_public.draw(df2, x='secFullName', y=['tradeVal'], type='column', title='{} 个股大宗交易成交金额'.format('2017-09-26'), x_type='str')


# ## plot multi-bar

# In[86]:


df3 = pd.read_msgpack('{}/money_flow1.msg'.format(file_path))
df3.tail(2)


# In[87]:


mof_public.draw(df3, x='tradeDate', y=['小单净流入', '中单净流入', '大单净流入'], type='column', title='市场成单资金分布', x_type='str')


# ## plot multi-line
# 
# - `stock=True`: will use highstock.js to make the drawing
# - `stock=False`: will use highcharts.js to make the drawing

# In[88]:


df4 = pd.read_msgpack('{}/risk_factor1.msg'.format(file_path))
df4.tail(2)


# In[89]:


mof.draw(df4, x='tradeDate', type='spline', title='大类风格因子表现',
         y=['MOMENTUM', 'BETA', 'SIZE', 'EARNYILD', 'LIQUIDTY', 'RESVOL', 'GROWTH', 'BTOP', 'LEVERAGE'])


# In[90]:


mof.draw(df4, x='tradeDate', type='spline', title='大类风格因子表现', stock=True,
         y=['MOMENTUM', 'BETA', 'SIZE', 'EARNYILD', 'LIQUIDTY', 'RESVOL', 'GROWTH', 'BTOP', 'LEVERAGE'])


# ## plot 2 plots in one raw

# In[91]:


figure1 = mof.draw(df4, x='tradeDate', type='spline', title='大类风格因子表现', stock=False,
                   y=['MOMENTUM', 'BETA', 'SIZE', 'EARNYILD', 'LIQUIDTY', 'RESVOL', 'GROWTH', 'BTOP', 'LEVERAGE'])
figure2 = mof_public.draw(df3, x='tradeDate', y=['小单净流入', '中单净流入', '大单净流入'], type='column', title='市场成单资金分布', x_type='str')


# In[92]:


get_ipython().run_line_magic('pinfo', 'mof_public.draw_figure')


# In[93]:


mof_public.draw_figure(figure1, figure2)

