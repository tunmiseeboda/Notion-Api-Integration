import os
from dotenv import load_dotenv
from examples.databases.create_database import notion
from notion_client import Client
import csv
from notion_client.client import ClientOptions
from collections import defaultdict

# Load environment variables from .env file
load_dotenv()

# Retrieve the Notion token from the .env file
notion_token = os.getenv("NOTION_KEY")

# Retrieve the Notion database ID from the .env file
notion_database_id = os.getenv("NOTION_DATABASE_ID")

# Initialize the Notion client
Notion_client = Client(options=ClientOptions(auth=notion_token))

# Create an empty array to store lists of columns
rating_info = {}

# Specify the path to the CSV file
csv_file_path = "/Users/tunmiseeboda/notion-sdk-py/ratings.csv"

# Open the CSV file in read mode
with open(csv_file_path, "r") as csv_file:
    field_names = ['Book', 'Name', 'Rating']

    # Create a CSV reader object with dictionary access and specified fieldnames
    csv_reader = csv.DictReader(csv_file, fieldnames=field_names)

    # Create a defaultdict to store book data
    grouped_books = defaultdict(list)

    # Initialize columns_array with empty lists for each column
    for column in field_names:
        rating_info[column] = []

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append values to their respective lists
        for column in field_names:
            rating_info[column].append(row[column])

    # Create a defaultdict to store total ratings for each book
    total_ratings_by_book = defaultdict(float)

    # Create a defaultdict to store favorite ratings for each book
    favorite_ratings_by_book = defaultdict(int)

    # Create a dictionary to store count and total rating for each book
    book_stats = {}

    # Set to keep track of processed books
    processed_books = set()

    # Iterate over the data and group members by name while storing their indices
    for i, Book in enumerate(rating_info["Book"]):
        lowercase_book = Book.lower().strip()
        name = rating_info["Name"][i].lower()
        rating = float(rating_info["Rating"][i])

        # Initialize the book_stats dictionary for the book if it's not present
        if lowercase_book not in book_stats:
            book_stats[lowercase_book] = {"count": 0, "total_rating": 0,
                                          "Favorite_Book": 0}

        # Append the rating to the total ratings for the book
        book_stats[lowercase_book]["count"] += 1
        book_stats[lowercase_book]["total_rating"] += rating

        if rating == 5:
            book_stats[lowercase_book]["Favorite_Book"] += 1

        # Mark the book as processed
        processed_books.add(lowercase_book)

    # Print book stats
    for book, stats in book_stats.items():
        notion_data = {
            "parent": {"database_id": notion_database_id},
            "properties": {
                "Title": {"title": [{"text": {"content": book}}]},
                "Book Count": {"number": stats["count"]},
                "Total Rating": {"number": stats["total_rating"]},
                "Average Rating": {"number": float(
                    "{:.2f}".format(stats["total_rating"] / stats["count"]))},
                "Favorites": {"number": stats["Favorite_Book"]}
            }
        }

        response = notion.pages.create(**notion_data)

        # Print the response
        print(response)