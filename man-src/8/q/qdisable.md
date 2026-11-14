---
title: "qdisable(8)"
name: "qdisable"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qdisable/"
description: "qdisable – disable input to a pbs destination"
---

<p>qdisable &#8211; disable input to a pbs destination</p>
<h2>Synopsis</h2>
<p>qdisable destination &#8230;</p>
<h2>Description</h2>
<p>The <code>qdisable</code> command directs that a destination should no longer accept batch jobs. If the command is accepted, the destination will no longer accept <i>Queue Job</i> requests which specified the disabled queue. Jobs which already reside in the queue will continue to be processed. This allows a queue to be &quot;drained.&quot; </p>
<p> In order to execute qdisable, the user must have PBS Operation or Manager privilege.</p>
<h2>Operands</h2>
<p>The qdisable command accepts one or more <i> operands. The operands are one of three forms:</p>
<dl>
<dd></i><code> </p>
</dl>
<p> If is specified, the request is to disable that queue at the default server. If the form is given, the request is to disable all the queues at that server. If a full destination identifier, is given, the request is to disable the named queue at the named server. </code></p>
<h2>Standard Error</h2>
<p>The qdisable command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qdisable command, the exit status will be a value of zero. </p>
<p> If the qdisable command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B), and <a href="//www.systutorials.com/docs/linux/man/8B-qenable/">qenable</a>(8B) </p>
