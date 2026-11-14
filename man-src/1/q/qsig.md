---
title: "qsig(1)"
name: "qsig"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsig/"
description: "qsig – signal pbs batch job"
---

<h2 class="name">NAME</h2>
<p> qsig &#8211; signal pbs batch job </p>
<h2>SYNOPSIS</h2>
<p> qsig [-s signal] job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qsig</code> command requests that a signal be sent to executing batch jobs. The signal is sent to the session leader of the job. </p>
<p> If the <i> option is not specified, </i><code>`SIGTERM&#8217; </code> is sent. The request to signal a batch job will be rejected if:</p>
<dl>
<dt>&#8211;</p>
<dd> The user is not authorized to signal the job.</p>
<dt>&#8211;</p>
<dd> The job is not in the <code>running</code> state.</p>
<dt>&#8211;</p>
<dd> The requested signal is not supported by the system upon which the job is executing.</dl>
<p> The qsig command sends a <i>Signal Job</i> batch request to the server which owns the job.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-s signal</p>
<dd> Declares which signal is sent to the job.</p>
<dl>
<dt>
<dd>
<p> The <i> argument is either a signal name, e.g. </i><code>SIGKILL</code>, the signal name without the <code>SIG</code> prefix, e.g. <code>KILL</code>, or a unsigned signal number, e.g. <code>9</code>. The signal name <code>SIGNULL</code> is allowed; the server will send the signal 0 to the job which will have no effect on the job, but will cause an obituary to be sent if the job is no longer executing. Not all signal names will be recognized by qsig. If it doesn&#8217;t recognize the signal name, try issuing the signal number instead. </p>
<p> Two special signal names, &quot;suspend&quot; and &quot;resume&quot;, are used to suspend and resume jobs. Cray systems use the Cray-specific suspend()/resume() calls. </p>
<p> On non-Cray system, suspend causes a SIGTSTP to be sent to all processes in job&#8217;s top task, wait 5 seconds, and then send a SIGSTOP to all processes in all tasks on all nodes in the job. This differs from TORQUE 2.0.0 which did not have the ability to propogate signals to sister nodes. Resume sends a SIGCONT to all processes in all tasks on all nodes. </p>
<p> When suspended, a job continues to occupy system resources but is not executing and is not charged for walltime. The job will be listed in the &quot;S&quot; state. Manager or operator privilege is required to suspend or resume a job. </p>
<p> Note that interactive jobs may not resume properly because the top-level shell will background the suspended child process.</dl>
</dl>
<h2>OPERANDS</h2>
<p> The qsig command accepts one or more <i> operands of the form: </i></p>
<h2>STANDARD ERROR</h2>
<p> The qsig command will write a diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qsig command, the exit status will be a value of zero. </p>
<p> If the qsig command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_sigjob/">pbs_sigjob</a>(3B), pbs_resources_*(7B) where * is system type, and the PBS ERS. </p>
<h2>Index</h2>
