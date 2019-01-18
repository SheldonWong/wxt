from pyspark import SparkContext, SparkConf
import numpy as np

conf = SparkConf().setAppName('gg').setMaster('local')
sc = SparkContext(conf=conf)

text = sc.textFile('file:///gradient/spam.data.txt')
#print(data.take(4))

def tofloat(x):
	x_s = x.split()
	return np.array([float(e) for e in x_s])

def sigmoid(w,x):
	return 1.0 / (1.0 + np.exp(np.dot(w,x)))

#def fit():
	
lines = text.map(tofloat)
#print(lines.take(2))

data = lines.map(lambda x: (x[:-1],x[-1]))
#print()
print(data.take(1))
print('feature:',data.take(1)[0][0])
print('label:',data.take(1)[0][1])

a = lines.take(1)
w_l = a[0].shape[0]-1


w = np.random.rand(w_l)
iterations = 10

for i in range(20):
	likehood = data.map(lambda p: (p[1]*sigmoid(w,p[0]) + (1.0 - p[1])*(1.0 - sigmoid(w,p[0]))) ).reduce(lambda x,y:x+y)
	if(i%5 == 0):
		print("likehood:",likehood)
	gradient = data.map(lambda p: p[0] * (p[1] - sigmoid(w,p[0]))).reduce(lambda x,y:x+y)
	w += 0.01 * gradient

print(w)


