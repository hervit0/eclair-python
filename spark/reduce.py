from pyspark import SparkContext
from operator import add

sc = SparkContext("local", "Reduce app")
sc.setLogLevel("ERROR")

nums = sc.parallelize([1, 2, 3, 4, 5])

adding = nums.reduce(add)
print("\n Adding all the elements 1 -> %i" % (adding))

# def f(x, y): x + y
# adding2 = nums.reduce(f)
# print("Adding all the elements 2 -> %i" % (adding2))

x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])
joined = x.join(y)
final = joined.collect()
print("\n Join RDD -> %s" % (final))
