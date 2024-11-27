import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    """
    Scrape book titles and prices from a sample bookstore website
    Note: Replace the URL with a real website you have permission to scrape
    """
    # URL of the bookstore website
    url = 'https://books.toscrape.com/catalogue/page-1.html'
    
    try:

        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book containers
        books = soup.find_all('article', class_='product_pod')
        
        # List to store book data
        book_data = []
        
        # Extract information from each book
        for book in books:
            # Extract title
            title = book.h3.a['title']
            
            # Extract price
            price = book.find('p', class_='price_color').text
            
            # Extract availability
            availability = book.find('p', class_='instock availability').text.strip()
            
            # Store book information
            book_data.append({
                'Title': title,
                'Price': price,
                'Availability': availability
            })
        
        # Save data to a CSV file
        save_to_csv(book_data)
        
        return book_data
    
    except requests.RequestException as e:
        print(f"Error occurred while scraping: {e}")
        return []

def save_to_csv(data):
    """
    Save scraped data to a CSV file
    """
    if not data:
        print("No data to save.")
        return
    
    # Specify the output file
    output_file = 'books_data.csv'
    
    # Write data to CSV
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            # Use the keys of the first dictionary as fieldnames
            fieldnames = data[0].keys()
            
            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data rows
            writer.writerows(data)
        
        print(f"Data saved to {output_file}")
    
    except IOError as e:
        print(f"Error saving to CSV: {e}")

def main():
    # Run the scraper
    scraped_books = scrape_books()
    
    # Print scraped data
    for book in scraped_books:
        print(f"Title: {book['Title']}")
        print(f"Price: {book['Price']}")
        print(f"Availability: {book['Availability']}")
        print("---")

if __name__ == "__main__":
    main()