# BOOKS = []


# def createBook():
#     {id='40c06c9c-770a-4f7b-9450-efca205503d6',
#                  title='title1',
#                  author='author1',
#                  description='description1',
#                  rating=10},

#     {id:'50c06c9c-770a-4f7b-9450-efca205503d6',
#                  title:'title2',
#                  author:'author2',
#                  description:'description2',
#                  rating:1},

# {id:'60c06c9c-770a-4f7b-9450-efca205503d6',
# title:'title3',
# author:'author3',
# description:'description3',
# rating:5}

#     book4 = Book(id='70c06c9c-770a-4f7b-9450-efca205503d6',
#                  title='title4',
#                  author='author4',
#                  description='description4',
#                  rating=7)

#     BOOKS.append(book1)
#     BOOKS.append(book2)
#     BOOKS.append(book3)
#     BOOKS.append(book4)

from pydantic import BaseModel, Field
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1)
    rating: int = Field(gt=-1, lt=11)


BOOKS = []


def createBook():
    book1 = {'id': '40c06c9c-770a-4f7b-9450-efca205503d6',
             'title': 'title1',
             'author': 'author1',
             'description': 'description1',
             'rating': 10}

    book2 = {'id': '40c06c9c-770a-4f7b-9450-efca205503d6',
             'title': 'title2',
             'author': 'author2',
             'description': 'description2',
             'rating': 7}

    BOOKS.append(book1)
    BOOKS.append(book2)


def main(author):
    createBook()
    for i in BOOKS:
        if i['author'] == author:
            # print(i)
            return i


# print(main('40c06c9c-770a-4f7b-9450-efca205503d6'))
print(main('author2'))
