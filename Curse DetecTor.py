import urllib

def read_text():
 quotes = open("/home/pavan/test.txt")
 contents_of_file = quotes.read()
 #print(contents_of_file)
 quotes.close()
 check_profanity(contents_of_file)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
         print("Profanity Alert!!")
    elif "false" in output:
         print("This Document has no Curse Words!!")
    else:
         print("Could Not scan the Document properly.")
         
read_text()
    
