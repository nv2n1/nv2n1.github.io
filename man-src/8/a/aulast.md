---
title: "aulast(8)"
name: "aulast"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aulast/"
description: "aulast – a program similar to last"
---

<p>aulast &#8211; a program similar to last</p>
<h2>Synopsis</h2>
<p><code>aulast [ options ] </code> </p>
<h2>Description</h2>
<p><code>aulast</code> is a program that prints out a listing of the last logged in users similarly to the program <code>last</code> and <code>lastb</code>. Aulast searches back through the audit logs or the given audit log file and displays a list of all users logged in (and out) based on the range of time in the audit logs. Names of users and tty’s can be given, in which case aulast will show only those entries matching the arguments. The pseudo user reboot logs in each time the system is rebooted. Thus last reboot will show a log of all reboots since the log file was created. The main difference that a user will notice is that <code>aulast</code> print events from oldest to newest, while <code>last</code> prints records from newest to oldest. Also, the audit system is not notified each time a tty or pty is allocated, so you may not see quite as many records indicating users and their tty&#8217;s. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;bad</code></p>
<dd>Report on the bad logins. </p>
<dt><code>&#8211;extract</code></p>
<dd>Write raw audit records used to create the displayed report into a file aulast.log in the current working directory. </p>
<dt><code>-f</code><i>file</i></p>
<dd>Use the file instead of the audit logs for input. </p>
<dt><code>&#8211;proof</code></p>
<dd>Print out the audit event serial numbers used to determine the preceding line of the report. A Serial number of 0 is a place holder and not an actual event serial number. The serial numbers can be used to examine the actual audit records in more detail. Also an ausearch query is printed that will let you find the audit records associated with that session. </p>
<dt><code>&#8211;stdin</code></p>
<dd>Take audit records from stdin. The audit events must be in the raw format. </p>
<dt><code>&#8211;tty</code></p>
<dd>Limit the report to a specific tty&#8217;s activity. The names of ttys can be abbreviated. For example, 0 is the same as tty0. </p>
<dt><code>&#8211;user</code><i>name</i></p>
<dd>Limit the report to a specific user. </p>
</dl>
<h2>Examples</h2>
<pre>To see this month's logins
<code>ausearch --start this-month --raw | aulast --stdin</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-last/">last</a></code>(1), <code><a href="/docs/linux/man/1-lastb/">lastb</a></code>(1), <code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
