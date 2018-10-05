# odoo-chile
Odoo Chile

Compendio de add-ons para la localización chilena de Odoo. Elementos contemplados en la localización:

- Plan de Cuentas SII
- Indicadores de Impuestos SII
- Factura Electrónica SII
- Cesión de Créditos SII
- Monedas Chile (UF y UTM)
- Actualización de Tipos de Cambio con API SBIF Chile (USD, EUR, UF y UTM)
- Nómina de Remuneraciones según Código del Trabajo de Chile

Este proyecto es un compendio de addons desarrollado por la comunadad Open-source de Odoo. La idea es generar un repositorio completo que pueda ser instalable en la versiòn 11 de Odoo (Enterprise).

Correcciones realizadas:

- Se han corregido algunos errores de dependencias Python que impedían las instalación en la versión 11.0 (ver archivo requirements.txt). 

- Errores que impedían la instalación del add-on para factura electrónica.

- El módulo "currency_rate_update" se ha ampliado para incluir la actualización de los tipos de cambio para USD, EUR, UF y UTM a partir del API provista por la SBIF (https://api.sbif.cl). Se deben crear las monedas UF y UTM en la instalación de Odoo.
