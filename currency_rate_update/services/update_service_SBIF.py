# © 2009 Camptocamp
# © 2009 Grzegorz Grzelak
# © 2018 Intellego-BI.com
# © 2018 Rodolfo Bermudez Neubauer
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from .currency_getter_interface import CurrencyGetterInterface

from datetime import datetime
from lxml import etree

import logging
_logger = logging.getLogger(__name__)

import requests
import xmltodict as xm

# Se debe solicitar un API KEY para cada empresa en el sitio de SBIF
# https://api.sbif.cl/uso-de-api-key.html
apikey = 'e96f651e08214ed0060771f21d11cdeb3b8b3305'
sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/dolar/?apikey=' + apikey + '&formato=xml'
rep = requests.get(sbifurl, allow_redirects=True)

req = requests.get(sbifurl, allow_redirects=True)
if req.status_code == 200:
    docs = xm.parse(req.content)
    fecha = docs['IndicadoresFinancieros']['Dolares']['Dolar']['Fecha']
else:
    fecha = datetime.today().strftime('%Y-%m-%d')

class SBIFGetter(CurrencyGetterInterface):
    """Implementation of Currency_getter_factory interface
    for SBIF service
    """
    code = 'SBIF'
    name = 'SBIF Chile'
    supported_currency_array = ["USD", "EUR", "UF", "UTM"]

    el1 = ''
    el2 = ''
    fecha = datetime.today().strftime('%Y-%m-%d')

    def rate_retrieve(self, dom, ns, curr):
        """Parse a dom node to retrieve-
        currencies data

        """
        apikey = 'e96f651e08214ed0060771f21d11cdeb3b8b3305'

        res = {}
        el1 = '''Dolares'''
        el2 = '''Dolar'''
        sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/dolar/?apikey=' + apikey + '&formato=xml'
        valor = '1,0'
        if curr == 'USD':
           sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/dolar/?apikey=' + apikey + '&formato=xml'
           el1 = '''Dolares'''
           el2 = '''Dolar'''


        if curr == 'UF':
           sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/uf/?apikey=' + apikey + '&formato=xml'
           el1 = '''UFs'''
           el2 = '''UF'''

        if curr == 'UTM':
           sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/utm/?apikey=' + apikey + '&formato=xml'
           el1 = '''UTMs'''
           el2 = '''UTM'''

        if curr == 'EUR':
           sbifurl = 'https://api.sbif.cl/api-sbifv3/recursos_api/euro/?apikey=' + apikey + '&formato=xml'
           el1 = '''Euros'''
           el2 = '''Euro'''

        rep = requests.get(sbifurl, allow_redirects=True)
        docu = xm.parse(rep.content)

        fecha = docu['IndicadoresFinancieros'][el1][el2]['Fecha']
        valor = docu['IndicadoresFinancieros'][el1][el2]['Valor']

        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

        res['rate_currency'] = float(valor)
        return res

    def get_updated_currency(self, currency_array, main_currency,
                             max_delta_days):
        """implementation of abstract method of Curreny_getter_interface"""
        url = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

        # We do not want to update the main currency
        if main_currency in currency_array:
            currency_array.remove(main_currency)
        _logger.debug("SBIF currency rate service : connecting...")

        dom = etree.fromstring(rep.content)
        _logger.debug("SBIF sent a valid XML file")
        ecb_ns = {'gesmes': 'http://www.gesmes.org/xml/2002-08-01',
                  'def': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

        rate_date = fecha
        # Don't use DEFAULT_SERVER_DATE_FORMAT here, because it's
        # the format of the XML of ECB, not the format of Odoo server !
        rate_date_datetime = datetime.strptime(rate_date, '%Y-%m-%d')
        self.check_rate_date(rate_date_datetime, max_delta_days)
        # We dynamically update supported currencies
        self.supported_currency_array.append('CLP')
        _logger.debug("Supported currencies = %s " %
                      self.supported_currency_array)
        self.validate_cur(main_currency)

        if main_currency == 'CLP':
            main_curr_data = self.rate_retrieve(dom, ecb_ns, main_currency)
        for curr in currency_array:
            self.validate_cur(curr)
            if curr == 'CLP':
                 rate = 1

            else:
                curr_data = self.rate_retrieve(dom, ecb_ns, curr)
                rate = curr_data['rate_currency']

            self.updated_currency[curr] = rate

            _logger.debug("Rate retrieved : 1 %s = %s %s" % (main_currency, rate, curr))
        return self.updated_currency, self.log_info
