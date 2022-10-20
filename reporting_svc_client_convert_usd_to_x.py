# need to set this value on facebook 0.000135
import json
from osSvcClient4py.reporting_svc_client import ReportingServiceClient

reporting_svc_client = ReportingServiceClient(app_name="irisTestApplication", env_domain="prod")

def convert_usd_to_x(value, to_currency):
    conv_map = reporting_svc_client.fetch_currency_conversion("USD")
    print(json.dumps(conv_map, indent = 4))
    if to_currency in conv_map:
        return value * (conv_map[to_currency])
    else:
        raise Exception("Currency conversion factor not found for currency: " + currency)

amount = 0.665 # in usd

print("INR")
budget = convert_usd_to_x(amount, "INR")
print(budget)

# print("ZAR")
# budget = convert_usd_to_x(amount, "ZAR")
# print(budget)


# print("USD")
# budget = convert_usd_to_x(amount, "ZAR")
# print(budget)
