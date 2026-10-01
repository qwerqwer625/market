
import streamlit as st
import pandas as pd
import numpy as np

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="تطبيق مراقبة الأسواق المالية",
    page_icon="📈",
    layout="wide"
)

st.title("📊 لوحة تحكم ومراقبة الأسواق المالية")
st.markdown("مرحباً بك! هذه النسخة المطورة من تطبيقك المالي التفاعلي.")

# الشريط الجانبي للإعدادات
st.sidebar.header("إعدادات العرض")
asset = st.sidebar.selectbox(
    "اختر الأصل المالي للمتابعة:",
    ["الأسهم الأمريكية (US Stocks)", "العملات الرقمية (Crypto)", "العملات الأجنبية (Forex)", "السلع (Commodities)"]
)

timeframe = st.sidebar.selectbox(
    "الإطار الزمني:",
    ["اليوم (1D)", "الأسبوع (1W)", "الشهر (1M)", "السنة (1Y)"]
)

st.sidebar.markdown("---")
st.sidebar.info("التطبيق متصل ومحدث تلقائياً عبر Streamlit Cloud.")

# عرض محتوى بناءً على الاختيار
st.subheader(f"تحليل الأداء لـ: {asset} ({timeframe})")

# محاكاة بيانات مالية لتجربة الواجهة والرسوم البيانية
chart_data = pd.DataFrame(
    np.random.randn(20, 3) * 10 + 150,
    columns=['السعر الأعلى', 'السعر الأدنى', 'سعر الإغلاق']
)

# عرض الرسم البياني التفاعلي
st.line_chart(chart_data)

# جدول بيانات تفصيلي
st.markdown("### 📋 أحدث التغيرات السعرية")
st.dataframe(chart_data, use_container_width=True)

# مؤشرات سريعة
col1, col2, col3 = st.columns(3)
col1.metric(label="السعر الحالي", value="$154.20", delta="+2.3%")
col2.metric(label="حجم التداول", value="1.2B", delta="-0.5%")
col3.metric(label="القيمة السوقية", value="$45B", delta="+1.2%")
