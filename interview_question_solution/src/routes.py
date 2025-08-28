from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from .db import db
from .models import PollingUnit, AnnouncedPUResult, LGA
import os


routes = Blueprint('routes', __name__)


@routes.route("/")
def index():
    return render_template("index.html")


# Question 1: Show results for a selected polling unit
@routes.route("/polling-unit", methods=["GET", "POST"])
def polling_unit_results():
    results = None
    if request.method == "POST":
        pu_id = request.form.get("pu_id")
        results = AnnouncedPUResult.query.filter_by(polling_unit_uniqueid=pu_id).all()
    return render_template("polling_unit.html", results=results)


# Question 2: Sum of results for an LGA
@routes.route("/lga", methods=["GET", "POST"])
def lga_results():
    lgas = LGA.query.all()
    for lga in lgas:
        print(lga.lga_id, lga.lga_name)

    results = None
    selected_lga = None

    if request.method == "POST":
        selected_lga = int(request.form.get("lga_id"))
        pus = PollingUnit.query.filter_by(lga_id=1).all()
        for pu in pus:
            print(pu.uniqueid, pu.polling_unit_name)

        results = (db.session.query(
                    AnnouncedPUResult.party_abbreviation,
                    func.sum(AnnouncedPUResult.party_score).label("total_score"))
                   .join(PollingUnit, AnnouncedPUResult.polling_unit_uniqueid == PollingUnit.uniqueid)
                   .filter(PollingUnit.lga_id == int(selected_lga))
                   .group_by(AnnouncedPUResult.party_abbreviation)
                   .all())
        print("Selected LGA: ", selected_lga)
        print("Results: ", results)
    return render_template("lga.html", lgas=lgas, results=results, selected_lga=selected_lga)


# Question 3: Enter new polling unit results
@routes.route("/add-result", methods=["GET", "POST"])
def add_result():
    message = None
    if request.method == "POST":
        pu_id = request.form.get("pu_id")
        party = request.form.get("party")
        score = request.form.get("score")

        new_result = AnnouncedPUResult(
            polling_unit_uniqueid=pu_id,
            party_abbreviation=party,
            party_score=score,
            entered_by_user="admin",
            date_entered="2025-08-27",
            user_ip_address="127.0.0.1"
        )
        db.session.add(new_result)
        db.session.commit()
        message = "Result added successfully!"
    return render_template("add_result.html", message=message)

    #if not os.path.exists("my_bincom_test.db"):
       # print(" Database not found! Please run: sqlite3 election.db < election.sql")
