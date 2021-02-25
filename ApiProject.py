import  requests
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
res = r.json()
print(res['data'])

li = res['data'].split(", ")
print(li)
li2 = []
for i in li[1: :2]:
    li2.append(i)
print(li2)


z = li2[0].split("=")
print(z[1])

li3 = []
for i in li2:
    temp = i.split("=")
    li3.append(int(temp[1]))
count = 0
for i in li3:
    if i >= 50:
        count += 1
print(count)