---
title: "qenable(8)"
name: "qenable"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qenable/"
description: "qenable – enable input to a pbs destination"
---

<p>qenable &#8211; enable input to a pbs destination</p>
<h2>Synopsis</h2>
<p>qenable destination &#8230;</p>
<h2>Description</h2>
<p>The <code>qenable</code> command directs that a destination should accept batch jobs. </p>
<p> The qenable command sends a <i>Manage</i> request to the batch server specified by <i> If the command is accepted, the destination will accept Queue Job</i> requests which specified the queue. </p>
<p> In order to execute qenable, the user must have PBS Operation or Manager privilege.</p>
<h2>Operands</h2>
<p>The qenable command accepts one or more <i> operands. The operands are one of three forms:</p>
<dl>
<dd></i><code> </p>
</dl>
<p> If is specified, the request is to enable that queue at the default server. If the form is given, the request is to enable all the queues at that server. If a full destination identifier, is given, the request is to enable the named queue at the named server. </code></p>
<h2>Standard Error</h2>
<p>The qenable command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qenable command, the exit status will be a value of zero. </p>
<p> If the qenable command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qdisable/">qdisable</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B) </p>
