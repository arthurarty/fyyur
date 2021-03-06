#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from app_config import app, db
from models import Venue, City, State, Artist, Show, Genre
#----------------------
# ------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  city_list = City.query.all()
  data = []
  for city in city_list:
    city_dict = {
      'city': city.name,
      'state': city.state.name,
      'venues': city.venues
    }
    data.append(city_dict)
  return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():
  search_term = request.form.get('search_term')
  venues = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).all()
  response={
    "count": len(venues),
    "data": venues,
  }
  return render_template('pages/search_venues.html', results=response, search_term=search_term)


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  venue = Venue.query.filter_by(id=venue_id).first_or_404()
  data = {
    "id": venue.id,
    "name": venue.name,
    "genres": venue.genres,
    "address": venue.address,
    "city": venue.city.name,
    "state": venue.city.state.name,
    "phone": venue.phone,
    "website": venue.website,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": venue.image_link,
    "past_shows": venue.past_shows,
    "upcoming_shows": venue.upcoming_shows,
    "past_shows_count": venue.past_shows_count,
    "upcoming_shows_count": venue.num_upcoming_shows,
  }
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  form_data = request.form
  state_name =  form_data.get('state')
  state = State.query.filter_by(name=state_name).first()
  city_name = form_data.get('city')
  city = City.query.filter(City.name.ilike(f'{city_name}')).first()
  genres_list = form_data.getlist('genres')
  genres_objs = [Genre.query.filter_by(name=genre).first() for genre in genres_list]

  try:
    venue = Venue()
    venue.name = form_data.get('name', 'Name')
    venue.address = form_data.get('address' , 'Address')
    venue.phone = form_data.get('phone', '0000-0000-0000')
    venue.image_link = form_data.get('image_link', 'example.com')
    venue.facebook_link = form_data.get('facebook_link', 'https://facebook.com')
    venue.website = form_data.get('website', 'example.com')
    if form_data.get('seeking_talent') == 'y':
      venue.seeking_talent = True
    venue.seeking_description = form_data.get('seeking_description')
    if city is None:
      new_city = City(name=city_name, state=state)
      venue.city = new_city
    else:
      venue.city = city
    venue.genres = genres_objs
    db.session.add(venue)
    db.session.commit()
    flash('Venue ' + form_data['name'] + ' was successfully listed!')
  except IntegrityError:
    flash('An error occurred. Venue ' + form_data['name'] + ' already exits!.')
    db.session.rollback()
  except:
    flash('An error occurred. Venue ' + form_data['name'] + ' could not be listed.')
    db.session.rollback()
  finally:
    db.session.close()
  return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  venue = Venue.query.filter_by(id=venue_id).first_or_404()
  try:
    db.session.delete(venue)
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({'success': True})


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term = request.form.get('search_term')
  artists = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
  response={
    "count": len(artists),
    "data": artists
  }
  return render_template('pages/search_artists.html', results=response, search_term=search_term)

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  artist = Artist.query.filter_by(id=artist_id).first_or_404()
  artist_dict = {
      'id': artist.id,
      'name': artist.name,
      'genres': artist.genres,
      'city': artist.city.name,
      'state': artist.city.state.name,
      'phone': artist.phone,
      'website': artist.website,
      'facebook_link': artist.facebook_link,
      'seeking_venue': artist.seeking_venue,
      'seeking_description': artist.seeking_description,
      'image_link': artist.image_link,
      'past_shows': artist.past_shows,
      'upcoming_shows': artist.upcoming_shows,
      'past_shows_count': artist.past_shows_count,
      'upcoming_shows_count': artist.upcoming_shows_count,
  }
  return render_template('pages/show_artist.html', artist=artist_dict)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist = Artist.query.filter_by(id=artist_id).first_or_404()
  return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  artist = Artist.query.filter_by(id=artist_id).first_or_404()
  data = request.form

  state = State.query.filter_by(name=data.get('state')).first()
  city = City.query.filter(City.name.ilike(f"{data.get('city')}")).first()
  if city is None:
    new_city = City(name=city_name, state=state)
    artist.city = new_city
  else:
    artist.city = city

  genres_list = data.getlist('genres')
  genres_objs = [Genre.query.filter_by(name=genre).first() for genre in genres_list]
  artist.genres = []
  artist.genres = genres_objs

  key_list = ['name', 'phone', 'image_link', 'facebook_link', 'website', 'seeking_description']
  for key in key_list:
    value = data.get(key)
    if len(value) > 0:
      setattr(artist, key, data.get(key))

  if data.get('seeking_venue') == 'y':
    artist.seeking_venue = True

  try:
    db.session.add(artist)
    db.session.commit()
    flash('Artist ' + request.form['name'] + ' was successfully updated!')
  except:
    flash('An error occurred. Artist ' + data.name + ' could not be updated.')
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue = Venue.query.filter_by(id=venue_id).first_or_404()
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  venue = Venue.query.filter_by(id=venue_id).first_or_404()
  data = request.form

  state = State.query.filter_by(name=data.get('state')).first()
  city = City.query.filter(City.name.ilike(f"{data.get('city')}")).first()
  if city is None:
    new_city = City(name=city_name, state=state)
    venue.city = new_city
  else:
    venue.city = city

  genres_list = data.getlist('genres')
  genres_objs = [Genre.query.filter_by(name=genre).first() for genre in genres_list]
  venue.genres = []
  venue.genres = genres_objs

  key_list = ['name', 'phone', 'image_link', 'facebook_link', 'website', 'seeking_description', 'address']
  for key in key_list:
    value = data.get(key)
    if len(value) > 0:
      setattr(venue, key, data.get(key))

  if data.get('seeking_venue') == 'y':
    venue.seeking_venue = True

  try:
    db.session.add(venue)
    db.session.commit()
    flash('Venue ' + request.form['name'] + ' was successfully updated!')
  except:
    flash('An error occurred. Venue ' + data.name + ' could not be updated.')
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form_data = request.form
  state_name =  form_data.get('state')
  state = State.query.filter_by(name=state_name).first()
  city_name = form_data.get('city')
  city = City.query.filter(City.name.ilike(f'{city_name}')).first()
  genres_list = form_data.getlist('genres')
  genres_objs = [Genre.query.filter_by(name=genre).first() for genre in genres_list]

  artist = Artist()
  artist.name = form_data.get('name')
  artist.phone = form_data.get('phone')
  artist.image_link = form_data.get('image_link')
  artist.facebook_link = form_data.get('facebook_link')
  artist.website = form_data.get('website')

  if form_data.get('seeking_venue') == 'y':
    artist.seeking_venue = True
  artist.seeking_description = form_data.get('seeking_description')
  if city is None:
    new_city = City(name=city_name, state=state)
    artist.city = new_city
  else:
    artist.city = city
  artist.genres = genres_objs

  try:
    db.session.add(artist)
    db.session.commit()
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  except IntegrityError:
    flash('An error occurred. Artist ' + form_data['name'] + ' already exits!.')
    db.session.rollback()
  except:
    flash('An error occurred. Artist ' + form_data.name + ' could not be listed.')
    db.session.rollback()
  finally:
    db.session.close()
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  show_list = Show.query.all()
  data = []
  for show in show_list:
    show_dict = {
      "venue_id": show.venue_id,
      "venue_name": show.venue.name,
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": str(show.start_time)
    }
    data.append(show_dict)
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  form_data = request.form
  try:
    artist_id = form_data.get('artist_id')
    venue_id = form_data.get('venue_id')
    start_time = form_data.get('start_time')
    venue = Venue.query.filter_by(id=venue_id).first()
    artist = Artist.query.filter_by(id=artist_id).first()
    if venue is not None and artist is not None:
      show = Show(artist=artist, venue=venue, start_time=start_time)
      db.session.add(show)
      db.session.commit()
      flash('Show was successfully listed!')
    else:
      flash('Venue or Artist does not exist.')
  except IntegrityError:
    flash('An error occurred. Show already exits!.')
    db.session.rollback()
  except:
    flash('An error occurred. Show could not be listed.')
    db.session.rollback()
  finally:
    db.session.close()
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
