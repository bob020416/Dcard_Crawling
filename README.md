# Dcard_Crawling
This Dcard Crawling Application is primarily intended for research usage. It's important to note that users must abide by the terms of service for web crawling on the Dcard forum. Misuse of the application for purposes outside of these terms will not be supported.  This Selenium Dcard crawler was thoughtfully designed and developed by Bob Chen. 

The script begins by importing necessary modules, some of which include:

- `undetected_chromedriver`: This module allows selenium to use a version of Chrome driver that can avoid detection.
- `pandas`: A popular data manipulation library.
- `selenium`: A web testing library used to automate browser activities.
- `time` and `random`: Standard Python libraries used for introducing delays.

Then, several functions are defined:

1. `initialize_driver()`: This function is used to set up the browser driver for Selenium. It also initializes `ActionChains` which allows you to automate low-level interactions such as mouse movements, mouse button actions, key press, etc. It returns the initialized driver and actions.

2. `scroll_down_page(driver, actions, iterations)`: This function scrolls down a webpage a specific number of times (iterations), with each scroll followed by a random delay between 0-3 seconds.

3. `scrape_articles(driver, query)`: This function takes the query you're interested in, loads the Dcard webpage for that query, waits for the page to load, and then scrapes all of the articles available on the page. It returns a set of unique URLs for these articles.

4. `scrape_article_details(driver, urls)`: This function opens each URL collected by `scrape_articles`, waits for it to load, and then scrapes the title, timestamp, and content of the article. It adds this data to a list of posts. 

5. `save_to_csv(data, filename)`: This function saves the data scraped by `scrape_article_details` into a CSV file using the Pandas library.

6. `main(query)`: This is the main function that calls all of the above functions. It initializes the web driver, scrolls down the page, scrapes article URLs, collects details from each article, and finally saves all the data to a CSV file. After everything is done, it closes the web driver.

The script ends by calling the main function with the specific search query (in this case, "疫苗副作用", which translates to "vaccine side effects").

Note: You can replace this search query and iteration number in `scroll_down_page(driver, actions, 10)` with any value you want based on your requirements. The iteration number refers to how many times the script will scroll down the page to load more articles. The higher the number, the more articles it will load and scrape.
