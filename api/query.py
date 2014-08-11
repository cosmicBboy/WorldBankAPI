# -*- coding: utf-8 -*-
'''
--------------------------------
Worldbank Data & Reports WDS API
--------------------------------

Class for handling D&R API queries

For more information about the API go to:
http://documents.worldbank.org/curated/en/developers
'''

import urllib2


class WdsQueryContainer(object):

    def __init__(self, baseUrl, params, rows=10, start=0):
        self.baseUrl = baseUrl
        self.params = params
        self.rows = rows
        self.start = start
        self.request = None
        self.total = None

    def setParam(self, param, value):
        #setter function for parameter
        #mainly used for resetting start parameter
        #for subsequent requests
        self.params[param] = value

    def setRequest(self):
        paramString = '&'.join(['='.join(p) for p in self.params.items()])
        self.request = ''.join([self.baseUrl, paramString])

    def getResponse(self):
        self.response = urllib2.urlopen(self.request).read()

    def getTotal(self):
        #get total number of documents for specified query
        pass

    def getDocs(self):
        #get document metadata from a response object
        pass

    def getBulk(self):
        #function for getting all documents within specified query
        pass

    def save2store(self, store):
        #function that takes a store object
        #in this case we'll be using an s3 connector
        #to save documents to s3 store
        pass


if __name__ == "__main__":
    baseUrl = "http://search.worldbank.org/api/v2/wds?"
    responseFormat = "json"

    #grab all metadata
    fields = ','.join(['abstracts','admreg','alt_title','authr','available_in',
        'bdmdt','closedt','colti','count','credit_no','disclosure_date',
        'disclosure_type','disclosure_type_date','display_title','docdt',
        'docna','docty','entityid','envcat','geo_reg','geo_reg','geo_reg_and_mdk',
        'id','isbn','keywd','lang','listing_relative_url','lndinstr','loan_no',
        'majdocty','majtheme','ml_abstract','ml_display_title','new_url','owner',
        'pdfurl','prdln','projn','repnb','repnme','sectr','src_cit','subsc','subtopic',
        'teratopic','theme','trustfund','txturl','unregnbr','url_friendly_title',
        'virt_coll','vol_title','volnb'])

    #setting parameters
    parameters = {
        'format': 'json',
        'fl': fields,
        'srt': 'docdt',
        'order': 'desc'
    }

    query = WdsQueryContainer(baseUrl, parameters)
    query.setRequest()
    query.getResponse()
    print query.response
