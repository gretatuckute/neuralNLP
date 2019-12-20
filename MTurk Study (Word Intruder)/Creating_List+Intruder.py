import random
import copy

list1 = ['mike', 'chris', 'steve', 'matt', 'tim', 'dave', 'jon', 'brian', 'joe']
list2 = ['linux', 'article', 'windows', 'ibm', 'microsoft', 'backup', 'error', 'hp', 'patch']
list3 = ['phone', 'fax', 'info', 'server', 'id', 'rocketshare', 'email', 'windows', 'linux']
list4 = ['article', 'writes', 'email', 'post', 'message', 'posting', 'mail', 'write', 'reply']
list5 = ['windows', 'disk', 'computer', 'ibm', 'software', 'xp', 'gb', 'linux', 'file']
list6 = ['windows', 'file', 'computer', 'linux', 'server', 'disk', 'software', 'files', 'xp']
list7 = ['ibm', 'cs', 'server', 'computer', 'ieee', 'windows', 'hp', 'systems', 'software']
list8 = ['god', 'people', 'israel', 'ca', 'article', 'law', 'americans', 'jesus', 'question']
list9 = ['university', 'stanford', 'college', 'institute', 'sciences', 'harvard', 'engineering', 'mit', 'rutgers']
list10 = ['answer', 'christians', 'ca', 'question', 'israel', 'argument', 'washington', 'id', 'utc']
list11 = ['server', 'university', 'newsgroups', 'linux', 'smtp', 'host', 'nntp', 'ftp', 'servers']
list12 = ['file', 'windows', 'files', 'disk', 'format', 'server', 'mb', 'gb', 'folder']
list13 = ['windows', 'disk', 'file', 'printer', 'scsi', 'interface', 'computer', 'format', 'adapter']
list14 = ['ibm', 'microsoft', 'server', 'linux', 'ieee', 'windows', 'unix', 'intel', 'hp']
list15 = ['reply', 'message', 'linux', 'microsoft', 'unix', 'user', 'email', 'ibm', 'windows']
list16 = ['windows', 'hp', 'ibm', 'xp', 'ghz', 'driver', 'linux', 'gb', 'disk']
list17 = ['printer', 'ibm', 'windows', 'server', 'file', 'hp', 'disk', 'linux', 'xp']
list18 = ['nntp', 'smtp', 'newsgroups', 'usenet', 'ftp', 'server', 'telnet', 'newsgroup', 'mail']
list19 = ['ibm', 'windows', 'hp', 'intel', 'computer', 'linux', 'microsoft', 'xp', 'cpu']
list20 = ['hp', 'ibm', 'engine', 'cs', 'cc', 'systems', 'ieee', 'tech', 'ghz']
list21 = ['file', 'server', 'windows', 'linux', 'ibm', 'unix', 'files', 'format', 'backup']
list22 = ['university', 'linux', 'ibm', 'microsoft', 'tech', 'stanford', 'uc', 'biology', 'engineering']
list23 = ['nhl', 'canadiens', 'mlb', 'bruins', 'yankees', 'sox', 'win', 'game', 'rangers']
list24 = ['linux', 'ibm', 'windows', 'org', 'microsoft', 'server', 'ieee', 'http', 'tech']
list25 = ['game', 'playoffs', 'win', 'nba', 'player', 'nhl', 'mlb', 'sox', 'bruins']
list26 = ['nhl', 'bruins', 'canucks', 'leafs', 'blackhawks', 'canadiens', 'sox', 'yankees', 'puck']
list27 = ['reply', 'linux', 'quote', 'windows', 'microsoft', 'ibm', 'post', 'email', 'message']
list28 = ['windows', 'server', 'linux', 'file', 'unix', 'ibm', 'files', 'error', 'email']
list29 = ['host', 'university', 'hosts', 'server', 'stanford', 'hosting', 'mit', 'uc', 'biology']
list30 = ['posting', 'post', 'reply', 'article', 'posts', 'thread', 'comment', 'email', 'replying']
list31 = ['ibm', 'windows', 'computer', 'linux', 'microsoft', 'hp', 'server', 'intel', 'xp']
list32 = ['writes', 'university', 'linux', 'ibm', 'computer', 'ieee', 'systems', 'server', 'communications']

topicList = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,
list18,list19,list20,list21,list22,list23,list24,list25,list26,list27,list28,list29,list30,list31,list32]

top5_lists = []
top_words = []
for i in range(len(topicList)):
    top = topicList[i][0]
    top5 = topicList[i][:5]
    top_words.append(top)
    top5_lists.append(top5)
#print(top_words)
#print(top5_lists)

topics_forStudy = []
for i in range(len(top5_lists)):
    top_words_new = copy.deepcopy(top_words)
    print("Top word list: ", top_words_new)
    current_list = top5_lists[i]
    print("Current List: ", current_list)
    removee = current_list[0]
    print("Removee: ",removee)
    top_words_new.remove(removee)
    print(top_words_new)
    intruder = random.choice(top_words_new)
    print("Intruder: ", intruder)
    current_list.append(intruder)
    print(len(current_list))
    topics_forStudy.append(current_list)
print(topics_forStudy)

import pandas as pd 
pd.DataFrame(topics_forStudy).to_csv("topicListWithIntruder.csv")