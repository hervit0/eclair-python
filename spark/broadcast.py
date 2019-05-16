from pyspark import SparkContext
sc = SparkContext("local", "Broadcast app")
sc.setLogLevel("ERROR")

# Broadcast
words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"])
data = words_new.value
print("\n Stored data -> %s" % (data))
elem = words_new.value[2]
print("\n Printing a particular element in RDD -> %s" % (elem))


# Accumulator
num = sc.accumulator(10)


def f(x):
  # this is super nasty imo
    global num
    num += x


rdd = sc.parallelize([20, 30, 40, 50])
rdd.foreach(f)
final = num.value
print("\n Accumulated value is -> %i" % (final))
