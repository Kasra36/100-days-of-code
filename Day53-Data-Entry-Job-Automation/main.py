from web_data import WebData
from automation import Automation

content = WebData()
g_form = Automation()

g_form.fill_form(content.addresses, content.prices, content.links)