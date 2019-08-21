# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class res_partner(models.Model):
    _inherit = 'res.partner'

    birthday_date = fields.Datetime('Birthday Date')

    @api.onchange('email')
    def _check_email(self):
        for part in self:
            if part.email:
                if len(part.email) > 10:
                    raise ValidationError('Max Email char lenght is 10')


    # @api.constrains('email')
    # def _check_email_func(self):
    #     self._check_email()

    def run_birthday_sync(self, days):
        # group = self.env['res.groups'].search([('name', '=', 'Admin Manager')])
        group = self.env.ref('contact_birthday.group_admin_manager')
        model_id = self.env['ir.model']._get(self._name).id
        for user in group.users:
            # print(recipient.users.id)
            # for user in recipient.users:
            domain = fields.Datetime.to_string(datetime.date(datetime.today()) + timedelta(days=days))
            partners = self.env['res.partner'].search([('birthday_date', '=', domain)])
            for partner in partners:
                self.env['mail.activity'].create(
                    {'res_id': partner.id,
                     'res_model_id': model_id,
                     'date_deadline': datetime.date(datetime.today()) + timedelta(days=days),
                     'note': 'Birthday Reminder',
                     'activity_type_id': self.env.ref('contact_birthday.mail_act_birthday').id,
                     'user_id': user.id})
