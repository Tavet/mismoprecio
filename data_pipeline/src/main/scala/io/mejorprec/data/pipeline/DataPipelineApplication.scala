package io.mejorprec.data.pipeline

import java.io.{BufferedReader, InputStreamReader}

import com.amazonaws.auth.{AWSStaticCredentialsProvider, BasicAWSCredentials}
import com.amazonaws.regions.{Region, Regions}
import com.amazonaws.services.s3.{AmazonS3, AmazonS3ClientBuilder}
import org.apache.spark

object DataPipelineApplication {
  final val region: Regions = Regions.US_WEST_2
  final val bucketName = "best-deal-stores-info"
  final val path = "clothes/data/raw/clothes-COL-diesel-data.json"
  final val s3Client: AmazonS3 = AmazonS3ClientBuilder.standard()
    .withRegion(region).build()
  final val s3 = s3Client.getObject(bucketName, path)

  def main(args: Array[String]): Unit = {
    val in = s3.getObjectContent
    val reader = new BufferedReader(new InputStreamReader(in))

    val data = Stream.continually(reader.read()).takeWhile(_ != -1).map(_.toChar).mkString
    print(data)
  }
}
