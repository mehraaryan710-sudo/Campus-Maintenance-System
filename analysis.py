import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DB_PATH = "data/campus.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


# -----------------------------------
# LOAD DATA
# -----------------------------------

def load_complaints():
    conn = get_connection()

    query = """
        SELECT
            complaint_id,
            student_name,
            department,
            building,
            room_no,
            category,
            problem,
            priority,
            status,
            date
        FROM complaints
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


def load_maintenance():
    conn = get_connection()

    query = """
        SELECT
            id,
            complaint_id,
            staff_name,
            repair_date,
            cost,
            remarks
        FROM maintenance
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


# -----------------------------------
# CALCULATE STATISTICS
# -----------------------------------

def get_statistics():

    complaints = load_complaints()
    maintenance = load_maintenance()

    total_complaints = len(complaints)

    pending = len(
        complaints[complaints["status"] == "Pending"]
    )

    in_progress = len(
        complaints[complaints["status"] == "In Progress"]
    )

    resolved = len(
        complaints[complaints["status"] == "Resolved"]
    )

    # Most common category
    if not complaints.empty:
        most_common_category = (
            complaints["category"].value_counts().idxmax()
        )
    else:
        most_common_category = "No Data"

    # Building with highest complaints
    if not complaints.empty:
        highest_complaint_building = (
            complaints["building"].value_counts().idxmax()
        )
    else:
        highest_complaint_building = "No Data"

    # Maintenance cost
    if not maintenance.empty:
        total_cost = maintenance["cost"].sum()
        average_cost = maintenance["cost"].mean()
    else:
        total_cost = 0
        average_cost = 0

    return {
        "total": total_complaints,
        "pending": pending,
        "in_progress": in_progress,
        "resolved": resolved,
        "most_common_category": most_common_category,
        "highest_building": highest_complaint_building,
        "total_cost": total_cost,
        "average_cost": average_cost
    }


# -----------------------------------
# CHART 1: CATEGORY BAR CHART
# -----------------------------------

def category_chart():

    df = load_complaints()

    if df.empty:
        print("No complaint data available.")
        return

    category_counts = df["category"].value_counts()

    plt.figure(figsize=(9, 5))

    category_counts.plot(kind="bar")

    plt.title("Complaints by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Complaints")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# -----------------------------------
# CHART 2: STATUS PIE CHART
# -----------------------------------

def status_chart():

    df = load_complaints()

    if df.empty:
        print("No complaint data available.")
        return

    status_counts = df["status"].value_counts()

    plt.figure(figsize=(7, 7))

    status_counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Complaint Status Distribution")
    plt.ylabel("")

    plt.show()


# -----------------------------------
# CHART 3: BUILDING BAR CHART
# -----------------------------------

def building_chart():

    df = load_complaints()

    if df.empty:
        print("No complaint data available.")
        return

    building_counts = df["building"].value_counts()

    plt.figure(figsize=(9, 5))

    building_counts.plot(kind="bar")

    plt.title("Complaints by Building")
    plt.xlabel("Building")
    plt.ylabel("Number of Complaints")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# -----------------------------------
# CHART 4: MONTHLY LINE CHART
# -----------------------------------

def monthly_chart():

    df = load_complaints()

    if df.empty:
        print("No complaint data available.")
        return

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    monthly_counts = (
        df.groupby(
            df["date"].dt.to_period("M")
        ).size()
    )

    plt.figure(figsize=(9, 5))

    monthly_counts.plot(
        kind="line",
        marker="o"
    )

    plt.title("Monthly Complaint Trend")
    plt.xlabel("Month")
    plt.ylabel("Number of Complaints")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# -----------------------------------
# CHART 5: COST BY CATEGORY
# -----------------------------------

def cost_category_chart():

    complaints = load_complaints()
    maintenance = load_maintenance()

    if complaints.empty or maintenance.empty:
        print("No maintenance data available.")
        return

    merged = pd.merge(
        maintenance,
        complaints[
            ["complaint_id", "category"]
        ],
        on="complaint_id",
        how="left"
    )

    cost_by_category = (
        merged.groupby("category")["cost"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 5))

    cost_by_category.plot(kind="bar")

    plt.title("Maintenance Cost by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Cost")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# -----------------------------------
# TEST ANALYSIS
# -----------------------------------

if __name__ == "__main__":

    stats = get_statistics()

    print("\n===== CAMPUS MAINTENANCE ANALYSIS =====")

    print("Total Complaints:", stats["total"])
    print("Pending:", stats["pending"])
    print("In Progress:", stats["in_progress"])
    print("Resolved:", stats["resolved"])

    print(
        "Most Common Category:",
        stats["most_common_category"]
    )

    print(
        "Highest Complaint Building:",
        stats["highest_building"]
    )

    print(
        "Total Maintenance Cost:",
        stats["total_cost"]
    )

    print(
        "Average Maintenance Cost:",
        stats["average_cost"]
    )