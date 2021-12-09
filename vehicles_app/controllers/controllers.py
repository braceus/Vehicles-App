# -*- coding: utf-8 -*-
# from odoo import http


# class /home/brajean/customAddons/vehiclesApp(http.Controller):
#     @http.route('//home/brajean/custom_addons/vehicles_app//home/brajean/custom_addons/vehicles_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/brajean/custom_addons/vehicles_app//home/brajean/custom_addons/vehicles_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/brajean/custom_addons/vehicles_app.listing', {
#             'root': '//home/brajean/custom_addons/vehicles_app//home/brajean/custom_addons/vehicles_app',
#             'objects': http.request.env['/home/brajean/custom_addons/vehicles_app./home/brajean/custom_addons/vehicles_app'].search([]),
#         })

#     @http.route('//home/brajean/custom_addons/vehicles_app//home/brajean/custom_addons/vehicles_app/objects/<model("/home/brajean/custom_addons/vehicles_app./home/brajean/custom_addons/vehicles_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/brajean/custom_addons/vehicles_app.object', {
#             'object': obj
#         })
