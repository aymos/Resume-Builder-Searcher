# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    c=auth.user_id
    response.flash = T("Welcome to web2py!")
    return locals()
    #return dict(message=T('Hello World'))
    
@auth.requires_login()
def Personal():
	c=auth.user_id
	db.Personal.pid.default=c
	db.Personal.pid.readable=True
	db.Personal.pid.writable=False
	form=SQLFORM(db.Personal)
	if form.process().accepted:
		response.flash='form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	return dict(form=form)
	
@auth.requires_login()
def Education():
	c=auth.user_id
	db.Education.eid.default=c
	db.Education.eid.readable=True
	db.Education.eid.writable=False
	form=SQLFORM(db.Education)
	if form.process().accepted:
		response.flash='form accepted'
	elif form.errors:
		response.flash='form has errors'
	return dict(form=form)

@auth.requires_login()
def Merit():	
	c=auth.user_id
	db.Merit.mid.default=c
	db.Merit.mid.readable=True
	db.Merit.mid.writable=False
	form=SQLFORM(db.Merit)
	if form.process().accepted:
		response.flash='form accepted'
	elif form.errors:
		response.flash='form has errors'
	return dict(form=form)

@auth.requires_login()
def Experience():
	c=auth.user_id
	db.Experience.exid.default=c
	db.Experience.exid.readable=True
	db.Experience.exid.writable=False
	form=SQLFORM(db.Experience)
	if form.process().accepted:
		response.flash='form accepted'
	elif form.errors:
		response.flash='form has errors'
	return dict(form=form)
	
@auth.requires_login()
def create():
	return locals()

@auth.requires_login()
def template_0():
	c=auth.user_id
	cont=db(db.auth_user.id==c).select(db.auth_user.ALL)
	pers=db(db.Personal.pid==c).select(db.Personal.ALL)
	edu=db(db.Education.eid==c).select(db.Education.ALL)
	mer=db(db.Merit.mid==c).select(db.Merit.ALL)
	exp=db(db.Experience.exid==c).select(db.Experience.ALL)
	return locals()
	
@auth.requires_login()	
def prin():
    return locals()

@auth.requires_login()
def template_1():
	c=auth.user_id
	cont=db(db.auth_user.id==c).select(db.auth_user.ALL)
	pers=db(db.Personal.pid==c).select(db.Personal.ALL)
	edu=db(db.Education.eid==c).select(db.Education.ALL)
	mer=db(db.Merit.mid==c).select(db.Merit.ALL)
	exp=db(db.Experience.exid==c).select(db.Experience.ALL)
	return locals()

@auth.requires_login()
def template_2():
	c=auth.user_id
	cont=db(db.auth_user.id==c).select(db.auth_user.ALL)
	pers=db(db.Personal.pid==c).select(db.Personal.ALL)
	edu=db(db.Education.eid==c).select(db.Education.ALL)
	mer=db(db.Merit.mid==c).select(db.Merit.ALL)
	exp=db(db.Experience.exid==c).select(db.Experience.ALL)
	return locals()
	
@auth.requires_login()
def template_3():
	c=auth.user_id
	cont=db(db.auth_user.id==c).select(db.auth_user.ALL)
	pers=db(db.Personal.pid==c).select(db.Personal.ALL)
	edu=db(db.Education.eid==c).select(db.Education.ALL)
	mer=db(db.Merit.mid==c).select(db.Merit.ALL)
	exp=db(db.Experience.exid==c).select(db.Experience.ALL)
	return locals()
	
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


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


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch,mm
from reportlab.lib.enums import TA_LEFT,TA_RIGHT,TA_CENTER,TA_JUSTIFY
from reportlab.lib import colors
from uuid import uuid4
from cgi import escape
import os

@auth.requires_login()
def get_pdf():   
    c=auth.user_id 
    cont=db(db.auth_user.id==c).select(db.auth_user.ALL)
    pers=db(db.Personal.pid==c).select(db.Personal.ALL)
    edu=db(db.Education.eid==c).select(db.Education.ALL)
    mer=db(db.Merit.mid==c).select(db.Merit.ALL)
    exp=db(db.Experience.exid==c).select(db.Experience.ALL)    	    
    title="This is Doc title"
    heading='Hello I am kisi ka resume'
    text=cont[0]['first_name']
    
    styles=getSampleStyleSheet()
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    doc=SimpleDocTemplate(tmpfilename)
    story=[]
    story.append(Paragraph(escape(title),styles["Title"]))
    story.append(Paragraph(escape(heading),styles["Heading2"]))
    story.append(Paragraph(escape(text),styles["Normal"]))
    story.append(Paragraph(escape("HELLLLO"),styles["Normal"]))
    story.append(Spacer(1,2*inch))
    doc.build(story)
    data=open(tmpfilename,"rb").read()
    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    return data
