import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from pyramid.view import view_config

from .models import (
    DBSession,
    Page,
    )

# regular expression used to find WikiWords
#wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

# @view_config(route_name='view_wiki')
# def view_wiki(request):
#     return HTTPFound(location = request.route_url('view_page',
#                                                   pagename='FrontPage'))

@view_config(route_name='browse', renderer='browse.mako')
def view_page(request):

    #page = DBSession.query(Page).filter_by(name=pagename).first()


    #return dict(page=page, content=content, edit_url=edit_url)
    return {}

# @view_config(route_name='add_page', renderer='templates/edit.pt')
# def add_page(request):
#     name = request.matchdict['pagename']
#     if 'form.submitted' in request.params:
#         body = request.params['body']
#         page = Page(name, body)
#         DBSession.add(page)
#         return HTTPFound(location = request.route_url('view_page',
#                                                       pagename=name))
#     save_url = request.route_url('add_page', pagename=name)
#     page = Page('', '')
#     return dict(page=page, save_url=save_url)

# @view_config(route_name='edit_page', renderer='templates/edit.pt')
# def edit_page(request):
#     name = request.matchdict['pagename']
#     page = DBSession.query(Page).filter_by(name=name).one()
#     if 'form.submitted' in request.params:
#         page.data = request.params['body']
#         DBSession.add(page)
#         return HTTPFound(location = request.route_url('view_page',
#                                                       pagename=name))
#     return dict(
#         page=page,
#         save_url = request.route_url('edit_page', pagename=name),
#         )
