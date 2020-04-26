######## Part 1 - Database design
""" 
This MongoDB contains two collections: lib_books and lib_users, which stores the information of eBooks and the details of users respectively. 
Within the lib_books collection(table), each document(row) represents check out records of each book.
Each document in lib_books includes bookid, title, author-combines primary author and secondary author as an array, date_of_first_publication, number_of_pages, publisher, translator, topics, and a user check out list.
Within each check out record of the book, it contains three comments and time of each comment that the user havs given to this book, the comments field is an array.
Within the lib_users collection, each document represents a user and books he/she has checked out before. 
Each document contains userid, name, phone, address, university_affiliation, and the book_list(an array includeing bookid, topics, date_checked_out, and comments that he/she has given), which stores the books that this user has checked out.
The reason why I designed the MongoDB like this is that it can be far efficient using the MongoDB feature to embed data whenever we can.
"""



### connect to the mongodb database
from pymongo import MongoClient
client = MongoClient()


######## Part 2 - Create a database named virtual_ebooks
db = client.virtual_ebooks



######## Part 3 - Create collections and insert documents -- populate the database
# First, create the book collections and insert information about book check out records

lib_books = db.lib_books

document_book1 = ({
	"bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0",
	"title" : "Machine learning",
	"author" : "Tom Michael",
	"date_of_first_publication" : "2000-10-02",
	"number_of_pages" : 414,
	"publisher" : "New York : McGraw-Hill",
	"topics" : ["Machine learning", "Computer algorithms"],
	"checkout_list" : [
	{
    	"time_checked_out" : "2020-03-20 09:11:22",
    	"userid" : "ef1234",
    	"comments" : [
    	{
    		"comment1" : "I just finished it and it is worth learning!",
    		"time_commented" : "2020-04-01 10:35:13"
    	},
    	{
    		"comment2" : "Some cases are a little bit outdated.",
    		"time_commented" : "2020-03-25 13:19:13"
    	},
    	{
    		"comment3" : "Can't wait to learning it!!!",
    		"time_commented" : "2020-03-21 08:21:42"
    	}]
    },
	{
		"time_checked_out" : "2020-03-04 16:18:02",
		"userid" : "ab1234",
		"comments" : [
		{
			"comment1" : "The book is a little bit difficult but worth reading.",
			"time_commented" : "2020-03-20 12:18:02"
		},
		{
			"comment2" : "It's hard and takes a lot of time to understand",
			"time_commented" : "2020-03-15 11:22:42"
		},
		{
			"comment3" : "I just start reading, the principle of model is well explained.",
			"time_commented" : "2020-03-05 09:11:42"
		}]
	}]
})

book1 = lib_books.insert_one(document_book1)

document_book2 = ({
	"bookid" : "99052fe9-6a9c-46c2-b949-38ef78858dd0",
	"title" : "1984",
	"author" : "George Orwell",
	"date_of_first_publication" : "1983-10-17",
	"number_of_pages" : 237,
	"publisher" : "Houghton Mifflin Harcourt",
	"topics" : "Fiction",
	"checkout_list" : {
		"time_checked_out" : "2020-03-30 11:12:32",
		"userid" : "cd1234",
		"comments" : [{
			"comment1" : "This is the fourth time I read the 1984!",
			"time_commented" : "2020-03-30 11:20:32"
		},
		{
			"comment2" : "The scenarios just like nowadays.",
			"time_commented" : "2020-04-05 14:20:32"
		},
		{
			"comment3" : "This is my favorite book and it is also the best book I have ever read!",
			"time_commented" : "2020-04-10 10:12:32"
		}]
	}
})

book2 = lib_books.insert_one(document_book2)


document_book3 = ({
	"bookid" : "99053fe9-6a9c-46c2-b949-38ef78858dd0",
	"title" : "Introduction to Machine Learning with Python: A Guide for Data Scientists",
	"author" : "Andreas Müller",
	"date_of_first_publication" : "2016-09-26",
	"number_of_pages" : 402,
	"publisher" : "OReilly Media",
	"topics" : ["Machine learning", "Computer algorithms"],
	"checkout_list" : [{
		"time_checked_out" : "2020-04-10 15:03:28",
		"userid" : "gh1234",
		"comments" : [{
			"comment1" : "The professor asked us to read this book, it helps a lot while taking the machine learning class.",
			"time_commented" : "2020-04-15 15:03:28"
		},
		{
			"comment2" : "The book mainly focuses on the application of machine learning",
			"time_commented" : "2020-04-15 21:03:28"
		},
		{
			"comment3" : "It helps me greatly and I will dive much deeper into machine learning right now!",
			"time_commented" : "2020-04-25 16:21:08"
		}]
	},
    {
    	"time_checked_out" : "2020-03-01 15:21:45",
    	"userid" : "jh1234",
    	"comments" : [{
			"comment1" : "Very well explained and easy to understand.",
			"time_commented" : "2020-03-05 11:03:28"
		},
		{
			"comment2" : "The book doesn't tell too much about the models' mathematical details!",
			"time_commented" : "2020-03-13 21:03:28"
		},
		{
			"comment3" : "You should start from this book if you want to know about machine learning.",
			"time_commented" : "2020-03-25 16:21:08"
		}]
    }]
})

book3 = lib_books.insert_one(document_book3)


document_book4 = ({
	"bookid" : "99054fe9-6a9c-46c2-b949-38ef78858dd0",
	"title" : "The little prince",
	"author" : "Saint-Exupéry, Antoine de",
	"date_of_first_publication" : "2000-05-15",
	"number_of_pages" : 96,
	"publisher" : "Mariner Books",
	"topics" : "Fiction",
	"checkout_list" : {
		"time_checked_out" : "2020-04-01 09:21:19",
		"userid" : "jh1234",
		"comments" : [{
			"comment1" : "It is always fun and educated every time I read the little prince!",
			"time_commented" : "2020-04-21 11:03:28"
		},
		{
			"comment2" : "All grown-ups were once children, but only few of them remember it.",
			"time_commented" : "2020-04-05 21:03:28"
		},
		{
			"comment3" : "The book still teaches me a lot even if I am an adult right now!",
			"time_commented" : "2020-04-10 16:21:08"
		}]
	}
})

book4 = lib_books.insert_one(document_book4)




# Second, create user collections and insert information about user details

lib_users = db.lib_users

document_user1 = ({
	"userid" : "ab1234",
	"name" : "Anna Bain",
	"phone" : "111-222-1212",
	"address" : "W 109th St",
	"university_affiliation" : "Columbia University",
	"book_list" : [{
		"bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : ["Machine learning", "Computer algorithms"],
		"time_checked_out" : "2020-03-04 16:18:02",
		"comments" : [{
			"comment1" : "The book is a little bit difficult but worth reading.",
			"time_commented" : "2020-03-20 12:18:02"
		},
		{
			"comment2" : "I just start reading, the principle of model is well explained.",
			"time_commented" : "2020-03-05 09:11:42"
		},
		{
			"comment3" : "It's hard and takes a lot of time to understand",
			"time_commented" : "2020-03-15 11:22:42"
		}]
	}]
})

user1 = lib_users.insert_one(document_user1)


document_user2 = ({
	"userid" : "cd1234",
	"name" : "Cat Dabbs",
	"phone" : "222-111-3131",
	"address" : "W 108th St",
	"university_affiliation" : "Columbia University",
	"book_list" : [{
		"bookid" : "99052fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : "Fiction",
		"time_checked_out" : "2020-03-30 11:12:32",
		"comments" : [{
			"comment1" : "This is the fourth time I read the 1984!",
			"time_commented" : "2020-03-30 11:20:32"
		},
		{
			"comment2" : "The scenarios just like nowadays.",
			"time_commented" : "2020-04-05 14:20:32"
		},
		{
			"comment3" : "This is my favorite book and it is also the best book I have ever read!",
			"time_commented" : "2020-04-10 10:12:32"
		}]
	}]
})

user2 = lib_users.insert_one(document_user2)


document_user3 = ({
	"userid" : "ef1234",
	"name" : "Eva Faber",
	"phone" : "333-221-1234",
	"address" : "W 107th St",
	"university_affiliation" : "Columbia University",
	"book_list" : [{
		"bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : ["Machine learning", "Computer algorithms"],
		"time_checked_out" : "2020-03-20 09:11:22",
		"comments" : [{
    		"comment1" : "Can't wait to learning it!!!",
    		"time_commented" : "2020-03-21 08:21:42"
    	},
    	{
    		"comment2" : "Some cases are a little bit outdated.",
    		"time_commented" : "2020-03-25 13:19:13"
    	},
    	{
    		"comment3" : "I just finished it and it is worth learning!",
    		"time_commented" : "2020-04-01 10:35:13"
    	}]
	}]
})

user3 = lib_users.insert_one(document_user3)


document_user4 = ({
	"userid" : "gh1234",
	"name" : "George Hack",
	"phone" : "900-222-1212",
	"address" : "W 106th St",
	"university_affiliation" : "New York University",
	"book_list" : [{
		"bookid" : "99053fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : ["Machine learning", "Computer algorithms"],
		"time_checked_out" : "2020-04-10 15:03:28",
		"comments" : [{
			"comment1" : "The professor asked us to read this book, it helps a lot while taking the machine learning class.",
			"time_commented" : "2020-04-15 15:03:28"
		},
		{
			"comment2" : "The book mainly focuses on the application of machine learning",
			"time_commented" : "2020-04-15 21:03:28"
		},
		{
			"comment3" : "It helps me greatly and I will dive much deeper into machine learning right now!",
			"time_commented" : "2020-04-25 16:21:08"
		}]
	}]
})

user4 = lib_users.insert_one(document_user4)


document_user5 = ({
	"userid" : "jh1234",
	"name" : "Jun Hui",
	"phone" : "361-111-3131",
	"address" : "W 105th St",
	"book_list" : [{
		"bookid" : "99054fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : "Fiction",
		"time_checked_out" : "2020-04-01 09:21:19",
		"comments" : [{
			"comment1" : "It is always fun and educated every time I read the little prince!",
			"time_commented" : "2020-04-21 11:03:28"
		},
		{
			"comment2" : "All grown-ups were once children, but only few of them remember it.",
			"time_commented" : "2020-04-05 21:03:28"
		},
		{
			"comment3" : "The book still teaches me a lot even if I am an adult right now!",
			"time_commented" : "2020-04-10 16:21:08"
		}]	
	    },
	    {
		"bookid" : "99053fe9-6a9c-46c2-b949-38ef78858dd0",
		"topics" : ["Machine learning", "Computer algorithms"],
		"time_checked_out" : "2020-03-01 15:21:45",
		"comments" : [{
			"comment1" : "Very well explained and easy to understand.",
			"time_commented" : "2020-03-05 11:03:28"
		},
		{
			"comment2" : "The book doesn't tell too much about the models' mathematical details!",
			"time_commented" : "2020-03-13 21:03:28"
		},
		{
			"comment3" : "You should start from this book if you want to know about machine learning.",
			"time_commented" : "2020-03-25 16:21:08"
		}]
	}]
})

user5 = lib_users.insert_one(document_user5)



######## Part 4 - The code for the queries


# Query 1. Which books have been checked out since such and such date - e.g. which books have been checked out since '2020-03-15'
query1_result = lib_books.find({"checkout_list.time_checked_out" : {"$gte": "2020-03-15"}}, {"title" : 1})
for x in query1_result:
	print(x)


# Query 2. Which users have checked out such and such book - e.g. which users have checked out 'Machine Learning'
query2 = {"book_list.bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0"}
query2_result = lib_users.find({"book_list.bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0"}, {"name" : 1})
for x in query2_result:
	print(x)


# Query 3. How many books does the library have on such and such topic - e.g. How many books does the library have on fiction
query3 = lib_books.aggregate([
	{"$group" : {"_id": "$topics", "number": {"$sum": 1}}}
])
for x in query3:
	print(x)



# Query 4. Which users from Columbia University have checked out books on Machine Learning between this date and that date - e.g. between '2020-03-15' and '2020-04-15'
query4_result = lib_users.find({"university_affiliation" : "Columbia University", "book_list.topics": "Machine learning", "book_list.time_checked_out" : {"$gte" : "2020-03-15", "$lte" : "2020-04-15"}}, {"name" : 1})
for x in query4_result:
	print(x)



# Query 5. What comments have been made by any User about such and such book between such and such dates, ordered from the most recent to the least recent.
# - e.g. What comments have been made about any book between '2020-03-20' and '2020-04-20'
pipeline = [{'$unwind':'$checkout_list'},
            {'$unwind':'$checkout_list.comments'},
            {'$match':{'checkout_list.comments.time_commented':{"$gte" : "2020-03-20", "$lte" : "2020-04-20"}}},
            {'$project':{'_id':0,'bookid':1,'title':1,'comment':'$checkout_list.comments.comment','time_commented':'$checkout_list.comments.time_commented'}},
            {'$sort':{'time_commented':-1}}]
query5_result = lib_books.aggregate(pipeline)
for x in query5_result:
	print(x)


# Query 6. Show for a given User, what comments they have made about such and such book. - e.g. User "Jun Hui"(userid - jh1234), for book "Introduction to Machine Learning with Python: A Guide for Data Scientists"
query6_result = lib_users.find({"userid" : "gh1234", "book_list.bookid" : "99053fe9-6a9c-46c2-b949-38ef78858dd0"}, {"book_list.comments" : 1})
for x in query6_result:
	print(x)








### here is the code just to test my database and redesign
#lib_books.delete_many({})
#lib_users.delete_many({})

