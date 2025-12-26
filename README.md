# URL Shortener - (FastAPI + SQLite + Docker + Render)
A simple URL Shortener built with:
- FastAPI - Web framework for building HTTP based APIs in Python
- SQLite - Simple Database
- Click Analytics(counts)
- Docker - Used to Containerize for deployment
- Render - Web service used for cloud hosting and deployment
It allows users to:

1) create a short link  
2) redirect automatically  
3) track clicks + visit history  
4) deploy easily anywhere 

# How It Works:
1) User enters a URL with json: 

for instance, { 
    "url" : "https://example.com"
}
2) Server generates a random code (for example: abc123), stores it and returns:
{
    "short_url": "https://localhost:8000/abc123
}
3) When the user pastes the short URL in the browser, it redirects to the original URL and it records a click.
4) User can access analytics in the form of:
{
  "short_code": "abc123",
  "original_url": "https://example.com",
  "clicks": 5,
  "history": [
    "2025-01-01T12:00:00",
    "2025-01-01T12:03:02"
  ]
}
# Installation(For local use):
1) After cloning the repo in your local system, create a "venv" environment by using the following command in your project directory:
`python -m venv venv`
then, activate the environment: `venv\Scripts\activate` (For Windows)
2) Install Dependencies:
`pip install -r requirements.txt`
3) Run the server:
`uvicorn main:app --reload`
4) Visit: http://localhost:8000/docs
5) Test By posting a URL and get the shortened URL and analytics.
# Deployed:
The containerized image was deployed using render web service. A Working link is: https://url-shortener-cx2i.onrender.com/docs
Note: The "/docs" extension is required for the link to work.