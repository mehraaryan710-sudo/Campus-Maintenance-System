import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import sqlite3
import database

st.set_page_config(page_title="Campus Maintenance System", page_icon="🏫", layout="wide")
database.create_tables()

def get_connection():
    return sqlite3.connect("data/campus.db")

def load_complaints():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM complaints", conn)
    conn.close()
    return df

def load_maintenance():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM maintenance", conn)
    conn.close()
    return df

# ---------- 40 SAMPLE COMPLAINTS ----------
def load_sample_data():
    if len(load_complaints()) >= 40:
        return False, "Sample data is already loaded."

    students = [
        ("Rahul Sharma","BCA"),("Priya Verma","BCA"),
        ("Aman Gupta","BTech CSE"),("Neha Singh","BTech IT"),
        ("Rohit Patel","BTech CSE"),("Anjali Mehta","BCA"),
        ("Vikas Yadav","BTech IT"),("Simran Khan","BTech CSE"),
        ("Karan Joshi","BCA"),("Pooja Mishra","BTech IT")
    ]

    records = [
        ("Block A","204","Electrical","Fan not working","Medium"),
        ("Block A","105","Electrical","Tube light not working","High"),
        ("Block A","310","Furniture","Broken classroom chair","Low"),
        ("Block A","112","Plumbing","Water leakage near washbasin","High"),
        ("Block A","215","IT","Projector not working","High"),
        ("Block A","301","Internet","Wi-Fi connection is unstable","Medium"),
        ("Block A","101","Cleaning","Classroom needs cleaning","Low"),
        ("Block A","405","AC/Cooling","AC not cooling properly","High"),
        ("Block A","208","Furniture","Desk drawer is damaged","Medium"),
        ("Block A","115","Electrical","Switchboard is damaged","High"),
        ("Block B","201","Electrical","Ceiling fan making noise","Medium"),
        ("Block B","109","Furniture","Broken student desk","Medium"),
        ("Block B","305","Plumbing","Tap is leaking","Medium"),
        ("Block B","120","IT","Computer monitor not working","High"),
        ("Block B","402","Internet","Wi-Fi unavailable","High"),
        ("Block B","103","Cleaning","Washroom requires cleaning","Medium"),
        ("Block B","210","AC/Cooling","Cooler not working","High"),
        ("Block B","307","Other","Classroom door handle damaged","Low"),
        ("Block B","116","Electrical","Power socket not working","High"),
        ("Block B","203","Furniture","Chair backrest broken","Low"),
        ("Block C","104","Plumbing","Water pipe leakage","High"),
        ("Block C","220","Electrical","Light flickering","Medium"),
        ("Block C","315","IT","Projector display issue","High"),
        ("Block C","108","Internet","Network speed is very slow","Medium"),
        ("Block C","401","Cleaning","Classroom floor needs cleaning","Low"),
        ("Block C","205","AC/Cooling","AC remote not working","Medium"),
        ("Block C","118","Furniture","Broken table","Medium"),
        ("Block C","309","Other","Window latch is damaged","Low"),
        ("Block C","207","Electrical","Fan regulator not working","Medium"),
        ("Block C","102","Plumbing","Tap handle broken","Medium"),
        ("Block D","111","Electrical","Tube light fused","Medium"),
        ("Block D","212","Furniture","Broken chair","Low"),
        ("Block D","304","Plumbing","Drainage blockage","High"),
        ("Block D","406","IT","Desktop computer not starting","High"),
        ("Block D","113","Internet","Wi-Fi signal weak","Medium"),
        ("Block D","206","Cleaning","Classroom cleaning required","Low"),
        ("Block D","302","AC/Cooling","AC water leakage","High"),
        ("Block D","105","Other","Door lock needs repair","Medium"),
        ("Block D","217","Electrical","Switch not working","Medium"),
        ("Block D","410","Furniture","Desk surface damaged","Low")
    ]

    dates = [
        "2026-05-05","2026-05-08","2026-05-12","2026-05-19","2026-05-25",
        "2026-06-02","2026-06-07","2026-06-14","2026-06-21","2026-06-28",
        "2026-07-03","2026-07-09","2026-07-15","2026-07-20","2026-07-27",
        "2026-08-01","2026-08-05","2026-08-10","2026-08-15","2026-08-19",
        "2026-08-21","2026-08-23","2026-08-25","2026-08-27","2026-08-29",
        "2026-09-01","2026-09-02","2026-09-03","2026-09-04","2026-09-05",
        "2026-09-06","2026-09-07","2026-09-08","2026-09-09","2026-09-10",
        "2026-09-10","2026-09-11","2026-09-11","2026-09-12","2026-09-12"
    ]

    statuses = [
        "Resolved","In Progress","Pending","Resolved","Pending",
        "Resolved","Pending","In Progress","Resolved","Pending",
        "In Progress","Resolved","Pending","Resolved","In Progress",
        "Pending","Resolved","Pending","In Progress","Resolved",
        "Pending","Resolved","In Progress","Pending","Resolved",
        "In Progress","Pending","Resolved","Pending","In Progress",
        "Resolved","Pending","In Progress","Resolved","Pending",
        "Resolved","In Progress","Pending","Resolved","In Progress"
    ]

    try:
        ids = []
        for i, (building, room, category, problem, priority) in enumerate(records):
            student, dept = students[i % len(students)]
            cid = database.add_complaint(
                student, dept, building, room, category,
                problem, priority, dates[i]
            )
            ids.append(cid)
            database.update_complaint_status(cid, statuses[i])

        repairs = [
            (0,"Amit",450,"Fan capacitor replaced"),
            (3,"Rakesh",300,"Leakage repaired"),
            (4,"Suresh",1500,"Projector cable replaced"),
            (5,"Amit",800,"Network router checked"),
            (8,"Rakesh",600,"Desk drawer repaired"),
            (11,"Suresh",700,"Tap repaired"),
            (13,"Amit",2200,"Computer monitor replaced"),
            (16,"Rakesh",900,"Cooler repaired"),
            (19,"Suresh",500,"Chair repaired"),
            (21,"Amit",350,"Light fitting repaired"),
            (24,"Rakesh",400,"Floor cleaning and maintenance"),
            (27,"Suresh",650,"Window latch replaced"),
            (30,"Amit",250,"Tube light replaced"),
            (33,"Rakesh",1800,"Desktop power supply repaired"),
            (35,"Suresh",900,"AC leakage repaired"),
            (38,"Amit",300,"Door lock repaired")
        ]

        for i, staff, cost, remarks in repairs:
            database.add_maintenance(ids[i], staff, dates[i], cost, remarks)

        return True, "40 sample complaints loaded successfully!"
    except Exception as e:
        return False, f"Error loading sample data: {e}"

# ---------- HEADER ----------
st.title("🏫 Campus Maintenance Complaint & Tracking System")
st.caption("Register, track, manage and analyze campus maintenance complaints.")
st.divider()

# ---------- SIDEBAR ----------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Select Module", [
    "🏠 Dashboard","📝 Register Complaint","📋 View Complaints",
    "🔍 Search Complaint","🔄 Update Status","🔧 Add Maintenance",
    "📊 Reports & Analysis"
])

st.sidebar.divider()
st.sidebar.subheader("🧪 Demo Data")
if st.sidebar.button("Load 40 Sample Complaints", use_container_width=True):
    ok, msg = load_sample_data()
    if ok:
        st.sidebar.success(msg)
        st.rerun()
    else:
        st.sidebar.info(msg)

# ---------- DASHBOARD ----------
if page == "🏠 Dashboard":
    st.header("📊 Dashboard")
    complaints = load_complaints()
    total = len(complaints)
    pending = len(complaints[complaints["status"]=="Pending"])
    progress = len(complaints[complaints["status"]=="In Progress"])
    resolved = len(complaints[complaints["status"]=="Resolved"])

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Complaints",total)
    c2.metric("Pending",pending)
    c3.metric("In Progress",progress)
    c4.metric("Resolved",resolved)

    st.subheader("📋 Recent Complaints")
    if total:
        cols=[c for c in ["complaint_id","student_name","category","building","priority","status","date"] if c in complaints.columns]
        st.dataframe(complaints[cols].tail(10),use_container_width=True,hide_index=True)
    else:
        st.info("No complaints yet. Click 'Load 40 Sample Complaints' in the sidebar.")

# ---------- REGISTER ----------
elif page == "📝 Register Complaint":
    st.header("📝 Register New Complaint")
    with st.form("complaint_form"):
        c1,c2=st.columns(2)
        with c1:
            student=st.text_input("Student Name *")
            dept=st.text_input("Department *")
            building=st.text_input("Building *")
            room=st.text_input("Room Number *")
            category=st.selectbox("Category",["Electrical","Furniture","Plumbing","IT","Internet","Cleaning","AC/Cooling","Other"])
        with c2:
            priority=st.selectbox("Priority",["Low","Medium","High"])
            complaint_date=st.date_input("Complaint Date",date.today())
            problem=st.text_area("Problem Description *")
        submit=st.form_submit_button("💾 Submit Complaint",use_container_width=True)

    if submit:
        if not all([student.strip(),dept.strip(),building.strip(),room.strip(),problem.strip()]):
            st.error("Please fill all required fields.")
        else:
            try:
                cid=database.add_complaint(student,dept,building,room,category,problem,priority,str(complaint_date))
                st.success(f"Complaint registered successfully! Complaint ID: {cid}")
            except Exception as e:
                st.error(f"Database error: {e}")

# ---------- VIEW ----------
elif page == "📋 View Complaints":
    st.header("📋 All Complaints")
    try:
        df=load_complaints()
        if len(df): st.dataframe(df,use_container_width=True,hide_index=True)
        else: st.info("No complaints found.")
    except Exception as e: st.error(f"Unable to load complaints: {e}")

# ---------- SEARCH ----------
elif page == "🔍 Search Complaint":
    st.header("🔍 Search Complaint")
    cid=st.text_input("Enter Complaint ID",placeholder="Example: CMP001")
    if st.button("🔎 Search",use_container_width=True):
        if not cid.strip(): st.warning("Please enter a complaint ID.")
        else:
            try:
                result=database.search_complaint(cid.strip())
                if result:
                    st.success("Complaint Found!")
                    st.write(result)
                else: st.error("Complaint Not Found")
            except Exception as e: st.error(f"Search error: {e}")

# ---------- UPDATE ----------
elif page == "🔄 Update Status":
    st.header("🔄 Update Complaint Status")
    cid=st.text_input("Complaint ID",placeholder="Example: CMP001")
    if cid:
        try:
            current=database.get_complaint_status(cid.strip())
            if current:
                st.info(f"Current Status: {current}")
                new=st.selectbox("Select New Status",["Pending","In Progress","Resolved"])
                if st.button("🔄 Update Status",use_container_width=True):
                    database.update_complaint_status(cid.strip(),new)
                    st.success(f"Status updated to {new}")
                    st.rerun()
            else: st.warning("Complaint ID not found.")
        except Exception as e: st.error(f"Error: {e}")

# ---------- MAINTENANCE ----------
elif page == "🔧 Add Maintenance":
    st.header("🔧 Add Maintenance Details")
    with st.form("maintenance_form"):
        cid=st.text_input("Complaint ID *")
        staff=st.text_input("Staff Name *")
        repair_date=st.date_input("Repair Date",date.today())
        cost=st.number_input("Maintenance Cost",min_value=0.0,step=100.0)
        remarks=st.text_area("Remarks")
        submit=st.form_submit_button("💾 Save Maintenance Details",use_container_width=True)
    if submit:
        if not cid.strip() or not staff.strip():
            st.error("Complaint ID and Staff Name are required.")
        else:
            try:
                if database.complaint_exists(cid.strip()):
                    database.add_maintenance(cid.strip(),staff,str(repair_date),cost,remarks)
                    st.success("Maintenance details saved successfully!")
                else: st.error("Complaint ID does not exist.")
            except Exception as e: st.error(f"Error: {e}")

# ---------- ANALYSIS ----------
elif page == "📊 Reports & Analysis":
    st.header("📊 Reports & Analysis")
    try:
        complaints=load_complaints()
        maintenance=load_maintenance()
        if len(complaints)==0:
            st.info("No complaint data available. Load sample data first.")
        else:
            total=len(complaints)
            pending=len(complaints[complaints["status"]=="Pending"])
            progress=len(complaints[complaints["status"]=="In Progress"])
            resolved=len(complaints[complaints["status"]=="Resolved"])
            common=complaints["category"].value_counts().idxmax()
            building=complaints["building"].value_counts().idxmax()
            total_cost=maintenance["cost"].sum() if len(maintenance) else 0
            avg_cost=maintenance["cost"].mean() if len(maintenance) else 0

            c1,c2,c3,c4=st.columns(4)
            c1.metric("Total Complaints",total)
            c2.metric("Pending",pending)
            c3.metric("Resolved",resolved)
            c4.metric("Total Maintenance Cost",f"₹{total_cost:,.2f}")
            st.info(f"📌 Most Common Category: {common}   |   🏢 Highest Complaint Building: {building}   |   💰 Average Cost: ₹{avg_cost:,.2f}")

            fig,ax=plt.subplots()
            complaints["category"].value_counts().plot(kind="bar",ax=ax)
            ax.set_title("Complaints by Category"); ax.set_xlabel("Category"); ax.set_ylabel("Complaints")
            plt.xticks(rotation=45); st.pyplot(fig); plt.close(fig)

            fig,ax=plt.subplots()
            complaints["status"].value_counts().plot(kind="pie",autopct="%1.1f%%",ax=ax)
            ax.set_ylabel(""); ax.set_title("Complaint Status Distribution")
            st.pyplot(fig); plt.close(fig)

            fig,ax=plt.subplots()
            complaints["building"].value_counts().plot(kind="bar",ax=ax)
            ax.set_title("Complaints by Building"); ax.set_xlabel("Building"); ax.set_ylabel("Complaints")
            st.pyplot(fig); plt.close(fig)

            tmp=complaints.copy()
            tmp["date"]=pd.to_datetime(tmp["date"])
            monthly=tmp.groupby(tmp["date"].dt.to_period("M")).size()
            monthly.index=monthly.index.astype(str)
            fig,ax=plt.subplots()
            monthly.plot(kind="line",marker="o",ax=ax)
            ax.set_title("Monthly Complaint Trend"); ax.set_xlabel("Month"); ax.set_ylabel("Complaints")
            st.pyplot(fig); plt.close(fig)

            if len(maintenance) and "complaint_id" in maintenance.columns:
                merged=maintenance.merge(complaints[["complaint_id","category"]],on="complaint_id",how="left")
                costs=merged.groupby("category")["cost"].sum()
                fig,ax=plt.subplots()
                costs.plot(kind="bar",ax=ax)
                ax.set_title("Maintenance Cost by Category"); ax.set_xlabel("Category"); ax.set_ylabel("Cost (₹)")
                plt.xticks(rotation=45); st.pyplot(fig); plt.close(fig)
            else:
                st.info("No maintenance cost data available.")

    except Exception as e:
        st.error(f"Analysis error: {e}")

st.divider()
st.caption("Campus Maintenance Complaint & Tracking System | Python • Streamlit • SQLite • Pandas • Matplotlib")
