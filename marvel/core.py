# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'


class MarvelObject(object):
    """
    Base class for all Marvel API classes
    """

    def __init__(self, marvel, _dict):
        """
        init
        marvel - instance of Marvel class caller
        _dict - dict of object
        
        """
        self.marvel = marvel
        self.dict = _dict

        
    def __unicode__(self):
        return self.dict['name']
    
    def to_dict(self):
        return self.dict
        
    @classmethod
    def resource_url(cls):
        return cls._resource_url
