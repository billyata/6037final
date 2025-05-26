import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Clara LU")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** claralu@gmail.com
    - **Phone:** +852 1234-5678
    - **LinkedIn:** [linkedin.com/in/claraluxxx](https://linkedin.com/in/claraluxxx)
    - **GitHub:** [github.com/claraluxxx](https://github.com/claraluxxx)
    """)

    st.header("Professional Summary")
    st.markdown("""
    Marketing analyst with 3+ years of experience blending creative campaign planning with data-driven insights to drive customer acquisition and brand growth
    """)

    st.header("Work Experience")
    st.markdown("""
    **Marketing Data Analyst | NovaGlow Cosmetics**  
    *Jul 2022 – Present | Hong Kong SAR*  
    - Built automated dashboards to track influencer ROI, leading to 20% budget reallocation toward high-converting creators.  
    - Conducted customer cohort analysis to inform CRM segmentation, increasing email CTR by 35%.  
    - Collaborated with product and content teams to A/B test landing pages and creative assets for seasonal campaigns.  
    - Developed a Python script to analyze hashtag trends on Instagram and Xiaohongshu for product positioning insights.

    **Marketing Associate | Trendora E-commerce**  
    *Jan 2021 – Jun 2022 | Remote*  
    - Managed daily operations for TikTok campaigns and affiliate programs across SEA markets.  
    - Created performance reports integrating Google Analytics, Shopify data, and influencer metrics.  
    - Assisted with SEO audits and supported monthly content calendar planning.  
    - Initiated competitor social media benchmarking project—presented findings to senior stakeholders.
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**  
    - Chinese University of Hong Kong  
    - *September 2024 - June 2025*
    - GPA: 3.9/4.0
    - Relevant Coursework: Marketing Analytics, Advanced Machine Learning, Deep Learning, Natural Language Processing, Data Visualization, Statistical Methods for Data Science, Big Data Analytics

    **Bachelor of Commerce, Marketing Major**  
    - Hong Kong Polytechnic University  
    - *September 2019 - June 2023*  
    - GPA: 3.8/4.0  
    - Relevant Coursework: Financial Accounting, Marketing Management, Business Communication, International Business
    """)

    st.header("Skills")
    st.markdown("""
    - **Marketing:** Influencer Marketing, Social Media Strategy, CRM Campaigns, A/B Testing  
    - **Analytics & Tools:** Python (pandas, seaborn), SQL, Excel (PivotTables, VLOOKUP), Google Analytics, Tableau  
    - **Platforms:** TikTok Ads Manager, Meta Business Suite, Klaviyo, Notion, Canva  
    - **Soft Skills:** Problem Solving, Cross-functional Collaboration, Presentation, Time Management
    """)

    st.header("Certifications")
    st.markdown("""
    - Google Data Analytics – Coursera  
    - Meta Blueprint: Digital Marketing Associate  
    - Tableau Desktop Specialist 
    """)

    st.header("Projects")
    st.markdown("""
    **Influencer Performance Dashboard**  
    - Built an interactive dashboard to evaluate ROI of influencer campaigns across Instagram and TikTok using Python and Tableau.  
    - Enabled data-driven KOL selection by integrating campaign data with Google Sheets API, improving conversion rates by 18%.

    **Social Media Sentiment Analysis for Product Launch**  
    - Scraped and analyzed user-generated content from Xiaohongshu using BeautifulSoup and TextBlob to assess launch sentiment.  
    - Identified top concerns and adjusted messaging, resulting in 1.6x higher engagement across social channels.

    **Email Campaign Optimization with A/B Testing**  
    - Analyzed open rates, click-through rates, and conversion using SQL and Google Analytics to evaluate A/B test performance.  
    - Boosted overall email conversion rate by 22% through subject line refinement and optimized CTA positioning.
    """)

    st.header("Languages")
    st.markdown("""
   - **English:** Fluent  
    - **Mandarin:** Native  
    - **Cantonese:** Conversational
    """)

    st.header("Interests")
    st.markdown("""
    - Beauty tech & consumer AI tools  
    - Data storytelling & dashboards  
    - K-pop marketing case studies  
    - Café-hopping & city photography
    """)

    st.markdown("---") 
