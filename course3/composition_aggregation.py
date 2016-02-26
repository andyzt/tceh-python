# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class Person(object):
    def __init__(self, name):
        self.name = name


class CompanyAggregation(object):
    def __init__(self, *people):
        self.clients = people


class CompanyComposition(object):
    def __init__(self, client_names):
        self.clients = []
        for client_name in client_names:
            client = Person(client_name)
            self.clients.append(client)


