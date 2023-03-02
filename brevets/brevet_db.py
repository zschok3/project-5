"""
Contains two database interaction functions for flask_brevets
"""
import os
from pymongo import MongoClient
import arrow
import sys
import logging

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

db = client.brevets

collection = db.tables

def get_brevet():
    """
    Obtains the newest document in the "lists" collection in database "brevets".
    Returns title (string) and items (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    brevets = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for brevet in brevets:
        # We store all of our lists as documents with two fields:
        ## title: string # title of our to-do list
        ## items: list   # list of items:

        ### every item has two fields:
        #### desc: string   # description
        #### priority: int  # priority
        return brevet["distance"], brevet["begin_date"], brevet["control_times"]


def insert_brevet(distance,begin_date,control_times):
    """
    Inserts a new to-do list into the database "todo", under the collection "lists".
    
    Inputs a title (string) and items (list of dictionaries)
    Returns the unique ID assigned to the document by mongo (primary key.)
    """
    output = collection.insert_one({
        "distance": distance,
        "begin_date": begin_date, 
        "control_times": control_times})

    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)
