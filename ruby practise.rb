require 'rubygems'
require 'uri'
require 'net/http'
require 'json'


#amount: should be in USD only
#toCurrency: is client currency of client_credits, check other entried in db and use same currency
client_id = ARGV[0]
amount = ARGV[1]
toCurrency = ARGV[2]
agencyId = ARGV[3]

def updateClientCredits(client_id, agencyId, amount, toCurrency)

    if(toCurrency != 'USD')
        conversionFactor = getCurrencyConvesrionFactor(client_id, 'USD', toCurrency)
        finalAmount = amount.to_f * conversionFactor
    else
       finalAmount = amount
    end

    puts "Updating Client Credits for client : #{client_id}...final amout #{finalAmount}#{toCurrency}"
    update_credits = <<-EOQ
MYSQL_PWD=osBilling_rwpppASJJE123KS_prod mysql --host=os_billing_db.onlinesales.ai --user=osBillingSvc_rw --port=5006 os_billing_db -e "INSERT INTO client_credits SET client_id = #{client_id}, agency_id = #{agencyId}, currency = '#{toCurrency}', amount = #{finalAmount}, tax_percentage = 0, tax = 0, status_type_id = 6, credit_type_id = 3, invoice_item_id = NULL, metadata = NULL, description = NULL, is_deleted = 0, amount_in_usd = #{amount};"
EOQ
    puts update_credits

end

def getCurrencyConvesrionFactor(clientId,fromCurrency, toCurrency)

    timeNow = Time.now
    dateToday = timeNow.strftime("%Y-%m-%d")

    url = URI("http://services.onlinesales.ai/reportingSvc/fetch?jsonQuery={%22restFileServletResponse%22:null,%22start%22:0,%22limit%22:100,%22partialData%22:true,%22selectors%22:[{%22alias%22:%22conversion_factor%22,%22canonicalColumn%22:%22.currency_conversion.conversion_factor%22,%22buckets%22:0,%22targetCurrency%22:null,%22isCount%22:false,%22isDistinct%22:false}],%22filters%22:[{%22canonicalColumn%22:%22.currency_conversion.date%22,%22operator%22:%22=%22,%22values%22:[%22#{dateToday}%22],%22type%22:%22date%22,%22isRhsColumn%22:false,%22targetCurrency%22:null},{%22canonicalColumn%22:%22.currency_conversion.from_currency%22,%22operator%22:%22=%22,%22values%22:[%22#{fromCurrency}%22],%22type%22:%22text%22,%22isRhsColumn%22:false,%22targetCurrency%22:null},{%22canonicalColumn%22:%22.currency_conversion.to_currency%22,%22operator%22:%22IN%22,%22values%22:[%22#{toCurrency}%22],%22type%22:%22text%22,%22isRhsColumn%22:false,%22targetCurrency%22:null}],%22orderingColumns%22:null,%22groupByColumns%22:null,%22clientIds%22:[#{clientId}],%22vendors%22:[%22sokrati%22],%22allowFromVendor%22:false,%22application%22:%22irisTestApplication%22}")

    http = Net::HTTP.new(url.host, url.port)

    request = Net::HTTP::Get.new(url)
    request["User-Agent"] = 'PostmanRuntime/7.15.0'
    request["Accept"] = '*/*'
    request["Cache-Control"] = 'no-cache'
    request["Postman-Token"] = 'a0429a26-55f1-4502-a9f3-dd284e8deefa,50b5ed30-b586-442c-b6c0-ad91df316454'
    request["Host"] = 'services.onlinesales.ai'
    request["accept-encoding"] = 'gzip, deflate'
    request["Connection"] = 'keep-alive'
    request["cache-control"] = 'no-cache'
    puts url
    response = http.request(request)
    responseData  = response.read_body
    puts responseData
    responseDataJson = JSON.parse(responseData)
    conversionFactor = responseDataJson["data"]["results"]["sokrati"][1][0]
    puts conversionFactor
    return conversionFactor.to_f
end

updateClientCredits(client_id, agencyId, amount, toCurrency)
puts "DONE"
