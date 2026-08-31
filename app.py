import streamlit as st
import re
import datetime
import random
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Page Config & Layout
st.set_page_config(
    page_title="Cyber Range: Digital Footprint & Safety Framework",
    page_icon="🛡️",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-color: #00FF7F; }
    .main { padding: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

# Title Banner
st.title("🛡️ Capstone Framework: Digital Footprint & Threat Mitigation")
st.caption("Interactive Cyber Range & Operational Threat Mitigation Portal")
st.markdown("---")

# Navigation Tabs (7 Comprehensive Modules)
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "👣 1. Footprint & Permanence",
    "⚠️ 2. Threat Vector Simulator",
    "💼 3. Real-World Impact",
    "📸 4. Live EXIF Metadata Inspector",
    "📋 5. Hardening Checklist",
    "📊 6. Audit & Scenario Quiz",
    "🚨 7. Incident Reporting & Helplines"
])

# MODULE 1: Active vs Passive
with tab1:
    st.header("1. Digital Footprint Dynamics & Data Permanence")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📤 Active Footprint")
        st.info("**Data deliberately shared by you.**")
        st.markdown("""
        * **Social Media:** Posts, comments, uploaded photos, and stories.
        * **Registration Data:** Forum sign-ups, web forms, and newsletter subscriptions.
        * **Public Activity:** Product reviews, tagged locations, and public playlists.
        """)
    with col2:
        st.subheader("🕵️ Passive Footprint")
        st.warning("**Data collected silently without active input.**")
        st.markdown("""
        * **Network Telemetry:** IP address, ISP, and geographic routing.
        * **Device Fingerprinting:** Screen resolution, browser engine, and OS metrics.
        * **Behavioral Analytics:** Search history, clickstream data, and session time.
        """)
    st.divider()
    st.subheader("♾️ Data Permanence Engine: *Why 'Delete' Doesn't Work*")
    term = st.select_slider(
        "Simulate time passed since a sensitive post was published:",
        options=["1 Second", "5 Minutes", "1 Hour", "1 Day", "1 Year"]
    )
    if term in ["1 Second"]:
        st.success("🟢 **Local System:** Post live. Search engine crawlers have been notified.")
    elif term in ["5 Minutes"]:
        st.warning("🟡 **Cached:** Web crawlers (e.g., Googlebot) indexed the URL. Automated scraping bots took snapshots.")
    else:
        st.error("🔴 **Permanent Archive:** The post is indexed in public web archives (Wayback Machine), cached across global edge servers, and saved via third-party screenshots.")

# MODULE 2: Threat Vector Simulator
with tab2:
    st.header("2. Social Media Threat Landscape Simulator")
    st.subheader("🎯 Threat Vector Simulator")
    has_bday = st.checkbox("Public Birthday & Birth Year")
    has_location = st.checkbox("Real-time Check-ins / Travel Posts")
    has_pets = st.checkbox("Pet Names & Family Tagging")
    has_job = st.checkbox("Workplace / School Role Details")
    st.markdown("### 🚨 Generated Attack Vectors:")
    if not (has_bday or has_location or has_pets or has_job):
        st.success("Minimal public exposure detected. Attackers have little OSINT (Open Source Intelligence) to work with.")
    else:
        if has_bday or has_pets:
            st.error("⚠️ **Credential Recovery Risk:** Attackers can guess security questions or brute-force common password combinations.")
        if has_location:
            st.error("⚠️ **Physical Safety & Cyberstalking Risk:** Geolocation tags enable physical tracking and burgling during travel.")
        if has_job:
            st.error("⚠️ **Spear-Phishing & BEC Risk:** Impersonators can send tailored phishing emails appearing to come from colleagues or management.")

# MODULE 3: Real-World Impact
with tab3:
    st.header("3. Real-World & Long-Term Impact")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🎓 Admissions & Career Background Checks")
        st.metric(label="Recruiters Screening Social Media", value="70%+", delta="Increasing Annually")
        st.write("""
        Academic institutions and employers routinely conduct OSINT audits on candidates. Flagged items include:
        * Offensive comments or hate speech.
        * Confidentiality breaches or unprofessional conduct.
        * Inconsistencies between resumes and social media histories.
        """)
    with c2:
        st.subheader("💥 Context Collapse & Reputational Damage")
        st.metric(label="Primary Cause of Reputation Leaks", value="Context Collapse", delta="High Severity")
        st.write("""
        **Context Collapse** happens when content intended for a specific private group is viewed by a broader, unintended audience.
        * Historical posts stripped of context are judged by modern standards.
        * Private jokes or old opinions can lead to public backlash, expulsion, or job termination.
        """)

# MODULE 4: REAL EXIF METADATA INSPECTOR (UPDATED)
with tab4:
    st.header("4. Real-Time Image EXIF Metadata Inspector")
    st.write("Upload an image taken directly from a smartphone or camera to inspect hidden background metadata.")
    
    uploaded_file = st.file_uploader("Upload an Image (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image Preview", use_container_width=True)
        
        exif_data = image._getexif()
        
        st.subheader("📸 Extracted EXIF Metadata Summary:")
        if exif_data:
            metadata_dict = {}
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                # Filter out raw byte streams for clean viewing
                if isinstance(value, (int, str)):
                    metadata_dict[tag_name] = value
                    
            if metadata_dict:
                st.json(metadata_dict)
                st.warning("⚠️ **Security Risk Detected:** Metadata contains sensitive camera/device details.")
            else:
                st.info("No text-based metadata fields found.")
        else:
            st.success("✅ **Clean Image:** No EXIF metadata found. (Social media sites like WhatsApp/Instagram often auto-strip metadata during upload).")

# MODULE 5: Hardening Checklist
with tab5:
    st.header("5. Step-by-Step Account Hardening Checklist")
    st.write("Complete these recommended platform security configurations:")
    
    st.checkbox("1. Enforce App-based Multi-Factor Authentication (MFA) on Primary Email")
    st.checkbox("2. Disable Location Services / EXIF Tagging in Phone Camera Settings")
    st.checkbox("3. Set Instagram / Facebook Profiles to 'Private' Mode")
    st.checkbox("4. Review & Revoke Unused 3rd Party OAuth App Permissions")
    st.checkbox("5. Configure WhatsApp 'Two-Step Verification' PIN")
    st.checkbox("6. Remove Public Personal Phone Number & Email from Bio Lines")

# MODULE 6: Audit & Quiz
with tab6:
    st.header("6. Interactive Assessment & Custom Audit Report")
    
    st.subheader("📝 Phishing & Social Engineering Quiz")
    q1 = st.radio(
        "1. You receive a DM from a close friend asking for a 2FA code sent to your phone to 'help them unlock their account'. What do you do?",
        ("Select an answer...", "Send the code immediately", "Refuse and call your friend directly", "Forward the code to support")
    )
    if q1 == "Refuse and call your friend directly":
        st.success("✅ **Correct!** The code belongs to your account. Your friend's account was compromised.")
        
    st.divider()
    st.subheader("📊 Footprint Vulnerability Audit")
    s1 = st.slider("Percentage of social profiles set to Public:", 0, 100, 40)
    s2 = st.checkbox("I reuse passwords across multiple services.")
    s3 = st.checkbox("MFA is disabled on primary accounts.")
    
    calc_score = int(s1 * 0.5) + (30 if s2 else 0) + (20 if s3 else 0)
    final_score = min(calc_score, 100)
    
    st.progress(final_score)
    st.write(f"**Calculated Exposure Index:** {final_score} / 100")
    
    report_text = f"DIGITAL FOOTPRINT ASSESSMENT REPORT\nGenerated: {datetime.datetime.now().strftime('%Y-%m-%d')}\nRisk Index: {final_score}/100"
    st.download_button("📥 Download Official Audit Summary (.txt)", data=report_text, file_name="footprint_audit_report.txt")

# MODULE 7: Incident Reporting & Helplines
with tab7:
    st.header("7. Incident Reporting Portal & Emergency Helplines")
    
    st.subheader("📞 Emergency Cyber Crime Helplines")
    col_h1, col_h2, col_h3 = st.columns(3)
    
    with col_h1:
        st.error("🚨 **National Cyber Crime**")
        st.markdown("**Helpline:** `1930`\n\n**Portal:** `cybercrime.gov.in`")
    with col_h2:
        st.warning("🛡️ **Women & Child Safety**")
        st.markdown("**Helpline:** `181` / `1091`\n\n**Coverage:** Cyberstalking & Abuse")
    with col_h3:
        st.info("🌐 **CERT-In Coordination**")
        st.markdown("**Contact:** `info@cert-in.org.in`\n\n**Coverage:** Data Breaches")
        
    st.divider()
    st.subheader("📝 Submit Incident Report")
    
    with st.form("incident_form"):
        incident_type = st.selectbox("Classification:", ["Financial Fraud", "Profile Impersonation", "Cyberbullying", "Account Takeover"])
        platform = st.selectbox("Platform:", ["WhatsApp", "Instagram", "Banking Portal", "Email"])
        details = st.text_area("Incident Description:")
        submit = st.form_submit_button("Submit Incident Report")
        
    if submit:
        ticket_id = f"CYBER-{random.randint(100000, 999999)}"
        st.success(f"✅ **Report Logged!** Escalation Ticket: `{ticket_id}`")
        st.info(f"If financial fraud occurred, immediately call **1930** to freeze transferred funds.")
