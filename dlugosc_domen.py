import requests

url = 'https://zajecia-programowania-xd.pl/flagi'
raw_info = requests.get( url)
text = raw_info.text

line_list = text.split('</p>')
links = []

for linia in line_list:
    if linia:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        links.append( link)

def longest_string(list) :
    longest = max(list, key = len)
    shortest = min(list, key = len)
    return longest, shortest

list_flag = longest_string(links)

for l in list_flag:
    print(l, len(l))
