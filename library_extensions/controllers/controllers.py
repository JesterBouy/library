# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryExtensions(http.Controller):
#     @http.route('/library_extensions/library_extensions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_extensions/library_extensions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_extensions.listing', {
#             'root': '/library_extensions/library_extensions',
#             'objects': http.request.env['library_extensions.library_extensions'].search([]),
#         })

#     @http.route('/library_extensions/library_extensions/objects/<model("library_extensions.library_extensions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_extensions.object', {
#             'object': obj
#         })

