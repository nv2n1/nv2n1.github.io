---
title: "qstop(8)"
name: "qstop"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qstop/"
description: "qstop – stop pbs batch job processing at a destination"
---

<p>qstop &#8211; stop pbs batch job processing at a destination</p>
<h2>Synopsis</h2>
<p>qstop destination &#8230;</p>
<h2>Description</h2>
<p>The <code>qstop</code> command directs that a destination should stop processing batch jobs. If the destination is a execution queue, the server will cease scheduling jobs that reside in the queue for execution. If the destination is a routing queue, the server will cease routing jobs from that queue. </p>
<p> In order to execute qstop, the user must have PBS Operation or Manager privilege.</p>
<h2>Operands</h2>
<p>The qstop command accepts one or more <i> operands. The operands are one of three forms:</p>
<dl>
<dd></i><code> </p>
</dl>
<p> If is specified, the request is to stop that queue at the default server. If the form is given, the request is to stop all the queues at that server. If a full destination identifier, is given, the request is to stop the named queue at the named server. </code></p>
<h2>Standard Error</h2>
<p>The qstop command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qstop command, the exit status will be a value of zero. </p>
<p> If the qstop command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstart/">qstart</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B) </p>
