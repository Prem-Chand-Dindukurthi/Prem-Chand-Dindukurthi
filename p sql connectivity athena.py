mport sys
import commands
import os


#marketplace_client_id = commands.getoutput(marketplace_client_id_query)


'''select mpd.merchant_id , mpd.sku_id, mpd.feed_sync_time, mpd.e_link  from os_product_ads_product_selection mps, merchandise_product_dimensions mpd , merchandise_product_intel mpi where mpi.client_id = mpd.client_id and mpi.sku_id =mpd.sku_id and mpi.currency = mpd.e_currency and mpi.country_code = mpd.country_code and mpi.merchant_id = mpd.merchant_id  and mpd.client_id = mps.client_id and mps.merchant_id = mpd.merchant_id and mpd.sku_id = mps.product_id and is_deleted = 0 and is_active = 1  and mpd.client_id = 100001 and mps.merchant_id in ('26487','53064') order by 1,2;'''

query="PGPASSWORD=234hujAn psql -h redshift.onlinesales.ai -U shantanu_r -d dev -p 5439 -c \"select mpd.merchant_id , mps.campaign_id, count(mpd.sku_id) from os_product_ads_product_selection mps, merchandise_product_dimensions mpd , merchandise_product_intel mpi where mpi.client_id = mpd.client_id and mpi.sku_id =mpd.sku_id and mpi.currency = mpd.e_currency and mpi.country_code = mpd.country_code and mpi.merchant_id = mpd.merchant_id  and mpd.client_id = mps.client_id and mps.merchant_id = mpd.merchant_id and mpd.sku_id = mps.product_id and is_deleted = 0 and is_active = 1  and mpd.client_id = 100001 and mps.merchant_id in (\'26487\',\'53064\') group by 1,2 order by 1,2; \" > \"file.tsv\" "

p=commands.getoutput(query)
#os.system("234hujAn")
print(p)
print(type(p))
print(p.split("\n"))
sys.exit(1)

