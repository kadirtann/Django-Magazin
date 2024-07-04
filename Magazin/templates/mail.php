<?php

$mail_to  = "youremail@email.com";  // replace it with your email

$name     = $_POST['name'];
$email    = $_POST['email'];
$subject    = $_POST['subject'];
$message  = $_POST['message'];

$subject = "Contact Request From: " . $name;

$body   = "New Message From: " . "$name " . "<$email>" . "\n\n";
$body   .= "----------------" . "\n\n";
$body   .= "Name: " . "$name" . "\n\n";
$body   .= "Email: " . "$email" . "\n\n";
$body   .= "subject: " . "$subject" . "\n\n";
$body   .= "Message: " . "\n\n" . "$message" . "\n\n";

$from  = "From: " . "$name " . "<$email>";

if (mail($mail_to, $subject, $body, $from)) {
  echo "Message sent!";
} else {
  echo "error!";
}
