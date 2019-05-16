from pyspark import SparkConf, SparkContext
from pyspark import SparkFiles

# Set a spark config
conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)

# Load a file
finddistance = "/home/hadoop/examples_pyspark/finddistance.R"
finddistancename = "finddistance.R"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
print("Absolute Path -> %s" % SparkFiles.get(finddistancename))

# Choose the storage level
# https://www.tutorialspoint.com/pyspark/pyspark_storagelevel.htm
rdd1 = sc.parallelize([1, 2])
rdd1.persist(pyspark.StorageLevel.MEMORY_AND_DISK_2)
rdd1.getStorageLevel()
print(rdd1.getStorageLevel())
