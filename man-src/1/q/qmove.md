---
title: "qmove(1)"
name: "qmove"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmove/"
description: "qmove – move pbs batch job"
---

<h2 class="name">NAME</h2>
<p> qmove &#8211; move pbs batch job </p>
<h2>SYNOPSIS</h2>
<p> qmove destination job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> To move a job is to remove the job from the queue in which it resides and instantiate the job in another queue. The <code>qmove</code> command issues a <i>Move Job</i> batch request to the batch server that currently owns each job specified by <i> </p>
<p> A job in the </i><code>Running ,</code> <code>Transiting ,</code> or <code>Exiting</code> state cannot be moved.</p>
<h2>OPERANDS</h2>
<p> The first operand is the new <i><br />
 </i><code> </p>
<p> See the PBS ERS section , &quot;Destination Identifiers&quot;. </p>
<p> If the </code><i> operand describes only a queue, then qmove will move jobs into the queue of the specified name at the job&#8217;s current server. </p>
<p> If the operand describes only a batch server, then qmove will move jobs into the default queue at that batch server. </p>
<p> If the operand describes both a queue and a batch server, then qmove will move the jobs into the specified queue at the specified server. </p>
<p> All following operands are which specify the jobs to be moved to the new The qmove command accepts one or more operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>STANDARD ERROR</h2>
<p> The qmove command will write a diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qmove command, the exit status will be a value of zero. </p>
<p> If the qmove command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_movejob/">pbs_movejob</a>(3B) </p>
<h2>Index</h2>
