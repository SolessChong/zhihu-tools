import zhihu
import pickle

user_url = "http://www.zhihu.com/people/rush"
user = zhihu.User(user_url)

fs = []
followees = user.get_followees()
print user.get_followees_num()
for f in followees:
	print '.',
	fs.append((f.get_followers_num(), f))
print ' '
fs = sorted(fs, key=lambda f: f[0], reverse=True)
followees_file = open('followees.pkl', 'wb')
pickle.dump([(f[0], f[1].user_url) for f in fs], followees_file)
followees_file.close()

questions = []
for i in range(10):
	qs = fs[i][1].get_asks()
	for j in range(min(3, fs[i][1].get_asks_num())):
		q = qs.next()
		questions.append((q.get_answers_num(), q))

qs_meta = [(q[1].get_answers_num(), q[1].get_topics(), q[1].url, q[1].get_title()) for q in questions]
qs_meta = sorted(qs_meta, key=lambda q: q[0])

f = open('questions.txt', 'wb')
for q in qs_meta:
	f.write('%6d, %s\n' % (q[0], q[3]))
	for t in q[1]:
		f.write('%6s, ' % t)
	f.write('\n%s\n' % (q[2]))
	f.write('============================\n')

f.close()