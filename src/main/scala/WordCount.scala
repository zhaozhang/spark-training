import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object WordCount {
  def main(args: Array[String]) {
    //val logFile = "/Users/zzhang/Works/spark/spark-1.6.1/conf" // Should be some file on your system
    val logFile = "/tmp/data/book.txt" // Should be some file on your system
    val conf = new SparkConf().setAppName("WordCount")
    val sc = new SparkContext(conf)
    val lines = sc.textFile(logFile).cache()
    val words = lines.flatMap(l => l.split(" "))
    val kwp = words.map(w => (w, 1))
    val res = kwp.reduceByKey(_ + _)
    val sorted = res.sortBy(_._2, false)

    println("Word Count results: "+sorted.collect.mkString(","))
  }

  def func(x: Int) = x*x
}
