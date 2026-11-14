---
title: "qrls-torque(1)"
name: "qrls-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrls-torque/"
description: "qrls – release hold on pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qrls &#8211; release hold on pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qrls [-h hold_list] [-t array_range] job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qrls</code> command removes or releases holds which exist on batch jobs. </p>
<p> A job may have one or more types of holds which make the job ineligible for execution. The types of holds are <font SIZE="-1"></font><font SIZE="-2"><code> and </code></font><font SIZE="-3"><code> The different types of holds may require that the user issuing the qrls command have special privilege. Typically, the owner of the job will be able to remove a </code></font><font SIZE="-4"><code> hold, but not an </code></font><font SIZE="-5"><code> or </code></font><font SIZE="-6"><code> hold. An Attempt to release a hold for which the user does not have the correct privilege is an error and no holds will be released for that job. </p>
<p> If no </code><i> option is specified, the </i></font><font SIZE="-7"><code> hold will be released. </p>
<p> If the job has no </code><i> </i></font><font SIZE="-8"><i> pending, the job will change to the </i><code>queued</code> state. If an <i> </i></font><font SIZE="-9"><i> is still pending, the job will change to the </i><code>waiting</code> state. </font></p>
<h2>OPTIONS</h2>
<dl>
<dt>-h hold_list</p>
<dd> Defines the types of hold to be released from the jobs. The <i> option argument is a string consisting of one or more of the letters &quot;</i><code>u</code>&quot;, &quot;<code>o</code>&quot;, an &quot;<code>s</code>&quot; in any combination. The hold type associated with each letter is:</p>
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
<p> The qrls command accepts one or more <i> operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>STANDARD ERROR</h2>
<p> The qrls command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qrls command, the exit status will be a value of zero. </p>
<p> If the qrls command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qhold/">qhold</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_holdjob/">pbs_holdjob</a>(3B), and <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rlsjob/">pbs_rlsjob</a>(3B). </p>
<h2>Index</h2>
