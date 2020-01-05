from dev import DevTo


if __name__ == '__main__':
    dev = DevTo('<TOKEN>')
    articles = dev.articles()
    print(articles)