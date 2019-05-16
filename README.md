# Eclair Python :snake:

My experiences, tutos, codewars around Python...

I need it for the machine learning we are carrying out at the moment.

## Notes

Run a pySpark script:
```
spark-submit spark/reduce.py
```

For this warning `UserWarning: Please install psutil to have better support with spilling`, as I'm running under python 3, I need to do that:
```
pip3 install psutil
```

To reduce the logs:
```
sc.setLogLevel("ERROR")
```

Adding libraries:
```
pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

## Resources

- [PySpark context API doc](https://spark.apache.org/docs/2.2.0/api/python/pyspark.html#pyspark.SparkContext)
