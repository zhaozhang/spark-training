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
   or press CTRL+d
