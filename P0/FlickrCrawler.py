import re
import httplib
import urllib2
from urlparse import urlparse
#from bs4 import BeautifulSoup
from collections import namedtuple
import csv
import time
import flickrapi
import json


class Crawler:
        seedUrl = ''
        apiKey = 'baadf1d312ede47ad550ea25d68b0c3a'
        apiSecret = 'a9443794da982105'
        flickrClient=flickrapi.FlickrAPI(apiKey,apiSecret)


        #flickrurl = re.compile('https://www.flickr.com//people/'+r'([a-z|0-9]*)')


        def __init__(self):
            self.self = self



        def getUserName(self,userid):
            user = self.flickrClient.people_getInfo(user_id=userid, format='json',nojsoncallback=1)
            jdata = json.loads(user)
            person = jdata['person']
            usercontent = person['username']
            username = usercontent['_content']
            print user
            return username


        def getContacts(self, userid):
            contactjson = self.flickrClient.contacts_getPublicList(user_id=userid,format='json',nojsoncallback=1)
            actualcontactjson = json.loads(contactjson)
            username = []
            jumpedcontacts = []
            i=0
            pages = actualcontactjson['contacts']['pages']
            page = 1
            try:
                while (page > pages) is not True:
                    localcontactjson = self.flickrClient.contacts_getPublicList(user_id=userid,format='json',nojsoncallback=1,page=page)
                    localactualjson = json.loads(localcontactjson)
                    contacts = localactualjson['contacts']['contact']
                    # if len(contacts) > 700 :
                    #    jumpedcontacts = contacts[:700:1]
                    #else:
                #    jumpedcontacts = contacts[:len(contacts):1]
                    for contact in contacts: #jumpedcontacts
                        username.append([contact['username'],contact['nsid']])
                    page = page+1
                print len(username)
                return username
            except KeyError:
                return None


        #def getNoOfFreinds(self,userid):
        #    urlToOpen = 'https://www.flickr.com/people/'+userid+'/contacts'
         #   pageresource = urllib2.urlopen(urlToOpen)
         #   s = pageresource.read()
         #   soup = BeautifulSoup(s)
         #   link = soup.find('div', attrs ={'class' : 'Results'}).contents
         #   numberFriends = (link[0].split(' ')[0].split('(')[1])
         #   number = ''
         #   if numberFriends.find(','):
          #      numberFriendsSplitted = numberFriends.split(',')
          #      numberString = ''.join(numberFriendsSplitted)
           #     return int(numberString)
           # else:
           #     number = int(numberFriends)
           #     return number

        def crawler(self, userid ):
            tocrawl = [userid]
            crawled = []
            i = 1
            j = 1
            dict = {}
            try:
                resultFile = open('D://EdgeList.csv','w')
            except IOError:
                print 'Error'
            csvwriter = csv.writer(resultFile , delimiter=',')

            try:
                mappingFile = open('D://Mapping.csv','w')
            except IOError:
                print 'Error'
            mappingwriter = csv.writer(mappingFile, delimiter=',')

            try:
                anonymizedFile = open('D://AnonymizedEdgeList.csv','w')
            except IOError:
                print 'Error'
            anonymizedwriter = csv.writer(anonymizedFile, delimiter = ',')

            dict[userid] = i
            mappingwriter.writerow([userid, dict[userid]])
            while tocrawl:
                nextUser=tocrawl.pop(0)
                print 'Crawled:'+nextUser + ' ' + str(j)
                j = j+1
                contacts = self.getContacts(nextUser)
                if contacts is None:
                    continue
                if nextUser not in crawled:
                    for username,flickrid in contacts:
                        utf8Usernamesplitted = unicode(username).encode('utf-8').split('\n')
                        utf8Username = ''.join(utf8Usernamesplitted)


                        if flickrid not in dict.keys():
                            i=i+1
                            dict[flickrid] = i
                            mappingwriter.writerow([flickrid, dict[flickrid]])
                            mappingFile.flush()
                            time.sleep(0.0000001)
                            tocrawl.append(flickrid)

                        try:
                            print utf8Username
                            print dict[flickrid]
                        except Exception:
                            print 'cant print username'



                        #explored.append([id],)
                        csvwriter.writerow([nextUser, flickrid])
                        resultFile.flush()
                        time.sleep(0.0000001)

                        anonymizedwriter.writerow([dict[nextUser], dict[flickrid]])
                        anonymizedFile.flush()
                        time.sleep(0.0000001)

                            #write mapping into the mapping file
                        #isValidUrl(l['href'])
                    crawled.append(nextUser)
                #print explored
                #csvwriter.writerows(explored)
                if j > 1000:
                    break
            resultFile.close()
            mappingFile.close()
            anonymizedFile.close()
            return crawled

inp = raw_input('Enter User ID:')
crawler1 = Crawler()
out=crawler1.getUserName(inp)
print out
username=[]
username=crawler1.getContacts(inp)
print username
crawler1.crawler(inp)


#printer = crawler1.getNoOfFreinds(inp)
#print printer
#crawleddata = crawler1.crawler(inp)
#print crawleddata


#username = raw_input('Please enter username')
#crawler('https://flickr.com/people/'+username+'/contacts/')
