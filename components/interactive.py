import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_influencer_dashboard(key_prefix="default_dashboard"):
    try:
        df = pd.read_csv("components/influencer_roi_data.csv")
    except FileNotFoundError:
        st.error("Error: 'influencer_roi_data.csv' not found. Please check the file path.")
        st.error(f"Looking in: components/influencer_roi_data.csv")
        return

    # User filter - Use the key_prefix to make the key unique
    selected_platform = st.selectbox(
        "Select Platform", 
        df['Platform'].unique(),
        key=f"{key_prefix}_platform_select"  # Dynamically created unique key
    )
    filtered_df = df[df['Platform'] == selected_platform]

    # Plot ROI trend
    st.markdown("### ROI Trend by Influencer")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_df, x="Week", y="ROI", hue="Influencer", marker="o", ax=ax)
    ax.set_title(f"Weekly ROI on {selected_platform}")
    st.pyplot(fig)

    # Download option
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name=f"roi_{selected_platform.lower()}.csv",
        mime="text/csv",
        key=f"{key_prefix}_download_button"  # Also give other widgets unique keys if in a loop
    )