''' This files provides the model for the User and Application classes '''

import json

class User():
    ''' User class describing behaviors and attributes of Users '''
    def __init__(self, name='', password='', address='', income='',
                 loan_status=''):
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.income = income
        self.loan_status = loan_status
        self.application_info = None

    def set_application(self, application):
        ''' Sets the application info of the user from the html page '''
        self.application_info = application

    def get_id(self):
        ''' Returns the _id of the user '''
        return self._id

    def get_name(self):
        ''' Returns the name of the user '''
        return self.name

    def get_username(self):
        '''Returns the username of the user'''
        return self.username

    def get_password(self):
        '''Returns the password of the user'''
        return self.password

    def get_address(self):
        '''Returns the password of the user'''
        return self.address

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        '''Returns string representation of object'''
        string = 'User: ' + self.username + ' ' + self.password + ' ' + self.firstname
        string += ' ' + self.lastname
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    @classmethod
    def from_dict(cls, input_user):
        '''Creates an instance of the class from a dictionary'''
        user = User()
        user.__dict__.update(input_user)
        return user

class ApplicationInfo():
    '''A class that defines attributes and how ApplicationInfo should behave'''
    def __init__(self, name='', username='', password='', address='', income=0):

        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.income = income

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        '''Returns string representation of an object'''
        string = 'Application: ' + self.username
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    @classmethod
    def from_dict(cls, input_apply):
        '''Creates an instance of the class from a dictionary'''
        apply = ApplicationInfo()
        apply.__dict__.update(input_apply)
        return apply


class ItemEncoder(json.JSONEncoder):
    ''' Allows us to serialize our objects as JSON '''
    def default(self, o):
        return o.to_dict()



