log = "file:///Users/h.ah-leung/sandbox/cloudWatch"
ld = sc.textFile(log).cache()
ld.filter(lambda s: 'a' in s).count()
