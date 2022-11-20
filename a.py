#!/usr/bin/env python3
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()
import os
print ('<html><body>找了第三者，找到了杀猪盘')
print ("<h2>关于<b>杀猪盘</b>的故事</h2>")
print ("这是一个关于我妻子的故事，她认为她会找到更好的丈夫，但成为 杀猪盘 的受害者仍然不明白")
print ("<hr><br>")


print ('<table>')
i=0
for x in os.listdir("/var/www/html"):
    if (i==0):
        print ("<tr>")
    if ((x.endswith(".mkv")) or (x.endswith('.mp4'))):
        # Prints only text file present in My Folder
#        print("Content-Type: text/html;charset=utf-8")
        print('<td>')
        print ('<video width="500" controls>')
        print('<source src="https://disanzhe.fsmaster.com/'+str(x)+'" type="video/mp4">')
        print('  Your browser does not support t')
        print ('</video>')
        print ('<br>')
        print ('<a href="/'+str(x)+'" download>'+str(x)+'</a>')
        print ('</td>')
        i=i+1
        if (i==3):
            print('</tr>')
            i=0
print ('</table>')
print ('</body></html>')
