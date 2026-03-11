import streamlit as st
import random
import copy

stanze=[{"nome":"Entrata", "pos_in":["entrata"], "pos_fin":["entrata"], "peso":0, "porte":3, "colore":["blu"]},
    {"nome": "Anticamera", "pos_in":["uscita"], "pos_fin":["uscita"], "peso":0, "porte":4, "colore":["blu"]},
    {"nome":"Spare Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["blu"]},
    {"nome":"Parlor", "pos_in": ["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["blu"]},
    {"nome":"Billiard Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["blu"]},
    {"nome":"Closet", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":1, "colore":["blu"]},
    {"nome":"Storeroom", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":1, "colore":["blu"]},
    {"nome":"Nook", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["blu"]},
    {"nome":"Den", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":3, "colore":["blu"]},
    {"nome":"Pantry", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["blu"]},
    {"nome":"Drawing Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":3, "colore":["blu"]},
    {"nome":"Bedroom", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["rosa"]},
    {"nome":"Guest Bedroom", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":1, "colore":["rosa"]},
    {"nome":"Nursery", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":1, "colore":["rosa"]},
    {"nome":"Hallway", "pos_in":["ovunque"], "pos_fin":["interno"], "peso":2.94, "porte":3, "colore":["arancione"]},
    {"nome":"Corridor", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["arancione"]},
    {"nome":"Passageway", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":4, "colore":["arancione"]},
    {"nome":"Kitchen", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":2, "colore":["giallo"]},
    {"nome":"Chapel", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":2.94, "porte":3, "colore":["rosso"]},
    {"nome":"Walk-in Closet", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["blu"]},
    {"nome":"Rumpus Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["blu"]},
    {"nome":"Office", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["blu"]},
    {"nome":"The Pool", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["blu"]},
    {"nome":"Utility Closet", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["blu"]},
    {"nome":"Security", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["blu"]},
    {"nome":"Laboratory", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["blu"]},
    {"nome":"Coat Check", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["blu"]},
    {"nome":"Dining Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["blu"]},
    {"nome":"Observatory", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["blu"]},
    {"nome":"Boudoir", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["rosa"]},
    {"nome":"West Wing Hall", "pos_in":["ovunque"], "pos_fin":["lato sinistro"], "peso":1.15, "porte":3, "colore":["arancione"]},
    {"nome":"Terrace", "pos_in":["interno"], "pos_fin":["lato destro", "lato sinistro"], "peso":1.15, "porte":1, "colore":["verde"]},
    {"nome":"Patio", "pos_in":["ovunque"], "pos_fin":["lato destro", "lato sinistro"], "peso":1.15, "porte":2, "colore":["verde"]},
    {"nome":"Courtyard", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["verde"]},
    {"nome":"Greenhouse", "pos_in":["lato sinistro", "lato destro"], "pos_fin":["lato destro", "lato sinistro"], "peso":1.15, "porte":1, "colore":["verde"]},
    {"nome":"Commissary", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["giallo"]},
    {"nome":"The Armory", "pos_in":["Room 46"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["giallo", "nero"]},
    {"nome":"Lavatory", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["rosso"]},
    {"nome":"Gymnasium", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["rosso"]},
    {"nome":"Darkroom", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.15, "porte":3, "colore":["rosso"]},
    {"nome":"The Kennel", "pos_in":["STUDIO"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["blu"]},
    {"nome":"Solarium", "pos_in":["STUDIO"], "pos_fin":["interno"], "peso":1.15, "porte":1, "colore":["verde"]},
    {"nome":"Dormitory", "pos_in":["STUDIO"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["rosa"]},
    {"nome":"Planetarium", "pos_in":["OBS"], "pos_fin":["ovunque"], "peso":1.15, "porte":1, "colore":["blu"]},
    {"nome":"Tunnel", "pos_in":["BAS"], "pos_fin":["ovunque"], "peso":1.15, "porte":2, "colore":["arancione"]},
    {"nome":"Garage", "pos_in":["ovunque"], "pos_fin":["lato sinistro"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Music Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Wine Cellar", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Ballroom", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Study", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Library", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Boiler Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":3, "colore":["blu"]},
    {"nome":"Pump Room", "pos_in":["POOL"], "pos_fin":["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Workshop", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Sauna", "pos_in": ["POOL"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Mail Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Conference Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":3, "colore":["blu"]},
    {"nome":"Aquarium", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":3, "colore":["blu", "rosso", "verde", "giallo", "rosa", "arancione", "nero"]},
    {"nome":"Servant's Quarters", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["rosa"]},
    {"nome":"Bunk Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["rosa"]},
    {"nome":"East Wing Hall", "pos_in": ["ovunque"], "pos_fin": ["lato destro"], "peso":0.45, "porte":3, "colore":["arancione"]},
    {"nome":"Secret Passage", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["arancione"]},
    {"nome":"Foyer", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["arancione"]},
    {"nome":"Great Hall", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":4, "colore":["arancione"]},
    {"nome":"Cloister", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":0.45, "porte":4, "colore":["verde"]},
    {"nome":"Veranda", "pos_in": ["ovunque"], "pos_fin": ["lato destro", "lato sinistro"],"peso":0.45, "porte":2, "colore":["verde"]},
    {"nome":"Locksmith", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["giallo"]},
    {"nome":"Maid's Chamber", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["rosso", "rosa"]},
    {"nome":"Archives", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.45, "porte":4, "colore":["rosso"]},
    {"nome":"Dovecote", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Clock Tower", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":0.45, "porte":1, "colore":["blu"]},
    {"nome":"Classroom", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["blu"]},
    {"nome":"Vestibule", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":0.45, "porte":4, "colore":["arancione"]},
    {"nome":"Casino", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["giallo"]},
    {"nome":"Mechanarium", "pos_in": ["BAS"], "pos_fin": ["interno"], "peso":0.45, "porte":4, "colore":["blu"]},
    {"nome":"Treasure Trove", "pos_in": ["BAS"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["nero"]},
    {"nome":"Conservatory", "pos_in": ["TENDA"], "pos_fin": ["lato sinistro", "lato destro"], "peso":0.45, "porte":2, "colore":["verde"]},
    {"nome":"Lost & Found", "pos_in": ["BAS"], "pos_fin": ["ovunque"], "peso":0.45, "porte":2, "colore":["rosso"]},
    {"nome":"The Foundation", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":0.23, "porte":3, "colore":["blu"]},
    {"nome":"Rotunda", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":0.23, "porte":2, "colore":["blu"]},
    {"nome":"Gallery", "pos_in": ["Room 46"], "pos_fin": ["ovunque"], "peso":0.23, "porte":2, "colore":["blu"]},
    {"nome":"Room 8", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":2, "colore":["blu"]},
    {"nome":"Attic", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":1, "colore":["blu"]},
    {"nome":"Locker Room", "pos_in": ["POOL"], "pos_fin": ["ovunque"], "peso":0.23, "porte":3, "colore":["blu"]},
    {"nome":"Trophy Room", "pos_in": ["Room 46"], "pos_fin": ["ovunque"], "peso":0.23, "porte":2, "colore":["blu"]},
    {"nome":"Vault", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":1, "colore":["blu"]},
    {"nome":"Chamber of Mirrors", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":0.23, "porte":4, "colore":["blu"]},
    {"nome":"Drafting Studio", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":2, "colore":["blu"]},
    {"nome":"Freezer", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":1, "colore":["blu"]},
    {"nome":"Her Ladyship's Chamber", "pos_in": ["lato sinistro"], "pos_fin": ["lato sinistro"], "peso":0.23, "porte":1, "colore":["rosa"]},
    {"nome":"Master Bedroom", "pos_in": ["ovunque"], "pos_fin": ["lato destro"], "peso":1, "porte":0.23, "colore":["rosa"]},
    {"nome":"Morning Room","pos_in":["B&U"],"pos_fin":["lato destro","lato sinistro"],"peso":0.23,"porte":2,"colore":["verde"]},
    {"nome":"Secret Garden", "pos_in": ["ovunque"], "pos_fin": ["lato destro", "lato sinistro"], "peso":0.23, "porte":3, "colore":["verde"]},
    {"nome":"Showroom", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":2, "colore":["giallo"]},
    {"nome":"Laundry Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":1, "colore":["giallo"]},
    {"nome":"Gift Shop", "pos_in": ["Room 46"], "pos_fin": ["ovunque"], "peso":0.23, "porte":3, "colore":["giallo"]},
    {"nome":"Weight Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":4, "colore":["rosso"]},    
    {"nome":"Furnace", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":0.23, "porte":1, "colore":["rosso"]},
    {"nome":"Throne Room", "pos_in": ["BAS"], "pos_fin": ["ovunque"], "peso":0.23, "porte":3, "colore":["nero"]},
    {"nome":"Closed Exhibit","pos_in":["STU"],"pos_fin":["ovunque"],"peso":0.23,"porte":3,"colore":["rosso"]}]
stanze_l=[
    {"nome":"Walk-in Closet", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":1, "colore":["blu"]},
    {"nome":"Rumpus Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["blu"]},
    {"nome":"Office", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["blu"]},
    {"nome":"The Pool", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":3, "colore":["blu"]},
    {"nome":"Utility Closet", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":1, "colore":["blu"]},
    {"nome":"Security", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":3, "colore":["blu"]},
    {"nome":"Laboratory", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["blu"]},
    {"nome":"Coat Check", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":1, "colore":["blu"]},
    {"nome":"Dining Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":3, "colore":["blu"]},
    {"nome":"Observatory", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["blu"]},
    {"nome":"West Wing Hall", "pos_in":["ovunque"], "pos_fin":["lato sinistro"], "peso":0.05, "porte":3, "colore":["arancione"]},
    {"nome":"Terrace", "pos_in":["ovunque"], "pos_fin":["lato destro", "lato sinistro"], "peso":0.05, "porte":1, "colore":["verde"]},
    {"nome":"Patio", "pos_in":["ovunque"], "pos_fin":["lato destro", "lato sinistro"], "peso":0.05, "porte":2, "colore":["verde"]},
    {"nome":"Greenhouse", "pos_in":["lato sinistro", "lato destro"], "pos_fin":["lato destro", "lato sinistro"], "peso":0.05, "porte":1, "colore":["verde"]},
    {"nome":"Commissary", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["giallo"]},
    {"nome":"The Armory", "pos_in":["Room 46"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["giallo", "nero"]},
    {"nome":"The Kennel", "pos_in":["STUDIO"], "pos_fin":["ovunque"], "peso":0.05, "porte":2, "colore":["blu"]},
    {"nome":"Solarium", "pos_in":["STUDIO"], "pos_fin":["interno"], "peso":0.05, "porte":1, "colore":["verde"]},
    {"nome":"Dormitory", "pos_in":["STUDIO"], "pos_fin":["ovunque"], "peso":0.05, "porte":1, "colore":["rosa"]},
    {"nome":"Planetarium", "pos_in":["OBS"], "pos_fin":["ovunque"], "peso":0.05, "porte":1, "colore":["blu"]},
    {"nome":"Garage", "pos_in":["ovunque"], "pos_fin":["lato sinistro"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Wine Cellar", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Study", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Boiler Room", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.92, "porte":3, "colore":["blu"]},
    {"nome":"Pump Room", "pos_in":["POOL"], "pos_fin":["ovunque"], "peso":1.92, "porte":2, "colore":["blu"]},
    {"nome":"Workshop", "pos_in":["ovunque"], "pos_fin":["ovunque"], "peso":1.92, "porte":2, "colore":["blu"]},
    {"nome":"Sauna", "pos_in": ["POOL"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Mail Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Conference Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":3, "colore":["blu"]},
    {"nome":"Aquarium", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":3, "colore":["blu", "rosso", "verde", "giallo", "rosa", "arancione", "nero"]},
    {"nome":"Servant's Quarters", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["rosa"]},
    {"nome":"Bunk Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["rosa"]},
    {"nome":"East Wing Hall", "pos_in": ["ovunque"], "pos_fin": ["lato destro"], "peso":1.92, "porte":3, "colore":["arancione"]},
    {"nome":"Secret Passage", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["arancione"]},
    {"nome":"Great Hall", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":4, "colore":["arancione"]},
    {"nome":"Veranda", "pos_in": ["ovunque"], "pos_fin": ["lato destro", "lato sinistro"],"peso":1.92, "porte":2, "colore":["verde"]},
    {"nome":"Locksmith", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["giallo"]},
    {"nome":"Archives", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":1.92, "porte":4, "colore":["rosso"]},
    {"nome":"Dovecote", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":1.92, "porte":2, "colore":["blu"]},
    {"nome":"Clock Tower", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":1.92, "porte":1, "colore":["blu"]},
    {"nome":"Classroom", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":1.92, "porte":2, "colore":["blu"]},
    {"nome":"Vestibule", "pos_in": ["STUDIO"], "pos_fin": ["ovunque"], "peso":1.92, "porte":4, "colore":["arancione"]},
    {"nome":"Mechanarium", "pos_in": ["BAS"], "pos_fin": ["interno"], "peso":1.92, "porte":4, "colore":["blu"]},
    {"nome":"Treasure Trove", "pos_in": ["BAS"], "pos_fin": ["ovunque"], "peso":1.92, "porte":2, "colore":["nero"]},
    {"nome":"Conservatory", "pos_in": ["TENDA"], "pos_fin": ["lato sinistro", "lato destro"], "peso":1.92, "porte":2, "colore":["verde"]},
    {"nome":"Lost & Found", "pos_in": ["BAS"], "pos_fin": ["ovunque"], "peso":1.92, "porte":2, "colore":["rosso"]},
    {"nome":"The Foundation", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":3.85, "porte":3, "colore":["blu"]},
    {"nome":"Rotunda", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":3.85, "porte":2, "colore":["blu"]},
    {"nome":"Gallery", "pos_in": ["Room 46"], "pos_fin": ["ovunque"], "peso":3.85, "porte":2, "colore":["blu"]},
    {"nome":"Locker Room", "pos_in": ["POOL"], "pos_fin": ["ovunque"], "peso":3.85, "porte":3, "colore":["blu"]},
    {"nome":"Chamber of Mirrors", "pos_in": ["ovunque"], "pos_fin": ["interno"], "peso":3.85, "porte":4, "colore":["blu"]},
    {"nome":"Freezer", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":3.85, "porte":1, "colore":["blu"]},
    {"nome":"Her Ladyship's Chamber", "pos_in": ["lato sinistro"], "pos_fin": ["lato sinistro"], "peso":3.85, "porte":1, "colore":["rosa"]},
    {"nome":"Morning Room", "pos_in": ["B&U"], "pos_fin": ["lato destro", "lato sinistro"], "peso":3.85, "porte":2, "colore":["verde"]},
    {"nome":"Laundry Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":3.85, "porte":1, "colore":["giallo"]},
    {"nome":"Bookshop", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":3.85, "porte":2, "colore":["giallo"]},
    {"nome":"Gift Shop", "pos_in": ["Room 46"], "pos_fin": ["ovunque"], "peso":3.85, "porte":3, "colore":["giallo"]},
    {"nome":"Weight Room", "pos_in": ["ovunque"], "pos_fin": ["ovunque"], "peso":3.85, "porte":4, "colore":["rosso"]},    
    {"nome":"Closed Exhibit", "pos_in": ["STU"], "pos_fin": ["ovunque"], "peso":3.85, "porte":3, "colore":["rosso"]}]
stanze_esterne=[{"nome":"Toolshed", "peso":1, "colore":["blu"]}, {"nome":"Shelter", "peso":1, "colore":["blu"]},
    {"nome":"Schoolhouse", "peso":1, "colore":["blu"]}, {"nome":"Shrine", "peso":1, "colore":["blu"]},
    {"nome":"Root Cellar", "peso":1, "colore":["verde"]}, {"nome":"Hovel", "peso":1, "colore":["rosa"]},
    {"nome":"Trading Post", "peso":1, "colore":["giallo"]}, {"nome":"Tomb", "peso":1, "colore":["nero"]}]
stanze_specchi_sinistro=["Spare Room", "Den", "Pantry", "Workshop", "Boudoir", "West Wing Hall", "East Wing Hall", "Gymnasium"]
stanze_specchi_destro=["Parlor", "Billiard Room", "Closet", "Storeroom", "Wine Cellar", "Observatory", "Aquarium", "Passageway"]
aggiunte_specchi=["Spare Room", "Parlor", "Billiard Room", "Closet", "Storeroom", "Nook", "Den", "Pantry", "Bedroom", "Guest Bedroom", "Patio",
    "Nursery", "Hallway", "Corridor", "Passageway", "Walk-in Closet", "Rumpus Room", "Observatory", "West Wing Hall", "Terrace", "Vault",
    "Courtyard", "Lavatory", "Solarium", "Music Room", "Ballroom", "Bunk Room", "East Wing Hall", "Foyer", "Cloister", "Veranda", "Attic",
    "Maid's Chamber", "Archives", "Rotunda" , "Trophy Room" , "Her Ladyship's Chamber", "Master Bedroom", "Morning Room", "Weight Room"]
modifiche_cons= ["The Foundation", "Gallery", "Room 8", "Garage", "Locker Room", "Sauna", "Veranda", "Morning Room", "Secret Garden",
                 "Bookshop", "The Armory", "Classroom", "Conservatory", "Pump Room", "Dovecote", "Freezer", "Stanze esterne"]
def algoritmo_gioco():
    stanze_run=stanze[:]
    stanze_library=stanze_l[:]
    stanze_specchi_dx=stanze_specchi_destro[:]
    stanze_specchi_sx=stanze_specchi_sinistro[:]
    doppioni=aggiunte_specchi[:]
    mod_cons=modifiche_cons[:]
    stanze_est=stanze_esterne[:]
    stanze_usate=[{"nome":"Entrata"}, {"nome": "Anticamera"}]
    stanze_trovate=[]
    camb=[]
    obiettivo="no"
    benedizione="nessuna"
    col="blu"
    d=1
    sta=0
    b=0
    h=0
    p=0
    o=0
    pa=0
    cl=0
    n=0
    g=0
    db=0
    while True:
        add=[]
        duplicati=[]
        stanze_run_cloi_agg=[]
        passi="si"
        q="no"
        a=0
        dx=0
        sx=0
        u=0
        pacco="no"
        while passi=="si":
            if stanze_run_cloi_agg!=[]:
                stanze_run=stanze_run_cloi_agg
                stanze_run_cloi_agg=[]
                if scelta in stanze_run:
                    stanze_run.remove(scelta)
            disegni=st.radio("Devi aggiungere dal DS?", ["si", "no"], index=None, key="disegni")
            duplica=st.radio("Devi duplicare dalla CM?", ["si", "no"], index=None, key="duplica")
            if disegni=="si":
                if a==0:
                    lista=[]
                    for stanza in stanze_run:
                        if stanza["pos_in"]==["STUDIO"]:
                            lista.append(stanza)
                    for i in range(1, 4):
                        pesi=[d["peso"] for d in lista]
                        s=random.choices(lista, weights=pesi, k=1)[0]
                        add.append(s)
                        lista.remove(s)
                        st.write(s["nome"])
                    a=1
                else:
                    for i in add:
                        st.write(i["nome"])
                q=st.radio("Vuoi aggiungere?", ["si", "no"], index=None, key="q")
                if q=="si":
                    agg=st.radio("Quale stanza vuoi aggiungere?", add["nome"], index=None, key="agg")
                    for stanza in stanze_run:
                        if stanza["nome"]==agg:
                            if agg=="Dovecote":
                                stanza["pos_in"]=["interno"]
                            else:
                                stanza["pos_in"]=["ovunque"]
                    for stanza in stanze_library:
                        if stanza["nome"]==agg:
                            if agg=="Dovecote":
                                stanza["pos_in"]=["interno"]
                                break
                            else:
                                stanza["pos_in"]=["ovunque"]
                                break
                    add=[s for s in add if s["nome"]==agg]
                continue
            if duplica=="si":
                angolo=input("Angolo destro o sinistro?") # Le risposte ammissibili sono "dx" o "sx"
                if angolo=="dx":
                    if dx==0:
                        lista=[]
                        for nome in stanze_specchi_dx:
                            originale=next((s for s in stanze_run if s["nome"]==nome), None)
                            if originale is None:
                                originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                            if originale:
                                lista.append(copy.deepcopy(originale))
                        pesi=[s["peso"] for s in lista]
                        estratto_dx=random.choices(lista, weights=pesi, k=1)[0]
                        st.write(estratto_dx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_dx)
                            stanze_run.append(estratto_dx)
                            stanze_specchi_dx.remove(estratto_dx["nome"])
                            if any(d["nome"]==estratto_dx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                        dx=1
                    else:
                        st.write(estratto_dx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_dx)
                            stanze_run.append(estratto_dx)
                            stanze_specchi_dx.remove(estratto_dx["nome"])
                            if any(d["nome"]==estratto_dx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                if angolo=="sx": 
                    if sx==0:
                        lista=[]
                        for nome in stanze_specchi_sx:
                            originale=next((s for s in stanze_run if s["nome"]==nome), None)
                            if originale is None:
                                originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                            if originale:
                                lista.append(copy.deepcopy(originale))
                        pesi=[s["peso"] for s in lista]
                        estratto_sx=random.choices(lista, weights=pesi, k=1)[0]
                        st.write(estratto_sx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_sx)
                            stanze_run.append(estratto_sx)
                            stanze_specchi_sx.remove(estratto_sx["nome"])
                            if any(d["nome"]==estratto_sx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                        sx=1
                    else:
                        st.write(estratto_sx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_sx)
                            stanze_run.append(estratto_sx)
                            stanze_specchi_sx.remove(estratto_sx["nome"])
                            if any(d["nome"]==estratto_sx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                continue
            B_U=input("Hai mangiato bacon e uova?") # Le risposte ammissibili sono "si" o "no"
            if B_U=="si":
                if b==0:
                    for stanza in stanze_run:
                        if stanza["nome"]=="Morning Room":
                            stanza["pos_in"]=["interno"]
                    for stanza in stanze_library:
                        if stanza["nome"]=="Morning Room":
                            stanza["pos_in"]=["interno"]
                    b=1
                else:
                    originale=next((s for s in stanze_run if s["nome"]=="Morning Room"), None)
                    originale_l=next(s for s in stanze_library if s["nome"]=="Morning Room")
                    if originale is None:
                        originale=next((s for s in stanze_usate if s["nome"]=="Morning Room"), None)
                    if originale:
                        duplicato=copy.deepcopy(originale)
                        stanze_run.append(duplicato)
                    if originale_l:
                        duplicato_l=copy.deepcopy(originale_l)
                        stanze_library.append(duplicato_l)
                continue
            aggi=input("Hai aggiornato?") # Le risposte ammissibili sono "si" o "no"
            if aggi=="si":
                aggiornamento=input("Quale stanza?") # Le risposte ammissibili sono "Spare Room", "Parlor", "Billiard Room", "Corridor", "Closet", "Nursery"
                if aggiornamento=="Spare Room":
                    nomi_mappa = {"rosa": "Spare Bedroom", "verde": "Spare Greenroom", "arancione": "Spare Hall"}
                    o=1
                    col=input("Che colore?") # Le risposte ammissibili sono "rosa", "verde", "arancione"
                    nuovo_nome=nomi_mappa.get(col)
                    originale=next((s for s in stanze_run if s["nome"]=="Spare Room"), None)
                    if originale: originale["colore"]=[col]
                    if col=="rosa": originale["nome"]="Spare Bedroom"
                    elif col=="verde": originale["nome"]="Spare Greenroom"
                    elif col=="arancione": originale["nome"]="Spare Hall"
                    if nuovo_nome:
                        if "Spare Room" in stanze_specchi_sx:
                            idx=stanze_specchi_sx.index("Spare Room")
                            stanze_specchi_sx[idx]=nuovo_nome
                        if "Spare Room" in doppioni:
                            idx=doppioni.index("Spare Room")
                            doppioni[idx]=nuovo_nome
                elif aggiornamento=="Parlor":
                    pa=1
                    originale=next((s for s in stanze_run if s["nome"]=="Parlor"), None)
                    if originale:
                        originale["colore"]=["rosso"]
                        originale["nome"]="Funeral Parlor"
                    if "Parlor" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Parlor")
                        stanze_specchi_dx[index]="Funeral Parlor"
                    if "Parlor" in doppioni:
                        index=doppioni.index("Parlor")
                        doppioni[index]="Funeral Parlor"
                elif aggiornamento=="Billiard Room":
                    p=1
                    target=["Foyer", "Great Hall", "Secret Passage"]
                    for nome in target:
                        originale=next((s for s in stanze_run if s["nome"]==nome), None)
                        if originale is None:
                            originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                        if originale:
                            duplicato=copy.deepcopy(originale)
                            stanze_run.append(duplicato)
                    originale=next((s for s in stanze_run if s["nome"]=="Billiard Room"), None)
                    if originale:
                        originale["colore"]=["arancione"]
                        originale["nome"]="Pool Hall"
                    if "Billiard Room" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Billiard Room")
                        stanze_specchi_dx[index]="Pool Hall"
                    if "Billiard Room" in doppioni:
                        index=doppioni.index("Billiard Room")
                        doppioni[index]="Pool Hall"
                elif aggiornamento=="Corridor":
                    h=1
                    originale=next((s for s in stanze_run if s["nome"]=="Hallway"), None)
                    if originale is None:
                        originale=next((s for s in stanze_usate if s["nome"]=="Hallway"), None)
                        if originale:
                            duplicato=copy.deepcopy(originale)
                            stanze_run.append(duplicato)
                elif aggiornamento=="Closet":
                    cl=1
                    originale=next((s for s in stanze_run if s["nome"]=="Closet"), None)
                    if originale:
                        originale["colore"]=["rosso"]
                        originale["nome"]="Empty Closet"
                    if "Closet" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Closet")
                        stanze_specchi_dx[index]="Empty Closet"
                    if "Closet" in doppioni:
                        index=doppioni.index("Closet")
                        doppioni[index]="Empty Closet"
                elif aggiornamento=="Nursery":
                    n=1
                    originale=next((s for s in stanze_run if s["nome"]=="Nursery"), None)
                    if originale:
                        originale["colore"]=["verde"]
                        originale["nome"]="Indoor Nursery"
                    if "Nursery" in doppioni:
                        index=doppioni.index("Closet")
                        doppioni[index]="Indoor Nursery"
                continue
            trov=input("Hai trovato una planimetria?") # Le risposte ammissibili sono "si" o "no"
            if trov=="si":
                name=input("Quale planimetria aggiungi?") # Le risposte ammissibili sono "Planetarium", "Mechanarium", "Throne Room", "Treasure Trove", "Tunnel", "Conservatory", "Lost & Found", "Closed Exhibit" 
                target=next((s for s in stanze_run if s["nome"]==name), None)
                target_l=next((sl for sl in stanze_library if sl["nome"]==name), None)
                if target: target["pos_in"]=["ovunque"]
                if target_l: target_l["pos_in"]=["ovunque"]
                stanze_trovate.append(target["nome"])
                continue
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro", "HLC", "RN", "Library", "CloAgg", "Tunnel", "esterno"
            arrivo=input("Dove vuoi andare?") # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro", "esterno"
            if partenza=="esterno" and arrivo=="esterno":
                scelta, benedizione, g, db=genera_stanze_esterne_e_scegli(stanze_est, stanze_run, stanze_usate, benedizione, d, g, db)
            else:
                if partenza=="CloAgg":
                    stanze_run_cloi_agg=stanze_run[:]
                    partenza=="interno"
                    agg_clo=input("Quale?") # Le risposte ammissibili sono "Rynna" o "Draxus"
                    if agg_clo=="Rynna":
                        [stanza.update({"peso": 1.15}) for stanza in stanze_run if "verde" in stanza["colore"]]
                    elif agg_clo=="Draxus":
                        stanze_run=[s for s in stanze_run if s["porte"] in (1, 2)]
                grado=int(input("In quale grado vuoi andare?")) # Le parole ammissibili sono 1, 2, 3, 4, 5, 6, 7, 8, 9
                chiave=key(grado, arrivo)
                if chiave=="esci":
                    continue
                opzioni, sta=terna(d, sta, partenza, arrivo, grado, chiave, stanze_run, stanze_library, stanze_usate)
                scelta, pacco=scegliere(opzioni, stanze_run, stanze_library, stanze_usate, doppioni, mod_cons, camb, pacco)
            passi=input("Hai dei passi disponibili?") # Le risposte ammissibili sono "si" o "no"
            if passi=="no":
                d+=1
                obiettivo=input("Hai sbloccato la Room 46?") # Le risposte ammissibili sono "si" o "no"
        reset(stanze_run, stanze_library, stanze_usate, stanze_trovate, h, p, d, g, db, u, q, o, pa, cl, n, col, add, dx, sx, duplicati, obiettivo, camb, stanze_specchi_sx, stanze_specchi_dx, doppioni, pacco, benedizione, stanze_est)
def reset(stanze_run, stanze_library, stanze_usate, stanze_trovate, h, p, d, g, db, u, q, o, pa, cl, n, col, add, dx, sx, duplicati, obiettivo, camb, stanze_specchi_sx, stanze_specchi_dx, doppioni, pacco, benedizione, stanze_est):
    stanze_trovabili=["Planetarium", "Mechanarium", "Throne Room", "Treasure Trove", "Tunnel", "Conservatory", "Lost & Found", "Closed Exhibit"]
    for stanza in stanze_run:
        if stanza["nome"]=="Morning Room" and stanza["pos_in"]=="interno":
            u+=1
    stanze_run=stanze[:]
    stanze_library=stanze_l[:]
    stanze_usate_due=[]
    if any(stanza["nome"]=="Freezer" for stanza in stanze_usate):
        stanza_da_togliere=next(s for s in stanze_run if s["nome"]=="Freezer")
        stanze_run.remove(stanza_da_togliere)
    if any(stanza["nome"]=="The Foundation" for stanza in stanze_usate):
        stanza_da_togliere=next(s for s in stanze_run if s["nome"]=="The Foundation")
        stanze_run.remove(stanza_da_togliere)
        stanze_usate_due.append(stanza_da_togliere)
    if any(stanza["nome"]=="The Pool" for stanza in stanze_usate):
        for stanza in stanze_run:
            if stanza["pos_in"]=="POOL":
                stanza["pos_in"]="ovunque"
    if g!=0 and d<=db:
        if benedizione=="Giardiniere":
            giardino=next(s for s in stanze_run if s["nome"]=="Courtyard")
            for _ in range(8):
                stanze_run.append(giardino)
        if benedizione=="Monaco":
            morte=input("In quale stanza hai terminato i passi?") # Le risposte ammissibili sono tutte le stanze in stanze_usate
            stanza_da_togliere=next(s for s in stanze_run if s["nome"]==morte)
            stanze_run.remove(stanza_da_togliere)
            stanze_est.append(stanza_da_togliere)
            stanza_da_togliere=next((s for s in stanze_library if s["nome"]==morte), None)
            if stanza_da_togliere: stanze_library.remove(stanza_da_togliere)
    stanze_usate=stanze_usate_due
    if q=="si" and add:
        for stanza in stanze_run:
            if stanza["nome"]==add[0]["nome"]:
                if stanza["nome"]=="Dovecote": stanza["pos_in"]==["interno"]
                else: stanza["pos_in"]==["ovunque"]
        for stanza in stanze_library:
            if stanza["nome"]==add[0]["nome"]:
                if stanza["nome"]=="Dovecote": stanza["pos_in"]==["interno"]
                else: stanza["pos_in"]==["ovunque"]
    if dx==1 or sx==1:
        for i in duplicati:
            if any(d["nome"]==i["nome"] for d in stanze_run):
                stanze_run.append(d)
            if any(d["nome"]==i["nome"] for d in stanze_library):
                stanze_library.append(d)
    if u!=0:
        stanze_run.remove({"nome":"Morning Room","pos_in":["B&U"],"pos_fin":["lato destro","lato sinistro"],"peso":0.23,"porte":2,"colore":["verde"]})
        stanze_library.remove({"nome":"Morning Room","pos_in":["B&U"],"pos_fin":["lato destro","lato sinistro"],"peso":3.85,"porte":2,"colore":["verde"]})
        for _ in range (u):
            stanze_run.append({"nome":"Morning Room","pos_in":["interno"],"pos_fin":["lato destro","lato sinistro"],"peso":0.23,"porte":2,"colore":["verde"]})
            stanze_library.append({"nome":"Morning Room","pos_in":["interno"],"pos_fin":["lato destro","lato sinistro"],"peso":3.85,"porte":2,"colore":["verde"]})
        b=1
    else: b=0
    for stanza in stanze_trovabili:
        if stanza in stanze_trovate:
            if any(room["nome"]==stanza for room in stanze_run):
                room["pos_in"]=["ovunque"]
            if any(room_l["nome"]==stanza for room_l in stanze_library):
                room_l["pos_in"]=["ovunque"]
    if h==1:
        stanze_run.append({"nome":"Hallway","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":2.94,"porte":3,"colore":["arancione"]})
    if p==1:
        stanze_run.append({"nome":"Secret Passage","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":1,"colore":["arancione"]})
        stanze_run.append({"nome":"Foyer","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":2,"colore":["arancione"]})
        stanze_run.append({"nome":"Great Hall","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":4,"colore":["arancione"]})      
        originale=next(s for s in stanze_run if s["nome"]=="Billiard Room")
        originale["colore"]=["rosso"]
        originale["nome"]="Pool Hall"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Billiard Room")
        originale["nome"]="Pool Hall"
        originale=next(s for s in doppioni if s["nome"]=="Billiard Room")
        originale["nome"]="Pool Hall"    
    if o==1:
        originale=next((s for s in stanze_run if s["nome"]=="Spare Room"), None)
        originale["colore"]=[col]
        if col=="rosa": originale["nome"]="Spare Bedroom"
        elif col=="verde": originale["nome"]="Spare Greenroom"
        elif col=="arancione": originale["nome"]="Spare Hall"
        originale=next((s for s in stanze_specchi_sx if s["nome"]=="Spare Room"), None)
        if originale:
            if col=="rosa": originale["nome"]="Spare Bedroom"
            elif col=="verde": originale["nome"]="Spare Greenroom"
            elif col=="arancione": originale["nome"]="Spare Hall"
        originale=next((s for s in doppioni if s["nome"]=="Spare Room"), None)
        if originale:
            if col=="rosa": originale["nome"]="Spare Bedroom"
            elif col=="verde": originale["nome"]="Spare Greenroom"
            elif col=="arancione": originale["nome"]="Spare Hall"
    if pa==1:
        originale=next(s for s in stanze_run if s["nome"]=="Parlor")
        originale["colore"]=["rosso"]
        originale["nome"]="Funeral Parlor"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Parlor")
        originale["nome"]="Funeral Parlor"
        originale=next(s for s in doppioni if s["nome"]=="Parlor")
        originale["nome"]="Funeral Parlor"
    if cl==1:
        originale=next(s for s in stanze_run if s["nome"]=="Closet")
        originale["colore"]=["rosso"]
        originale["nome"]="Empty Closet"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Closet")
        originale["nome"]="Empty Closet"
        originale=next(s for s in doppioni if s["nome"]=="Closet")
        originale["nome"]="Empty Closet"
    if n==1:
        originale=next(s for s in stanze_run if s["nome"]=="Nursery")
        originale["colore"]=["verde"]
        originale["nome"]="Indoor Nursery"
        originale=next(s for s in doppioni if s["nome"]=="Nursery")
        originale["nome"]="Indoor Nursery"
    if camb!=[]:
        mappa_cambiamenti = {s["nome"]: s["peso"] for s in camb}
        for stanza in stanze_run:
            nome=stanza["nome"]
            if nome in mappa_cambiamenti:
                stanza["peso"]=mappa_cambiamenti[nome]
    if obiettivo=="si":
        for stanza in stanze_run:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
        for stanza in stanze_library:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
    elif d>=46:
        for stanza in stanze_run:
            if stanza["nome"]=="Gallery": stanza["pos_in"]=["ovunque"]
        for stanza in stanze_library:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
    if pacco=="si":
        stanza=next(s for s in stanze_run if s["nome"]=="Mail Room")
        stanza["peso"]=2.94
        stanza=next(s for s in stanze_library if s["nome"]=="Mail Room")
        stanza["peso"]=0.05
def terna(d, sta, partenza, arrivo, grado, chiave, stanze_run, stanze_library, stanze_usate):
    if d==1 and sta==0:
        opzioni=[{"nome":"Bedroom"}, {"nome":"Closet"}, {"nome":"Hallway"}]
        for stanza in opzioni: st.write(stanza["nome"])
        return opzioni, 1
    else:
        if partenza=="HLC":
            targets={"Boudoir", "Walk-in Closet"}
            for s in stanze_run:
                if s["nome"] in targets: s["peso"]=2.94
            opzioni=genera_stanze("lato sinistro", arrivo, grado, chiave, stanze_run, stanze_usate)
            for stanza in opzioni: st.write(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze("lato sinistro", arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: st.write(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
            for stanza in stanze_run:
                if stanza["nome"]=="Boudoir" or stanza["nome"]=="Walk-in Closet": stanza["peso"]=1.15
        elif partenza=="RN":
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            if not any(d["nome"]=="Library" for d in opzioni):
                opzioni[2]={"nome":"Library"}
                if not any(d["nome"]=="Library" for d in stanze_usate): stanze_usate.append({"nome":"Library"})
            for stanza in opzioni: st.write(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                if not any(d["nome"]=="Library" for d in opzioni):
                    opzioni[2]={"nome":"Library"}
                for stanza in opzioni: st.write(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        elif partenza=="Library" and (chiave=="chiave" or chiave=="nessuna"):
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze_library(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
            for stanza in opzioni: st.write(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze_library(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
                for stanza in opzioni: st.write(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        elif partenza=="Tunnel":
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            opzioni[0]={"nome":"Tunnel"}
            for stanza in opzioni: st.write(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: st.write(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"    
        else:
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            for stanza in opzioni: st.write(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: st.write(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        return opzioni, 1
def scegliere (opzioni, stanze_run, stanze_library, stanze_usate, doppioni, mod_cons, camb, pacco):
    scelta=input("Quale stanza scegli?") # Le opzioni saranno i tre nomi delle stanze in opzioni
    stanza_scelta=next(s for s in opzioni if s["nome"]==scelta)
    dizionario_run_scelto=next((d for d in stanze_run if d["nome"]==stanza_scelta["nome"]), None)
    if dizionario_run_scelto==None: dizionario_run_scelto=next((d for d in stanze_usate if d["nome"]==stanza_scelta["nome"]), None)
    else:
        stanze_run.remove(dizionario_run_scelto)
        stanze_usate.append(dizionario_run_scelto)
    if scelta=="The Pool":
        for stanza in stanze_run + stanze_library:
            if stanza.get("pos_in")==["POOL"]: stanza["pos_in"]="ovunque"
    elif scelta=="Chamber of Mirrors":
        nuovi_doppioni=[]
        nuovi_doppioni_l=[]
        for stanza in stanze_run + stanze_usate:
            if stanza["nome"] in doppioni:
                duplicati=copy.deepcopy(stanza)
                nuovi_doppioni.append(duplicati)
        stanze_run.extend(nuovi_doppioni)
        for stanza in stanze_library:
            if stanza.get("nome") in doppioni:
                duplicati_l=copy.deepcopy(stanza)
                nuovi_doppioni_l.append(duplicato)
        stanze_library.extended(nuovi_doppioni_l)
    elif scelta=="Greenhouse":
        for s in stanze_run:
            if s["nome"]=="Secret Passage" or "verde" in s.get("colore", []): s["peso"]=1.15
    elif scelta=="Furnace":
        for s in stanze_run:
            if "rosso" in s.get("colore", []): s["peso"]=1.15
    elif scelta=="Solarium":
        for stanza in stanze_run:
            if stanza["peso"]==2.94: stanza["peso"]=0.23
            elif stanza["peso"]==1.15: stanza["peso"]=0.45
            elif stanza["peso"]==0.45: stanza["peso"]=1.15
            elif stanza["peso"]==0.23: stanza["peso"]=2.94
    elif scelta=="Conservatory":
        possibili=[]
        for stanza in stanze_run:
            if not stanza["nome"] in mod_cons:
                possibili.append(stanza)
        draft=random.sample(possibili, k=3)
        camb=[{"nome": s["nome"], "rarità": converti(s["peso"])} for s in draft]
        mod="si"
        while mod=="si":
            for elemento in camb:
                st.write(elemento["nome"], elemento["rarità"])
            sta=input("Quale stanza vuoi cambiare?") # Le risposte ammissibili sono i nomi degli elementi in nuova_lista
            pes=input("Quale rarità scegli?") # Le risposte ammissibili sono "comune", "standard", "insolito", "raro"
            for elemento in camb:
                if elemento["nome"]==sta:
                    elemento["rarità"]=pes
            nuovo_peso=converti(pes)
            for stanza in stanze_run:
                if stanza["nome"]==sta:
                    stanza["peso"]=nuovo_peso
            mod=input("Vuoi modificare altro?") # Le risposte ammissibili sono "si" o "no"
    elif scelta=="Mail Room":
        pacco=input("Hai spedito un pacco?")
    return dizionario_run_scelto, pacco
def genera_stanze_esterne_e_scegli(stanze_est, stanze_run, stanze_usate, benedizione, d, g, db):
    speciale=next((s for s in stanze_est if s["peso"] != 1), None)
    if speciale:
        speciale["peso"]=1
    opzioni=random.sample(stanze_est, 3)
    if speciale and speciale not in opzioni:
        opzioni[2]=speciale
    for s in opzioni: st.write(s["nome"])
    dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
    while dadi=="si":
        lista=[]
        for s in opzioni:
            stanze_est.remove(s)
            lista.append(s)
        opzioni=random.sample(stanze_est, 3)
        for s in lista: stanze_est.append(s)
        for s in opzioni: st.write(s["nome"])
        dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
    scelta=input("Quale stanza scegli?") # Le risposte ammissibili sono i nomi delle stanze in opzioni
    if scelta=="Schoolhouse":
        aula=next((s for s in stanze_run if s["nome"]=="Classroom"), None)
        if aula==None: aula=next((s for s in stanze_usate if s["nome"]=="Classroom"), None)
        for _ in range(8):
            stanze_run.append(aula)
    if scelta=="Shrine":
        benedizione=input("Quale benedizione?") # Le risposte ammissibili sono "Ballerino", "High Roller", "Giardiniere", "Generale", "Chef", "Monaco", "Raccoglitore di bacche", "nessuna"
        if benedizione!="nessuna":
            g=int(input("Per quanti giorni?")) # Le risposte ammissibili sono 3, 4, 5, 6, 7
            db=d+g-1
            if benedizione=="Giardiniere":
                giardino=next((s for s in stanze_run if s["nome"]=="Courtyard"), None)
                if giardino==None: giardino=next((s for s in stanze_usate if s["nome"]=="Courtyard"), None)
                for _ in range(8):
                    stanze_run.append(giardino)
    stanza_scelta=next(s for s in opzioni if s["nome"]==scelta)
    stanze_usate.append(stanza_scelta)
    return stanza_scelta, benedizione, g, db
def filtra_stanze (i_pos, f_pos, grado, chiave, stanze_run, stanze_usate):
    if i_pos=="Library":
        i_pos=input("Dove ti trovi?") # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
    stanze_valide=[s for s in stanze_run if (s["pos_in"] == ["ovunque"] or i_pos in s["pos_in"]) and (s["pos_fin"] == ["ovunque"] or f_pos in s["pos_fin"])]
    target=["The Foundation", "Garage", "Boiler Room", "Sauna", "West Wing Hall", "East Wing Hall", "Secret Passage", "Greenhouse", "Morning Room", "Dormitory", "Throne Room"]
    if grado==1 or grado==9: stanze_valide=[s for s in stanze_valide if s.get("nome") not in target]
    else:
        stanze_valide=[s for s in stanze_valide if s.get("nome")!="Conservatory"]
        if grado==2 or grado==3: stanze_valide=[s for s in stanze_valide if (s.get("nome")!="The Foundation" and s.get("nome")!="Garage")]
    if chiave=="Chiave d'argento":
        stanze_valide=[s for s in stanze_valide if s.get("porte") in [3, 4] and s.get("nome") != "The Foundation"]
    if chiave=="Chiave prismatica":
        colore=input("La stanza dove ti trovi che colore è?") # Le risposte sono "verde", "arancione", "rosa", "rosso", "giallo", "altro"
        if colore!="altro":
            da_escludere=["Secret Passage", "Tunnel"] if colore=="arancione" else []
            stanze_valide=[s for s in stanze_valide if colore in s.get("colore", []) and s.get("nome") not in da_escludere]
    return(stanze_valide)
def estraz_stanze(stanze_valide, grado, chiave):
    if chiave=="Chiave 8":
        risultato=[{"nome":"Room 8","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.23,"porte":2,"colore":["blu"]}]
    elif chiave=="Chiave del giardino segreto":
        risultato=[{"nome":"Secret Garden","pos_in":["ovunque"],"pos_fin":["lato destro", "lato sinistro"],"peso":0.23,"porte":3,"colore":["verde"]}]
    else:
        weights_temp=[]
        for stanza in stanze_valide:
            peso=stanza["peso"]
            if grado in [1, 2, 3] and peso==4:
                peso *= 10
            elif grado in [4, 5] and peso==3:
                peso *= 10
            elif grado in [6, 7] and peso==2:
                peso *= 10
            elif grado in [8, 9] and peso==1:
                peso *= 10
            weights_temp.append(peso)
        stanze_temp=stanze_valide.copy()
        risultato=[]
        for _ in range(min(3, len(stanze_temp))):
            scelta=random.choices(stanze_temp, weights=weights_temp, k=1)[0]
            index=stanze_temp.index(scelta)
            risultato.append(scelta)
            stanze_temp.pop(index)
            weights_temp.pop(index)
    return risultato
def key(grado, arrivo):
    if (grado==4 or grado==5 and random.random()<=1/3) or (grado==6 or grado==7 and random.random()<=2/3) or (grado==8 or grado==9):
        chiave=input("La porta è bloccata!") # Le risposte ammissibili sono: "chiave", "chiave speciale", "esci".
        if chiave=="chiave speciale":
            if grado==8:
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave d'argento", "Chiave 8", "Chiave prismatica".
            elif (grado==4 or grado==5 or grado==6 or grado==7) and (arrivo=="lato sinistro" or arrivo=="lato destro"):
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave del giardino segreto", "Chiave d'argento", "Chiave prismatica".
            else:
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave d'argento", "Chiave prismatica".
    else: chiave="nessuna"
    return chiave
def genera_stanze_library (partenza, arrivo, grado, chiave, stanze_library, stanze_usate):
    stanze_valide=filtra_stanze(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
    opzioni=[]
    for i in range(1, 4):
        pesi = [d["peso"] for d in stanze_valide]
        s=random.choices(stanze_valide, weights=pesi, k=1)[0]
        opzioni.append(s)
        stanze_valide.remove(s)
    return opzioni
def converti(valore):
    TABELLA_RARITA = {2.94: "comune", 1.15: "standard", 0.45: "insolito", 0.23: "raro"}
    TABELLA_INVERSA = {valore: chiave for chiave, valore in TABELLA_RARITA.items()}
    if isinstance(valore, (int, float)):
        return TABELLA_RARITA.get(valore, "sconosciuto")
    elif isinstance(valore, str):
        return TABELLA_INVERSA.get(valore.lower(), None)
def genera_stanze(i_pos, f_pos, grado, chiave, stanze_run, stanze_usate):
    stanze_valide=filtra_stanze(i_pos, f_pos, grado, chiave, stanze_run, stanze_usate)
    opzioni=estraz_stanze(stanze_valide, grado, chiave)
    return opzioni


algoritmo_gioco()

