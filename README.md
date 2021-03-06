# MongoDB Connection
Create a virtual e-Books MongoDB database and connecting to it through Python (Using PyMongo)
In this project, I created a database for a virtual library. The books from the library can be be “checked out” by Users for a fixed period of time. For this assignment let us assume that books cannot be renewed. A User may check out any number of books at a time. Since the books are eBooks, any number of Users can check out a book at the same time.

+ The library contains a collection of eBooks. Basic information about each book needs to be stored: Title, primary author, secondary authors (if any), date of first publication, number of pages, publisher, translator (if any)
+ For non-fiction books, a list of the key topics covered by the book needs to be stored. For works of fiction (including poems, plays, novels, collection of stories), the topic is just ‘fiction’.
+ For each book, we also need to store information about when it was checked out by which User.
+ For each User we need to store certain information: User id, name, phone, address, university affiliation (if any)
+ For each book and User, we need to store the comments made about the book by the User

This mongodb connection can also fulfill such queries:
+ Which books have been checked out since such and such date
+ Which users have checked out such and such book
+ How many books does the library have on such and such topic
+ Which users from Columbia University have checked out books on Machine Learning between this date and that date.
+ What comments have been made by any User about such and such book between such and such dates, ordered from the most recent to the least recent.
+ Show for a given User, what comments they have made about such and such book.
