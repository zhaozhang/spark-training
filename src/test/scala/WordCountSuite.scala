import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.scalatest.FunSuite

class WordCountSuite extends FunSuite{
  test("WordCount Test"){
  	val sc = new SparkContext("local", "test")
    val rdd = sc.parallelize(List(1,2,3,4))
    val res = rdd.map(WordCount.func(_))
    assert(res.collect.sameElements(Array(1,4,9,16)))
  }
}
