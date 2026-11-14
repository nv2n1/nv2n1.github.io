---
title: "mimedefang-multiplexor(8)"
name: "mimedefang-multiplexor"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mimedefang-multiplexor/"
description: "mimedefang-multiplexor – Process pool controller for mail filters."
---

<p>mimedefang-multiplexor &#8211; Process pool controller for mail filters.</p>
<h2>Synopsis</h2>
<p><code>mimedefang-multiplexor </code>[<i>options</i>] </p>
<h2>Description</h2>
<p><code>mimedefang-multiplexor</code> manages a pool of Perl processes for scanning e-mail. It is designed to work in conjunction with <code><a href="/docs/linux/man/8-mimedefang/">mimedefang</a></code>(8) and <code><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a></code>(8). <code>mimedefang-multiplexor</code> opens a UNIX-domain socket and listens for requests for work from <code>mimedefang</code>. As requests come in, <code>mimedefang-multiplexor</code> creates Perl processes as needed to scan mail. The Perl processes are not killed when scanning is completed, but continue to run in a loop. Perl processes are re-used for subsequent e-mail messages. This eliminates the large overhead of starting a new Perl process for each incoming message. To avoid memory leaks, the Perl processes are killed after they have handled some number of scans. </p>
<h2>Options</h2>
<dl>
<dt><code>-U </code><i>user</i></p>
<dd>Runs the multiplexor as <i>user</i> rather than <i>root</i>. This option is mandatory, and must match the <code>-U</code> option supplied to <code>mimedefang</code>. </p>
<dt><code>-m </code><i>minSlaves</i></p>
<dd>The minimum number of Perl processes to keep running at all times. The default is zero. </p>
<dt><code>-x </code><i>maxSlaves</i></p>
<dd>The maximum number of Perl processes to run simultaneously. If a request comes in and all processes are busy, a temporary failure is signalled to the SMTP peer. The default is 2. </p>
<dt><code>-r </code><i>maxRequests</i></p>
<dd>The maximum number of requests a given process handles before it is killed and a replacement started. The default is 500. </p>
<dt><code>-i </code><i>idleTime</i></p>
<dd>The idle time in seconds after which to kill of excess Perl processes. That is, if the process is idle for longer than this time, and there are more than <i>minSlaves</i> running, the process is killed. Note that this is implemented as a timer which ticks every <i>idleTime</i> seconds; therefore, processes may be idle for up to twice this time before they are killed. The default for <i>idleTime</i> is 300 seconds. </p>
<dt><code>-b </code><i>busyTime</i></p>
<dd>The longest a Perl process is allowed to spend scanning an e-mail before it is declared hung up and killed. The default is 120 seconds. </p>
<dt><code>-Z</code></p>
<dd>This option specifies that the multiplexor should accept and process &quot;status updates&quot; from busy slaves. Note that this consumes one extra file descriptor per slave, plus a small amount of CPU time per status update. </p>
<dt><code>-c </code><i>cmdTime</i></p>
<dd>The timeout for communication between <code>mimedefang-multiplexor</code> and <code>mimedefang</code>, or between <code>mimedefang-multiplexor</code> and a Perl scanning process. The default is 10 seconds. This timeout should be kept quite short. </p>
<dt><code>-w </code><i>waitTime</i></p>
<dd>When <code>mimedefang-multiplexor</code> starts the initial slaves, or needs to bring the number of running slaves up to the number defined by the <code>-m</code> option, it does not start all the slaves at once, because this could overload your server. Instead, it starts one slave every <i>waitTime</i> seconds. The default value for <i>waitTime</i> is 3. </p>
<dt><code>-W </code><i>waitTime</i></p>
<dd>If you use this option, <code>mimedefang-multiplexor</code> will <i>never</i> activate a slave until <i>waitTime</i> seconds have elapsed since the last slave activation. This could result in mail being tempfailed if slave activations do not keep pace with incoming mail. However, it may be preferable to tempfail mail rather than allow the load on your server to spike up too quickly. The default value for this option is 0, meaning that <code>mimedefang-multiplexor</code> will start slaves as quickly as necessary to keep up with incoming mail. </p>
<dt><code>-z </code><i>spooldir</i></p>
<dd>Set the spool directory to <i>spooldir</i>. If this option is omitted, the spool directory defaults to /var/spool/MIMEDefang. </p>
<dt><code>-s </code><i>pathName</i></p>
<dd>The UNIX-domain socket on which <code>mimedefang-multiplexor</code> listens for requests. This should be specified as an absolute pathname. If this option is not supplied, it defaults to mimedefang-multiplexor.sock under the spool directory. </p>
<dt><code>-a </code><i>socket</i></p>
<dd>A socket for listening for requests. This is similar to the <code>-s</code> socket, except that a restricted set of requests are processed. On this socket, the multiplexor will only process requests asking for status; it will not accept any commands to do scanning or that would consume a slave. See the SOCKET SPECIFICATION section for the format of <i>socket</i>. </p>
<dt><code>-p </code><i>fileName</i></p>
<dd>Causes <code>mimedefang-multiplexor</code> to write its process-ID (after becoming a daemon) to the specified file. </p>
<dt><code>-f </code><i>filter_path</i></p>
<dd>Normally, <code>mimedefang-multiplexor</code> executes a Perl filter script called <code>mimedefang.pl</code> to scan the e-mail. However, you can have it execute any program you like by specifying the full path to the program with the <code>-f</code> option. This program must obey the protocol documented in <code><a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a></code>(7); see that manual page for details. </p>
<p> Note that the <code>-f</code> option does <i>not</i> specify the &quot;filter&quot; to use with <code>mimedefang.pl</code>; instead, it specifies the program for <code>mimedefang-multiplexor</code> to execute. You almost certainly should <i>not</i> use this option unless you wish to replace <code>mimedefang.pl</code> with your own program. </p>
<dt><code>-F </code><i>rules_path</i></p>
<dd>Specifies the path to the filter rules. By default, <code>/etc/mail/mimedefang-filter</code> is used. If you use the <code>-F</code> option, its value is passed to the underlying Perl filter program using <code>-f</code>. </p>
<dt><code>-l</code></p>
<dd>Log certain events, including the output of the Perl slaves&#8217; standard-error, using syslog. Normally, the multiplexor does not log much information. </p>
<dt><code>-d</code></p>
<dd>Write debugging information about event-handling code in /var/log/mimedefang-event-debug.log. This is only of use to people debugging <code>mimedefang-multiplexor</code>. </p>
<dt><code>-R </code><i>kbytes</i></p>
<dd>Limits the resident-set size of the slave filter processes to <i>kbytes</i> kilobytes. This limit is not supported on all operating systems; it is known to work on Linux. </p>
<dt><code>-M </code><i>kbytes</i></p>
<dd>Limits the total memory space of slave filter processes to <i>kbytes</i> kilobytes. This limit is supported on all operating systems which support the <a href="/docs/linux/man/2-setrlimit/">setrlimit</a>(2) system call. This should include most modern UNIX systems. </p>
<p> We recommend that you monitor your slave filter processes and get a feel for how much memory they use. You should then limit the memory to two or three times the worst-case that you have observed. This can help mitigate denial-of-service attacks which use complicated MIME messages to force <code>mimedefang.pl</code> to consume lots of memory. </p>
<dt><code>-h</code></p>
<dd>Print usage information and exit. </p>
<dt><code>-t </code><i>filename</i></p>
<dd>Log statistical information to <i>filename</i>. See the section STATISTICS for more information. </p>
<dt><code>-T</code></p>
<dd>Log statistical information using <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2). You may use any <code>-t</code> and <code>-T</code> together, in which case statistical information is logged in a file and using <code>syslog</code>. </p>
<dt><code>-u</code></p>
<dd>Flush the statistics file after every write. Normally, <code>mimedefang-multiplexor</code> does not flush the file; this is the best choice for minimizing disk I/O on a busy mail server. However, if you wish to watch statistics entries in real-time, you should enable flushing. </p>
<dt><code>-D</code></p>
<dd>Do not fork into the background and become a daemon. Instead, stay in the foreground. Useful mainly for debugging or if you have a supervisory process managing <code>mimedefang-multiplexor</code>. </p>
<dt><code>-q </code><i>queue_size</i></p>
<dd>Normally, if all slaves are busy and <code>mimedefang-multiplexor</code> receives another request, it fails it with the error &quot;No free slaves.&quot; However, if you use the <code>-q</code> option, then up to <i>queue_size</i> requests will be queued. As soon as a slave becomes free, the queued requests will be handed off in FIFO order. If the queue is full and another request comes in, then the request is failed with &quot;No free slaves&quot;. </p>
<dt><code>-Q </code><i>queue_timeout</i></p>
<dd>Queued requests should not stay on the queue indefinitely. If a queued request cannot be processed within <i>queue_timeout</i> (default 30) seconds of being placed on the queue, it is failed with a &quot;Queued request timed out&quot; message. See the section &quot;QUEUEING REQUESTS&quot; for more discussion. </p>
<dt><code>-O </code><i>sock</i></p>
<dd>Listen on a <i>notification socket</i> for connections from <i>listeners</i>. <code>mimedefang-multiplexor</code> can inform external programs of state changes by sending messages over a notification socket. The external programs connect to this socket and then listen for notifications. See the section SOCKET SPECIFICATION for the format of <i>sock</i>. </p>
<p> See the <code><a href="/docs/linux/man/7-mimedefang-notify/">mimedefang-notify</a></code>(7) man page for details of the notification protocol. </p>
<dt><code>-N </code><i>map_sock</i></p>
<dd>Listen on a <i>map socket</i> for Sendmail SOCKETMAP connections. As of Sendmail 8.13, you can define a Sendmail map type that talks to a daemon over a socket. <code>mimedefang-multiplexor</code> implements that protocol; consult the <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) man page for detils (see the SOCKET MAPS section). </p>
<p> See the section SOCKET SPECIFICATION for the format of <i>map_sock</i>. </p>
<dt><code>-I </code><i>backlog</i></p>
<dd>When <code>mimedefang-multiplexor</code> creates a listening socket, it calculates the &quot;backlog&quot; argument to <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) based on the maximum number of slaves. However, you can explicitly set this backlog with the <code>-I</code> option. Setting the backlog to a high value (around 30-50) may help on a very busy server. If you see mail log messages saying &quot;MXCommand: socket: Connection refused&quot; during busy periods, then that&#8217;s an indication you need a higher listen backlog. </p>
<dt><code>-L </code><i>interval</i></p>
<dd>Log the slave status every <i>interval</i> seconds. This logs a line using syslog; the line looks like this: </p>
<dt>
<pre><dd>Slave status: Stopped=s Idle=i Busy=b Killed=k Queued=q Msgs=m Activations=a</pre>
<p>Here, &quot;Stopped&quot; is the number of non-running slaves, &quot;Idle&quot; is the number of idle slaves, &quot;Busy&quot; is the number of busy slaves, &quot;Killed&quot; is the number of killed slaves yet to be reaped, &quot;Queued&quot; is the number of queued requests, &quot;Msgs&quot; is the total number of messages processed since the multiplexor began running, and &quot;Activations&quot; is the number of times a Perl process has been started since the multiplexor began running. </p>
<p> If you supply an <i>interval</i> of 0 (which is the default), no periodic status logging is performed. If you supply an <i>interval</i> of less than 5 seconds, it is silently reset to 5 seconds. </p>
<dt><code>-S </code><i>facility</i></p>
<dd>Specifies the syslog facility for log messages. The default is <i>mail</i>. See <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3) for a list of valid facilities. You can use either the short name (&quot;mail&quot;) or long name (&quot;LOG_MAIL&quot;) for the facility name. </p>
<dt><code>-E</code></p>
<dd>Specifies that the multiplexor should create an embedded Perl interpreter. This can improve performance dramatically. But see the section &quot;EMBEDDING PERL&quot; for more information. </p>
<dt><code>-X</code> <i>n</i></p>
<dd>Specifies that the multiplexor should initiate a &quot;tick&quot; request every <i>n</i> seconds. This causes your <i>filter_tick</i> function (if defined) to be called. Note that you have no control over which slave executes <i>filter_tick</i>. If all slaves are busy when a tick occurs, that tick request is skipped and a warning message is logged. </p>
<dt><code>-P</code> <i>n</i></p>
<dd>Specifies that the multiplexor should run <i>n</i> tick requests in parallel. Each tick is run as often as specified with the <code>-X</code> argument. (If you omit the <code>-P</code> option, then the multiplexor behaves as if <code>-P 1</code> had been specified.) </p>
<p> If you run parallel ticks, each tick is assigned an integer identifying its &quot;type&quot;. The type ranges from 0 to <i>n</i>-1. While there may be as many as <i>n</i> tick requests running at a time, only one tick of each type will be active at any time. </p>
<dt><code>-Y</code> <i>label</i></p>
<dd>Sets the tag used in the multiplexor&#8217;s syslog messages to <i>label</i> instead of <code>mimedefang-multiplexor</code>. </p>
<dt><code>-G</code></p>
<dd>Normally, <code>mimedefang-multiplexor</code> uses a umask of 027 when creating listening sockets. If you would like the sockets to be readable and writeable by the group as well as the owner, supply the <code>-G</code> option. This causes the umask to be 007 whenever UNIX-domain sockets are created. </p>
<dt><code>-y</code> <i>n</i></p>
<dd>Limits the maximum number of concurrent <code>recipok</code> checks to <i>n</i> on a per-domain basis. The value of <i>n</i> can range from 0 (in which case no limit is applied) to <i>maxSlaves</i>, where <i>maxSlaves</i> is the argument to the <code>-x</code> option. If <i>n</i> is outside that range, it is ignored (and no limit is applied.) </p>
<dl>
<dd>The <code>recipok</code> command ultimately invokes the <code>filter_recipient</code> function in your filter. If you are doing recipient verification against servers that may be slow or unreliable, you can use the <code>-y</code> option to limit the number of concurrent recipient verifications per domain. That way, if one domain&#8217;s server becomes very slow, it won&#8217;t consume all available slaves for recipient verification. Instead, its RCPT commands will be tempfailed and there will be slaves available to handle RCPT commands for other domains.</dl>
</dl>
<h2>Socket Specification</h2>
<p>The <code>-a</code>, <code>-N</code> and <code>-O</code> options take a socket as an argument. This socket can be specified as: </p>
<dl>
<dt><code>/path/to/socket</code></p>
<dd>A UNIX-domain socket </p>
<dt><code>inet:portnum</code></p>
<dd>A TCP socket bound to port <i>portnum</i>, but which accepts connections only from the IPv4 loopback address (127.0.0.1). </p>
<dt><code>inet_any:portnum</code></p>
<dd>A TCP socket bound to port <i>portnum</i> which will accept connections from any address. <i>Use inet_any with caution!</i> </p>
<dt><code>inet6:portnum</code></p>
<dd>A TCP socket bound to port <i>portnum</i> listening on the IPv6 loopback address. </p>
<dt><code>inet6_any:portnum</code></p>
<dd>A TCP socket bound to port <i>portnum</i> listening on the IPv6 wildcard address. </p>
</dl>
<h2>Queueing Requests</h2>
<p>Normally, if all slaves are busy, any additional requests are failed immediately. However, the <code>-q</code> and <code>-Q</code> options allow you to queue requests for a short amount of time. This facility is intended to gracefully handle a temporary overload; most of the time, your queue should be empty. </p>
<p> Because <code>mimedefang</code> checks the number of free slaves when a connection is opened and fails the connection if there are no free slaves, the intent of the queue is to allow SMTP transactions that are already underway to continue if there is a slight overload. Any new connections will be failed if all slaves are busy, but existing connections are allowed to continue. Queuing requests may improve throughput on extremely busy servers. </p>
<p> Note that if you supply the <code>-q</code> option to <code>mimedefang</code>, then even new connections are allowed to queue. This may improve throughput by keeping the slave utilization higher. </p>
<p> The <code>-R</code> option to <code>mimedefang</code> can be used to reserve a specified number of slaves for connections from the loopback address. Using the <code>-R</code> option has the side-effect of permitting new connections from the loopback address to queue.</p>
<h2>Embedding Perl</h2>
<p>Normally, when <code>mimedefang-multiplexor</code> activates a slave, it forks and execs <code>mimedefang.pl</code>. However, if the multiplexor was compiled with embedded Perl support, and you supply the <code>-E</code> command-line option, the multiplexor works like this: </p>
<dl>
<dt>1</p>
<dd>It creates an embedded Perl interpreter, and sources <code>mimedefang.pl</code> with a special command-line argument telling it to read the filter, but not to enter the main loop. </p>
<dt>2</p>
<dd>Each time a slave is activated, the multiplexor calls fork() and runs the <code>mimedefang.pl</code> main loop. This invokes <code>filter_initialize</code> and then runs the main loop. </p>
</dl>
<p> On some platforms (for example, Red Hat Linux 7.3 with Perl 5.6.1), it is not safe to destroy and recreate a Perl interpreter without causing a memory leak. On those platforms, if you attempt to reread the filter file (by sending the multiplexor a HUP signal or reread command), the filter will <i>not</i> be re-read, and a message will be logged to syslog. On those platforms, you must kill and restart MIMEDefang if you change the filter file. </p>
<p> On most platforms, however, a filter reread is accomplished by destroying and re-creating the embedded interpreter, re-sourcing <code>mimedefang.pl</code> and killing slaves as soon as they are idle.</p>
<h2>Statistics</h2>
<p>With the <code>-t</code> option, <code>mimedefang-multiplexor</code> logs certain events to a file. This file can be post-processed to gather statistics about the multiplexor. You can use it to tune the number of slaves you run, adjust timeouts, and so on. </p>
<p> Each line of the file looks like this: </p>
<pre> YYYY/MM/DD:HH:MM:SS timestamp event key=val key=val...</pre>
<p>Here, YYYY/MM/DD:HH:MM:SS is the local time of day. Timestamp is the number of seconds since January 1, 1970. Event is the name of an event. The valid events are: </p>
<dl>
<dt><code>StartSlave</code></p>
<dd>A slave process has been started. </p>
<dt><code>KillSlave</code></p>
<dd>A slave process has been killed. </p>
<dt><code>ReapSlave</code></p>
<dd>A dead slave process has been reaped. It is possible to have a ReapSlave event without a previous KillSlave event if the slave process terminated abnormally. </p>
<dt><code>StartFilter</code></p>
<dd>A slave process has begun filtering an e-mail message. </p>
<dt><code>EndFilter</code></p>
<dd>A slave process has finished filtering an e-mail message. </p>
</dl>
<p> The possible keys in the key=value pairs are: </p>
<dl>
<dt><code>slave=</code><i>n</i></p>
<dd>The slave involved in the event. Every slave is identified by a small integer. </p>
<dt><code>nslaves=</code><i>n</i></p>
<dd>The total number of running slaves immediately after the event happened. </p>
<dt><code>nbusy=</code><i>n</i></p>
<dd>The number of busy slaves (slaves which are processing an e-mail message) immediately after the event happened. </p>
<dt><code>reason=</code><i>string</i></p>
<dd>The reason for a StartSlave or KillSlave event. (Present only for these events.) </p>
<dt><code>numRequests=</code><i>n</i></p>
<dd>The number of e-mails processed by the slave. Present only for an EndFilter event. </p>
</dl>
<p> If you send the <code>mimedefang-multiplexor</code> process a SIGHUP signal (kill -1 <i>pid</i>), it closes and reopens the statistics file. This is useful during log file rotation. </p>
<p> If you send the <code>mimedefang-multiplexor</code> process a SIGINT signal (kill -INT <i>pid</i>), it terminates all active-but-idle slaves. Also, any active-and-busy slaves terminate as soon as they finish filtering the current message. This is useful to force a reread of the filter rules file without stopping and restarting Sendmail. </p>
<p> If you send the <code>mimedefang-multiplexor</code> process a SIGTERM signal (kill <i>pid</i>), it terminates all slaves and exits immediately.</p>
<h2>Author</h2>
<p><code>mimedefang-mulitplexor</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7) </p>
