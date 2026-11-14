---
title: "md-mx-ctrl(8)"
name: "md-mx-ctrl"
section: "8"
letter: "m"
url: "/docs/linux/man/8-md-mx-ctrl/"
description: "md-mx-ctrl – Control mimedefang-multiplexor"
---

<p>md-mx-ctrl &#8211; Control mimedefang-multiplexor</p>
<h2>Synopsis</h2>
<p><code>md-mx-ctrl </code>[<i>options</i>] <i>command</i> </p>
<h2>Description</h2>
<p><code>md-mx-ctrl</code> is a command-line tool for communicating with <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8). </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Displays usage information. </p>
<dt><code>-s </code><i>path</i></p>
<dd>Specifies the path to the <code>mimedefang-multiplexor</code> socket. If not specified, defaults to /var/spool/MIMEDefang/mimedefang-multiplexor.sock. </p>
<dt><code>-i</code></p>
<dd>This flag causes <code>md-mx-ctrl</code> to sit in a loop, reading commands on standard input and printing results to standard output. It is intended for use by a monitoring program such as <code>watch-mimedefang</code>. </p>
</dl>
<h2>Commands</h2>
<p>The following commands are available: </p>
<dl>
<dt><code>status</code></p>
<dd>Prints the status of all slave Perl processes in human-readable format. </p>
<dt><code>rawstatus</code></p>
<dd>Prints the status of all slave Perl processes in a format easy to parse by computer. The result is a single line with six words on it. The words are separated by a single space character. </p>
<p> Each character in the first word corresponds to a slave, and is &quot;I&quot; for an idle slave, &quot;B&quot; for a busy slave, &quot;S&quot; for a slave which is not running, and &quot;K&quot; for a slave which has been killed, but has not yet exited. A slave is &quot;idle&quot; if there is a running Perl process waiting to do work. &quot;Busy&quot; means the Perl process is currently filtering a message. &quot;S&quot; means there is no associated Perl process with the slave, but one can be started if the load warrants. Finally, &quot;K&quot; means the slave Perl process has been killed, but has yet to terminate. </p>
<p> The second word is the total number of messages processed since the multiplexor started up. The third word is the total number of slaves which have been activated since the multiplexor started up. (That is, it&#8217;s a count of the number of times the multiplexor has forked and exec&#8217;d the Perl filter.) </p>
<p> The fourth word is the size of the queue for request queuing, and the fifth word is the actual number of requests in the queue. The sixth word is the number of seconds elapsed since the multiplexor was started. </p>
<dt><code>barstatus</code></p>
<dd>Prints the status of busy slaves and queued requests in a nice &quot;bar chart&quot; format. This lets you keep an eye on things with a script like this: </p>
<pre> while true ; do
 md-mx-ctrl barstatus
 sleep 1
 done</pre>
<dt><code>histo</code></p>
<dd>Prints a histogram showing the number of slaves that were busy each time a request was processed. A single line is printed for the numbers from 1 up to the maximum number of slaves. Each line contains the count of busy slaves (1, 2, 3 up to MX_MAXIMUM), a space, and the number of times that many slaves were busy when a request was processed. </p>
<dt><code>load</code></p>
<dd>Prints a table showing &quot;load averages&quot; for the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> Each row in the table corresponds to a time interval, displayed in the first column. The remaining columns in the table are: </p>
<p> <code>Msgs:</code> The number of messages scanned within the row&#8217;s time interval. </p>
<p> <code>Msgs/Sec:</code> The average number of messages scanned per second within the row&#8217;s time interval. </p>
<p> <code>Avg Busy Slaves:</code> The average number of busy slaves whenever a message was scanned. (If you are processing any mail at all, this number will be at least 1, because there is always 1 busy slave when a message is scanned.) </p>
<p> If you have the <code><a href="/docs/linux/man/1-watch/">watch</a></code>(1) command on your system, you can keep an eye on the load with this command: </p>
<pre> watch -n 10 md-mx-ctrl load</pre>
<p>If you do not have <code>watch</code>, the following shell script is a less fancy equivalent: </p>
<pre> #!/bin/sh
 while true; do
 clear
 date
 md-mx-ctrl load
 sleep 10
 done</pre>
<dt><code>rawload</code></p>
<dd>Prints the load averages in computer-readable format. The format consists of twenty-nine space-separated numbers: </p>
<p> The first four are integers representing the number of messages scanned in the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The second four are floating-point numbers representing the average number of busy slaves in the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The third four are floating-point numbers representing the average time per scan in milliseconds over the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The fourth four are the number of slave activations (new slaves started) over the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The fifth four are the number of slaves reaped (slaves that have exited) over the last 10 seconds, 1 minute, 5 minutes and 10 minutes. </p>
<p> The sixth four are the number of busy, idle, stopped and killed slaves. </p>
<p> The seventh four are the number of messages processed, the number of slave activations, the size of the request queue, and the number of requests actually on the queue. </p>
<p> The final number is the number of seconds since the multiplexor was started. </p>
<dt><code>load-relayok</code></p>
<dd>Similar to <code>load</code>, but shows timings for <code>filter_relay</code> calls. </p>
<dt><code>load-senderok</code></p>
<dd>Similar to <code>load</code>, but shows timings for <code>filter_sender</code> calls. </p>
<dt><code>load-recipok</code></p>
<dd>Similar to <code>load</code>, but shows timings for <code>filter_recipient</code> calls. </p>
<dt><code>rawload-relayok</code></p>
<dd>Similar to <code>rawload</code>, but shows timings for <code>filter_relay</code> calls. Note that the slave activation and reap statistics are present, but always 0. They are only valid in a <code>rawload</code> command. </p>
<dt><code>rawload-senderok</code></p>
<dd>Similar to <code>rawload</code>, but shows timings for <code>filter_sender</code> calls. Note that the slave activation and reap statistics are present, but always 0. They are only valid in a <code>rawload</code> command. </p>
<dt><code>rawload-recipok</code></p>
<dd>Similar to <code>rawload</code>, but shows timings for <code>filter_recipient</code> calls. Note that the slave activation and reap statistics are present, but always 0. They are only valid in a <code>rawload</code> command. </p>
<dt><code>load1 </code><i>nsecs</i></p>
<dd>The <code>load1</code> command displays the load for various commands over the last <i>nsecs</i> seconds, where <i>nsecs</i> is an integer from 10 to 600. The <code>load1</code> command combines the output of <code>load</code>, <code>load-relayok</code>, <code>load-senderokf</code> and <code>load-recipok</code> into one display. </p>
<p> You might use the command like this: </p>
<pre> watch -n 10 md-mx-ctrl load1 60</pre>
<dt><code>rawload1 </code><i>nsecs</i></p>
<dd>Returns the <code>load1</code> data in human-readable format. The result is a line containing twenty-six space-separated numbers: </p>
<p> The first three numbers are the number of scans performed in the last <i>nsecs</i> seconds, the average number of busy slaves when a scan was initiated and the average number of milliseconds per scan. </p>
<p> The second three are the same measurements for <code>filter_relay</code> calls. </p>
<p> The third three are the same measurements for <code>filter_sender</code> calls. </p>
<p> The fourth three are the same measurements for <code>filter_relay</code> calls. </p>
<p> The thirteenth through sixteenth numbers are the number of busy, idle, stopped and killed slaves, respectively. </p>
<p> The seventeenth number is the number of scans since <code>mimedefang-multiplexor</code> was started. </p>
<p> The eighteenth number is the number of times a new slave has been activated since program startup. </p>
<p> The nineteenth number is the size of the request queue and the twentieth number is the actual number of queued requests. </p>
<p> The twenty-first number is the time since program startup and the twenty-second number is a copy of <i>nsecs</i> for convenience. </p>
<p> The twenty-third through twenty-sixth numbers are the number of slaves currently executing a scan, relayok, senderok and recipok command respectively. </p>
<dt><code>slaves</code></p>
<dd>Displays a list of slaves and their process IDs. Each line of output consists of a slave number, a status (I, B, K, or S), and for idle or busy slaves, the process-ID of the slave. For busy slaves, the line may contain additional information about what the slave is doing. </p>
<dt><code>busyslaves</code></p>
<dd>Similar to <code>slaves</code>, but only outputs a line for each busy slave. </p>
<dt><code>slaveinfo </code><i>n</i></p>
<dd>Displays information about slave number <i>n</i>. </p>
<dt><code>reread</code></p>
<dd>Forces <code>mimedefang-multiplexor</code> to kill all idle slaves, and terminate and restart busy slaves when they become idle. This forces a reread of filter rules. </p>
<dt><code>msgs</code></p>
<dd>Prints the total number of messages scanned since the multiplexor started. </p>
</dl>
<h2>Additional Commands</h2>
<p>You can supply any other command and arguments to <code>md-mx-ctrl</code>. It percent-encodes each command-line argument, glues the encoded arguments together with a single space between each, and sends the result to the multiplexor as a command. This allows you to send arbitrary commands to your Perl slaves. See the section &quot;EXTENDING MIMEDEFANG&quot; in <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) for additional details.</p>
<h2>Permissions</h2>
<p><code>md-mx-ctrl</code> uses the multiplexor&#8217;s socket; therefore, it probably needs to be run as <i>root</i> or the same user as <code>mimedefang-multiplexor</code>.</p>
<h2>Author</h2>
<p><code>md-mx-ctrl</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7), <a href="/docs/linux/man/8-watch-mimedefang/">watch-mimedefang</a>(8) </p>
