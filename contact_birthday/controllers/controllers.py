# -*- coding: utf-8 -*-
from odoo import http

# class ContactBirthday(http.Controller):
#     @http.route('/contact_birthday/contact_birthday/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_birthday/contact_birthday/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_birthday.listing', {
#             'root': '/contact_birthday/contact_birthday',
#             'objects': http.request.env['contact_birthday.contact_birthday'].search([]),
#         })

#     @http.route('/contact_birthday/contact_birthday/objects/<model("contact_birthday.contact_birthday"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_birthday.object', {
#             'object': obj
#         })