from app_config import app, db, migrate
from datetime import datetime


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
genres_venues = db.Table(
  'genres_venues',
  db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
  db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id'), primary_key=True)
)


genres_artists = db.Table(
  'genres_artists',
  db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
  db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id'), primary_key=True)
)

class Venue(db.Model):
    __tablename__ = 'Venue'
    __table_args__ = (
      db.UniqueConstraint('name', 'address', 'city_id', name='unique_venue'),
    ) # a venue is unique basing on its name and address
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(250), nullable=True)
    seeking_talent = db.Column(db.Boolean(), default=False, nullable=True)
    seeking_description =  db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='venue', lazy=True, cascade="all, delete-orphan")
    city_id = db.Column(
      db.Integer, db.ForeignKey('City.id'), nullable=False)
    genres = db.relationship(
      'Genre', secondary=genres_venues, backref=db.backref('venues', lazy=True))

    @property
    def upcoming_shows(self):
        """
        Returns a list of upcoming shows
        """
        current_time = datetime.now()
        shows_list = self.shows
        upcoming_shows = [show for show in shows_list if show.start_time >= current_time]
        upcoming_shows_list = []
        for show in upcoming_shows:
          show_dict = {
            'artist_id': show.artist_id,
            'artist_name': show.artist.name,
            'artist_image_link': show.artist.image_link,
            'start_time': str(show.start_time),
            }
          upcoming_shows_list.append(show_dict)
        return upcoming_shows_list

    @property
    def num_upcoming_shows(self):
        """
        Returns the number of upcoming shows
        """
        upcoming_shows = self.upcoming_shows
        return len(upcoming_shows)
  
    @property
    def past_shows(self):
        """
        Returns a list of past shows
        """
        current_time = datetime.now()
        past_shows = [show for show in self.shows if show.start_time < current_time]
        past_shows_list = []
        for show in past_shows:
          show_dict = {
            'artist_id': show.artist_id,
            'artist_name': show.artist.name,
            'artist_image_link': show.artist.image_link,
            'start_time': str(show.start_time),
            }
          past_shows_list.append(show_dict)
        return past_shows_list

    @property
    def past_shows_count(self):
        """
        Returns number of past shows
        """
        return len(self.past_shows)
    def __repr__(self):
        return f'<Venue: id: {self.id} name: {self.name}>'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    phone = db.Column(db.String(120), unique=True)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(250), nullable=True)
    seeking_venue = db.Column(db.Boolean(), default=False, nullable=True)
    seeking_description =  db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='artist', lazy=True)
    city_id = db.Column(
      db.Integer, db.ForeignKey('City.id'), nullable=False)
    genres = db.relationship(
      'Genre', secondary=genres_artists, backref=db.backref('artists', lazy=True))

    @property
    def upcoming_shows(self):
        """
        Returns a list of upcoming shows
        """
        current_time = datetime.now()
        upcoming_shows = [show for show in self.shows if show.start_time > current_time]
        upcoming_show_list = []
        for show in upcoming_shows:
          show_dict = {
            'venue_id':show.venue_id,
            'venue_name':show.venue.name,
            'venue_image_link': show.venue.image_link,
            'start_time': str(show.start_time),
          }
          upcoming_show_list.append(show_dict)
        return upcoming_show_list

    @property
    def past_shows(self):
        """
        Returns a list of past shows
        """
        current_time = datetime.now()
        past_shows = [show for show in self.shows if show.start_time < current_time]
        past_shows_list = []
        for show in past_shows:
            show_dict = {
            'venue_id':show.venue_id,
            'venue_name':show.venue.name,
            'venue_image_link': show.venue.image_link,
            'start_time': str(show.start_time),
            }
            past_shows_list.append(show_dict)
        return past_shows_list

    @property
    def past_shows_count(self):
        """
        Returns number of past shows
        """
        return len(self.past_shows)

    @property
    def upcoming_shows_count(self):
        """
        Returns number of upcoming shows
        """
        return len(self.upcoming_shows)

    def __repr__(self):
        return f'<Artist: id: {self.id} name: {self.name}>'

class Show(db.Model):
  __tablename__ = 'Show'
  __table_args__ = (
    db.UniqueConstraint('artist_id', 'venue_id', 'start_time', name='unique_show'),
  )
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'),
        nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'),
        nullable=False)
  start_time = db.Column(db.DateTime, nullable=False)


class State(db.Model):
  __tablename__ = 'State'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(2), nullable=False, unique=True)
  cities = db.relationship('City', backref='state', lazy=True)

  def __repr__(self):
    return f'<State: id: {self.id} name: {self.name}>'

class City(db.Model):
  __tablename__ = 'City'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  state_id = db.Column(
    db.Integer, db.ForeignKey('State.id'), nullable=False)
  venues = db.relationship('Venue', backref='city', lazy=True)
  artists = db.relationship('Artist', backref='city', lazy=True)

  def __repr__(self):
    return f'<City: id: {self.id} name: {self.name}>'


class Genre(db.Model):
  __tablename__ = 'Genre'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)

  def __repr__(self):
    return self.name