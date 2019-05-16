from pyspark import SparkContext
from operator import add

# Reduce
sc = SparkContext("local", "Reduce app")
sc.setLogLevel("ERROR")

nums = sc.parallelize([1, 2, 3, 4, 5])

adding = nums.reduce(add)
print("\n Adding all the elements -> %i" % (adding))


def menos(x, y): return x - y


menosing = nums.reduce(menos)
print("\n Subscrtacing all the elements -> %i" % (menosing))

# Join
x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])
joined = x.join(y)
final = joined.collect()
print("\n Join RDD -> %s" % (final))

# Cache
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)
words.cache()
caching = words.persist().is_cached
print("\n Words got chached > %s" % (caching))
