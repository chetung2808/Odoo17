from odoo import http
from odoo.http import request

class QwebEstateTemplate(http.Controller):
    @http.route('/test', type="http", auth="public", website=True)
    def qweb_estate_template(self):
        return request.render("test.estate_template", {})