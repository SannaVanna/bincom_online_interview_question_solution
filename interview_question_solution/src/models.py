from .db import db


class LGA(db.Model):
    __tablename__ = "lga"
    lga_id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String)
    state_id = db.Column(db.Integer)


class Ward(db.Model):
    __tablename__ = "ward"
    ward_id = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)
    ward_name = db.Column(db.String)


class PollingUnit(db.Model):
    __tablename__ = "polling_unit"
    uniqueid = db.Column(db.Integer, primary_key=True)
    polling_unit_id = db.Column(db.Integer)
    ward_id = db.Column(db.Integer)
    lga_id = db.Column(db.Integer)
    polling_unit_name = db.Column(db.String)


class AnnouncedPUResult(db.Model):
    __tablename__ = "announced_pu_results"
    result_id = db.Column(db.Integer, primary_key=True)
    polling_unit_uniqueid = db.Column(db.Integer, db.ForeignKey("polling_unit.uniqueid"))
    party_abbreviation = db.Column(db.String)
    party_score = db.Column(db.Integer)
    entered_by_user = db.Column(db.Integer)
    date_entered = db.Column(db.Integer)
    user_ip_address = db.Column(db.Integer)


class AnnouncedLGAResult(db.Model):
    __tablename__ = "announced_lga_results"
    result_id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String)
    party_abbreviation = db.Column(db.String)
    party_score = db.Column(db.Integer)
