---
title: "qrun(8)"
name: "qrun"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qrun/"
description: "qrun – run a pbs batch job"
---

<p>qrun &#8211; run a pbs batch job</p>
<h2>Synopsis</h2>
<p>qrun [-a] [-H host] job_identifier &#8230;</p>
<h2>Description</h2>
<p>The <code>qrun</code> command is used to force a batch server to initiate the execution of a batch job. The job is run regardless of scheduling position, resource requirements, or state. </p>
<p> In order to execute qrun, the user must have PBS Operation or Manager privilege.</p>
<h2>Options</h2>
<dl>
<dt>-a</p>
<dd>Specifies the job(s) is to be run asynchronously.</p>
<dt>-H host</p>
<dd>Specifies the host within the cluster on which the job(s) are to be run. The <i> argument is the name of a host that is a member of the cluster of hosts managed by the server. If the option is not specified, the server will select the &quot;worst possible&quot; host on which to execute the job.</dl>
<p> </i></p>
<h2>Operands</h2>
<p>The qrun command accepts one or more <i> operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>Standard Error</h2>
<p>The qrun command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qrun command, the exit status will be a value of zero. </p>
<p> If the qrun command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched/">pbs_sched</a>(8B), <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B) </p>
