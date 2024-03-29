from __future__ import print_function
import sys
from pyspark.ml import PipelineModel
from pyspark.ml.classification import DecisionTreeClassifier,DecisionTreeClassificationModel
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Decision_Tree_Spark <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("DecisionTreeClassificationExample")\
        .getOrCreate()

    # Load the data stored in LIBSVM format as a DataFrame.
    data = spark.read.format("libsvm").load(sys.argv[1])

    # Index labels, adding metadata to the label column.
    # Fit on whole dataset to include all labels in index.
    labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)
    # Automatically identify categorical features, and index them.
    # We specify maxCategories so features with > 4 distinct values are treated as continuous.
    featureIndexer =\
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)

    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Load the DecisionTree model.
    model = PipelineModel.load("../test/DTModel")   #breast cancer model

    # Make predictions.
    predictions = model.transform(testData)

    # Select example rows to display.
    predictions.select("prediction", "indexedLabel", "features").show(5)

    # Select (prediction, true label) and compute test error
    evaluator = MulticlassClassificationEvaluator(
        labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test Error = %g " % (1.0 - accuracy))

    spark.stop()