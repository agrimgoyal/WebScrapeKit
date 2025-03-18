import requests
import os

def download_webpage(url, output_name=None, output_dir=None):
    """
    Download HTML content from a URL and save it to a file.
    
    Args:
        url (str): URL of the webpage to download
        output_name (str, optional): Base name for the output file (without extension)
        output_dir (str, optional): Directory to save the file
        
    Returns:
        str: Path to the saved file or None if download failed
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Get the webpage name from the URL if not provided
        if not output_name:
            output_name = url.split("/")[-1] or "index"
        
        # Define the filename with '.html' extension
        filename = f"{output_name}.html"
        
        # If output directory is specified, use it
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
        else:
            filepath = filename
        
        # Save the HTML content to the file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(response.text)
        
        print(f"HTML content saved to {filepath}")
        return filepath
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

if __name__ == "__main__":
    # Example usage when script is run directly
    url = "https://www.example.com"
    download_webpage(url)
