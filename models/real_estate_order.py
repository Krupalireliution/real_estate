# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from itertools import groupby
import json

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.osv import expression
from odoo.tools import float_is_zero, html_keep_url, is_html_empty

from odoo.addons.payment import utils as payment_utils



class RealEstate(models.Model):
    _name = "real.estate.order"
    _description = "Real Estate"

    name = fields.Char(string='Name', required=False, copy=False, readonly=False)
    description = fields.Text(string='Description', required=False, copy=False, readonly=False)
    postcode = fields.Char(string='Postcode', required=False, copy=False, readonly=False)
    date_availability = fields.Date(string='Data Availability', required=False, copy=False, readonly=False)
    expected_price = fields.Float(string='Expected Price', required=False, copy=False, readonly=False)
    selling_price = fields.Float(string='Selling Price', readonly=True)
    bedrooms = fields.Integer(string='Bedrooms', required=False, copy=False, readonly=False)
    living_area = fields.Integer(string='Living Area', required=False, copy=False, readonly=False)
    facades = fields.Integer(string='Facades', required=False, copy=False, readonly=False)
    garage = fields.Boolean(string='Garage', required=False, copy=False, readonly=False)
    garden = fields.Boolean(string='Garden', required=False, copy=False, readonly=False)
    garden_area = fields.Integer(string='Garden Area', required=False, copy=False, readonly=False)
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
    ])
    properties_type_id = fields.Many2one("properties.type", string="Properties Type")
    salesman = fields.Many2one("res.users", string='Salesman')
    buyer = fields.Many2one("res.partner", string='Buyer')
    properties_tags_ids = fields.Many2many("properties.tags", string="Properties Tags")
    offer_ids = fields.One2many("properties.offers", inverse_name="property_id")
    total = fields.Float(compute="_compute_total")

    @api.onchange("garden")
    def _onchange_garden(self):
        for rec in self:
            if rec.garden:
                rec.garden_orientation = "west"
            if rec.garden:
                 rec.garden_area = 100
            else:
                rec.garden_orientation = None
                rec.garden_area = 0

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
             record.total = record.living_area + record.garden_area

    @api.depends("partner_id.price")
    def _compute_best_offer(self):
        for record in self:
            record.description = "Test for partner %s" % record.partner_id.price
