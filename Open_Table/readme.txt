open_table_data_download.ipynb and restaurantMetaData.ipynb have been created to scrape and download the data from open table website and API.


open_table_data.csv has been created from https://opentable.herokuapp.com API for some reason API has given duplicates for unique set of zip codes.
The data from open_table_data.csv has been cleaned and open_table_data_csv.csv and open_table_data_final.csv has been created.

All the raw and unedited files are placed in raw folder.

open_table_data_final contains the following fields with 596 observations
	name	
	address	city	
	state	
	area		
	postal_code	
	country	
	phone	
	lat	
	lng	
	price	
	reserve_url	
	mobile_reserve_url	
	image_url


metaDataRestaurant has been cleaned by removing all the null values
metaDataRestaurant contains following fields with 378 observations
	overall_rating	
	recommended_to_a_friend	food	
	service	ambiance	
	noise_level		
	dining_style	
	cuisines	
	price_range	
	hours_of_operation

A xml file has been created for menus from restaurants since menus are too big to be stored in each cell.
Following is the general format for menu from a restaurant.
<restaurants>
	<menu id="1">
		menus for the restaurant with id 1
	</menu>
	<menu id="2">
		menus for the restaurant with id 2
	</menu>
</restaurants>