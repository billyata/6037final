import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **Chinese University of Hong Kong** | *September 2024 - June 2025*
    
    - GPA: 3.9/4.0
    - Relevant Coursework: Marketing Analytics, Advanced Machine Learning, Deep Learning, Natural Language Processing, Data Visualization, Statistical Methods for Data Science, Big Data Analytics
    
    ### Bachelor of Commerce, Marketing
    **Hong Kong Polytechnic University** | *September 2019 - June 2023*

    - GPA: 3.8/4.0
    - Graduated with Distinction
    - Relevant Coursework: Financial Accounting, Marketing Management, Business Communication, International Business
""")
   
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### Google Data Analytics Certificate
        **Coursera** | *March 2022*
        
       Developed hands-on skills in data cleaning, visualization, and analysis using tools such as Excel, SQL, and R.
        """)
        
    with cert2:
        st.markdown("""
        ### Meta Certified Digital Marketing Associate
        **Meta (Facebook)** | *August 2021*
        
        Certified understanding of foundational digital marketing concepts including ad creation, performance tracking, and audience targeting on Meta platforms.
        """)
        
    with cert3:
        st.markdown("""
        ### Tableau Desktop Specialist
        **Tableau** | *June 2021*
        
        Demonstrated ability to connect data sources, create interactive dashboards, and apply basic analytics in Tableau.
        """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    st.markdown("""
    ### Cross-Platform Influencer ROI Tracker
    - Designed a cross-platform Excel model to evaluate content creators based on CPM, CTR, engagement rate, and conversion.  
    - Used results to adjust the influencer roster for upcoming campaign cycles.
    
    ### Hashtag Sentiment Monitor for Product Launches
    - Developed a Python-based tracker for brand-related keywords on Xiaohongshu, filtering for sentiment and virality.  
    - Helped the brand reposition key messaging before a major launch.
    """)
    
    st.markdown("---") 