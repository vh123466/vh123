import streamlit as st
st.markdown('# 🤦‍♂️学生小张—数字档案')
st.markdown('## 🤏基础信息')

st.markdown('''### 学生ID：411大王
注册时间: :red[2025-10-20]  |精神状态: :red[神经👵]

当前教室: :green[实训楼204] |安全等级: :red[已泄密]''')

st.subheader('天气情况⛅')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="温度", value="28℃", delta="31℃")
c2.metric(label="湿度", value="76%", delta="73%")
c3.metric(label="风速", value='F2', delta="2%")

import pandas as pd
st.markdown('***')
st.markdown(' ## 篮球赛🏀')
data = {
    '1号':[12, 8, 11, 5, 18],
    '2号':[2, 2, 5, 3, 6],
    '3号':[20, 24, 18, 15, 25],
}
# 定义数据框所用的索引
index = pd.Series(['01场', '02场', '03场', '04场', '05场'], name='场数')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.write(df)
st.markdown('***')
st.markdown(' ## 最新代码成果🌱')
str = '''import pandas as pd
st.markdown('***')
st.markdown(' ## 篮球赛🏀')
data = {
    '1号':[12, 8, 11, 5, 18],
    '2号':[2, 2, 5, 3, 6],
    '3号':[20, 24, 18, 15, 25],
}'''
st.code(str)
st.markdown('***')
st.markdown(''' :green[>> SYSTEM MESSAGE:] 下一个目标已结算

 :green[>> COUNTDOWN:] 2025-10-20 11:48''')
