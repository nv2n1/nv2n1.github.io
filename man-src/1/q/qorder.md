---
title: "qorder(1)"
name: "qorder"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qorder/"
description: "qorder – exchange order of two pbs batch jobs in a queue."
---

<h2 class="name">NAME</h2>
<p> qorder &#8211; exchange order of two pbs batch jobs in a queue. </p>
<h2>SYNOPSIS</h2>
<p> qorder job_identifier job_identifier</p>
<h2>DESCRIPTION</h2>
<p> To order two jobs is to exchange the jobs positions in the queue or queues in which the jobs resides. The two jobs must be located at the same server. No attribute of the job, such as priority is changed. The impact of interchanging the order with the queue(s) is dependent on local job scheduled policy, contact your systems administrator. </p>
<p> A job in the <code>running</code> state cannot be reordered.</p>
<h2>OPERANDS</h2>
<p> Both operands are <i> which specify the jobs to be exchanged. The qorder command accepts two operands of the form:<br />
 </i><code><br />
 The server specification for the two jobs must agree as to the current location of the two job IDs. </code></p>
<h2>STANDARD ERROR</h2>
<p> The qorder command will write diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qorder command, the exit status will be a value of zero. </p>
<p> If the qorder command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qmove/">qmove</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_orderjob/">pbs_orderjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_movejob/">pbs_movejob</a>(3B) </p>
<h2>Index</h2>
