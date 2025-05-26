import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Clara LU</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:claralu@gmail.com">claralu@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "clara.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent master’s graduate in Marketing from Chinese University of Hong Kong, with a strong interest in combining data and creativity to drive impactful marketing decisions. Throughout my studies, I developed practical skills in digital campaign performance analysis, customer segmentation, and marketing dashboard design.

        During my academic and project experience, I worked on multiple real-world datasets—from influencer ROI tracking to consumer behavior clustering—using tools such as Python, SQL, and Tableau. These experiences deepened my ability to translate data into actionable strategies.

        Passionate about digital marketing, consumer insights, and storytelling with data, I am eager to contribute to a data-driven team where I can learn, collaborate, and grow into a marketing analytics professional.
        """
    )

    st.markdown(
        """
        ### Skills
        - **Programming & Tools:** Python, SQL, Excel (PivotTables, VLOOKUP), Google Sheets  
        - **Data Analysis:** pandas, seaborn, matplotlib, A/B Testing, Cohort Analysis  
        - **Marketing Analytics:** Google Analytics, Meta Business Suite, Klaviyo, Shopify  
        - **Data Visualization:** Tableau, Looker Studio, PowerPoint  
        - **CRM & Campaigns:** Email Automation, UTM Tracking, Segmentation Strategy  
        - **Statistical Techniques:** Hypothesis Testing, Regression, Customer Clustering  
        - **Communication:** Data Storytelling, Marketing Reports, Cross-functional Collaboration  
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 