import streamlit as st
# Ensure you are importing the modified function correctly
from components.interactive import display_influencer_dashboard as display_interactive_chart 

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Marketing Data Analyst Intern
    **NovaGlow Cosmetics** | *March 2025 - Present*
    
   - Built automated dashboards to track influencer ROI, leading to 20% budget reallocation toward high-converting creators.  
    - Conducted customer cohort analysis to inform CRM segmentation, increasing email CTR by 35%.  
    - Collaborated with product and content teams to A/B test landing pages and creative assets for seasonal campaigns.  
    - Developed a Python script to analyze hashtag trends on Instagram and Xiaohongshu for product positioning insights.
    """)
    
    st.markdown("""
    ### Marketing Associate
    **Trendora E-commerce** | *January 2021 - May 2023*
    - Managed daily operations for TikTok campaigns and affiliate programs across SEA markets.  
    - Created performance reports integrating Google Analytics, Shopify data, and influencer metrics.  
    - Assisted with SEO audits and supported monthly content calendar planning.  
    - Initiated competitor social media benchmarking project—presented findings to senior stakeholders.
    """)
    
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Influencer Performance Dashboard",
            "description": "Built an interactive dashboard to evaluate ROI of influencer campaigns across Instagram and TikTok.",
            "skills": ["Python", "scikit-learn", "Pandas", "Google Sheets API", "Tableau"],
            "outcome": "Enabled data-driven KOL selection, improving campaign conversion rates by 18%.."
        },
        {
            "title": "Social Media Sentiment Analysis for Product Launch",
            "description": "Scraped and analyzed user-generated content from Xiaohongshu to assess public sentiment during a skincare launch..",
            "skills": ["Python", "BeautifulSoup", "TTextBlob", "Seaborn"],
            "outcome": "Identified top concerns and adjusted messaging, resulting in 1.6x higher engagement."
        },
        {
            "title": "Email Campaign Optimization with A/B Testing",
            "description": "Analyzed open rates, CTR, and conversion across email variations using A/B testing.",
            "skills": ["Excel", "SQL", "Google Analytics", "Tableau"],
            "outcome": "Boosted overall email conversion rate by 22% through subject line and CTA optimization.s."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
            # Only display the interactive chart for the 'Influencer Performance Dashboard' project
            if project['title'] == "Influencer Performance Dashboard":
                st.markdown("### Interactive Dashboard") # Add a subheader for the dashboard
                st.markdown("**Description:** Track ROI across platforms and weeks using interactive charts.")
                # Pass a unique key_prefix for the dashboard function
                display_interactive_chart(key_prefix=f"influencer_dashboard_interactive")
    
    st.markdown("---")

    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)