from application import db

class WorkTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    month = db.Column(db.String(20), nullable=False)
    workday_type = db.Column(db.String(20), nullable=False)
    time_in = db.Column(db.Time, nullable=True)
    time_out = db.Column(db.Time, nullable=True)
    
       
    def __str__(self):
        return self.id