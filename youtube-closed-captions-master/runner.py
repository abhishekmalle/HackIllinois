from ytcc.download import Download
#from textstat.textstat import textstat
import string

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
a,b = url.split("?v=")
video_id = b
download = Download()
captions = download.get_captions(video_id)
print (captions)
#captions = ''.join([x for x in captions if x in string.ascii_letters + '\'- '])
#print(captions)
#words = []
#oldValue = 0
#for value in range(len(captions)):
#    if captions[value] == captions[value].upper():
#        words.append(captions[oldValue:value+1])
#print(words)
print(captions)
#print(textstat.automated_readability_index(captions))
