# Exercises of Introduction to Scala for Spark

## Exercise 1.1: Three Ways to Run a Scala Program

### Compile and Execute

```scala
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
  }
}
```

### Scripting

```scala
#!/usr/bin/env scala
 
object HelloWorld extends App{
    println("Hello, world!")
}
HelloWorld.main(args)
```

### Scala shell1

```scala
println(“Hello World!”)
```