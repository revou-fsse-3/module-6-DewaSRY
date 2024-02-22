

from os import path,getcwd


def getSqlPhat():
    """alternative db for db in locale"""
    basedir = path.join(getcwd(), "app", "data")
    dbPhat='sqlite:///' + path.join(basedir, 'data.db')
    return dbPhat




