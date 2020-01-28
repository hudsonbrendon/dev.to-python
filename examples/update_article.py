from dev import DevTo

from decouple import config


if __name__ == "__main__":

    article = {
        "article": {
            "title": "Post Test",
            "published": True,
            "body_markdown": "Hello DEV, this is my first post test",
            "tags": ["discuss", "help"],
            "series": "Hello series",
            "canonical_url": "https://example.com/blog/hello/teste",
        }
    }

    dev_to = DevTo(api_key=config("API_KEY"))
    print(dev_to.update_article(article=article))
