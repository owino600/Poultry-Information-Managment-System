#!/usr/bin/python3
"""Class DBStorage"""
from models.base_model import BaseModel, Base
from models.medication_operations import Medication
from models.sales import Sales
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {"medication_operation": Medication, "product_sales": Sales}
class DBStorage:
    """intaract with MySQL database"""
    __engine = None
    __session = None
    
    def __init__(self):
        """instantiate a DBStorage"""
        PIMS_MYSQL_USER = getenv('PIMS_MYSQL_USER')
        PIMS_MYSQL_PWD = getenv('PIMS_MYSQL_PWD')
        PIMS_MYSQL_HOST = getenv('PIMS_MYSQL_HOST')
        PIMS_MYSQL_DB = getenv('PIMS_MYSQL_DB')
        STORAGE_T = getenv('STORAGE_T')
        self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.format
                                      (PIMS_MYSQL_USER,
                                        PIMS_MYSQL_PWD,
                                        PIMS_MYSQL_HOST,
                                        PIMS_MYSQL_DB,))
        
        if STORAGE_T == "test":
            Base.metadata.drop_all(self.__engine)
            Base.metadata.create_all(self.__engine)
        
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session()
        
    def all(self, cls=None):
        """create query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                obj = self.__session.query(classes[clss]).all()
                for objs in obj:
                    key = objs.__class__.__name__ + '.' + objs.id
                    new_dict[key] = objs 
        return (new_dict)
    def new(self, objs):
        """add object to the current database session"""
        self.__session.add(objs)
    def save(self):
        """commit all changes"""
        self.__session.commit()
    def delete(self, objs=None):
        """delete from the current database"""
        if objs is not None:
            self.__session.delete(objs)
    def reload(self):
        """relaod data from database"""
        self.__session.remove()
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        
    def close(self):
        """close private session attribute"""
        self.__session.remove()
    def get(self, cls, id):
        """retrive one object"""
        if cls not in classes:
            return None
        return self.__session.query(classes[cls]).get(id)