import streamlit as st
import re
from datetime import datetime
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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab 8 = st.tabs([
    "👣 1. Footprint & Permanence",
    "⚠️ 2. Threat Vector Simulator",
    "💼 3. Real-World Impact",
    "📸 4. Live EXIF Metadata Inspector",
    "📋 5. Hardening Checklist",
    "📊 6. Audit & Scenario Quiz",
    "🚨 7. Action Plan & Evidence Generator"
    "🚨 8. Fake Media Takedown"
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
    
    report_text = f"DIGITAL FOOTPRINT ASSESSMENT REPORT\nGenerated: {datetime.now().strftime('%Y-%m-%d')}\nRisk Index: {final_score}/100"
    st.download_button("📥 Download Official Audit Summary (.txt)", data=report_text, file_name="footprint_audit_report.txt")
# MODULE 7: Cyber Incident Action Plan & Evidence Report Generator
with tab7:
    st.header("7. Cyber Incident Action Plan & Evidence Docket Generator")
    st.markdown("""
    Generate an **Official Cyber Crime Triage Report & Evidence Summary** tailored to your incident. 
    This generator produces a standardized docket that can be downloaded and submitted directly to local law enforcement or financial institutions.
    """)
    
    st.divider()
    
    col_input, col_output = st.columns([1, 1])
    
    with col_input:
        st.subheader("📋 Incident Details Intake")
        
        victim_name = st.text_input("Reporter / Victim Name (Optional):", placeholder="e.g. John Doe")
        incident_type = st.selectbox(
            "Classification of Crime:",
            [
                "Financial Cyber Fraud (UPI/Credit Card/NetBanking)",
                "Social Media Account Takeover / Hacking",
                "Cyberbullying, Harassment & Stalking",
                "Profile Impersonation & Identity Theft",
                "Phishing / Malicious Link Exposure"
            ]
        )
        platform_affected = st.selectbox(
            "Platform / Medium:",
            ["WhatsApp", "Instagram", "Facebook", "UPI / Payment App", "Email / Gmail", "SMS / Phone Call", "Other Web Portal"]
        )
        financial_loss = st.radio("Was there any financial loss involved?", ["No", "Yes"])
        loss_amount = 0
        if financial_loss == "Yes":
            loss_amount = st.number_input("Approximate Loss Amount (₹):", min_value=1, value=5000, step=500)
            
        incident_description = st.text_area(
            "Detailed Incident Narrative:",
            placeholder="Describe what happened, including dates, usernames, phone numbers, or transaction IDs involved...",
            height=120
        )
        
        generate_btn = st.button("🚀 Generate Triage Report & Evidence Docket", type="primary")

    with col_output:
        st.subheader("📄 Action Plan & Generated Deliverables")
        
        if generate_btn:
            if not incident_description.strip():
                st.warning("⚠️ Please provide a brief incident narrative before generating the report.")
            else:
                # Generate unique ticket reference
                ticket_id = f"EVIDENCE-DOCKET-{random.randint(100000, 999999)}"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                st.success(f"✅ **Docket Successfully Generated!**")
                st.code(f"Docket Reference ID: {ticket_id}", language="text")
                
                # Immediate Triage Advice based on selection
                st.markdown("### 🚨 Immediate Response Actions:")
                if "Financial" in incident_type or financial_loss == "Yes":
                    st.error("""
                    **1. Call National Cyber Crime Helpline Immediately:** Dial **`1930`** (India) to initiate a bank freeze window under CFCFRMS.  
                    **2. Notify Your Bank:** Lock your debit/credit card or UPI handle immediately via banking app.
                    """)
                elif "Takeover" in incident_type or "Impersonation" in incident_type:
                    st.warning("""
                    **1. Secure Secondary Accounts:** Change passwords for recovery emails immediately.  
                    **2. Report Account:** Submit impersonation/hacking report via official platform links (Meta/Google).
                    """)
                else:
                    st.info("""
                    **1. Preserve Evidence:** Do not delete screenshots, chat logs, or sender headers.  
                    **2. Block Aggressor:** Mute and block suspect profiles on affected platforms.
                    """)
                
                # Format Tangible File Content
                docket_text = f"""================================================================================
          OFFICIAL CYBER INCIDENT TRIAGE & EVIDENCE SUMMARY DOCKET
================================================================================
Docket Reference ID : {ticket_id}
Generated Timestamp : {timestamp}
Victim Name         : {victim_name if victim_name else 'Anonymous Reporter'}
--------------------------------------------------------------------------------
INCIDENT CLASSIFICATION
--------------------------------------------------------------------------------
Crime Category      : {incident_type}
Affected Platform   : {platform_affected}
Financial Loss      : {'₹ ' + str(loss_amount) if financial_loss == 'Yes' else 'None Reported'}

--------------------------------------------------------------------------------
INCIDENT NARRATIVE & STATEMENTS
--------------------------------------------------------------------------------
{incident_description}

--------------------------------------------------------------------------------
RECOMMENDED LEGAL & INVESTIGATIVE NEXT STEPS
--------------------------------------------------------------------------------
1. Emergency Hotline: If financial loss occurred, call 1930 immediately with this 
   docket and transaction IDs.
2. Formal Filing: Upload this docket file along with transaction/chat screenshots 
   to the National Cyber Crime Reporting Portal (cybercrime.gov.in) or submit to 
   your nearest Cyber Crime Police Station.
3. Evidence Handling: Retain original digital records (chat exports, email headers, 
   bank statements) without altering files or metadata.
================================================================================
"""

                st.markdown("### 📥 Download Output Package")
                st.download_button(
                    label="💾 Download Official Incident Docket (.txt)",
                    data=docket_text,
                    file_name=f"{ticket_id}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.info("👈 Fill out the incident details on the left and click **Generate** to produce your downloadable evidence docket.")
# --- MODULE 8: FAKE MEDIA & DEEPFAKE TAKEDOWN ASSISTANT ---
with tab8:
    st.header("8. Fake Media & Deepfake Takedown Assistant")
    st.caption("🔒 Direct platform routing, automated legal takedown notices, and law enforcement escalation paths.")

    col1, col2 = st.columns(2)

    with col1:
        content_type = st.selectbox("Type of Infringing Content", [
            "Deepfake / AI-Generated Image or Video",
            "Morphed / Doctored Photo",
            "Non-Consensual Intimate Image (NCII)",
            "Impersonation Profile / Fake Account"
        ])
        platform = st.selectbox("Platform Hosting Content", [
            "Instagram / Facebook (Meta)",
            "X (Twitter)",
            "YouTube / Google",
            "Telegram",
            "Reddit",
            "Other Website / Unknown"
        ])

    with col2:
        target_url = st.text_input("URL of Infringing Post / Account", placeholder="https://...")
        uploader_handle = st.text_input("Uploader Handle / Profile Name", placeholder="@username")

    st.markdown("---")

    # Section A: Direct Platform Actions
    st.subheader("1. Direct Platform Reporting Routes")

    if content_type == "Non-Consensual Intimate Image (NCII)":
        st.info("💡 **Recommended Tool:** Submit a digital fingerprint to **StopNCII.org**. It hashes the image locally on your device so participating tech platforms can block re-uploads automatically without seeing the original photo.")

    platform_links = {
        "Instagram / Facebook (Meta)": "https://help.instagram.com/535503073130320",
        "X (Twitter)": "https://help.twitter.com/forms/impersonation",
        "YouTube / Google": "https://support.google.com/youtube/contact/privacy",
        "Reddit": "https://www.reddit.com/report",
        "Telegram": "Contact abuse@telegram.org or use in-app report buttons.",
        "Other Website / Unknown": "Look for 'Contact Us', 'Abuse', or 'DMCA Takedown' in the site footer."
    }

    st.markdown(f"🔗 **Direct Portal Link:** [{platform_links.get(platform)}]({platform_links.get(platform)})")

    # Section B: Automated Notice Generator
    st.markdown("---")
    st.subheader("2. Automated Takedown Request Notice")

    if st.button("📄 Generate Legal Takedown Notice"):
        if not target_url:
            st.warning("Please provide the target content URL above.")
        else:
            import datetime as dt
            notice_text = f"""SUBJECT: URGENT TAKEDOWN REQUEST - UNAUTHORIZED / FAKE MEDIA REMOVAL

To the Trust & Safety Team at {platform},

I am writing to formally request the immediate removal of unauthorized and falsified content hosted on your platform.

INFRACTING CONTENT DETAILS:
- Target URL: {target_url}
- Uploader Handle: {uploader_handle}
- Type of Violating Content: {content_type}

LEGAL & POLICY GROUNDS:
1. Impersonation & Right to Privacy: The content uses my likeness/identity without consent.
2. Terms of Service Violation: This post violates platform safety policies regarding synthetic media, deepfakes, non-consensual imagery, and harassment.

REMEDIAL ACTION REQUIRED:
Please remove or disable access to the specified material within 24-48 hours to prevent further harm.

Submitted On: {dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
            st.success("✅ Notice Generated!")
            st.code(notice_text, language="text")
            st.download_button(
                label="📥 Download Takedown Request (.txt)",
                data=notice_text,
                file_name=f"takedown_request_{dt.datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )

    # Section C: Law Enforcement Guidance
    st.markdown("---")
    st.subheader("3. Official Law Enforcement Escalation")
    st.markdown("""
    * **National Cybercrime Helpline:** Call **1930** immediately.
    * **Online Complaint:** Submit a report at **[cybercrime.gov.in](https://cybercrime.gov.in)** under *Women & Children Safety* or *Cyber Crime Against Individuals*.
    * **Forensic Evidence:** Take full-screen screenshots showing the full URL bar, profile handle, and timestamp before the post is taken down.
    """)
