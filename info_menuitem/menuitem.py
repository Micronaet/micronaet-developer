# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os
import sys
from openerp import netsvc
import logging
from openerp.osv import orm, fields
from datetime import datetime, timedelta
from openerp.tools import (
    DEFAULT_SERVER_DATE_FORMAT, 
    DEFAULT_SERVER_DATETIME_FORMAT, 
    DATETIME_FORMATS_MAP, 
    float_compare)
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _


_logger = logging.getLogger(__name__)

class ir_ui_menu(orm.Model):
    ''' Add extra info for developer
    '''
    
    _name = "ir.ui.menu"
    _inherit = "ir.ui.menu"

    def _get_developer_info(self, cr, uid, ids, fields, args, context=None):
        ''' Get extra info for developer
        '''
        res = {}
        menu_pool = self.pool.get('ir.model.data')

        for item_id in ids:
            menu_ids =  menu_pool.search(cr, uid, [
                ('model', '=', 'ir.ui.menu'),
                ('res_id', '=', item_id),
                ], context=context)
            if menu_ids:
                menu_proxy = menu_pool.browse(
                    cr, uid, menu_ids, context=context)[0]
                res[item_id] = "%s.%s" % (menu_proxy.module, menu_proxy.name)
            else:
                res[item_id] = False
        return res        

    _columns = {
        'developer_info': fields.function(_get_developer_info, method=True,
            type='char', size=120, string='Developer info', store=False),
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
