# Tripago - The AI Powered Travel Guide
## Description
Tripago is a 24hr hackathon project made with the intent of leveraging Generative AI and LLMs to streamline the trip planning process by adding functionality such as -
1. Suggesting a trip plan after taking inputs about a few details from the user and then applying prompt engineering to get a cohesive itinerary plan
2. Creating an itinerary for a travel plan that has been finalized with blank spaces instead of suggestions for omitted details to be shared with friends
3. An AI chatbot to answer all your travel related queries on the go
## Requirements
Python Version: 3.10.13 (other versions might work but have not been tested)
## Setup
1. Create a virtual environment with python version = 3.10.13
2. Open terminal and activate virtual environment
3. Change directory to folder where you want to place the project and run the following code in terminal
   ```
   git clone https://github.com/jai-gaurav/tripago-travel-website.git
   ```
5. Change directory to inside the tripago-travel-website folder
   ```
   cd tripago-travel-website
   ```
6. Install dependencies by running the command in terminal
   ```
   pip install -r requirements.txt
   ```
7. Run the command to run migration and add all tables
   ```
   python manage.py migrate
   ```
8. Start the django server with the following command in terminal
   ```
   python manage.py runserver
   ```
9. Ctrl + Click the link in the output message to navigate to the website
10. Plan your trip
## Credits
All backend development was done by github user jai-gaurav (Jai Gaurav)\
All frontend development was done by github user HimanshuKumarSah (Himanshu Kumar Sah)
