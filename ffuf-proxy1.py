import os
import sys

folder = sys.argv[4]
os.system("mkdir /var/www/html/contentdis/" + folder + "/")
word= sys.argv[3]
pref = sys.argv[5]
wordlist = "/payloads/new/" + word
count = 0

for line in open(sys.argv[1], "r+").readlines():
    line = line.split("\n")
    line = line[0]
    file = line.split("://")
    protocol = file[0]
    file = file[1]
    file = file.split("/")
    file = file[0]
    part2 = word.replace(".txt", "")
    filename = word + "_" + protocol + "_" + file + pref + "" + "+" + str(count) + ".html"
    full_path = "/var/www/html/contentdis/" + folder + "/" + filename
    print("Write to: " + full_path)
    command = "ffuf -c -mc 301,200,500,302,401 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0' -of html -o " + full_path + " -t 100 -rate 150 -w " + wordlist + " -u " + line + "/FUZZ" + sys.argv[2]
    os.system(command)
   # os.system("service tor restart")
    count = count + 1
