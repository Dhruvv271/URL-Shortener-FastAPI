# URL Shortener (FastAPI + SQLite + Docker)

A Simple URL Shortener built with:
-  FastAPI (Web Framework and API architecture used for Python)
-  SQLite (simple database)
-  Click analytics (counts)
-  Docker support (easy deploy)
-  Ready for cloud hosting (Render)

---

## Features

It allows users to:

- create a short link  
- redirect automatically  
- track clicks + visit history  
- deploy easily anywhere  


## How it works
- User enters a URL into the JSON input. 
`{
    url: "https://www.google.com/"
}`

- Server generates a random short code(for ex: abc123), stores it and returns:
`{
  "short_url": "http://localhost:8000/abc123"
}`
- When the user pastes this link into a browser, they get redirected to the original link and the click counter increments.
- The user can check the analytics in the form of:
```
  {"short_code": "abc123",
  "original_url": "https://example.com",
  "clicks": 5,
  "history": [
    "2025-01-01T12:00:00",
    "2025-01-01T12:03:02"
  ]
  }
```
## Installation(For your local system):
- After cloning the repository, create a venv environment in the directory of your folder.

`python -m venv venv`
`source venv/bin/activate   # Windows: venv\Scripts\activate`

- Install dependencies:
`pip install -r requirements.txt`
- Run the server
`uvicorn main:app --reload`
- Visit the link: 
`http://localhost:8000/docs`

## Link for accessing the interface
- The Docker container for this project was deployed on the cloud for testing using Render web service. The link is:
`https://url-shortener-cx2i.onrender.com/docs`
**Note:** Use the "/docs' in the URL to access the project, its necessary.

