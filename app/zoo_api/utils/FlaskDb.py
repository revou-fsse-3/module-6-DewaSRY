""" testing """

from flask_sqlalchemy import SQLAlchemy

class FlaskDb:
    """  SessionFlaskModel"""
    db:SQLAlchemy= None
    
    def getDb()-> SQLAlchemy: 
        if FlaskDb.db== None:        
            FlaskDb.db= SQLAlchemy()
        return FlaskDb.db
