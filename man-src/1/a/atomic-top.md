---
title: "atomic-top(1)"
name: "atomic-top"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-top/"
description: "atomic-top – Run a top-like list of active container processes"
---

<h2 class="name">NAME</h2>
<p> atomic-top &#8211; Run a top-like list of active container processes </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic top</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-d</code>][<code>-o, &#8211;optional=[time, stime, ppid, uid, gid, user, group]</code>][<code>-n</code>] [Containers to monitor] </p>
<h2>DESCRIPTION</h2>
<p> <code>Atomic top</code> displays an interactive, top-like view of the processes running in active containers. </p>
<p> While in the interactive view, you can sort the columns of information by pressing a single character that correlates to the column header. Any column that you can sort on will have a set of parentheses that surround a single character. For example, if you want to sort by the &#8216;(P)ID&#8217; column, simply press the &#8216;p&#8217; key. </p>
<p> Like top, you can exit the interactive view and return to the command line, use the &#8216;q&#8217; character key. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-d</code><br />
&nbsp;<wbr>&nbsp;<wbr>Define the interval in seconds on which you want to refresh the process information.&nbsp;<wbr>&nbsp;<wbr>The interval should be an<br />
&nbsp;<wbr>&nbsp;<wbr>integer greater than 0.&nbsp;<wbr>&nbsp;<wbr>The default interval is set to 1. </p>
<p> <code>-n</code><br />
&nbsp;<wbr>&nbsp;<wbr>The number of iterations.&nbsp;<wbr>&nbsp;<wbr>Must be greater than 0. </p>
<p> <code>-o</code> <code>&#8211;optional</code><br />
&nbsp;<wbr>&nbsp;<wbr>Add more fields of data to collect for each process.&nbsp;<wbr>&nbsp;<wbr>The fields resemble fields commonly used by<br />
&nbsp;<wbr>&nbsp;<wbr>ps -o.&nbsp;<wbr>&nbsp;<wbr>They currently are:&nbsp;<wbr>[time, stime, ppid, uid, gid, user, group] </p>
<p> Specify one option per -o flag to include the fields. </p>
<h2>EXAMPLES</h2>
<p> Monitor processes with default fields. </p>
<dl>
<dt>
<dd>
<pre>
atomic top
</pre>
</dl>
<p> Monitor processes with default fields on a 5 second interval for 3 iterations </p>
<dl>
<dt>
<dd>
<pre>
atomic top -d 5 -n 3
</pre>
</dl>
<p> Monitor processes and add in the data for the parent PIDs and UID. </p>
<dl>
<dt>
<dd>
<pre>
atomic top -o ppid -o uid
</pre>
</dl>
<h2>HISTORY</h2>
<p> December 2015, Originally written by Brent Baude (bbaude at redhat dot com) </p>
<h2>Index</h2>
