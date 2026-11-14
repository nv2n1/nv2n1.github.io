---
title: "qchkpt(1)"
name: "qchkpt"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qchkpt/"
description: "qchkpt – checkpoint pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qchkpt &#8211; checkpoint pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qchkpt job_identifier &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qchkpt </code> command requests that the PBS Mom generate a checkpoint file for a running job. </p>
<p> <font SIZE="-1">This is an extension to POSIX.2d.</font> </p>
<p> The qchkpt command sends a <i>Chkpt Job</i> batch request to the server as described in the general section.</p>
<h2>OPTIONS</h2>
<p> None </p>
<h2>OPERANDS</h2>
<p> The qchkpt command accepts one or more <i> operands of the form: </i><code> </p>
<p> </code></p>
<h2>STANDARD ERROR</h2>
<p> The qchkpt command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qchkpt command, the exit status will be a value of zero. </p>
<p> If the qchkpt command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qhold/">qhold</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrls/">qrls</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_holdjob/">pbs_holdjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rlsjob/">pbs_rlsjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_job_attributes/">pbs_job_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_unicos8/">pbs_resources_unicos8</a>(7B) </p>
<h2>Index</h2>
