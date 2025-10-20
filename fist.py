import streamlit as st

st.title("我的第一个Streamlit应用")
st.text("Hello World!")

import streamlit as st   # 导入Streamlit并用st代表它

# 第一个普通文本展示元素，无工具提示
st.text("这是一个普通文本展示元素。")
# 第二个普通文本展示元素，有工具提示
st.text('这也是一个普通文本展示元素，带有工具提示',help='这是工具提示')
# 第三个普通文本展示元素，展示一些转义字符
st.text('''读者们，\n你们好\t！欢迎学习Streamlit''')

import streamlit as st   # 导入Streamlit并用st代表它
# 这里为了演示创建了多个标题展示元素

# 创建一个标题展示元素，内容是全英文的，默认锚点为first-title
st.title("first title")

# 创建一个标题展示元素，内容是全中文的
# 如不定义anchor参数，则无锚点
st.title("标题")

# 创建一个标题展示元素，内容是中英文混杂的
# 默认的锚点是英文部分的，即chinese
st.title("这是chinese标题")

# 标题展示元素,并增加了工具提示
st.title('这是第五个标题', help='工具提示')

import streamlit as st   # 导入Streamlit并用st代表它

# 创建一个为动物的标题，并指定锚点为动物
st.title("动物",anchor='动物')
# 创建一个文本，介绍一下动物
st.text('''动物（Animal）是生物的一个种类。它们一般以有机物为食，
是能够自主运动或能够活动的有感觉的生物。人类也是动物之一''')


# 创建一个章节，该章节为哺乳动物
st.header("哺乳动物:koala:")
# 创建一个文本，介绍一下哺乳动物
st.text('哺乳动物是动物世界中形态结构最高等。')


# 创建一个章节，该章节为爬行动物
st.header("爬行动物:turtle:")
# 创建一个文本，介绍一下爬行动物
st.text('爬行动物的代表有乌龟、鳄鱼、蜥蜴等。')


# 创建一个章节，该章节为鱼类
st.header("鱼类:fish:")
# 创建一个文本，介绍一下鱼类
st.text('鱼类，是最古老的脊椎动物。')

# 创建一个章节，该章节为鸟类
st.header("鸟类:bird:")
# 创建一个文本，介绍一下鸟类
st.text('由于能飞行，鸟类可以在世界的任何一个角落生存。')

import streamlit as st   # 导入Streamlit并用st代表它

# 创建一个为山西省的标题，并指定锚点为山西省
st.title("山西省",anchor='shanxi')
# 创建一个为简介的章节，并指定锚点为简介
st.header("简介",anchor='introduction')
# 创建一个普通文本，介绍山西省
st.text('''山西省，简称“晋”，中华人民共和国省级行政区，省会太原市，位于中国华北，东与河北省为邻，西与陕西省
相望，南与河南省接壤，北与内蒙古自治区毗连，介于北纬34°34′—40°44′，东经110°14′—114°33′。''')

# 创建一个为行政区划的章节，并指定锚点为行政区划
st.header("行政区划",anchor='area')
# 创建一个为太原市的子章节，并指定行政区划为简介
st.subheader("太原市", anchor='taiyuan')
st.text('''太原市，简称“并（bīng）”，古称晋阳，别称并州、龙城，山西省辖地级市、省会、Ⅰ型大城市，
国务院批复确定的中部地区重要的中心城市、以能源、重化工为主的工业基地''')

st.subheader("临汾市",anchor='linfen')
st.text('''临汾市，别称平阳、卧牛城、花果城，山西省辖地级市，位于山西西南部，东倚太岳，与长治、晋城为邻；西临
黄河，与陕西延安、渭南隔河相望，北起韩信岭，与晋中、吕梁毗连；南与运城接壤，因地处汾水之滨而得名''')

st.subheader("未完待续……")
st.subheader("🙎‍♂️何承霖大王驾到.......")

st.caption('这是一段yhon代码')
str = '''a = 1
    b = 2
    print(a*b)'''
a = 1
b = 2
st.code(a*b)
st.code(str)
st.code(str,language = None)

st.markdown('***')
st.markdown('# :red[阿梁大王来访]')
st.markdown('**啊啊啊啊啊**')
