import re

texto = 'Buenas tardes a todos'

patron = 'B.*t.*s'
patron2 = 't.*o'

coincidencia = re.match(patron, texto)

coincidencia2 = re.search(patron2,texto)

pass