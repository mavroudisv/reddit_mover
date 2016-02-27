import datetime
import praw

from functions import utilities

class comment:

    def __init__(self, c_type, content, created, created_utc, subreddit, editted, score, parent):
	#comment/text post/link
	
        self.c_type = c_type #comment type
        self.content = content 
        self.subreddit = subreddit
        self.created = created
        self.created_utc = created_utc
        self.editted = editted #T/F
        self.score = score
        self.parent = parent
        self.last_modified = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def on_edit(self):
        self.last_modified = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


class user:

#last_scanned
#link karma
#comment karma
#trophies
#comments list of comment objects
#subreddits posted in (extracted from list of comments)
#registered
#moderator in
#gold


    def __init__(self, username, id, link_karma, comment_karma, has_verified_email, is_gold, is_mod, mod_subs, comments, created, created_utc, url):
        self.username = username
        self.id = id
        self.link_karma = link_karma
        self.comment_karma = comment_karma
        self.has_verified_email = has_verified_email
        self.is_gold = is_gold
        self.is_mod = is_mod
        self.mod_subs = mod_subs        
        #self.trophies = trophies
        self.comments = comments
        self.subreddits = self.extract_subs(comments)
        self.created = created
        self.created_utc = created_utc
        self.url = url
        self.karma_breakdown = self.breakdown()
        
        
        #self.last_modified = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    #def on_edit(self):
        #self.last_modified = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def extract_subs(self, comments):
        set_temp = Set()
        for c in comments:
            set_temp.add(c.subreddit)   
        return set_temp


    def breakdown(self):
         karma_by_subreddit = {}
         for c in self.comments:
             subreddit = c.subreddit
             #print subreddit
             karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + c.score)
         #import pprint
         #pprint.pprint(karma_by_subreddit)
         return karma_by_subreddit

    def export_comments_to_file(self, filename):
       file_ = open("profiles/"+ filename + ".txt", 'w')
       final_str = ""
       for c in self.comments:
            final_str += utilities.remove_quotes(c.body) + "\n"
       file_.write(final_str)
       file_.close()   		



