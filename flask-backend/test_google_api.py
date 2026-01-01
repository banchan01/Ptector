from dotenv import load_dotenv
import os
from controllers.google_index_controller import get_google_index
import sys

# Load environment variables
load_dotenv()

def test_google_api():
    print("Testing Google Custom Search API...")
    
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    
    if not api_key or not cx:
        print("ERROR: API Key or Search Engine ID not found in .env")
        print(f"Key present: {bool(api_key)}, CX present: {bool(cx)}")
        return

    # Test case 1: Known indexed site
    test_url_1 = "www.google.com"
    print(f"\nChecking URL: {test_url_1}")
    result_1 = get_google_index(test_url_1)
    print(f"Result: {result_1}")
    
    if result_1.get('is_indexed'):
        print("SUCCESS: Google.com identified as indexed.")
    else:
        print("FAILURE: Google.com not found. Check quota or keys.")

    # Test case 2: Random site
    test_url_2 = "this-is-likely-not-a-valid-site-12345.com"
    print(f"\nChecking URL: {test_url_2}")
    result_2 = get_google_index(test_url_2)
    print(f"Result: {result_2}")
    
    if not result_2.get('is_indexed'):
        print("SUCCESS: Random site identified as not indexed.")
    else:
        print("WARNING: Random site found (unexpected).")

if __name__ == "__main__":
    test_google_api()
