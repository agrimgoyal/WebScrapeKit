import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.htmlToPdf import convert_html_to_pdf

# Example 1: Convert a single HTML file
convert_html_to_pdf("templates/bhavcopy-downloader.html", "output/single.pdf")

# Example 2: Convert multiple HTML files from a directory
if not os.path.exists("templates"):
    print("Templates directory not found, creating examples first...")
    os.makedirs("output", exist_ok=True)
    
    # Create sample HTML files if needed
    with open("output/sample1.html", "w") as f:
        f.write("<html><body><h1>Sample 1</h1><p>This is a test</p></body></html>")
    with open("output/sample2.html", "w") as f:
        f.write("<html><body><h1>Sample 2</h1><p>This is another test</p></body></html>")
    
    convert_html_to_pdf("output", "output/multiple.pdf")
else:
    convert_html_to_pdf("templates", "output/templates.pdf")

# Example 3: Convert specific files
convert_html_to_pdf(
    ["templates/bhavcopy-downloader.html", "templates/webpage.html"],
    "output/selected.pdf"
)
