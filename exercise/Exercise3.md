# Exercises of MLlib

## Exercise 3.1
### Linear Regression with Single Variable
```
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.regression.LinearRegressionWithSGD

val lines = sc.textFile("/tmp/data/scaled-sf-ny-housing-train.csv")
val data = lines.map(l => {
  val w = l.split(",")
  LabeledPoint(w(3).toDouble, Vectors.dense(w(5).toDouble))
})
val model = LinearRegressionWithSGD.train(data,100)

model.weights

val trainError = lines.map(l => {
  val w = l.split(",")
  model.predict(Vectors.dense(w(5).toDouble))-w(3).toDouble
})
val mseTrain = trainError.map(x=>x*x).reduce(_+_)/400
mseTrain
//mseTrain: Double = 0.06472201882476669

val tlines = sc.textFile("/tmp/data/scaled-sf-ny-housing-test.csv")
val testError = tlines.map(l => {
  val w = l.split(",")
  model.predict(Vectors.dense(w(5).toDouble))-w(3).toDouble
})
val mseTest = testError.map(x=>x*x).reduce(_+_)/92
mseTest
//mseTest: Double = 0.05897075938607083
```

### Linear Regression with Multiple Variables
```
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.regression.LinearRegressionWithSGD

val lines = sc.textFile("/tmp/data/scaled-sf-ny-housing-train.csv")
val data = lines.map(l => {
  val w = l.split(",")
  LabeledPoint(w(3).toDouble, Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble))
})
val model = LinearRegressionWithSGD.train(data,100)

model.weights

val trainError = lines.map(l => {
  val w = l.split(",")
  model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble))-w(3).toDouble
})
val mseTrain = trainError.map(x=>x*x).reduce(_+_)/400
mseTrain
//mseTrain: Double = 0.06222798683227797

val tlines = sc.textFile("/tmp/data/scaled-sf-ny-housing-test.csv")
val testError = tlines.map(l => {
  val w = l.split(",")
  model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble))-w(3).toDouble
})
val mseTest = testError.map(x=>x*x).reduce(_+_)/92
mseTest
//mseTest: Double = 0.05444971758384607
```

## Exercise 3.2
### Logistic Regression
```
import org.apache.spark.mllib.classification.{LogisticRegressionModel, LogisticRegressionWithLBFGS}
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint

val lines = sc.textFile("/tmp/data/scaled-sf-ny-housing-train.csv")
val data = lines.map(l => {
  val w = l.split(",")
  LabeledPoint(w(0).toDouble, Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble))
})
val model = new LogisticRegressionWithLBFGS().setNumClasses(2).run(data)

model.weights

val trainPrediction = lines.map(l => {
  val w = l.split(",")
  (model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble)), w(0).toDouble)
})

val metrics = new MulticlassMetrics(trainPrediction)
metrics.precision
//res12: Double = 0.6575

val tlines = sc.textFile("/tmp/data/scaled-sf-ny-housing-test.csv")
val testPrediction = tlines.map(l => {
  val w = l.split(",")
  (model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble)), w(0).toDouble)
})

val metrics = new MulticlassMetrics(testPrediction)
metrics.precision
//res12: Double = 0.6956521739130435
```

## Exercise 3.3
### Support Vector Machine
```
import org.apache.spark.mllib.classification.{SVMModel, SVMWithSGD}
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint

val lines = sc.textFile("/tmp/data/scaled-sf-ny-housing-train.csv")
val data = lines.map(l => {
  val w = l.split(",")
  LabeledPoint(w(0).toDouble, Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble))
})
val model = SVMWithSGD.train(data, 1000)

model.weights

val trainPrediction = lines.map(l => {
  val w = l.split(",")
  (model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble)), w(0).toDouble)
})

val metrics = new MulticlassMetrics(trainPrediction)
metrics.precision
//> res12: Double = 0.525

val tlines = sc.textFile("/tmp/data/scaled-sf-ny-housing-test.csv")
val testPrediction = tlines.map(l => {
  val w = l.split(",")
  (model.predict(Vectors.dense(w(5).toDouble, w(4).toDouble, w(1).toDouble)), w(0).toDouble)
})

val metrics = new MulticlassMetrics(testPrediction)
metrics.precision
//> res12: Double = 0.6304347826086957
```
## Exercise 3.4
### Alternating Least Squares
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel
import org.apache.spark.mllib.recommendation.Rating

// Load and parse the data
val data = sc.textFile("/tmp/data/ratings-missing.data")
val ratings = data.map(_.split(',') match { case Array(user, item, rate) =>
  Rating(user.toInt, item.toInt, rate.toDouble)
})

// Build the recommendation model using ALS
val rank = 10
val numIterations = 10
val model = ALS.train(ratings, rank, numIterations, 0.01)

// Evaluate the model on rating data
val usersProducts = ratings.map { case Rating(user, product, rate) =>
  (user, product)
}
val predictions =
  model.predict(usersProducts).map { case Rating(user, product, rate) =>
    ((user, product), rate)
  }
val ratesAndPreds = ratings.map { case Rating(user, product, rate) =>
  ((user, product), rate)
}.join(predictions)
val MSE = ratesAndPreds.map { case ((user, product), (r1, r2)) =>
  val err = (r1 - r2)
  err * err
}.mean()
println("Mean Squared Error = " + MSE)
//MSE: Double = 4.586503035462018E-5


## Exercise 3.5
### k-means Clustering
```
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.clustering.{KMeans, KMeansModel}

val lines = sc.textFile("/tmp/spark-training/data/scaled-sf-ny-housing-train.csv")

val data = lines.map(l => {
  val w = l.split(",")
  Vectors.dense(w(1).toDouble, w(2).toDouble, w(3).toDouble, w(4).toDouble, w(5).toDouble, w(6).toDouble)
})

val clusters = KMeans.train(data, 2, 100)

val pred = lines.map(l => {
  val w = l.split(",")
  val v = Vectors.dense(w(1).toDouble, w(2).toDouble, w(3).toDouble, w(4).toDouble, w(5).toDouble, w(6).toDouble)
  math.pow(cluster.predict(v) - w(0).toInt, 2)
})

val res = pred.reduce(_+_)
res
//res: Int = 177
```

## Exercise 3.6
### PageRank with GraphX
```
import org.apache.spark.graphx._
import org.apache.spark.graphx.util.GraphGenerators

val graph = GraphLoader.edgeListFile(sc, “/tmp/data/followers.txt")
val ranks = graph.pageRank(0.0001).vertices
ranks.sortBy(_._2, false).collect
// you should see res10: Array[(org.apache.spark.graphx.VertexId, Double)] = Array((1,1.4588814096664682), (2,1.390049198216498),  (7,1.2973176314422592), (3,0.9993442038507723),  (6,0.7013599933629602), (4,0.15))
```

## Exercise 3.7
### DataFrame and SparkSQL
```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.Pipeline

val spark = SparkSession.builder().appName("Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()
import spark.implicits._

val df = spark.read.format("csv").option("header", false).load("/tmp/data/shuffled-scaled-fs-ny-housing.csv").selectExpr("_c3 + 0.0 as sqft", "_c5 + 0.0 as label")

val training = df.sample(false, 0.8)
val test = df.except(training)
val assembler = new VectorAssembler().setInputCols(Array("sqft")).setOutputCol("features")

val lr = new LinearRegression().setMaxIter(10).setRegParam(0.2).setElasticNetParam(0.0)
val pipeline = new Pipeline().setStages(Array(assembler, lr))
val lrModel = pipeline.fit(training)

val result = lrModel.transform(test).select('sqft, 'label, 'prediction)
result.show
```