# WebScrapeKit

A collection of Python utilities for web scraping, HTML content manipulation, and document conversion. This toolkit helps developers automate the process of retrieving web content and transforming it into different formats.

## Overview

WebScrapeKit provides modular scripts that can be used individually or together to:
- Download HTML content from websites
- Extract and process specific HTML elements
- Convert HTML documents to PDF files
- Manipulate and transform web page structures

## Features

- **HTML Downloader**: Simple utility to fetch and save HTML content from any URL
- **HTML to PDF Converter**: Convert single or multiple HTML files to PDF documents
- **Bhavcopy HTML Template**: Sample HTML template for financial data presentation
- **Web Content Parser**: Extract specific components from web pages

##  Technologies Used

- **Python 3.7+**: Core programming language
- **Requests**: For HTTP requests and web page retrieval
- **pdfkit**: HTML to PDF conversion (wrapper for wkhtmltopdf)
- **BeautifulSoup4**: HTML parsing and manipulation (commented in code)
- **OS module**: File and directory handling

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/WebScrapeKit.git
   cd WebScrapeKit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install wkhtmltopdf (required for pdfkit):
   - **Windows**: Download from [wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html)
   - **macOS**: `brew install wkhtmltopdf`
   - **Linux**: `sudo apt-get install wkhtmltopdf`

## Requirements

Create a `requirements.txt` file in the repository with:
```
requests==2.28.2
pdfkit==1.0.0
beautifulsoup4==4.11.2
```

## Usage

### HTML Page Downloader

Download HTML content from a specific URL:

```python
from scripts.page_html import download_webpage

# Download a webpage
download_webpage("https://example.com", "example")
```

### HTML to PDF Converter

Convert a directory of HTML files to a single PDF:

```python
from scripts.htmlToPdf import convert_html_to_pdf

# Convert HTML files to PDF
convert_html_to_pdf("html_pages", "output.pdf")
```

## Project Structure

```
WebScrapeKit/
├── scripts/
│   ├── __init__.py
│   ├── page_html.py         # HTML downloading script
│   ├── htmlToPdf.py         # HTML to PDF conversion script
│   └── extract_links.py     # Link extraction utility (to be implemented)
├── templates/
│   ├── bhavcopy-downloader.html  # Sample HTML template
├── examples/
│   ├── download_example.py  # Usage examples
│   └── convert_example.py   # Conversion examples
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Challenges Overcome

- **Cross-platform compatibility**: Ensured the PDF conversion works consistently across different operating systems
- **Character encoding handling**: Implemented proper UTF-8 encoding to handle international characters
- **Error handling**: Added robust exception handling for network issues and failed conversions
- **Resource management**: Optimized file operations to handle large HTML files efficiently

## Future Enhancements

- Add support for JavaScript-rendered websites using Selenium
- Implement parallel processing for batch PDF conversions
- Create a command-line interface (CLI) for easier usage
- Develop a simple GUI using Tkinter or PyQt
- Add support for additional output formats (EPUB, DOCX)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
