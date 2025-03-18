import os
import pdfkit

def convert_html_to_pdf(html_input, output_pdf):
    """
    Convert HTML file(s) to PDF.
    
    Args:
        html_input (str or list): Path to HTML file, directory of HTML files, or list of file paths
        output_pdf (str): Path for the output PDF file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # If input is a directory, get all HTML files
        if isinstance(html_input, str) and os.path.isdir(html_input):
            html_files = [os.path.join(html_input, f) for f in os.listdir(html_input) if f.endswith('.html')]
            if not html_files:
                print("No HTML files found in the directory.")
                return False
            # Sort files for consistent order
            html_files.sort()
        elif isinstance(html_input, str) and os.path.isfile(html_input):
            html_files = html_input
        elif isinstance(html_input, list):
            html_files = html_input
        else:
            print("Invalid input: must be a file path, directory path, or list of file paths")
            return False
            
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(output_pdf)), exist_ok=True)
        
        # Convert HTML to PDF
        options = {
            'page-size': 'A4',
            'encoding': "UTF-8",
            'quiet': ''
        }
        
        pdfkit.from_file(html_files, output_pdf, options=options)
        print(f"PDF created successfully: {output_pdf}")
        return True
        
    except Exception as e:
        print(f"Error occurred while creating PDF: {e}")
        return False

if __name__ == "__main__":
    # Example usage when script is run directly
    html_directory = "html_pages"  # Change to your directory
    output_pdf_file = "combined.pdf"
    convert_html_to_pdf(html_directory, output_pdf_file)
