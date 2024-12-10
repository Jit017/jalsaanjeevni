from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data Model for an Article
class Article(BaseModel):
    id: int
    title: str
    content: str
    image_url: str

# In-Memory Database (For Demo)
articles_db: List[Article] = [
    Article(id=1, title="Article Title 1", content="This is the content of article 1.", image_url="https://via.placeholder.com/300x200"),
    Article(id=2, title="Article Title 2", content="This is the content of article 2.", image_url="https://via.placeholder.com/300x200"),
    Article(id=3, title="Article Title 3", content="This is the content of article 3.", image_url="https://via.placeholder.com/300x200"),
]

# API Endpoints

# 1. Get all articles
@app.get("/articles", response_model=List[Article])
def get_articles():
    return articles_db

# 2. Get article by ID
@app.get("/articles/{article_id}", response_model=Article)
def get_article(article_id: int):
    article = next((a for a in articles_db if a.id == article_id), None)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

# 3. Add a new article
@app.post("/articles", response_model=Article)
def add_article(article: Article):
    # Check if ID already exists
    if any(a.id == article.id for a in articles_db):
        raise HTTPException(status_code=400, detail="Article with this ID already exists")
    articles_db.append(article)
    return article

# 4. Update an article
@app.put("/articles/{article_id}", response_model=Article)
def update_article(article_id: int, updated_article: Article):
    for idx, article in enumerate(articles_db):
        if article.id == article_id:
            articles_db[idx] = updated_article
            return updated_article
    raise HTTPException(status_code=404, detail="Article not found")

# 5. Delete an article
@app.delete("/articles/{article_id}")
def delete_article(article_id: int):
    global articles_db
    articles_db = [a for a in articles_db if a.id != article_id]
    return {"message": "Article deleted successfully"}
