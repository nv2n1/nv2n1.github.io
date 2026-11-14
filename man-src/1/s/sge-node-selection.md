---
title: "sge-node-selection(1)"
name: "sge-node-selection"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge-node-selection/"
description: "busy-nodes, idle-nodes, dead-nodes, nodes-in-job, qselect-node-list – List xxQS_NAMExx node names by various criteria"
---

<h2 class="name">NAME</h2>
<p> busy-nodes, idle-nodes, dead-nodes, nodes-in-job, qselect-node-list &#8211; List xxQS_NAMExx node names by various criteria </p>
<h2>SYNOPSIS</h2>
<p> <code>busy-nodes</code> [<code>-w</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
 <code>idle-nodes</code> [<code>-w</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
 <code>dead-nodes</code> [<code>-w</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
 <code>nodes-in-job</code> [<code>-w</code>] [<code>-h</code>|<code>&#8211;help</code>] <i>jobid</i><br />
 <code>qselect-node-list</code> [<code>-h</code>|<code>&#8211;help</code>] <i>qselect_arg</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>busy-nodes</code>, <code>idle-nodes</code>, and <code>dead-nodes</code> respectively list xxQS_NAMExx nodes which are: busy with one or more jobs, idle (without a job running), and &quot;dead&quot; (their xxQS_NAMExx exec daemon is not responding). <code>nodes-in-job</code> list nodes which are running the given <i>jobid</i> (presumably a parallel one). <code>qselect-node-list</code> runs with the given arguments. The node list is printed one node per line unless the <code>-w</code> option is used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&#8211;help</code></p>
<dd> Print usage information.</p>
<dt><code>-w</code></p>
<dd> Print the output in a form compatible with the <code>-w</code> argument of</dl>
<h2>EXAMPLES</h2>
<p> The following would reboot all idle nodes. (It is actually preferable to submit a job to reboot nodes, to avoid a race with job further submission.)</p>
<dl>
<dt>
<dd> <code>pdsh -w `idle-nodes -w` reboot</code></dl>
<p> The following would run selecting only nodes in job number &quot;123&quot;.</p>
<dl>
<dt>
<dd> <code>qhost `nodes-in-job 123`</code></dl>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> Dave Love &lt;d.love [at] liverpool.ac.uk&gt; </p>
<h2>Index</h2>
