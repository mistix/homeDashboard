# -*- coding: utf-8 -*-
import cgi
import cherrypy

from lib.model.temperature import Temperature

__all__ = ['WeatherStation']

class WeatherStation(object):
    @cherrypy.expose
    @cherrypy.tools.render(template="index.mako")
    def index(self):
        pass

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def last_24_hours(self):
        db = cherrypy.request.db
        temperature = {}
        for temperature in Temperature.get_last_24_hours(db):
            node = {
                "readingDateTime": temperature.readingDate,
                "airTemperature": temperature.airTemperature,
                "heaterTemperature": temperature.heaterTemperature
            }
        temperature.append(node)
        return temperature 

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def last_48_hours(self):
        db = cherrypy.request.db
        temperature = {}
        for temperature in Temperature.get_last_48_hours(db):
            node = {
                "readingDateTime": temperature.readingDate,
                "airTemperature": temperature.airTemperature,
                "heaterTemperature": temperature.heaterTemperature
            }
        temperature.append(node)
        return temperature 

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def reading_in_range(self, fromDate, toDate):
        db = cherrypy.request.db
        temperature = {}
        for temperature in Temperature.get_reading_inrange(db, fromDate, toDate):
            node = {
                "readingDateTime": temperature.readingDate,
                "airTemperature": temperature.airTemperature,
                "heaterTemperature": temperature.heaterTemperature
            }
        temperature.append(node)
        return temperature
