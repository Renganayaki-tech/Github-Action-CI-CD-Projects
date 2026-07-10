from flask import Flask, render_template, request, redirect, url_for
from database import (
    get_all_employees,
    add_employee,
    get_employee_by_id,
    update_employee,
    delete_employee
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/employees")
def employee_list():
    employees = get_all_employees()
    return render_template("employees.html", employees=employees)

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        add_employee(
            request.form["id"],
            request.form["name"],
            request.form["department"]
        )

        return redirect(url_for("employee_list"))

    return render_template("add_employee.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    if request.method == "POST":

        update_employee(
            id,
            request.form["name"],
            request.form["department"]
        )

        return redirect(url_for("employee_list"))

    employee = get_employee_by_id(id)

    return render_template(
        "edit_employee.html",
        employee=employee
    )
    
@app.route("/delete/<int:id>")
def delete(id):

    delete_employee(id)

    return redirect(url_for("employee_list"))

if __name__ == "__main__":
    app.run(debug=True)