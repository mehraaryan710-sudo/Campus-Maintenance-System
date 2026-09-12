import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date

import database
import analysis


# ============================================================
# APPLICATION THEME
# ============================================================

COLORS = {
    "primary": "#1E3A8A",
    "secondary": "#2563EB",
    "background": "#F3F6FA",
    "card": "#FFFFFF",
    "text": "#1F2937",
    "white": "#FFFFFF",
    "success": "#16A34A",
    "warning": "#F59E0B",
    "danger": "#DC2626",
    "border": "#D1D5DB",
    "light_blue": "#E8F0FE",
    "dark": "#111827"
}

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_HEADING = ("Segoe UI", 15, "bold")
FONT_NORMAL = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 10, "bold")
FONT_BUTTON = ("Segoe UI", 10, "bold")


# ============================================================
# DATABASE
# ============================================================

database.create_tables()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def style_window(window, title, width, height):
    """Apply common styling to all child windows."""

    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg=COLORS["background"])
    window.resizable(False, False)


def create_header(parent, title, subtitle=None):
    """Create a blue header."""

    header = tk.Frame(
        parent,
        bg=COLORS["primary"],
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text=title,
        font=FONT_HEADING,
        bg=COLORS["primary"],
        fg=COLORS["white"]
    ).pack(pady=(18, 2))

    if subtitle:
        tk.Label(
            header,
            text=subtitle,
            font=FONT_SUBTITLE,
            bg=COLORS["primary"],
            fg="#DCE6FF"
        ).pack()


def create_button(
    parent,
    text,
    command,
    bg=None,
    width=25
):
    """Create a consistent modern button."""

    if bg is None:
        bg = COLORS["secondary"]

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=FONT_BUTTON,
        width=width,
        height=2,
        bg=bg,
        fg=COLORS["white"],
        activebackground=COLORS["primary"],
        activeforeground=COLORS["white"],
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    return button


def create_label(parent, text):
    """Create a standard label."""

    return tk.Label(
        parent,
        text=text,
        font=FONT_LABEL,
        bg=COLORS["background"],
        fg=COLORS["text"]
    )


# ============================================================
# REGISTER COMPLAINT
# ============================================================

def register_complaint():

    window = tk.Toplevel(root)

    style_window(
        window,
        "Register Complaint",
        600,
        700
    )

    create_header(
        window,
        "Register Complaint",
        "Enter details of the campus maintenance issue"
    )

    # Form card
    form_card = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    form_card.pack(
        padx=30,
        pady=20,
        fill="both"
    )

    # Configure columns
    form_card.columnconfigure(1, weight=1)

    # --------------------------------------------------------
    # STUDENT NAME
    # --------------------------------------------------------

    create_label(
        form_card,
        "Student Name:"
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    student_entry = tk.Entry(
        form_card,
        width=32,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    student_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=12
    )

    # --------------------------------------------------------
    # DEPARTMENT
    # --------------------------------------------------------

    create_label(
        form_card,
        "Department:"
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    department_entry = tk.Entry(
        form_card,
        width=32,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    department_entry.grid(
        row=1,
        column=1,
        padx=20,
        pady=12
    )

    # --------------------------------------------------------
    # BUILDING
    # --------------------------------------------------------

    create_label(
        form_card,
        "Building:"
    ).grid(
        row=2,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    building_entry = tk.Entry(
        form_card,
        width=32,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    building_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=12
    )

    # --------------------------------------------------------
    # ROOM NUMBER
    # --------------------------------------------------------

    create_label(
        form_card,
        "Room No.:"
    ).grid(
        row=3,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    room_entry = tk.Entry(
        form_card,
        width=32,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    room_entry.grid(
        row=3,
        column=1,
        padx=20,
        pady=12
    )

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    create_label(
        form_card,
        "Category:"
    ).grid(
        row=4,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    category_combo = ttk.Combobox(
        form_card,
        values=[
            "Electrical",
            "Furniture",
            "Plumbing",
            "IT",
            "Internet",
            "Cleaning",
            "AC/Cooling",
            "Other"
        ],
        state="readonly",
        width=29,
        font=FONT_NORMAL
    )

    category_combo.grid(
        row=4,
        column=1,
        padx=20,
        pady=12
    )

    category_combo.current(0)

    # --------------------------------------------------------
    # PROBLEM
    # --------------------------------------------------------

    create_label(
        form_card,
        "Problem:"
    ).grid(
        row=5,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    problem_entry = tk.Entry(
        form_card,
        width=32,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    problem_entry.grid(
        row=5,
        column=1,
        padx=20,
        pady=12
    )

    # --------------------------------------------------------
    # PRIORITY
    # --------------------------------------------------------

    create_label(
        form_card,
        "Priority:"
    ).grid(
        row=6,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    priority_combo = ttk.Combobox(
        form_card,
        values=[
            "Low",
            "Medium",
            "High"
        ],
        state="readonly",
        width=29,
        font=FONT_NORMAL
    )

    priority_combo.grid(
        row=6,
        column=1,
        padx=20,
        pady=12
    )

    priority_combo.current(1)

    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    create_label(
        form_card,
        "Date:"
    ).grid(
        row=7,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    date_label = tk.Label(
        form_card,
        text=str(date.today()),
        font=FONT_NORMAL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    )

    date_label.grid(
        row=7,
        column=1,
        padx=20,
        pady=12,
        sticky="w"
    )

    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    def submit_complaint():

        student_name = student_entry.get().strip()
        department = department_entry.get().strip()
        building = building_entry.get().strip()
        room_no = room_entry.get().strip()
        category = category_combo.get()
        problem = problem_entry.get().strip()
        priority = priority_combo.get()
        complaint_date = str(date.today())

        if student_name == "":
            messagebox.showerror(
                "Error",
                "Please enter student name.",
                parent=window
            )
            return

        if department == "":
            messagebox.showerror(
                "Error",
                "Please enter department.",
                parent=window
            )
            return

        if building == "":
            messagebox.showerror(
                "Error",
                "Please enter building.",
                parent=window
            )
            return

        if room_no == "":
            messagebox.showerror(
                "Error",
                "Please enter room number.",
                parent=window
            )
            return

        if problem == "":
            messagebox.showerror(
                "Error",
                "Please enter problem description.",
                parent=window
            )
            return

        try:

            complaint_id = database.add_complaint(
                student_name,
                department,
                building,
                room_no,
                category,
                problem,
                priority,
                complaint_date
            )

            messagebox.showinfo(
                "Success",
                f"Complaint Registered Successfully!\n\n"
                f"Complaint ID: {complaint_id}\n"
                f"Status: Pending",
                parent=window
            )

            student_entry.delete(0, tk.END)
            department_entry.delete(0, tk.END)
            building_entry.delete(0, tk.END)
            room_entry.delete(0, tk.END)
            problem_entry.delete(0, tk.END)

            category_combo.current(0)
            priority_combo.current(1)

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to save complaint.\n\n{e}",
                parent=window
            )

    create_button(
        window,
        "Submit Complaint",
        submit_complaint,
        COLORS["success"],
        25
    ).pack(pady=10)


# ============================================================
# VIEW COMPLAINTS
# ============================================================

def view_complaints():

    window = tk.Toplevel(root)

    style_window(
        window,
        "View Complaints",
        1000,
        600
    )

    create_header(
        window,
        "All Complaints",
        "View all registered maintenance complaints"
    )

    table_frame = tk.Frame(
        window,
        bg=COLORS["card"]
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=20
    )

    columns = (
        "Complaint ID",
        "Student",
        "Category",
        "Building",
        "Priority",
        "Status",
        "Date"
    )

    # --------------------------------------------------------
    # TREEVIEW STYLE
    # --------------------------------------------------------

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        "Treeview",
        background=COLORS["white"],
        foreground=COLORS["text"],
        rowheight=32,
        fieldbackground=COLORS["white"],
        font=FONT_NORMAL
    )

    style.configure(
        "Treeview.Heading",
        background=COLORS["primary"],
        foreground=COLORS["white"],
        font=("Segoe UI", 10, "bold")
    )

    style.map(
        "Treeview",
        background=[
            ("selected", COLORS["secondary"])
        ],
        foreground=[
            ("selected", COLORS["white"])
        ]
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for column in columns:

        tree.heading(
            column,
            text=column
        )

    tree.column(
        "Complaint ID",
        width=110,
        anchor="center"
    )

    tree.column(
        "Student",
        width=170,
        anchor="center"
    )

    tree.column(
        "Category",
        width=130,
        anchor="center"
    )

    tree.column(
        "Building",
        width=130,
        anchor="center"
    )

    tree.column(
        "Priority",
        width=100,
        anchor="center"
    )

    tree.column(
        "Status",
        width=130,
        anchor="center"
    )

    tree.column(
        "Date",
        width=120,
        anchor="center"
    )

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    try:

        complaints = database.get_all_complaints()

        for complaint in complaints:

            tree.insert(
                "",
                tk.END,
                values=complaint
            )

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            f"Unable to load complaints.\n\n{e}",
            parent=window
        )


# ============================================================
# SEARCH COMPLAINT
# ============================================================

def search_complaint():

    window = tk.Toplevel(root)

    style_window(
        window,
        "Search Complaint",
        650,
        650
    )

    create_header(
        window,
        "Search Complaint",
        "Find a complaint using its Complaint ID"
    )

    search_card = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    search_card.pack(
        padx=30,
        pady=20,
        fill="x"
    )

    tk.Label(
        search_card,
        text="Complaint ID:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )

    complaint_id_entry = tk.Entry(
        search_card,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    complaint_id_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )

    result_frame = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    result_frame.pack(
        padx=30,
        pady=5,
        fill="both",
        expand=True
    )

    def perform_search():

        complaint_id = (
            complaint_id_entry
            .get()
            .strip()
            .upper()
        )

        if complaint_id == "":

            messagebox.showerror(
                "Error",
                "Please enter Complaint ID.",
                parent=window
            )

            return

        try:

            complaint = database.search_complaint(
                complaint_id
            )

            for widget in result_frame.winfo_children():
                widget.destroy()

            if complaint is None:

                messagebox.showerror(
                    "Not Found",
                    "Complaint Not Found",
                    parent=window
                )

                return

            tk.Label(
                result_frame,
                text="Complaint Details",
                font=FONT_HEADING,
                bg=COLORS["card"],
                fg=COLORS["primary"]
            ).pack(pady=15)

            labels = [
                ("Complaint ID", complaint[0]),
                ("Student Name", complaint[1]),
                ("Department", complaint[2]),
                ("Building", complaint[3]),
                ("Room No.", complaint[4]),
                ("Category", complaint[5]),
                ("Problem", complaint[6]),
                ("Priority", complaint[7]),
                ("Status", complaint[8]),
                ("Date", complaint[9])
            ]

            for label, value in labels:

                row = tk.Frame(
                    result_frame,
                    bg=COLORS["card"]
                )

                row.pack(
                    fill="x",
                    padx=25,
                    pady=4
                )

                tk.Label(
                    row,
                    text=f"{label}:",
                    font=FONT_LABEL,
                    width=17,
                    anchor="w",
                    bg=COLORS["card"],
                    fg=COLORS["text"]
                ).pack(side="left")

                tk.Label(
                    row,
                    text=str(value),
                    font=FONT_NORMAL,
                    anchor="w",
                    bg=COLORS["card"],
                    fg=COLORS["text"]
                ).pack(side="left")

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to search complaint.\n\n{e}",
                parent=window
            )

    create_button(
        window,
        "🔍  Search Complaint",
        perform_search,
        COLORS["secondary"],
        22
    ).pack(pady=10)


# ============================================================
# UPDATE STATUS
# ============================================================

def update_status():

    window = tk.Toplevel(root)

    style_window(
        window,
        "Update Complaint Status",
        550,
        500
    )

    create_header(
        window,
        "Update Complaint Status",
        "Track the progress of a maintenance complaint"
    )

    form = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    form.pack(
        padx=30,
        pady=25,
        fill="both"
    )

    tk.Label(
        form,
        text="Complaint ID:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )

    complaint_id_entry = tk.Entry(
        form,
        width=28,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    complaint_id_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )

    current_status_label = tk.Label(
        form,
        text="Current Status: -",
        font=("Segoe UI", 11, "bold"),
        bg=COLORS["card"],
        fg=COLORS["primary"]
    )

    current_status_label.grid(
        row=1,
        column=0,
        columnspan=2,
        pady=15
    )

    tk.Label(
        form,
        text="New Status:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=2,
        column=0,
        padx=20,
        pady=15
    )

    status_combo = ttk.Combobox(
        form,
        values=[
            "Pending",
            "In Progress",
            "Resolved"
        ],
        state="readonly",
        width=26
    )

    status_combo.grid(
        row=2,
        column=1,
        padx=20,
        pady=15
    )

    status_combo.current(0)

    def find_complaint():

        complaint_id = (
            complaint_id_entry
            .get()
            .strip()
            .upper()
        )

        if complaint_id == "":

            messagebox.showerror(
                "Error",
                "Please enter Complaint ID.",
                parent=window
            )

            return

        try:

            current_status = (
                database.get_complaint_status(
                    complaint_id
                )
            )

            if current_status is None:

                messagebox.showerror(
                    "Not Found",
                    "Complaint Not Found.",
                    parent=window
                )

                current_status_label.config(
                    text="Current Status: -"
                )

                return

            current_status_label.config(
                text=f"Current Status: {current_status}"
            )

            status_combo.set(current_status)

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to find complaint.\n\n{e}",
                parent=window
            )

    def change_status():

        complaint_id = (
            complaint_id_entry
            .get()
            .strip()
            .upper()
        )

        new_status = status_combo.get()

        if complaint_id == "":

            messagebox.showerror(
                "Error",
                "Please enter Complaint ID.",
                parent=window
            )

            return

        if new_status == "":

            messagebox.showerror(
                "Error",
                "Please select a new status.",
                parent=window
            )

            return

        try:

            current_status = (
                database.get_complaint_status(
                    complaint_id
                )
            )

            if current_status is None:

                messagebox.showerror(
                    "Not Found",
                    "Complaint Not Found.",
                    parent=window
                )

                return

            rows_updated = (
                database.update_complaint_status(
                    complaint_id,
                    new_status
                )
            )

            if rows_updated > 0:

                current_status_label.config(
                    text=f"Current Status: {new_status}"
                )

                messagebox.showinfo(
                    "Success",
                    f"Status Updated Successfully!\n\n"
                    f"Complaint ID: {complaint_id}\n"
                    f"New Status: {new_status}",
                    parent=window
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to update status.\n\n{e}",
                parent=window
            )

    create_button(
        window,
        "Find Complaint",
        find_complaint,
        COLORS["secondary"],
        22
    ).pack(pady=5)

    create_button(
        window,
        "Update Status",
        change_status,
        COLORS["success"],
        22
    ).pack(pady=5)


# ============================================================
# ADD MAINTENANCE
# ============================================================

def add_maintenance():

    window = tk.Toplevel(root)

    style_window(
        window,
        "Add Maintenance Details",
        600,
        600
    )

    create_header(
        window,
        "Add Maintenance Details",
        "Record repair and maintenance information"
    )

    form = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    form.pack(
        padx=30,
        pady=20,
        fill="both"
    )

    # --------------------------------------------------------
    # COMPLAINT ID
    # --------------------------------------------------------

    tk.Label(
        form,
        text="Complaint ID:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    complaint_id_entry = tk.Entry(
        form,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    complaint_id_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=15
    )

    # --------------------------------------------------------
    # STAFF NAME
    # --------------------------------------------------------

    tk.Label(
        form,
        text="Staff Name:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    staff_entry = tk.Entry(
        form,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    staff_entry.grid(
        row=1,
        column=1,
        padx=20,
        pady=15
    )

    # --------------------------------------------------------
    # REPAIR DATE
    # --------------------------------------------------------

    tk.Label(
        form,
        text="Repair Date:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=2,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    repair_date_entry = tk.Entry(
        form,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    repair_date_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=15
    )

    repair_date_entry.insert(
        0,
        str(date.today())
    )

    # --------------------------------------------------------
    # COST
    # --------------------------------------------------------

    tk.Label(
        form,
        text="Repair Cost (₹):",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=3,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    cost_entry = tk.Entry(
        form,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    cost_entry.grid(
        row=3,
        column=1,
        padx=20,
        pady=15
    )

    # --------------------------------------------------------
    # REMARKS
    # --------------------------------------------------------

    tk.Label(
        form,
        text="Remarks:",
        font=FONT_LABEL,
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).grid(
        row=4,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    remarks_entry = tk.Entry(
        form,
        width=30,
        font=FONT_NORMAL,
        relief="solid",
        bd=1
    )

    remarks_entry.grid(
        row=4,
        column=1,
        padx=20,
        pady=15
    )

    # --------------------------------------------------------
    # SAVE MAINTENANCE
    # --------------------------------------------------------

    def save_maintenance():

        complaint_id = (
            complaint_id_entry
            .get()
            .strip()
            .upper()
        )

        staff_name = staff_entry.get().strip()
        repair_date = repair_date_entry.get().strip()
        cost_text = cost_entry.get().strip()
        remarks = remarks_entry.get().strip()

        if complaint_id == "":

            messagebox.showerror(
                "Error",
                "Please enter Complaint ID.",
                parent=window
            )

            return

        if staff_name == "":

            messagebox.showerror(
                "Error",
                "Please enter maintenance staff name.",
                parent=window
            )

            return

        if repair_date == "":

            messagebox.showerror(
                "Error",
                "Please enter repair date.",
                parent=window
            )

            return

        if cost_text == "":

            messagebox.showerror(
                "Error",
                "Please enter repair cost.",
                parent=window
            )

            return

        try:

            cost = float(cost_text)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Repair cost must be a number.",
                parent=window
            )

            return

        if cost < 0:

            messagebox.showerror(
                "Error",
                "Repair cost cannot be negative.",
                parent=window
            )

            return

        try:

            exists = database.complaint_exists(
                complaint_id
            )

            if not exists:

                messagebox.showerror(
                    "Not Found",
                    "Complaint ID does not exist.",
                    parent=window
                )

                return

            database.add_maintenance(
                complaint_id,
                staff_name,
                repair_date,
                cost,
                remarks
            )

            messagebox.showinfo(
                "Success",
                f"Maintenance details saved successfully!\n\n"
                f"Complaint ID: {complaint_id}\n"
                f"Staff: {staff_name}\n"
                f"Repair Cost: ₹{cost:.2f}",
                parent=window
            )

            complaint_id_entry.delete(
                0,
                tk.END
            )

            staff_entry.delete(
                0,
                tk.END
            )

            repair_date_entry.delete(
                0,
                tk.END
            )

            repair_date_entry.insert(
                0,
                str(date.today())
            )

            cost_entry.delete(
                0,
                tk.END
            )

            remarks_entry.delete(
                0,
                tk.END
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to save maintenance details.\n\n{e}",
                parent=window
            )

    create_button(
        window,
        "Save Maintenance",
        save_maintenance,
        COLORS["success"],
        25
    ).pack(pady=15)


# ============================================================
# REPORTS & ANALYSIS
# ============================================================

def reports_analysis():

    window = tk.Toplevel(root)

    style_window(
        window,
        "Reports & Analysis",
        750,
        700
    )

    create_header(
        window,
        "Reports & Analysis",
        "Campus maintenance statistics and data visualization"
    )

    try:

        stats = analysis.get_statistics()

    except Exception as e:

        messagebox.showerror(
            "Analysis Error",
            f"Unable to load analysis data.\n\n{e}",
            parent=window
        )

        return

    # --------------------------------------------------------
    # STATISTICS TITLE
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Key Statistics",
        font=FONT_HEADING,
        bg=COLORS["background"],
        fg=COLORS["primary"]
    ).pack(pady=(15, 5))

    # --------------------------------------------------------
    # STATISTICS CARDS
    # --------------------------------------------------------

    stats_frame = tk.Frame(
        window,
        bg=COLORS["background"]
    )

    stats_frame.pack(
        padx=20,
        pady=5
    )

    # Card creation helper
    def create_stat_card(
        parent,
        title,
        value,
        row,
        column
    ):

        card = tk.Frame(
            parent,
            bg=COLORS["card"],
            width=210,
            height=80,
            bd=1,
            relief="solid"
        )

        card.grid(
            row=row,
            column=column,
            padx=7,
            pady=7
        )

        card.grid_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            bg=COLORS["card"],
            fg="#6B7280"
        ).pack(pady=(10, 0))

        tk.Label(
            card,
            text=str(value),
            font=("Segoe UI", 15, "bold"),
            bg=COLORS["card"],
            fg=COLORS["primary"]
        ).pack(pady=3)

    create_stat_card(
        stats_frame,
        "TOTAL COMPLAINTS",
        stats["total"],
        0,
        0
    )

    create_stat_card(
        stats_frame,
        "PENDING",
        stats["pending"],
        0,
        1
    )

    create_stat_card(
        stats_frame,
        "IN PROGRESS",
        stats["in_progress"],
        1,
        0
    )

    create_stat_card(
        stats_frame,
        "RESOLVED",
        stats["resolved"],
        1,
        1
    )

    create_stat_card(
        stats_frame,
        "TOTAL COST",
        f"₹{stats['total_cost']:.2f}",
        2,
        0
    )

    create_stat_card(
        stats_frame,
        "AVERAGE COST",
        f"₹{stats['average_cost']:.2f}",
        2,
        1
    )

    # --------------------------------------------------------
    # OTHER INFORMATION
    # --------------------------------------------------------

    info_frame = tk.Frame(
        window,
        bg=COLORS["card"],
        bd=1,
        relief="solid"
    )

    info_frame.pack(
        padx=30,
        pady=10,
        fill="x"
    )

    tk.Label(
        info_frame,
        text=(
            f"Most Common Category: "
            f"{stats['most_common_category']}    |    "
            f"Highest Complaint Building: "
            f"{stats['highest_building']}"
        ),
        font=("Segoe UI", 10, "bold"),
        bg=COLORS["card"],
        fg=COLORS["text"]
    ).pack(pady=12)

    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    tk.Label(
        window,
        text="Data Visualization",
        font=FONT_HEADING,
        bg=COLORS["background"],
        fg=COLORS["primary"]
    ).pack(pady=(5, 5))

    charts_frame = tk.Frame(
        window,
        bg=COLORS["background"]
    )

    charts_frame.pack()

    create_button(
        charts_frame,
        "📊  Complaints by Category",
        analysis.category_chart,
        COLORS["secondary"],
        30
    ).grid(
        row=0,
        column=0,
        padx=7,
        pady=5
    )

    create_button(
        charts_frame,
        "🥧  Status Distribution",
        analysis.status_chart,
        COLORS["secondary"],
        30
    ).grid(
        row=0,
        column=1,
        padx=7,
        pady=5
    )

    create_button(
        charts_frame,
        "🏢  Complaints by Building",
        analysis.building_chart,
        COLORS["secondary"],
        30
    ).grid(
        row=1,
        column=0,
        padx=7,
        pady=5
    )

    create_button(
        charts_frame,
        "📈  Monthly Complaint Trend",
        analysis.monthly_chart,
        COLORS["secondary"],
        30
    ).grid(
        row=1,
        column=1,
        padx=7,
        pady=5
    )

    create_button(
        charts_frame,
        "💰  Maintenance Cost by Category",
        analysis.cost_category_chart,
        COLORS["secondary"],
        30
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        pady=5
    )

    create_button(
        window,
        "Close",
        window.destroy,
        COLORS["danger"],
        18
    ).pack(pady=12)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Campus Maintenance Complaint & Tracking System"
)

root.geometry("650x720")

root.configure(
    bg=COLORS["background"]
)

root.resizable(
    False,
    False
)


# ============================================================
# MAIN HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=COLORS["primary"],
    height=135
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


tk.Label(
    header,
    text="CAMPUS MAINTENANCE",
    font=FONT_TITLE,
    bg=COLORS["primary"],
    fg=COLORS["white"]
).pack(
    pady=(28, 2)
)


tk.Label(
    header,
    text="Complaint & Tracking System",
    font=("Segoe UI", 12),
    bg=COLORS["primary"],
    fg="#DCE6FF"
).pack()


# ============================================================
# WELCOME
# ============================================================

tk.Label(
    root,
    text="Manage campus complaints efficiently",
    font=("Segoe UI", 11),
    bg=COLORS["background"],
    fg=COLORS["text"]
).pack(
    pady=(20, 10)
)


# ============================================================
# MAIN MENU
# ============================================================

menu_frame = tk.Frame(
    root,
    bg=COLORS["background"]
)

menu_frame.pack(
    pady=5
)


create_button(
    menu_frame,
    "📝  Register Complaint",
    register_complaint,
    COLORS["secondary"],
    34
).pack(pady=5)


create_button(
    menu_frame,
    "📋  View Complaints",
    view_complaints,
    COLORS["secondary"],
    34
).pack(pady=5)


create_button(
    menu_frame,
    "🔍  Search Complaint",
    search_complaint,
    COLORS["secondary"],
    34
).pack(pady=5)


create_button(
    menu_frame,
    "🔄  Update Status",
    update_status,
    COLORS["secondary"],
    34
).pack(pady=5)


create_button(
    menu_frame,
    "🔧  Add Maintenance",
    add_maintenance,
    COLORS["secondary"],
    34
).pack(pady=5)


create_button(
    menu_frame,
    "📊  Reports & Analysis",
    reports_analysis,
    COLORS["primary"],
    34
).pack(pady=5)


# ============================================================
# EXIT
# ============================================================

create_button(
    root,
    "Exit",
    root.destroy,
    COLORS["danger"],
    22
).pack(
    pady=15
)


# ============================================================
# FOOTER
# ============================================================

tk.Label(
    root,
    text="SQLite  •  Pandas  •  Matplotlib  •  Tkinter",
    font=("Segoe UI", 8),
    bg=COLORS["background"],
    fg="#6B7280"
).pack(
    side="bottom",
    pady=8
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()