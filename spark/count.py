from pyspark import SparkContext

sc = SparkContext("local", "count app")
sc.setLogLevel("ERROR")
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

counts = words.count()
print("\n")
print("Number of elements in RDD -> %i" % (counts))

coll = words.collect()
print("\n")
print("Elements in RDD -> %s" % (coll))

def f(x): print(x)
fore = words.foreach(f)
