# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import json

json_obj = ""

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
    """
    form = SQLFORM(db.leave_application)
    if form.process().accepted:
        response.flash = 'form accepted'
        """
        leavetype = form.vars.leave_type
        fromdate = form.vars.from_date
        tilldate = form.vars.till_date
        """
        #redirect(URL('jsonformat'), vars=dict(leavetype=leavetype, fromdate=fromdate, tilldate=tilldate))
        redirect(URL('jsonobject'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

def jsonobject():
    """
    data = request.vars
    """
    """
    leavetype = request.vars.leavetype
    fromdate = request.vars.fromdate
    tilldate = request.vars.tilldate
    appObj = {'form': 'leave_application', 'content': {'leave_type': leavetype,
                                                           'from_date': fromdate,
                                                           'till_date': tilldate,
                                                           }}
    json_obj = json.JSONEncoder().encode(appObj)
    """

    #leaveapps = db().select(db.leave_application.ALL)    #WORKS CORRECT
    apprecord = db(db.leave_application).select().last()
    appObj = {'form': 'leave_application', 'content': {'leave_type': apprecord.leave_type,
                                                           'from_date': str(apprecord.from_date),
                                                           'till_date': str(apprecord.till_date),
                                                           'user_name': apprecord.user_name,
                                                           'apptimestamp': str(apprecord.apptimestamp)
                                                           }}

    
    
    json_obj = json.JSONEncoder().encode(appObj)

    #return json_obj
    #return dict(leaveapps=leaveapps)

    
    
    
    return dict(jsonobj=json_obj)

def so_submit() :
    if request.vars :
        db.applications.insert(application_object=request.vars.AO, signature=request.vars.SO, user_name=auth.user)
    return "Sign Object stored in the database !!!"

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


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
