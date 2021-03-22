<?php
include_once 'Credentials.php';
require 'AmazonS3.php';
//require 'AmazonSNS.php';
//require 'AmazonCloudWatch.php';

// AWS Credentials
$options = Credentials::Amazon();


// ----------------------CLOUDWATCH LOGGING ------------------//
// Log Success Data to AWS Cloudwatch Logs
//$Data = 'failure data';
//$log = AmazonCloudWatchLog::pushSuccessDataToLogStream($options, $Data);

// Log Failure Data to AWS Cloudwatch Logs
//$Data = 'failure data';
//$log = AmazonCloudWatchLog::pushFailureDataToLogStream($options, $Data);
// ---------------------CLOUDWATCH LOGGING--------------------//



// ------------------SIMPLE STORAGE SERVICE-------------------//
// Public Bucket = BUCKET-2
// Private Buckets = BUCKET-1/3/4
//$bucket = ['BUCKET-1', 'BUCKET-2', 'BUCKET-3', 'BUCKET-4'];
//$list = AmazonS3::listSpecificFiles($options, $bucket[1], 'jpg');

// Empty AWS S3 Bucket
//$empty = AmazonS3::deleteS3Files($options, $bucket[2]);

// Download Files From S3 Bucket
//$download = AmazonS3::downloadS3Files($options, $bucket[2]);

// Upload Files From S3 Bucket
//$upload = AmazonS3::uploadS3Files($options, $bucket[2]);
// -------------------SIMPLE STORAGE SERVICE------------------//



// -----------------SIMPLE NOTIFICATION SERVICE---------------//
// Send Text Message using AWS SNS
//if(PHP_SAPI === 'cli'){
//    if(isset($argv[2])){
//        $message = $argv[1].$argv[2];
//    };
//    $message = $argv[1];
//}
//$sendMessage = \AmazonSNS::sendMessage($options, $message);
// -----------------SIMPLE NOTIFICATION SERVICE---------------//

