# Exercises of Introduction to Scala for Spark

## Login Wrangler

### Terminal
```bash
ssh -u $username@wrangler.tacc.utexas.edu

cd ~

git clone https://github.com/zhaozhang/spark-training.git
```
### Zeppelin
```bash
%shell

cd ~

git clone https://github.com/zhaozhang/spark-training.git
```

## Exercise 1.1: Three Ways to Run a Scala Program

### Compile and Execute
1. Create HelloWorld.scala using your text editor, then type the following code:

```scala
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
  }
}
```
2. Complie the source code
```bash
scalac HelloWorld.scala
```

3. Execute the compiled program
```bash
scala HelloWorld
```

### Scripting

1. Create HelloWorld.sh, then type in the following code:

```scala
#!/usr/bin/env scala
 
object HelloWorld extends App{
    println("Hello, world!")
}
HelloWorld.main(args)
```

2. Change execution permission
```bash
chmod 755 HelloWorld.sh
```

3. Run the script
```bash
./HelloWorld.sh
```

### Scala shell

1. Open Scala shell
```bash
scala
```

2. Type the following code then press ENTER
```scala
println(“Hello World!”)
```

3. Quit the shell
```scala
:quit
```
&nbsp;&nbsp;&nbsp;or press CTRL+d

## Exercise 1.2: What is immutable when we say a list is immutable?
1. The variable *l* ?

```scala
val l = List(1,2,3)
l = List(4,5,6)
```

2. The list that *l* points to?

```scala
l += 7
```

3. The elements of *l* ?

```scala
l(1) = 8
```

### What if *var l* ?
1. The variable *l* ?

```scala
var l = List(1,2,3)
l = List(4,5,6)
```

2. The list that *l* points to?

```scala
l += 7
```

3. The elements of *l* ?

```scala
l(1) = 8
```

### Using ListBuffer if you need a mutable list

```scala
import scala.collection.mutable.ListBuffer

var l = new ListBuffer[Any]()
l += 1
l += 2
l += 3
l

l(1) = 9
l
```

## Exercise 1.3: Iterate a list
### Multiply each element of a list by 2
```scala
val l = List(1,2,3)
```

1. Using *while* 
```scala
import scala.collection.mutable.ListBuffer

val r = new ListBuffer[Any]()
var i = 0
while(i<l.length){
  r += l(i)*2
}

r
```

2. Using *for*
```scala
import scala.collection.mutable.ListBuffer

val r = for(x <-l) yield(x*2)

r
```

3. Using *map*
```scala
val r = l.map(x => x*2)

r
```
### Play with List
```scala
val l = List(1,2,3,4,5)
l.head
l.tail
l.last
l.length
l.map(_*2)
l.reverse
l.sorted
```

## Exercise 1.4: Functions
### Iterate over a list and multiply every element by 2
1. Anonymous function
```scala
val l = List(1,2,3)

val r = l.map((x:Int) => x*2)
r

val r = l.map(x => x*2)
r

val r = l.map(_*2)
r
```

2. Named function
```
def func(x: Int) = x*2

val r = l.map(x => func(x))
r
```

3. Multiple Inputs
```scala
val l = List((1,2), (3,4))

val r = l.map{case(x:Int, y: Int) => x+y}
r

val r = l.map{case(x, y) => x+y}
r
```

4. Multiple Outputs
```scala
val l = List((1,2), (3,4))

val r = l.map{case(x, y) => (x*2, y*2)}
r
```

## Exercise 1.5: Pattern Matching
### Iterate over a list of integer and print only the odd number
```scala
val l = List(1,2,3,4,5)
```

1. Using if ... else ...
```scala
val r = l.foreach(x => {
  if (x%2 == 1)
    x
})
```

2. Using match ... case ...
```scala
val r = l.foreach(x => x%2 match{
  case 1 => x
  case _ =>
})
```

### Pattern matching on variable type
```scala
def func(a: Any) = a match {
  case i:Int => println(“a is an int”)
  case f:Float => println(”a is a float”)
  case d:Double => println(“a is a double”)
  case s:String => println(“a is a string”)
  case l: List[_] => println(“a is a list”)
  case _ => println(“unknown type”)
})
```

```scala
func(1)
func(1.0)
func(1.toFloat)
func(“abc”)
func(List(1,2,3))
func(Array(1,2,3))
```

## Exercise 1.6: Iterator
1. Basic operation
```scala
val l = List(1,2,3,4,5,6)

val i = l.toIterator

val r1 = l.map(_*2)

val r = i.map(_*2)
r.hasNext
r.next

val r2 = r.toList
```

2. Verify late evaluation
```scala
val l = List(1,2,3,4,5,6)

val i = l.toIterator

val r = i.map(x => {
  Thread.sleep(1000)
  x*2
})

r.toList
```