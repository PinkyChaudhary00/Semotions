""" Models and database function for ***** """
from views import db
class User(db.Model):
    """ User Information"""

    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    refresh_token = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User id={self.id}>"

class Track(db.Model):
    """ Song Information """

    __tablename__ = 'tracks'
    uri = db.Column(db.String, primary_key=True)
    id = db.Column(db.String)
    name = db.Column(db.String)
    energy = db.Column(db.Numeric(4,3))
    valence = db.Column(db.Numeric(4,3))
    users = db.relationship('User', secondary = 'user_track', backref = 'tracks')
    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Track id={self.id}>"


class UserTrack(db.Model):
    """ All tracks for a user """

    __tablename__ = 'user_track'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    track_uri = db.Column(db.String, db.ForeignKey('tracks.uri'), nullable=False)


def connect_to_db(app):
    """Connect the database to app."""

    # Configure to use PostgreSQL database
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # For interactive mode
    from views import app
    
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
