# Ptector

Ptector is a URL-based anti-phishing Chrome extension developed as a **CS204 - interconnection of CPS course project at SMU**.<br>
It detects phishing websites in real time using a ML model and provides immediate feedback through a browser extension.

https://github.com/user-attachments/assets/cc699968-08d1-4491-9550-54d7f96a7190


## Features

- Real-time URL analysis
- Machine learning-based phishing detection
- Detailed analysis popup
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/e72e4ff2-172c-46fe-aca0-b2354e6ea149" width="280"/><br/>
      <b>Safe Website</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/d2f21782-d171-4cc7-923b-2a6436bd9ad2" width="280"/><br/>
      <b>Phishing Detected</b>
    </td>
  </tr>
</table>



## Architecture

The project consists of three main components:

1. **Chrome Extension**
   - Content scripts for webpage interaction
   - Background service worker
   - Popup interface for results display

2. **Flask Backend**
   - REST API for URL analysis
   - Integration with ML model
   - Page rank and Google index checking

3. **Machine Learning**
  - **CNN (Raw URL-based)**
    <img width="1359" height="602" alt="image" src="https://github.com/user-attachments/assets/672328f6-6489-4cb9-bb96-32d90e3fea25" />
    Initially trained a CNN model directly on raw URL strings, achieving approximately **92% accuracy**.  
    This approach captured character-level patterns but lacked interpretability and flexibility.
  
  - **DNN (Feature-based)**
    <img width="1394" height="579" alt="image" src="https://github.com/user-attachments/assets/df43c93a-db1b-4004-a359-1102faccab50" />
    Switched to a feature-based DNN after identifying the need for explicit learning of URL characteristics.  
    This improved performance to approximately **95% accuracy** by leveraging structured URL features.
  
  - **Random Forest (Final Model)**
    <img width="1000" height="600" alt="model-rf-5" src="https://github.com/user-attachments/assets/37c1094f-882b-4dce-b684-bcd0706a7ce2" />
    Due to the limited dataset size and model complexity, a Random Forest model was selected as the final approach.  
    Applied **feature importance-based feature selection**, achieving **94% accuracy** with significantly faster inference, making it more suitable for real-time browser usage.


## Installation

1. Install Python dependencies:
- Run `cd flask-backend` to navigate to the backend directory.
- Set-up python virtual environment `python3 -m venv venv`
- Activate the virtual environment with `source venv/bin/activate` (Mac) or `myenv\Scripts\activate` (Windows)
- Install dependencies with `pip install -r requirements.txt`

2. Set up environment variables:
- Create `.env` file in flask-backend directory
- Copy the code and replace 
    ```bash
    # API Keys
    OPENPAGE_API_KEY=<your_openpage_api_key>

    # Google Index API Key
    GOOGLE_API_KEY=<your_google_api_key>
    GOOGLE_SEARCH_ENGINE_ID=<your_google_search_engine_id>

3. Steps to get required API keys
- OpenPage Rank API
    - Visit OpenPageRank : https://www.domcop.com/openpagerank/
    - Create an account/Sign up
    - Navigate to API dashboard
    - Replace `<your_openpage_api_key>` in `.env` with your actual API key

- Google API Key
    - Go to Google Cloud Console : https://console.cloud.google.com/
    - Create new project/Select existing project
    - Go to "APIs & Services" > "Library"
    - Enable "Custom Search API"
    - Go to "Credentials"
    - Create API Key (Create Credentials > API Key)
    - Replace `<your_google_api_key>` in `.env` with your actual API key

- Google Search Engine ID
    - Go to Programmable Search Engine : https://programmablesearchengine.google.com/
    - Click "Create Search Engine"
    - Configure settings:
        - Set search engine name
        - Use "*" for all sites
        - Click "Create" to finalize the setup
        - Copy `Search Engine ID` and replace `<your_google_search_engine_id>` in `.env`
    
4. Load the Chrome extension:
- Open Chrome extensions page
- Enable Developer mode
- Click "Load unpacked"
- Select the /chromeExtension directory

## Usage
1. Start the Flask backend:
    - Run `cd flask-backend` to navigate to the backend directory.
    - Start the app with `python app.py`.
    - Enjoy the extension!

## Tech Stack

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

### Machine Learning
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### APIs
![OpenPageRank](https://img.shields.io/badge/OpenPageRank-2E8B57?style=for-the-badge)
![Google Custom Search](https://img.shields.io/badge/Google%20Search-4285F4?style=for-the-badge&logo=google&logoColor=white)


## License
MIT License

Copyright (c) 2024 banchan_01

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
