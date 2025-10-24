import streamlit as st

st.set_page_config(page_title='视频播放器', page_icon='🥽')
st.header('弄弄囔囔视频播放器🥽')



audio_file = [{
    'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/03/80/33150208003/33150208003-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&deadline=1761301881&oi=771356656&nbs=1&os=cosovbv&mid=0&uipk=5&trid=cf2039839498427487e8c16cd924f24h&gen=playurlv3&og=cos&upsig=0ba151af47a2d491eb2e54264a274cdf&uparams=e,platform,deadline,oi,nbs,os,mid,uipk,trid,gen,og&bvc=vod&nettype=0&bw=715939&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'parm': '赋能哥',
    '🕶️': '1'},
              {
    'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/01/16/33062651601/33062651601-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=c6f0df6c544a4556aa126ae11947578h&os=cosovbv&og=cos&nbs=1&platform=html5&deadline=1761302043&gen=playurlv3&uipk=5&mid=0&oi=771356656&upsig=f0912953f47b58754cebe03bedfa4880&uparams=e,trid,os,og,nbs,platform,deadline,gen,uipk,mid,oi&bvc=vod&nettype=0&bw=526332&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'parm': '赋能哥',
    '🕶️': '2'},
              {
    'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/54/75/32609337554/32609337554-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=fbc3c3c0013e4765aa887298e4f9e6dh&oi=771356656&platform=html5&nbs=1&uipk=5&gen=playurlv3&os=cosovbv&og=hw&deadline=1761302068&mid=0&upsig=acbcda68cfc3d0f0a0a3d427bfdf8cbe&uparams=e,trid,oi,platform,nbs,uipk,gen,os,og,deadline,mid&bvc=vod&nettype=0&bw=613550&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
    'parm': '赋能哥',
    '🕶️': '3'},
              {
    'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/86/72/32355387286/32355387286_qe1-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=2e24b8d7218f42f485d9c5d93f4b67dh&uipk=5&platform=html5&gen=playurlv3&os=cosovbv&og=hw&deadline=1761302101&nbs=1&oi=771356656&mid=0&upsig=90edbd6bb12e8ae064af225e948ef133&uparams=e,trid,uipk,platform,gen,os,og,deadline,nbs,oi,mid&bvc=vod&nettype=0&bw=625624&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
    'parm': '赋能哥',
    '🕶️': '4'},
              {
     'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/38/08/32888130838/32888130838-1-192.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302121&gen=playurlv3&os=cosovbv&mid=0&oi=771356656&nbs=1&og=hw&platform=html5&uipk=5&trid=08169b26c5304cd4ae2c1b54b0ee1e3h&upsig=91e31c63297bf33bc7b553b6f192dd1e&uparams=e,deadline,gen,os,mid,oi,nbs,og,platform,uipk,trid&bvc=vod&nettype=0&bw=837474&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
    'parm': '赋能哥',
    '🕶️': '5'}
              
              ]


if 'a' not in st.session_state:
    st.session_state['a'] = 0
    
st.title(audio_file[st.session_state['a']]['parm']+ '-第'+audio_file[st.session_state['a']]['🕶️']+ '集')
st.video(audio_file[st.session_state['a']]['url'], width = 600)


def nextimg(arg):
    st.text(arg)
    st.session_state['a'] = int(arg)

for i in range(len(audio_file)):

    st.button('第'+str(i + 1)+'集', use_container_width=True, on_click=nextimg,args=[i])
    
