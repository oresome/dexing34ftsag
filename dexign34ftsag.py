import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
import plotly.graph_objects as go
import pandas as pd
import pytz
#import pyecharts.options as opts
#from pyecharts.charts import Gauge
# mapbox_access_token = open(".mapbox_token").read()
#def SMOOTH_CURVE(data, window):
#    yhat = savgol_filter(data, window, 3)
#    return yhat


def serieschart_plot(df):
    # plot time sereis chart
    #dtm = []
    #wl = []

    #for df in sensorSeri:
    #    dtm_tmp, wl_tmp = WEAR_DATA_PARSE(df)
    #    dtm.append(dtm_tmp)
    #    wl.append(wl_tmp)

    # wl = SMOOTH_CURVE(wl, 21)
    #np.savetxt("wearData.csv", wl, delimiter=",")
    fig2 = go.Figure()
    config = {'displayModeBar': False}
    fig2.add_trace(
        go.Scatter(x=df["日期"], y=df["#35排传感器"],
                   line=dict(color='royalblue', width=5),
                   name="#35排传感器当前厚度 - [mm]"
                   )
    )

    fig2.add_trace(
        go.Scatter(x=df["日期"], y=df["#37排传感器"],
                   line=dict(color='coral', width=5),
                   name="#37排传感器当前厚度 - [mm]"
                   )
    )

    fig2.update_layout(
        xaxis_title="运行日期",
        yaxis_title="当前厚度 - [mm]",
        yaxis_range=[0, 350],
        showlegend=False,
        margin=dict(l=5, r=5, t=5, b=5),
        font=dict(
            family="sans serif, regular",
            size=11,
            color="Black"
        )
    )
    fig2.write_html("timeSeriesSensor.html", config=config)
    return

def WEAR_DATA_PARSE(wf):
    date = wf.split('.txt')[0].split('/')[-1].split('_')[0]
    # hours, minutes, secends = wf.split('.txt')[0].split('_')[1].split('-')
    hours, minutes, secends = wf.split('.txt')[0].split(date)[1].split('_')[1].split('-')
    dtm_obj = date + ' ' + hours + ':' + minutes + ':' + secends
    with open(wf) as f:
        lines = f.readlines()
    wl_obj = int(lines[9].split('\n')[0]) - 2
    ss_obj = int(lines[4].split('\n')[0])
    return dtm_obj, wl_obj, ss_obj


def main():
    st.set_page_config(page_title="耐普矿机IoT", layout="wide", initial_sidebar_state='auto')
    st.markdown(
            f"""
            <style>
                .reportview-container .main .block-container{{
                    max-width: 1600px;
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                    padding-bottom: 1rem;
                }}

                .fullScreenFrame > div {{
                    display: flex;
                    justify-content: left;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    #page = st.markdown(
    ##            f"""
    #            <style>
    #            .stApp {{
    #                background: url("https://kycg.s3.ap-east-1.amazonaws.com/sidebarBG.png");
    #                background-size: cover
    #            }}
    #            </style>
    #            """,
    #            unsafe_allow_html=True,
    #)

    # define files dir for all inputs
    #     cwd = os.getcwd()
    #cwd = "E:\\2项目资料\\耐普云平台demo"
    #sensorDataDir = 'UDP/'
    

    #sensorName = sensorDataDir + '*.txt'
    #sorted(glob.glob(sensorName))
    #sorted(glob.glob(sensorName), key=os.path.getmtime)
    #sensorSeri = glob.glob(sensorName)
    ##sensorSeri.sort(key=os.path.getmtime)
    #sensen1_data = []
    #sensen2_data = []
    #sensen3_data = []

    #sensen1_dt = []
    #sensen2_dt = []
    #sensen3_dt = []
    #for sss in sensorSeri:
    #    if sss != 'tmp.txt':
    #        latestDate, latestRead, sensor_label = WEAR_DATA_PARSE(sss)
    #        if sensor_label == 1:
    #            sensen1_dt.append(latestDate)
    #            sensen1_data.append(latestRead)
    #        elif sensor_label == 2:
    #            sensen2_dt.append(latestDate)
    #            sensen2_data.append(latestRead)
    #        elif sensor_label == 3:
    #            sensen3_dt.append(latestDate)
    #            sensen3_data.append(latestRead)

    #serieschart_plot(sensen1_dt, sensen1_data, sensen2_dt, sensen2_data, sensen3_dt, sensen3_data)
    #indicator_plot(latestRead)
    sensen1_data = 325
    sensen2_data = 325
    sensen3_data = 325
    sensen4_data = 0


    ###  第一部分  模型展示  ###
    top = st.container()
    with top:
        colll1, colll3 = st.columns([5,1])
        with colll1:
            st.title("江西耐普矿机智能监测系统 - 大山34尺半自磨机")
            #st.title("云南驰宏锌锗-会泽矿业")
            #st.subheader("当前状态（在运行） ")
            components.html(
                    """
                        <head>
                            <title> Blinking feature using JavaScript </title>
                            <style>
                                #blink {
                                    font-size: 20px;
                                    font-weight: bold;
                                    font-family: Microsoft Yahei;
                                    color: #6495ED;
                                    transition: 0.05s;
                                }
                            </style>
                        </head>

                        <body>
                            <p id="blink"> 当前状态（在运行） </p>
                            <script type="text/javascript">
                                var blink = document.getElementById('blink');
                                setInterval(function() {
                                    blink.style.opacity = (blink.style.opacity == 0 ? 1 : 0);
                                }, 1000);
                            </script>
                        </body>
                    """,
                    height = 50
                )
        with colll3:
            st.markdown("###")
            st.image("naipu.png")






    st.markdown("###")
    st.markdown("----------------------------------")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("#35排磨损传感器当前状态")
        current_thickness1 = str(sensen1_data) + " mm"
        delta_thickness1 = str(sensen1_data-325) + " mm"
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness1, delta=delta_thickness1)

    with col2:
        st.subheader("#37排磨损传感器当前状态")
        current_thickness3 = str(sensen3_data) + " mm"
        delta_thickness3 = str(sensen3_data-325) + " mm"
        st.markdown("最新状态时间：" + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness3, delta=delta_thickness3)
        #with col4:
    #with col3:
    #    # echats
    #    PLOT_GAUGE(3.4)
    #    HtmlFile = open("gauge_base.html", "r", encoding='utf-8')
    #    source_code_2 = HtmlFile.read()
    #    components.html(source_code_2, height=400)
        
    
    
    installDate = date(2022, 9, 25)
    currentDate = date.today()
    deltaDays = (currentDate - installDate).days
    st.subheader("已运行时间： " + str(deltaDays) + " Days")
    st.markdown("_______________________________________________________________________")
    #pyLogo = Image.open("install.png")
    st.subheader("传感器安装示意三维")
    #HtmlFile_tSS1 = open("dexxxing.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS1, height=500)
    #imgcol1, imgcol2, imgcol3 = st.columns(3)
    #with imgcol1:
    ##im1 = Image.open("install.png")
    #st.image(im1)
    #with imgcol2:
    #    im2 = Image.open("photos/image2.jpg")
    #    st.image(im2)
    #with imgcol3:
    #    im3 = Image.open("photos/image3.jpg")
    #    st.image(im3)
    #@st.cache
    #st.markdown("建设中，敬请期待！")
    iframeLINK = "https://dexing-pump-nzjah350-7b9d991d6fe-1306024390.tcloudbaseapp.com/Dexing.html"
    st.write(
            f'<iframe src=' + iframeLINK + ' height = "1000" width = "100%"></iframe>',
            unsafe_allow_html=True,
    )
    st.markdown("_______________________________________________________________________")

    ###  第三部分  磨损趋势  ###
    st.subheader("磨损历史数据")
    df = pd.read_csv("sensorThickness.csv")
    serieschart_plot(df)



    #st.subheader("Time Series Wear History")
    HtmlFile_tSS = open("timeSeriesSensor.html", 'r', encoding='utf-8').read()
    components.html(HtmlFile_tSS, height=600)


    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






if __name__ == "__main__":
    main()











