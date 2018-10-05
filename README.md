# odoo-chile
Odoo Chile

Compendio de add-ons para la localización chilena de Odoo. Elementos contemplados en la localización:

- Plan de Cuentas SII
- Indicadores de Impuestos SII
- Factura Electrónica SII
- Cesión de Créditos SII
- Moneda CLP (Tipo de Cambio Inverso, por ejemplo: 650 CLP por USD)
- Monedas Chile (UF y UTM)
- Actualización de Tipos de Cambio con API SBIF Chile (USD, EUR, UF y UTM)
- Nómina de Remuneraciones según Código del Trabajo de Chile

Este proyecto es un compendio de addons desarrollado por la comunadad Open-source de Odoo. La idea es generar un repositorio completo que pueda ser instalable en la versiòn 11 de Odoo (Enterprise).

Los componentes fueron tomados de los siguientes repositorios:

- Actualización de Tipos de Cambio y T/C Inverso:
git@github.com:OCA/currency.git#11.0

- Facturación Electrónica:
git@github.com:odoocoop/facturacion_electronica.git#11.0

- Nómina Chile:
git@github.com:KonosCL/addons-konos.git#11.0


Correcciones realizadas:

- El módulo "currency_rate_update" se ha ampliado para incluir la actualización de los tipos de cambio para USD, EUR, UF y UTM a partir del API provista por la SBIF (https://api.sbif.cl). Se crean las monedas UF y UTM en la instalación.

- Se han corregido algunos errores de dependencias Python que impedían las instalación de los componentes de Factura Electrónica en la versión 11.0 (ver archivo requirements.txt). 

- Error en archivo de monedas que impedían la instalación del add-on para factura electrónica (archivo res_currency.csv).
