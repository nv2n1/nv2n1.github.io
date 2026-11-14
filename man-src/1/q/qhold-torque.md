---
title: "qhold-torque(1)"
name: "qhold-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qhold-torque/"
description: "qhold – hold pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qhold &#8211; hold pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qhold [-h hold_list] [-t array_range] job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qhold </code> command requests that a server place one or more holds on a job. A job that has a hold is not eligible for execution. There are three supported holds: <font SIZE="-1"></font><font SIZE="-2"><code> (also known as operator), and </code></font><font SIZE="-3"><code> </p>
<p> A user may place a </code></font><font SIZE="-4"><code> hold upon any job the user owns. An &quot;operator&quot;, who is a user with &quot;operator privilege,&quot; may place ether an </code></font><font SIZE="-5"><code> or an </code></font><font SIZE="-6"><code> hold on any job. The batch administrator may place any hold on any job. </p>
<p> If no </code><i> option is given, the USER hold will be applied to the jobs described by the operand list. </p>
<p> If the job identified by is in the </i><code>queued</code>, <code>held</code>, or <code>waiting</code> states, then all that occurs is that the hold type is added to the job. The job is then placed into <code>held</code> state if it resides in an execution queue. </p>
<p> If the job is in <code>running</code> state, then the following additional action is taken to interrupt the execution of the job. If checkpoint / restart is supported by the host system, requesting a hold on a running job will (1) cause the job to be checkpointed, (2) the resources assigned to the job will be released, and (3) the job is placed in the <code>held</code> state in the execution queue. </p>
<p> If checkpoint / restart is not supported, qhold will only set the the requested hold attribute. This will have no effect unless the job is rerun with the <code>qrerun </code> command. </p>
<p> The qhold command sends a <i>Hold Job</i> batch request to the server as described in the general section. </font></p>
<h2>OPTIONS</h2>
<dl>
<dt>-h hold_list</p>
<dd> Defines the types of holds to be placed on the job.</p>
<dt>
<dd> The <i> argument is a string consisting of one or more of the letters &quot;</i><code>u</code>&quot;, &quot;<code>o</code>&quot;, or &quot;<code>s</code>&quot; in any combination. The hold type associated with each letter is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>u &#8211;</p>
<dd> <font SIZE="-1"><code></p>
<dt>o &#8211;</p>
<dd> </code></font><font SIZE="-2"><code></p>
<dt>s &#8211;</p>
<dd> </code></font><font SIZE="-3"><code></dl>
</dl>
<dt>-t array_range</p>
<dd> The array_range argument is an integer id or a range of integers. Multiple ids or id ranges can be combined in a comma delimted list. Examples: -t 1-100 or -t 1,10,50-100</p>
<dt>
<dd> If an array range isn&#8217;t specified, the command tries to operate on the entire array. The command acts on the array (or specified range of the array) just as it would on an individual job.</dl>
<p> </code></font></p>
<h2>OPERANDS</h2>
<p> The qhold command accepts one or more <i> operands of the form: </i><code> </p>
<p> </code></p>
<h2>STANDARD ERROR</h2>
<p> The qhold command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qhold command, the exit status will be a value of zero. </p>
<p> If the qhold command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qrls/">qrls</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_holdjob/">pbs_holdjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rlsjob/">pbs_rlsjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_job_attributes/">pbs_job_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_unicos8/">pbs_resources_unicos8</a>(7B) </p>
<h2>Index</h2>
