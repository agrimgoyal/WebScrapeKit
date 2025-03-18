import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.page_html import download_webpage

# Example 1: Basic usage
webpage = download_webpage("https://www.example.com", "example")
print(f"Downloaded page: {webpage}")

# Example 2: Save to specific directory
webpage = download_webpage(
    "https://www.python.org",
    "python_homepage",
    "downloaded_pages"
)
print(f"Downloaded page to specific directory: {webpage}")

# Example 3: Handle errors gracefully
result = download_webpage("https://nonexistentwebsite123456789.org")
if not result:
    print("Failed to download non-existent website as expected")
