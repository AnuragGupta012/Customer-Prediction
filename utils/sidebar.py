import streamlit as st

def sidebar():

    with st.sidebar:

        # Center Logo
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/logo.png", width=120)

        # Center Title
        st.markdown(
            "<h3 style='text-align:center;'>Customer Churn</h3>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.success("👨‍💻 Developed by Anurag Gupta")

        st.caption("B.Tech CSE")

        st.markdown("---")

        st.info("🤖 Random Forest")

        st.info("📊 IBM Telco Dataset")

        st.info("🎯 Accuracy : 82%")