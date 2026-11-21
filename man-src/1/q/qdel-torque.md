---
title: "qdel-torque(1)"
name: "qdel-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qdel-torque/"
description: "qdel – delete pbs batch job"
---

<h2 class="name">NAME</h2>
<p> qdel &#8211; delete pbs batch job </p>
<h2>SYNOPSIS</h2>
<p> qdel [-a] [-c] [-m message] [-p] [-t array_range] [-W delay] job_identifier&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qdel </code> command deletes jobs in the order in which their job identifiers are presented to the command. A job is deleted by sending a <i>Delete Job</i> batch request to the batch server that owns the job. A job that has been deleted is no longer subject to management by batch services. </p>
<p> A batch job may be deleted by its owner, the batch operator, or the batch administrator. </p>
<p> A batch job being deleted by a server will be sent a <code>SIGTERM</code> signal following by a <code>SIGKILL </code> signal. The time delay between the two signals is an attribute of the execution queue from which the job was run (settable by the administrator). This delay may be overridden by the <i> option. </p>
<p> See the PBS ERS section 3.1.3.3, &quot;Delete Job Request&quot;, for more information. </i></p>
<h2>OPTIONS</h2>
<dl>
<dt>-W delay</dt>
<dd> Specify the delay between the sending of the SIGTERM and SIGKILL signals. The argument <i> specifies a unsigned integer number of seconds.</dd>
<dt>-a</dt>
<dd> Request the job(s) be deleted asynchronously, which for a Running job means that the reply will return before the MOM is requested to delete the job.</dd>
<dt>-c</dt>
<dd> Clean up unreported jobs from the server. This should only be used if the scheduler is unable to purge unreported jobs. This option is only available to a batch operator or the batch administrator.</dd>
<dt>-p</dt>
<dd> Forcibly purge the job from the server. This should only be used if a running job will not exit because its allocated nodes are unreachable. The admin should make every attempt at resolving the problem on the nodes. If a job&#8217;s mother superior recovers after purging the job, any epilogue scripts may still run. This option is only available to a batch operator or the batch administrator.</dd>
<dt>-m message</dt>
<dd> Specify a comment to be included in the email. The argument specifies the comment to send. This option is only available to a batch operator or the batch administrator.</dd>
<dt>-t array_range</dt>
<dd> The array_range argument is an integer id or a range of integers. Multiple ids or id ranges can be combined in a comma delimted list. Examples: -t 1-100 or -t 1,10,50-100</dd>
<dt>
</dt><dd> If an array range isn&#8217;t specified, the command tries to operate on the entire array. The command acts on the array (or specified range of the array) just as it would on an individual job.</dd></dl>
<p> </i></p>
<h2>OPERANDS</h2>
<p> The qdel command accepts one or more <i> operands of the form:<br />
 </i><code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or </p>
<p> </code></p>
<h2>STANDARD ERROR</h2>
<p> The qdel command will write a diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qdel command, the exit status will be a value of zero. </p>
<p> If the qdel command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> qsub(1B), qsig(1B), and pbs_deljob(3B) </p>
