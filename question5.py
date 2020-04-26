### connect to the mongodb database
from pymongo import MongoClient
client = MongoClient()


### Part two - Create a database named virtual_ebooks
db = client.virtual_ebooks



### Part three - Create collections and insert documents -- populate the database
# First, create the book collections and insert information about book check out records
 
lib_books = db.lib_books

#lib_users = db.lib_users

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



# 5. What comments have been made by any User about such and such book between such and such dates, ordered from the most recent to the least recent.
# - e.g. What comments have been made about "Machien learning" between '2020-03-15' and '2020-04-25'
query5_result = lib_books.find({"bookid" : "99051fe9-6a9c-46c2-b949-38ef78858dd0", "checkout_list.comments.time_commented" : {"$gte" : "2020-03-20", "$lte" : "2020-04-20"}}, {"checkout_list.comments" : 1}).sort("checkout_list.comments", -1)
for x in query5_result:
	print(x)