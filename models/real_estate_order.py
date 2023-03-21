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
    _name = "real.estate"
    _description = "Real Estate"


    name = fields.Char(string='Name', required=False, copy=False, readonly=False, default=lambda self: _('New'))
    description = fields.Text(string='Description', required=False, copy=False, readonly=False)
    postcode = fields.Char(string='Postcode', required=False, copy=False, readonly=False)
    date_availability = fields.Date(string='Data Availability', required=False, copy=False, readonly=False)
    expected_price = fields.Float(string='Expected Price', required=False, copy=False, readonly=False)
    selling_price = fields.Float(string='Selling Price', required=False, copy=False, readonly=False)
    bedrooms = fields.Integer(string='Bedrooms', required=False, copy=False, readonly=False)
    living_area = fields.Integer(string='Living Area', required=False, copy=False, readonly=False)
    facades = fields.Integer(string='Facades', required=False, copy=False, readonly=False)
    garage = fields.Boolean(string='Garage', required=False, copy=False, readonly=False)
    garden = fields.Boolean('Garden', required=False, copy=False, readonly=False)
    garden_area = fields.Integer(string='Garden Area', required=False, copy=False, readonly=False)
    garden_orientation =fields.Selection(string='Garden Orientation',
       selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')])
