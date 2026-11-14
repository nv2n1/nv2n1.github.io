---
title: "condor_check_userlogs(1)"
name: "condor_check_userlogs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_check_userlogs/"
---

<h2>Name</h2>

 

 <i>condor_check_userlogs</i> Check job event log files for errors 

 

 

<h2>Synopsis</h2>

 <i>condor_check_userlogs</i> <i>UserLogFile1</i> [ <i>UserLogFile2 ... UserLogFileN </i> ] 

<h2>Description</h2>

 

 <i>condor_check_userlogs</i> is a program for checking a job event log or a set of job event logs for errors. Output includes an indication that no errors were found within a log file, or a list of errors such as an execute or terminate event without a corresponding submit event, or multiple terminated events for the same job. 

 <i>condor_check_userlogs</i> is especially useful for debugging <i>condor_dagman</i> problems. If <i>condor_dagman</i> reports an error it is often useful to run <i>condor_check_userlogs</i> on the relevant log files. 

<h2>Exit Status</h2>

 

 <i>condor_check_userlogs</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. 

<h2>Author</h2>

 Center for High Throughput Computing, University of Wisconsin-Madison

<h2>Copyright</h2>

 Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. 

<h2>Index</h2>


