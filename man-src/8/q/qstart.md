---
title: "qstart(8)"
name: "qstart"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qstart/"
description: "qstart – start pbs batch job processing at a destination"
---

<p>qstart &#8211; start pbs batch job processing at a destination</p>
<h2>Synopsis</h2>
<p>qstart destination &#8230;</p>
<h2>Description</h2>
<p>The <code>qstart</code> command directs that a destination should process batch jobs. If the destination is an execution queue, the server will begin to schedule jobs that reside in the queue for execution. If the destination is a routing queue, the server will begin to route jobs from that queue. </p>
<p> In order to execute qstart, the user must have PBS Operation or Manager privilege.</p>
<h2>Operands</h2>
<p>The qstart command accepts one or more <i> operands. The operands are one of three forms:</p>
<dl>
<dd></i><code> </p>
</dl>
<p> If is specified, the request is to start that queue at the default server. If the form is given, the request is to start all queues at that server. If a full destination identifier, is given, the request is to start the named queue at the named server. </code></p>
<h2>Standard Error</h2>
<p>The qstart command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qstart command, the exit status will be a value of zero. </p>
<p> If the qstart command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstop/">qstop</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B) </p>
