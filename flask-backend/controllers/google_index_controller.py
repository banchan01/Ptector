import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv() 

def get_google_index(url):
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

        if not api_key or not search_engine_id:
            print("Google API credentials missing")
            return {'url': url, 'is_indexed': False, 'total_results': '0'}

        parsed = urlparse(url)
        domain = parsed.netloc or url
        domain = domain.strip()

        domain = domain.replace("https://", "").replace("http://", "").strip("/")

        api_url = 'https://www.googleapis.com/customsearch/v1'
        
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': f'site:{domain}'
        }

        response = requests.get(api_url, params=params)
        if response.status_code != 200:
            print(f"Google API HTTP Error: {response.status_code} - {response.text[:200]}")
            return {"url": url, "is_indexed": False, "total_results": 0}
        data = response.json()

        # Check for errors in response
        if 'error' in data:
            print(f"Google API Error: {data['error'].get('message')}")
            return {'url': url, 'is_indexed': False, 'total_results': '0'}
        
        # Check if searchInformation exists and has totalResults
        search_info = data.get('searchInformation', {})
        total_results = search_info.get('totalResults', '0')
        
        # If items list exists, it means results were found
        items = data.get("items", [])
        is_indexed = len(items) > 0

        return {"url": url, "is_indexed": is_indexed, "total_results": total_results}

    except Exception as e:
        print(f'Google Index API Error: {str(e)}')
        return {'url': url, 'is_indexed': False, 'total_results': '0'}