name := "data_pipeline"

version := "0.1"

scalaVersion := "2.13.4"

libraryDependencies ++= Seq(
  "org.apache.spark" % "spark-core_2.11" % "2.1.0",
  "com.amazonaws" % "aws-java-sdk-s3" % "1.11.926"
)

