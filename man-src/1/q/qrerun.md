---
title: "qrerun(1)"
name: "qrerun"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrerun/"
description: "qrerun – rerun a pbs batch job"
---

<h2 class="name">NAME</h2>
<p> qrerun &#8211; rerun a pbs batch job </p>
<h2>SYNOPSIS</h2>
<p> qrerun [-f] job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qrerun</code> command directs that the specified jobs are to be rerun if possible. </p>
<p> To rerun a job is to terminate the session leader of the job and return the job to the queued state in the execution queue in which the job currently resides. </p>
<p> If a job is marked as not rerunable then the rerun request will fail for that job. If the mini-server running the job is down, or the rejects the request, the <i>Rerun Job</i> batch request will return a failure unless -f is used. </p>
<p> Using -f violates IEEE Batch Processing Services Std and should be handled with great care. It should only be used under exceptional circumstances. Best practice is to fix the problem mini-server host and letting qrerun run normally. The previous nodes may need manual cleaning. See the <i> option on the </i><code>qsub </code> and <code>qalter</code> commands.</p>
<h2>OPERANDS</h2>
<p> The qrerun command accepts one or more <i> operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>STANDARD ERROR</h2>
<p> The qrerun command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qrerun command, the exit status will be a value of zero. </p>
<p> If the qrerun command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rerunjob/">pbs_rerunjob</a>(3B) </p>
<h2>Index</h2>
