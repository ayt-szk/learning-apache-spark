import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions  import *

conf = SparkConf().setAppName("simpleApp").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.config(conf=sc.getConf()).getOrCreate()

csv_path = "/root/data/bread_basket.csv"

schema = StructType(
    [
        # 3つめの引数はNullを許容するかどうか
        StructField("Transaction", IntegerType(), True),
        StructField("Item", StringType(), True),
        StructField("date_time", StringType(), True),
        StructField("period_day", StringType(), True),
        StructField("weekday_weekend", StringType(), True)
    ]
)

spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
csv_df = (
    spark.read.option("header", True)
    .option("mode", "PERMISSIVE")
    .option("sep", r",")
    .option("enforceSchema", False)
    .schema(schema)
    .csv(csv_path)
)

# date_timeをtimestamp型に変換したformat_date_timeカラムの追加
df = csv_df.withColumn("format_date_time", to_timestamp(col("date_time"), "dd-MM-yy HH:mm"))
df.createOrReplaceTempView("BreadBasket")

# dfの型確認
# df.printSchema()

query = f"""
            SELECT 
                *
            FROM 
                BreadBasket 
            WHERE 
                Item = 'Coffee'
            AND
                format_date_time BETWEEN '2016-11-01 00:00' AND '2016-12-01 00:00'
            LIMIT 10
        """

# query = "SELECT COUNT(*) FROM BreadBasket"

df = spark.sql(query)

df.show()
spark.stop()