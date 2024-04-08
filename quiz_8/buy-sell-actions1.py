#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

r"""
 Counts words in UTF8 encoded, '\n' delimited text received from the network.
 Usage: structured_network_wordcount.py <hostname> <port>
   <hostname> and <port> describe the TCP server that Structured Streaming
   would connect to receive data.

 To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/sql/streaming/structured_network_wordcount.py
    localhost 9999`
"""
import sys, time

import pyspark
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import Window

def setLogLevel(sc, level):
    from pyspark.sql import SparkSession
    spark = SparkSession(sc)
    spark.sparkContext.setLogLevel(level)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: structured_network_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    print ('Argv', sys.argv)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    print ('host', type(host), host, 'port', type(port), port)

    sc_bak = SparkContext.getOrCreate()
    sc_bak.stop()
    
    time.sleep(15)
    print ('Ready to work!')

    ctx = pyspark.SparkContext(appName = "Price Work", master="local[*]")
    print ('Context', ctx)

    spark = SparkSession(ctx).builder.getOrCreate()
    sc = spark.sparkContext

    setLogLevel(sc, "WARN")

    print ('Session:', spark)
    print ('SparkContext', sc)
    
    # sc = SparkContext(conf=conf)

    # Create DataFrame representing the stream of input lines from connection to host:port
    streaming_prices = spark\
        .readStream\
        .format('socket')\
        .option('host', host)\
        .option('port', port)\
        .load()

    # Split the lines into words
    data_prices = streaming_prices.select(
        split(col("value"), " ")[0].alias("date"),
        split(col("value"), " ")[1].cast("double").alias("GOOG"),
        split(col("value"), " ")[2].cast("double").alias("MSFT")
    )

    stream_prices_GOOG = data_prices.select("date", "GOOG").withWatermark("date", "1 minute")
    stream_prices_MSFT = data_prices.select("date", "MSFT").withWatermark("date", "1 minute")

    # Step 5: Calculate rolling averages using window functions
    window_spec_10_day = Window.orderBy("date").rangeBetween(-9, 0)
    window_spec_40_day = Window.orderBy("date").rangeBetween(-39, 0)

    goog10Day = stream_prices_GOOG \
        .withColumn("GOOG_10",avg("GOOG").over(window_spec_10_day)) \
        .select("date","GOOG_10")

    # Start running the query that prints the running counts to the console
    query = goog10Day\
        .writeStream\
        .outputMode("append") \
        .format('console')\
        .start()
        # To print more than 20 lines, add .option("numRows", 100000)\ after format('console')\

    query.awaitTermination()

    # ../Python-3.9.2/bin/spark-submit
