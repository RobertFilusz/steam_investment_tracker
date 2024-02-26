# steam_investment_tracker
This is my very first project after learning the basics of python with py4e.org. This script fetches item names and prices from the Steam Community Market API (currently cs2 only). In the older version it was a html scraper.<br />

## How to use:
1. run the script<br />
2. enter item name<br />
   example: "M4A1-S | Black Lotus (Factory New)", AK-47 | Vulcan (Field-Tested)<br />
   will not work: "deagle blaze mw", "paris 2023 capsule", "ak empress"<br />
3. when finished type "done"<br />
4. all input items will be saved in item_prices.xlsx<br />
   if you run the script again, any new items will be added to the table, items already there will have their price updated
5. In Investment.xlsx, there is a table you can fill with data like number of items or price when bought so you can track how your investment has fared so far


## To do:
- [x] get prices of any item on steam market through user input<br />
- [ ] add scraping of multiple market pages ***skipped***
- [x] change method of aquiring data from scraping HTML to API ***current***<br />
- [ ] make it so it doesn't require exact item name<br />
- [ ] add data from buff163 (and maybe few other sites), for comparison with steam market<br />
- [ ] maybe add a simple GUI?