# Exercises of Programming Spark
## Exercise 2.1: Spark transformations and actions
### Basic RDD

1. Map function
```scala
val rdd = val rdd = sc.parallelize(0 until 100)
val res = rdd.map(x => x*2)
res.collect()
```

2. flatMap function
```scala
val rdd = sc.parallelize(List(List(1,2,3,4), List(5,6,7,8)))
val res = rdd.flatMap(x => x)
res.collect()

val res = rdd.flatMap(x => x.map(y => y*2))
res.collect()
```

3. filter function
```scala
val rdd = sc.parallelize(0 until 100)
val res = rdd.filter(x => x%2 == 0)
res.collect()
```

4. mapPartitions function
```scala
val rdd = sc.parallelize(0 until 8, 2)
val res = rdd.mapPartitions(x => List(x.sum).iterator)
res.collect()
```

5. zipWithIndex function
```scala
val rdd = sc.parallelize(List(“a”, “b”, “c”, “d”))
val res = rdd.zipWithIndex()
res.collect()
```

6. groupBy function
```scala
val rdd = sc.parallelize(0 until 100)
val res = rdd.groupBy(x => x%2 == 0)
res.collect()
```

7. reduce function
```scala
val rdd = sc.parallelize(0 until 10)
val res = rdd.reduce(_ + _)
```

### Pair RDD 
1. groupByKey function
```scala
val l = List(“a”, “b”, “a”, “b”).zipWithIndex
val rdd = sc.parallelize(l)
val res = rdd.groupByKey()
res.collect()
```

2. reduceByKey function
```scala
val l = List(“a”, “b”, “a”, “b”).zipWithIndex
val rdd = sc.parallelize(l)
val res = rdd.reduceByKey(_ + _)
res.collect()
```

3. join function
```scala
val person = List(“adam”, “ben”, “chris”, “david”)
val age = List(27, 42, 53, 23)
val dept = List(“HPC”, “Data”, “Vis”, “Edu”)
val rdd1 = sc.parallelize(person.zip(age))
val rdd2 = sc.parallelize(person.zip(dept))
val res = rdd1.join(rdd2)
res.collect()
```
## Exercise 2.2: Word Count
1. reading files into memory
```scala
val lines = sc.textFile(“/tmp/spark-training/conf/”)
val words = lines.flatMap(l => l.split(“ ”))
words.collect()
```

2. count word frequency
```scala
val kwp = words.map(w => (w, 1))
val res = kwp.reduceByKey(_ + _)
res.collect()
```

3. sort results
```scala
val sorted = res.sortBy(_._2, false)
sorted.collect()
```

## Exercise 2.3: Build Spark application with Maven
```bash
cd ~/spark-training

module load maven

mvn package

spark-submit --class "WordCount" target/WordCount-1.0-SNAPSHOT.jar
```

## Exercise 2.4: Unit Test with scalatest and Maven
Go to training2017/
```
mvn test
```
