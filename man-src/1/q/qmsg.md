---
title: "qmsg(1)"
name: "qmsg"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmsg/"
description: "qmsg – send message to pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qmsg &#8211; send message to pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qmsg [-E] [-O] message_string job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> To send a message to a job is to write a message string into one or more output files of the job. Typically this is done to leave an informative message in the output of the job. </p>
<p> The <code>qmsg</code> command writes messages into the files of jobs by sending a <i>Message Job</i> batch request to the batch server that owns the job. The qmsg command does not directly write the message into the files of the job.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-E</p>
<dd> Specifies that the message is written to the standard error of each job.</p>
<dt>-O</p>
<dd> Specifies that the message is written to the standard output of each job.</dl>
<p> If neither the <i> nor the option is specified, the message will be written to the standard error of the job. </i></p>
<h2>OPERANDS</h2>
<p> The first operand, <i> is the message to be written. If the string contains blanks, the string must be quoted. If the final character of the string is not a newline, a newline character will be added when written to the job&#8217;s file. </p>
<p> All following operands are which specify the jobs to receive the message string. The qmsg command accepts one or more operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>STANDARD ERROR</h2>
<p> The qmsg command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qmsg command, the exit status will be a value of zero. </p>
<p> If the qmsg command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_msgjob/">pbs_msgjob</a>(3B) </p>
<h2>Index</h2>
