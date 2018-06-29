from django.db import models


class Linios(models.Model):
	category,
	product_name,
	product_sku,
	product_availabi,
	product_price,
	product_price_sec,
	product_review,
	product_ratValue,
	product_url,
	time
	

class BestB(models.Model):
	(category,product_name,product_upc,product_sku,product_availableinStore,product_onlineAvailability,product_salePrice,product_regularPrice,product_custumerRating,product_numReviews,product_productURL,time)
	

class Wallmar(models.Model):
	(category,product_name,product_upc,product_itemid,product_stock,product_availableOnline,product_salePrice,product_msrp,product_custumerRating,product_numReviews,product_productURL,time)
	
class Mercado(models.Model):
	(category,product_name,product_itemid,product_stock,product_sold,product_salePrice,product_custumerRating,product_numReviews,product_productURL,time)
 