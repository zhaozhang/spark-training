# Exercises of Introduction to Scala for Spark

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