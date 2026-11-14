---
title: "qsched(1)"
name: "qsched"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsched/"
description: "qsched, process-scheduler-log – show scheduling information on resource reservation"
---

<h2 class="name">NAME</h2>
<p> qsched, process-scheduler-log &#8211; show scheduling information on resource reservation </p>
<h2>SYNTAX</h2>
<p> <code>qsched</code> [<code>-u&nbsp;</code><i>user</i>|<code>&#8211;user=</code><i>user</i>] [<code>-a</code>|<code>&#8211;all</code>] [<code>-j&nbsp;</code><i>jid_list</i>|<code>&#8211;jid=</code><i>jid_list</i>] [<code>-f</code>|<code>&#8211;full</code>] [<code>-s</code> <code>j</code>|<code>&#8211;sort=j</code>] [<code>-q</code>|<code>&#8211;queues</code>] [<code>-d</code>|<code>&#8211;debug</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
 <code>process-scheduler-log</code> [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>qsched</code> reports resources being reserved for jobs on the basis of the <i>schedule</i> file, which is processed by <code>process-scheduler-log</code>, which runs continuously. Generating <i>schedule</i> requires setting <code>MONITOR=1</code> in the <code>params</code> parameter of the scheduler (see </p>
<p> <code>process-scheduler-log</code> should simply be started in the background as it does not currently daemonize itself. Alternatively, it could be run under or adapted to run as a global load sensor (see It needs <i>SGE_ROOT</i> and <i>SGE_CELL</i> set in the environment when it starts. </p>
<p> <code>qsched</code> and <code>process-scheduler-log</code> both potentially need editing to configure for the local installation, particularly the definition of <code>$trim_string</code> in <code>qsched</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a&nbsp;</code>|&nbsp;<code>&#8211;all</code></p>
<dd> View jobs belonging to all users (synonym for <code>-u user</code><i>)</i> View jobs belonging to <i>user</i>.</p>
<dt><code>-d&nbsp;</code>|&nbsp;<code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-f&nbsp;</code>|&nbsp;<code>&#8211;full</code></p>
<dd> Print all available data for each job.</p>
<dt><code>-h&nbsp;</code>|&nbsp;<code>&#8211;help</code></p>
<dd> Print help information.</p>
<dt><code>-j&nbsp;</code><i>jid_list&nbsp;</i>| &#8211;jid=<i>jid_list</i></p>
<dd> <i>jid_list</i> is a comma-separated list of job ids to view.</p>
<dt><code>-q | &#8211;queues</code></p>
<dd> Sort output by queue.</p>
<dt><code>-s j&nbsp;</code>| &#8211;sort=j</p>
<dd> Sort output by job id.</p>
<dt><code>-u user&nbsp;</code>| &#8211;user=<i>user</i></p>
<dd> View jobs belonging to <i>user</i>.</p>
<dt><code>-v</code></p>
<dd> Print information on standard output. <code>-u *</code>).</dl>
<p> The default is to sort by start time.</p>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/sgeprocschedlog.pid</i></p>
<dd> Contains the process id of <i>process-scheduler-log</i>.</p>
<dt><i>${SGE_ROOT}/${SGE_CELL}/common/act_qmaster</i></p>
<dd> Consulted to check that the qmaster is active.</p>
<dt><i>${SGE_ROOT}/${SGE_CELL}/common/schedule</i></p>
<dd> Normal schedule monitoring file.</p>
<dt><i>${SGE_ROOT}/${SGE_CELL}/common/schedule.last</i></p>
<dd> Contents of last complete scheduling interval seen in <i>schedule</i> file.</dl>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> Mark Dixon &lt;m.c.dixon [at] leeds.ac.uk&gt;<br />
 Man page by Dave Love &lt;d.love [at] liverpool.ac.uk&gt; </p>
<h2>Index</h2>
