from flask import request, jsonify
from service import app
from service.models import Venue, Field, field_schema, fields_schema, fields2_schema, fields3_schema, Pitch
from datetime import datetime
from service import db

# Create new Field
@app.route("/field/<Id>", methods=['POST'])
def add_field(Id):
    venue = Venue.query.get(Id)
    venue_id = venue.id
    name = request.json["name"]
    num_pitches = request.json["num_pitches"]
    colour = request.json["colour"]
    num_pitches = "0"
    created_at = datetime.now()
    updated_at = datetime.now()
    new_field = Field(name, venue_id, num_pitches, colour, created_at, updated_at)

    db.session.add(new_field)
    db.session.commit()

    return field_schema.jsonify(new_field)


# Get lists of Field

@app.route("/field", methods=["GET"])
def get_fields():
    all_fields = Field.query.all()
    result = fields_schema.dump(all_fields)
    return jsonify(result)


# Get lists of Fields based on Venue ID
@app.route("/fields/<venue_id>", methods=["GET"])
def get_fields_based_on_venue_id(venue_id):
    all_fields = Field.query.filter_by(venue_id=venue_id).all()
    result = fields3_schema.dump(all_fields)
    return fields3_schema.jsonify(result)


# Get field based on Id
@app.route("/field/<Id>", methods=["GET"])
def get_fields_based_on_id(Id):
    field = Field.query.get(Id)
    return field_schema.jsonify(field)

# Update a Field
@app.route("/field/<Id>", methods=["PUT"])
def update_field(Id):
    field = Field.query.get(Id)

    name = request.json["name"]
    num_pitches = request.json["num_pitches"]
    colour = request.json["colour"]
    updatedat = datetime.now()

    field.name = name
    field.num_pitches = num_pitches
    field.colour = colour
    field.updatedat = updatedat

    db.session.commit()

    return field_schema.jsonify(field)

# Delete Field
@app.route("/field/<Id>", methods=["DELETE"])
def delete_field(Id):
    field = Field.query.get(Id)

    db.session.delete(field)
    db.session.commit()

    return field_schema.jsonify(field)
