import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import sqlite3
import database

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Campus Maintenance System",
    page_icon="🏫",
    layout="wide"
)

# Create database tables
database.create_tables()

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 38px;
    font-weight: 700;
    color: #1E3A8A;
}

.subtitle {
    font-size: 18px;
    color: #555;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.metric-title {
    font-size: 15px;
    color: #666;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #1E3A8A;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="title">🏫 Campus Maintenance Complaint & Tracking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Register, track, manage and analyze campus maintenance complaints.</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "📝 Register Complaint",
        "📋 View Complaints",
        "🔍 Search Complaint",
        "🔄 Update Status",
        "🔧 Add Maintenance",
        "📊 Reports & Analysis"
    ]
)

# ---------------------------------------------------------
# DATABASE HELPER
# ---------------------------------------------------------

def get_connection():
    return sqlite3.connect("data/campus.db")


def load_complaints():
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    return df


def load_maintenance():
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM maintenance",
        conn
    )

    conn.close()

    return df


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.header("📊 Dashboard")

    try:
        complaints = load_complaints()

        total = len(complaints)

        pending = len(
            complaints[complaints["status"] == "Pending"]
        )

        in_progress = len(
            complaints[complaints["status"] == "In Progress"]
        )

        resolved = len(
            complaints[complaints["status"] == "Resolved"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Complaints", total)

        with col2:
            st.metric("Pending", pending)

        with col3:
            st.metric("In Progress", in_progress)

        with col4:
            st.metric("Resolved", resolved)

        st.divider()

        st.subheader("📋 Recent Complaints")

        if len(complaints) > 0:

            display_columns = [
                col for col in [
                    "complaint_id",
                    "student_name",
                    "category",
                    "building",
                    "priority",
                    "status",
                    "date"
                ]
                if col in complaints.columns
            ]

            st.dataframe(
                complaints[display_columns].tail(10),
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No complaints have been registered yet.")

    except Exception as e:
        st.error(f"Unable to load dashboard: {e}")


# =========================================================
# REGISTER COMPLAINT
# =========================================================

elif page == "📝 Register Complaint":

    st.header("📝 Register New Complaint")

    with st.form("complaint_form"):

        col1, col2 = st.columns(2)

        with col1:

            student_name = st.text_input(
                "Student Name *"
            )

            department = st.text_input(
                "Department *"
            )

            building = st.text_input(
                "Building *"
            )

            room_no = st.text_input(
                "Room Number *"
            )

            category = st.selectbox(
                "Category",
                [
                    "Electrical",
                    "Furniture",
                    "Plumbing",
                    "IT",
                    "Internet",
                    "Cleaning",
                    "AC/Cooling",
                    "Other"
                ]
            )

        with col2:

            priority = st.selectbox(
                "Priority",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )

            complaint_date = st.date_input(
                "Complaint Date",
                value=date.today()
            )

            problem = st.text_area(
                "Problem Description *"
            )

        submitted = st.form_submit_button(
            "💾 Submit Complaint",
            use_container_width=True
        )

        if submitted:

            if not student_name.strip():
                st.error("Please enter student name.")

            elif not department.strip():
                st.error("Please enter department.")

            elif not building.strip():
                st.error("Please enter building.")

            elif not room_no.strip():
                st.error("Please enter room number.")

            elif not problem.strip():
                st.error("Please describe the problem.")

            else:

                try:

                    complaint_id = database.add_complaint(
                        student_name,
                        department,
                        building,
                        room_no,
                        category,
                        problem,
                        priority,
                        str(complaint_date)
                    )

                    st.success(
                        f"Complaint registered successfully! Complaint ID: {complaint_id}"
                    )

                except Exception as e:

                    st.error(
                        f"Error while registering complaint: {e}"
                    )


# =========================================================
# VIEW COMPLAINTS
# =========================================================

elif page == "📋 View Complaints":

    st.header("📋 All Complaints")

    try:

        complaints = load_complaints()

        if len(complaints) == 0:

            st.info("No complaints found.")

        else:

            st.dataframe(
                complaints,
                use_container_width=True,
                hide_index=True
            )

    except Exception as e:

        st.error(
            f"Unable to load complaints: {e}"
        )


# =========================================================
# SEARCH COMPLAINT
# =========================================================

elif page == "🔍 Search Complaint":

    st.header("🔍 Search Complaint")

    complaint_id = st.text_input(
        "Enter Complaint ID",
        placeholder="Example: CMP001"
    )

    if st.button(
        "🔎 Search",
        use_container_width=True
    ):

        if not complaint_id.strip():

            st.warning(
                "Please enter a complaint ID."
            )

        else:

            try:

                result = database.search_complaint(
                    complaint_id.strip()
                )

                if result:

                    st.success("Complaint Found!")

                    st.write(result)

                else:

                    st.error(
                        "Complaint Not Found"
                    )

            except Exception as e:

                st.error(
                    f"Search error: {e}"
                )


# =========================================================
# UPDATE STATUS
# =========================================================

elif page == "🔄 Update Status":

    st.header("🔄 Update Complaint Status")

    complaint_id = st.text_input(
        "Complaint ID",
        placeholder="Example: CMP001"
    )

    if complaint_id:

        try:

            current_status = database.get_complaint_status(
                complaint_id.strip()
            )

            if current_status:

                st.info(
                    f"Current Status: {current_status}"
                )

                new_status = st.selectbox(
                    "Select New Status",
                    [
                        "Pending",
                        "In Progress",
                        "Resolved"
                    ]
                )

                if st.button(
                    "🔄 Update Status",
                    use_container_width=True
                ):

                    database.update_complaint_status(
                        complaint_id.strip(),
                        new_status
                    )

                    st.success(
                        f"Status updated to {new_status}"
                    )

                    st.rerun()

            else:

                st.warning(
                    "Complaint ID not found."
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================================================
# ADD MAINTENANCE
# =========================================================

elif page == "🔧 Add Maintenance":

    st.header("🔧 Add Maintenance Details")

    with st.form("maintenance_form"):

        complaint_id = st.text_input(
            "Complaint ID *",
            placeholder="Example: CMP001"
        )

        staff_name = st.text_input(
            "Staff Name *"
        )

        repair_date = st.date_input(
            "Repair Date",
            value=date.today()
        )

        cost = st.number_input(
            "Maintenance Cost",
            min_value=0.0,
            step=100.0
        )

        remarks = st.text_area(
            "Remarks"
        )

        submitted = st.form_submit_button(
            "💾 Save Maintenance Details",
            use_container_width=True
        )

        if submitted:

            if not complaint_id.strip():

                st.error(
                    "Please enter complaint ID."
                )

            elif not staff_name.strip():

                st.error(
                    "Please enter staff name."
                )

            else:

                try:

                    if database.complaint_exists(
                        complaint_id.strip()
                    ):

                        database.add_maintenance(
                            complaint_id.strip(),
                            staff_name,
                            str(repair_date),
                            cost,
                            remarks
                        )

                        st.success(
                            "Maintenance details saved successfully!"
                        )

                    else:

                        st.error(
                            "Complaint ID does not exist."
                        )

                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )


# =========================================================
# REPORTS & ANALYSIS
# =========================================================

elif page == "📊 Reports & Analysis":

    st.header("📊 Reports & Analysis")

    try:

        complaints = load_complaints()

        maintenance = load_maintenance()

        if len(complaints) == 0:

            st.info(
                "No complaint data available for analysis."
            )

        else:

            # ---------------------------------------------
            # METRICS
            # ---------------------------------------------

            total = len(complaints)

            pending = len(
                complaints[
                    complaints["status"] == "Pending"
                ]
            )

            in_progress = len(
                complaints[
                    complaints["status"] == "In Progress"
                ]
            )

            resolved = len(
                complaints[
                    complaints["status"] == "Resolved"
                ]
            )

            most_common_category = (
                complaints["category"].value_counts().idxmax()
            )

            highest_building = (
                complaints["building"].value_counts().idxmax()
            )

            total_cost = (
                maintenance["cost"].sum()
                if len(maintenance) > 0
                else 0
            )

            average_cost = (
                maintenance["cost"].mean()
                if len(maintenance) > 0
                else 0
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Complaints",
                total
            )

            col2.metric(
                "Pending",
                pending
            )

            col3.metric(
                "Resolved",
                resolved
            )

            col4.metric(
                "Total Maintenance Cost",
                f"₹{total_cost:,.2f}"
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"📌 Most Common Category: {most_common_category}"
                )

            with col2:

                st.info(
                    f"🏢 Highest Complaint Building: {highest_building}"
                )

            st.info(
                f"💰 Average Maintenance Cost: ₹{average_cost:,.2f}"
            )

            # ---------------------------------------------
            # CATEGORY CHART
            # ---------------------------------------------

            st.subheader(
                "📊 Complaints by Category"
            )

            category_counts = (
                complaints["category"]
                .value_counts()
            )

            fig1, ax1 = plt.subplots()

            category_counts.plot(
                kind="bar",
                ax=ax1
            )

            ax1.set_xlabel("Category")
            ax1.set_ylabel("Number of Complaints")
            ax1.set_title("Complaints by Category")

            plt.xticks(rotation=45)

            st.pyplot(fig1)

            # ---------------------------------------------
            # STATUS PIE CHART
            # ---------------------------------------------

            st.subheader(
                "🥧 Complaint Status Distribution"
            )

            status_counts = (
                complaints["status"]
                .value_counts()
            )

            fig2, ax2 = plt.subplots()

            ax2.pie(
                status_counts.values,
                labels=status_counts.index,
                autopct="%1.1f%%"
            )

            ax2.set_title(
                "Complaint Status Distribution"
            )

            st.pyplot(fig2)

            # ---------------------------------------------
            # BUILDING CHART
            # ---------------------------------------------

            st.subheader(
                "🏢 Complaints by Building"
            )

            building_counts = (
                complaints["building"]
                .value_counts()
            )

            fig3, ax3 = plt.subplots()

            building_counts.plot(
                kind="bar",
                ax=ax3
            )

            ax3.set_xlabel("Building")
            ax3.set_ylabel("Complaints")
            ax3.set_title(
                "Complaints by Building"
            )

            plt.xticks(rotation=45)

            st.pyplot(fig3)

            # ---------------------------------------------
            # MONTHLY CHART
            # ---------------------------------------------

            st.subheader(
                "📅 Monthly Complaint Trend"
            )

            try:

                complaints["date"] = pd.to_datetime(
                    complaints["date"]
                )

                monthly = (
                    complaints
                    .groupby(
                        complaints["date"].dt.to_period("M")
                    )
                    .size()
                )

                monthly.index = (
                    monthly.index.astype(str)
                )

                fig4, ax4 = plt.subplots()

                monthly.plot(
                    kind="line",
                    marker="o",
                    ax=ax4
                )

                ax4.set_xlabel("Month")
                ax4.set_ylabel("Complaints")
                ax4.set_title(
                    "Monthly Complaint Trend"
                )

                st.pyplot(fig4)

            except Exception:

                st.warning(
                    "Monthly chart could not be generated."
                )

            # ---------------------------------------------
            # COST BY CATEGORY
            # ---------------------------------------------

            st.subheader(
                "💰 Maintenance Cost by Category"
            )

            if (
                len(maintenance) > 0
                and "complaint_id" in maintenance.columns
            ):

                merged = maintenance.merge(
                    complaints[
                        ["complaint_id", "category"]
                    ],
                    on="complaint_id",
                    how="left"
                )

                cost_category = (
                    merged
                    .groupby("category")["cost"]
                    .sum()
                )

                fig5, ax5 = plt.subplots()

                cost_category.plot(
                    kind="bar",
                    ax=ax5
                )

                ax5.set_xlabel("Category")
                ax5.set_ylabel("Cost (₹)")
                ax5.set_title(
                    "Maintenance Cost by Category"
                )

                plt.xticks(rotation=45)

                st.pyplot(fig5)

            else:

                st.info(
                    "No maintenance cost data available."
                )

    except Exception as e:

        st.error(
            f"Analysis error: {e}"
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Campus Maintenance Complaint & Tracking System | "
    "Python • Streamlit • SQLite • Pandas • Matplotlib"
)
