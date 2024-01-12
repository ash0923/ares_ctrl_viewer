import streamlit as st
import pandas as pd
import numpy as np


card_css = """
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 5px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
}

.map-container {
  height: 300px;
}
</style>

"""

st.markdown(card_css, unsafe_allow_html=True)

# カードを作成する関数


def create_card(title, content):
    with st.container():
        # カードのCSSクラスを適用
        st.markdown(f"""
        <div class="card">
          <div class="container">
            <h4><b>{title}</b></h4>
            <p>{content}</p>
          </div>
        </div>
        """,
                    unsafe_allow_html=True)


def card_with_map(dataframe):
    # カードのデザインを適用
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # マップの描画エリアを指定
    st.markdown('<div class="map" id="map">', unsafe_allow_html=True)
    # Streamlitのマップを埋め込む
    st.map(dataframe)
    # HTMLタグを閉じる
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


imu_data, wheel_data, radio_and_timer = st.columns(3)

data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

with imu_data:
    with st.container():
        st.map(data)
        st.markdown("""
        <div class="card">
          <div class="container">
            <h4><b>IMU data</b></h4>
            <p>imu data is here!</p>
          </div>
        </div>
        """,
                    unsafe_allow_html=True)


with wheel_data:
    create_card("Wheel DATA", "data")

with radio_and_timer:
    with st.container():
        create_card("Radio", "data")
    with st.container():
        create_card("timer", "data")

st.write("---")

col4, col5 = st.columns([2, 1], gap="large")

with col4:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    card_with_map(df)

with col5:
    st.header("Column 2, Row 2")

st.write("---")
