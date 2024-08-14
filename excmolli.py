from pyspark.sql.functions import randint

df.withColumn("code2", randint(IntegerType(), 8, 10))
