from .extensions import db


class Professor(db.Model):
    __tablename__ = 'professors'

    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FullName = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(150), nullable=False)
    UpdatedDate = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    classes = db.relationship("Class", backref="professor", cascade="all, delete")


class Class(db.Model):
    __tablename__ = 'classes'

    CID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PID = db.Column(db.Integer, db.ForeignKey('professors.PID', ondelete='CASCADE'), nullable=False)
    Title = db.Column(db.String(100), nullable=False)
    UpdatedDate = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    assignments = db.relationship("Assignment", backref="class_ref", cascade="all, delete")


class StatusLookup(db.Model):
    __tablename__ = 'status_lookup'

    SID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)


class Assignment(db.Model):
    __tablename__ = 'assignments'

    AID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(500))
    DueDate = db.Column(db.DateTime)

    SID = db.Column(db.Integer, db.ForeignKey('status_lookup.SID'))
    Grade = db.Column(db.DECIMAL(5, 2), default=0.00)

    CID = db.Column(db.Integer, db.ForeignKey('classes.CID', ondelete='CASCADE'))
    UpdatedDate = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    status = db.relationship("StatusLookup", backref="assignments")