# Book Scraper

## Overview

This Python script scrapes book information from the Books to Scrape website (https://books.toscrape.com/), extracting details such as title, price, and availability for books on a specific page.

## Features

- Fetches book data from a specified website
- Extracts book titles, prices, and availability
- Saves scraped data to a CSV file
- Simple and easy-to-use command-line interface

## Prerequisites

### Required Libraries
- `requests`
- `beautifulsoup4`
- `csv` (built-in Python library)

### Installation

1. Ensure you have Python 3.7+ installed
2. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. Clone the repository
2. Navigate to the script directory
3. Run the script:
   ```bash
   python book_scraper.py
   ```

## How It Works

1. Sends a GET request to the Books to Scrape website
2. Parses the HTML content using BeautifulSoup
3. Finds book containers and extracts:
   - Book title
   - Book price
   - Book availability
4. Saves extracted data to `books_data.csv`
5. Prints book details to the console

## Customization

To scrape a different page or website:
- Modify the `url` variable in the `scrape_books()` function
- Adjust HTML tag and class selectors as needed

## Error Handling

- Handles network request exceptions
- Provides error messages for failed scraping attempts
- Checks for data availability before saving

## Limitations

- Currently scrapes only the first page
- Designed for the specific structure of Books to Scrape website
- Requires modification for different website layouts

## Best Practices

- Always check website's `robots.txt`
- Respect website's terms of service
- Add delays between requests for large-scale scraping


## Contact

[Kabutey Manasseh Kwame](kabuteymanasseh5@gmail.com)