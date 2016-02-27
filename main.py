"""
main.py

Usage:
    main.py (--username=USERNAME | -u=USERNAME) (--password=PASSWORD | -p=PASSWORD) (--load | --store)
    main.py --version
    main.py (-h | --help)

Options:
    -h, --help  Show this help message.
    -v, --version  Show the version and exit.
    -u <USERNAME>, --username <USERNAME>  Username of the account
    -p <PASSWORD>, --password <PASSWORD>  Password of the account
	-l, --load   Load profile from file
	-s, --store  Store profile to file
"""

import time
import praw
from docopt import docopt
from classes import objects
from pprint import pprint
import csv

subs_file = "subs.csv"

def main(options):
    
    #Log in
    r = praw.Reddit(user_agent='Profile manager 1.0')
    r.login(options["--username"], options["--password"], disable_warning=True)
    me = r.user
	
    #Load Subs
    if options["--load"]:
        print "Loading subreddits from file..."
        with open(subs_file, 'rb') as f:
            reader = csv.reader(f)
            subs = list(reader)
            print "Done."
            print "Subscribing to subs:"
            for sub in subs:
                print sub[0]
                r.get_subreddit(sub[0]).subscribe()
        print "Done."
	
    #Retrieve Subs
    elif options["--store"]:
        print "Storing subreddits..."
        with open(subs_file, 'wb+') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            for sub in r.get_my_subreddits(limit=1000):        
                writer.writerow([sub.display_name])
        print "Done."	

		

if __name__ == "__main__":
    options = docopt(__doc__, version='1.0')
    main(options)


