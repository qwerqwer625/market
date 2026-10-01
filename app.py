import streamlit as st
import pandas as pd
import numpy as np

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="منصة مراقبة الأسواق المالية - EO Style",
    page_icon="📊",
    layout="wide"
)

st.title("📈 لوحة المؤشرات المالية المتقدمة")
st.markdown("مرحباً بك! هذه النسخة المطورة والمجهزة بمؤشرات فنية تفاعلية.")

# الشريط الجانبي للإعدادات المتقدمة
st.sidebar.header("⚙️ إعدادات المنصة")
asset = st.sidebar.selectbox(
    "اختر الأصل المالي:",
    ["العملات الرقمية (Crypto)", "الأسهم (Stocks)", "الفوركس (Forex)", "السلع (Commodities)"]
)

timeframe = st.sidebar.selectbox(
    "الإطار الزمني:",
    ["دقيقة (1m)", "ساعة (1h)", "يومي (1D)", "أسبوعي (1W)"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🧮 حاسبة الصفقة السريعة")
entry_price = st.sidebar.number_input("سعر الدخول ($)", value=150.0)
investment = st.sidebar.number_input("مبلغ الاستثمار ($)", value=1000.0)
target_profit = st.sidebar.slider("نسبة الهدف المستهدف (%)", 1, 50, 10)

expected_return = investment * (target_profit / 100)
st.sidebar.success(f"الربح المتوقع: ${expected_return:.2f}")

# توليد بيانات محاكاة واقعية للسعر مع مؤشرات فنية
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")
prices = 150 + np.cumsum(np.random.randn(30) * 2)

df = pd.DataFrame({
    'السعر': prices,
    'المتوسط المتحرك (SMA 5)': pd.Series(prices).rolling(5).mean(),
    'المتوسط المتحرك (SMA 10)': pd.Series(prices).rolling(10).mean()
}, index=dates)

# عرض القسم الرئيسي
st.subheader(f"تحليل الأداء الحي لـ: {asset} ({timeframe})")

# المؤشرات السريعة (Metrics)
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="السعر الحالي", value=f"${prices[-1]:.2f}", delta="+3.4%")
col2.metric(label="أعلى سعر اليوم", value=f"${max(prices):.2f}", delta="+1.2%")
col3.metric(label="أقل سعر اليوم", value=f"${min(prices):.2f}", delta="-0.8%")
col4.metric(label="مؤشر القوة النسبية RSI", value="58.4", delta="محايد")

# الرسم البياني المتقدم
st.markdown("### 📉 الرسم البياني وحركة الأسعار مع المتوسطات المتحركة")
st.line_chart(df)

# جدول بيانات الأسعار
st.markdown("### 📋 سجل الأسعار التفصيلي")
st.dataframe(df.tail(10), use_container_width=True)

st.markdown("---")
st.caption("تم تطوير لوحة المؤشرات هذه وتحديثها بنجاح عبر الأيباد والتخزين السحابي.")
