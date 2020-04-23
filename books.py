import os,csv
from booksdata import *
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session,sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

def main():
    Base.metadata.create_all(bind=engine)
    f=open("books.csv")
    reader=csv.reader(f)
    next(reader)
    for isbn,title,author,year in reader:
        book=Books(isbn=isbn,title=title,author=author,year=int(year))
        db.add(book)
    db.commit()
    db.close()

if __name__=="__main__":
    main()
