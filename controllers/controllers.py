# -*- coding: utf-8 -*-
from odoo import http

# class NigeriaStates(http.Controller):
#     @http.route('/nigeria_states/nigeria_states/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nigeria_states/nigeria_states/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nigeria_states.listing', {
#             'root': '/nigeria_states/nigeria_states',
#             'objects': http.request.env['nigeria_states.nigeria_states'].search([]),
#         })

#     @http.route('/nigeria_states/nigeria_states/objects/<model("nigeria_states.nigeria_states"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nigeria_states.object', {
#             'object': obj
#         })