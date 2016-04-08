/**
  * Created by vilas on 3/3/2016.
  */

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.hadoop.util
import org.apache.spark.sql.SQLContext

object wc5540 {
  def main(args: Array[String]) {
    System.setProperty("hadoop.home.dir","C:\\Users\\vilas\\Downloads\\hadoop-common-2.2.0-bin-master")
    // initialise spark context
    val conf = new SparkConf().setAppName("WordCountSpark").setMaster("local[2]").set("spark.executor.memory","8g")
    val sc = new SparkContext(conf)

val sqlContext = new SQLContext(sc)

val textFile = sqlContext.jsonFile("E:\\study\\twitdata\\Tweets4.json")
    textFile.registerTempTable("tweets")
    textFile.printSchema();
    textFile.collect()
val textFile2 = sqlContext.jsonFile("E:\\study\\twitdata\\Tweets2.json")
    textFile2.registerTempTable("tweets2")
    textFile2.printSchema();
    textFile2.collect()

val count1  =  sqlContext.sql("SELECT user.location as location,COUNT(*) AS ENGCOUNT FROM tweets WHERE lang='en' and user.location NOT IN ('INDIA','India','india','null') GROUP BY user.location order by 2 desc limit 10")
        count1.show()
//        count1.save("output1","json")

val count2  =  sqlContext.sql("select user.screen_name as username,max(user.followers_count) As followers_count from tweets2 WHERE user.followers_count IS NOT NULL  group by user.screen_name,user.followers_count limit 10")
       count2.show()
  //     count2.save("output2","json")

val count3  =  sqlContext.sql("select distinct possibly_sensitive,count(*) as Counts from tweets2 group by possibly_sensitive")
    count3.show()
    //count3.save("output3","json")

val count4  =  sqlContext.sql("SELECT user.time_zone as timezone, SUBSTR(created_at, 0, 10) as postedtime, COUNT(*) AS total_count FROM tweets2 WHERE user.time_zone IS NOT NULL AND SUBSTR(created_at, 0, 10) in ('Sat Feb 27') GROUP BY user.time_zone,SUBSTR(created_at, 0, 10) ORDER BY total_count DESC LIMIT 10")
    count4.show()
//count4.save("output4","json")


val count5  =  sqlContext.sql("SELECT distinct user.location as location,count(*) AS total_count FROM tweets2 GROUP BY user.location ORDER BY total_count DESC LIMIT 20")
    count5.show()
  //  count5.save("output5","json")


 val count6  =  sqlContext.sql("select distinct source,count(*) AS total_count from tweets2  where source like '%Twitter for Android%' or source like '%Twitter for iPhone%' or source like '%Twitter Web Client%' or source like '%twitterfeed%' or source like '%Facebook%' group by source limit 10")
  count6.show()
  //count6.save("output6","json")

    val count7  =  sqlContext.sql("select SUBSTR(user.created_at, 26, 30) as Account_created,count(*) as Counts  from tweets3 where SUBSTR(user.created_at, 26, 30) is not null  group by SUBSTR(user.created_at, 26, 30) order by Account_created limit 15 ")
    count7.show()
//count7.save("output7","json")



    val count8  =  sqlContext.sql("select distinct user.screen_name as username,max(user.statuses_count) As statuses_count from tweets2 WHERE user.statuses_count IS NOT NULL  group by user.screen_name limit 30")
 count8.show()
//count8.save("output8","json")
  }
}