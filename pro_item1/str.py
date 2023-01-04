s = "hell\nwwww0"
s = "hell\twwww0"
s = 'hell\"nwwww0'
s = 'hell"nwwww0'
s = 'hell\\nwwww0'

s = r"hell\nwwww0"
# s = "hell\twwww0"
# s = 'hell\"nwwww0'
# s = 'hell"nwwww0'
# s = 'hell\\nwwww0'

# s = '''hell\ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# ddddddddddddddddddddddddddddddddddddddddddddddddddddd
# dddddddddddnwwww'''

print(s)

ss = int("80")
ss = float("80.0")

ss=int("AB",16)
i=32
ss='i*i='+str(i*i)
ss='i*i={}'.format(i*i)
ss='{0}*{0}={1}'.format(i,i*i)
ss='{p1}*{p1}={p2}'.format(p1=i,p2=i*i)

print(ss)
money=5845.55
name="tom"

print('{0:s}的年龄是:{1:d},工资是{2:f}'.format(name,20,money))
print('{0}的年龄是:{1},工资是{2:0.2f}'.format(name,20,money))
print('{0}的今天收入是{1:G}'.format(name,money))
print('{0}的今天收入是{1:e}'.format(name,money))
print('十进制的数{0:d}转八进制的值是{0:o}'.format(18))
print('十进制的数{0:d}转十六进制的值是{0:x}'.format(18))


ssss='Hrrdrrooessd'

print(ssss.find('e'))
print(ssss.find('d',5))
print(ssss.find('d',5,10))


tx='AB CD EF G0'
print(tx.replace(' ','|',2))

print(tx.split(' '))
print(tx.split(' ',maxsplit=0))
print(tx.split(' ',maxsplit=1))
print(tx.split(' ',maxsplit=2))



wordString='''
    it was the best times it was the worst times.
    it was the age of wisdom it was the age of foolishness.
    '''

wordString=wordString.replace(".",'')
wordList = wordString.split()
print(wordList)
worsres=[]
for w in wordList:
    worsres.append(wordList.count(w))

d=dict(zip(wordList,worsres))
print(d)

print('{0:3}'.format('Pyhon'))

s='Hello World'
print(s[-4:-1])
