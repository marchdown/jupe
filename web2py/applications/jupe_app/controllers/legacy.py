# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
    # return auth.wiki()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

def happyqueen():
    """
   see file:///Users/marchdown/Downloads/Mariano%20Reingart,%20Bruno%20Cezar%20Rocha,%20Jonathan%20Lundell,%20Pablo%20Martin%20Mulone,%20Michele%20Comitini,%20Richard%20Gordon,%20Massimo%20Di%20Pierro-web2py%20Application%20Development%20Cookbook-Packt%20Publishing%20(2012).pdf page 79
    """
    return dict()
def ryba():
    """
   see file:///Users/marchdown/Downloads/Mariano%20Reingart,%20Bruno%20Cezar%20Rocha,%20Jonathan%20Lundell,%20Pablo%20Martin%20Mulone,%20Michele%20Comitini,%20Richard%20Gordon,%20Massimo%20Di%20Pierro-web2py%20Application%20Development%20Cookbook-Packt%20Publishing%20(2012).pdf page 79
    """
    return dict()
def ryba2():
    """
   see file:///Users/marchdown/Downloads/Mariano%20Reingart,%20Bruno%20Cezar%20Rocha,%20Jonathan%20Lundell,%20Pablo%20Martin%20Mulone,%20Michele%20Comitini,%20Richard%20Gordon,%20Massimo%20Di%20Pierro-web2py%20Application%20Development%20Cookbook-Packt%20Publishing%20(2012).pdf page 79
    """
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


