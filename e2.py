import requests

url = 'http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/'

lines = []
with open("election_year_id.txt", "r") as f:
    items = f.read().split('\n')
    for item in items:
        lines.append(item.split())



for line in lines:
    if len(line) < 2:
        continue

    resp = requests.get(url % (line[1]))
    doc2 = year + ".csv"
    with open(doc2, "w") as out:
        out.write(resp.text)
    
