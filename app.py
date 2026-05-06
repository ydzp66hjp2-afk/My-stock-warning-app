import streamlit as st

st.set_page_config(page_title="五檔防禦執行器", layout="centered")

st.title("🛡️ 籌碼防禦執行面板")
st.write("請於每日 17:00 數據更新後填入以下數值")

# 第一部分：今日即時數據[span_2](start_span)[span_2](end_span)
st.subheader("第一步：輸入今日收盤數據")
col1, col2, col3 = st.columns(3)
with col1:
    today_ratio = st.number_input("今日融資維持率 (%)", value=165.0, format="%.1f")
with col2:
    today_margin = st.number_input("今日融資餘額 (億)", value=3000.0)
with col3:
    today_index = st.number_input("今日加權指數收盤", value=20000.0)

# 第二部分：對比基準[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
st.subheader("第二步：輸入 20 個交易日前數據")
col_a, col_b = st.columns(2)
with col_a:
    base_margin = st.number_input("20日前融資餘額 (億)", value=2800.0)
with col_b:
    base_index = st.number_input("20日前加權指數", value=19000.0)

# 第三部分：自動計算與指令[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)
st.divider()

# 計算變動率與 K 值[span_8](start_span)[span_8](end_span)
margin_chg = (today_margin / base_margin) - 1
index_chg = (today_index / base_index) - 1
k_val = round(margin_chg / index_chg, 2) if index_chg != 0 else 0

st.header(f"計算結果：K 值 = {k_val}")

if today_ratio > 190 and k_val > 1.5:
    st.error("🚨 【第五檔：崩潰邊緣】")
    st.warning("指令：大盤 70% / 固收 30% (活存 15% / 00713 15%)")
elif today_ratio > 185 and k_val > 1.3:
    st.warning("⚠️ 【第四檔：過熱期】")
    st.info("指令：大盤 75% / 25% (活存 12.5% / 00713 12.5%)")
elif today_ratio >= 170 and k_val >= 1.0:
    st.info("🟡 【第三檔：警戒區】")
    st.info("指令：大盤 80% / 20% (活存 10% / 00713 10%)")
else:
    st.success("✅ 【常態/安全區】")
    st.info("維持原配置，無需變動。")

