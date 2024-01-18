# CSV to Notion Database Populator

## Description
This program reads data from a CSV file (ratings.csv) containing the book name, member name, and ratings. This function processes it to calculate average ratings for each book, favorite counts, the book counts, and the total ratings. Then, it populates a Notion database with the results. 

## Challenges
1. Issues with reading the first row of the CSV file (No headers)
2. learning new Python syntax.
3. learning how to populate the database.

## Sources
Here are the primary sources and references I used during the development of this project:
- Notion API Documentation: Notion API Docs
- learning notion API with Python: https://www.python-engineer.com/posts/notion-api-python/
- creating a notion page with Python: https://medium.com/@plasmak_/how-to-create-a-notion-page-using-python-9994bf01299
- notion-sdk-py: https://github.com/ramnes/notion-sdk-py

## Dependencies
os: used to work with the operating system.
dotenv: reading key-value pairs from a .env file
notion and notion_client: used for working with the notion API
csv: A module for reading and writing CSV files.
collections: used to work with data structures like defaultdict

## Edge Cases
- Edge case(Handled): Empty CSV file 
- Edge case(Handled): Missing Field Names
- Edge case(Handled): Missing Values in CSV Rows
- Edge case(Handled): Case Insensitivity
- Edge case(Not Handled): Where code runs more than once and certain rows are removed from the csv file
- Edge Case(not handled): Handling cases for csv files with headers.


