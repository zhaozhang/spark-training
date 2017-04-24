import org.scalatest.FunSuite

class WordCountSuite extends FunSuite{
  test("WordCount Test"){
    val s = "hello, world!"
    assert(s == "hello, world!")
  }
}
