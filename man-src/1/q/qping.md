---
title: "qping(1)"
name: "qping"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qping/"
description: "qping – check application status of xxQS_NAMExx daemons."
---

<h2 class="name">NAME</h2>
<p> qping &#8211; check application status of xxQS_NAMExx daemons.</p>
<h2>SYNTAX</h2>
<p> <code>qping</code> [<code>-help</code>] [<code>-noalias</code>] [<code>-ssl</code>|<code>-tcp</code>] [[[<code>-i</code> <i>interval</i>] [<code>-info</code>] [<code>-f</code>]] | [[ <code>-dump_tag</code> <i>tag</i> [<i>param</i>]] [<code>-dump</code>] [<code>-nonewline</code>]]] <i>host port name id</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>Qping</i> is used to validate the runtime status of a xxQS_NAMExx service daemon. The current xxQS_NAMExx implementation allows one to query the xxQS_NAME_Sxx_QMASTER daemon and any running xxQS_NAME_Sxx_EXECD daemon. The command is used to send a SIM (Status Information Message) to the destination daemon. The communication layer of the specified daemon will respond with a SIRM (Status Information Response Message) which contains status information about that daemon. It also has options allow an administrator to observe the communication protocol data flow of a xxQS_NAMExx service daemon. </p>
<h2>OPTIONS</h2>
<h3><code>-f</code></h3>
<p> Show full status information on each ping interval. </p>
<p> <i>First output line:</i> The first output line shows the date and time of the request. </p>
<p> <i>SIRM version:</i> Internal version number of the SIRM (Status Information Response Message) </p>
<p> <i>SIRM message id:</i> Current message id for this connection </p>
<p> <i>start time:</i> Start time of daemon. The format is as follows: </p>
<p> MM/DD/YYYY HH:MM:SS (seconds since 01.01.1970) </p>
<p> <i>run time [s]:</i> Run time in seconds since start time </p>
<p> <i>messages in read buffer:</i> Number of buffered messages in the communication read buffer. The messages are buffered for the application (daemon). When this number grows too large the daemon is not able to handle all messages sent to it. </p>
<p> <i>messages in write buffer:</i> Number of buffered messages in the communication write buffer. The messages are sent from the application (daemon) to the connected clients, but the communication layer wasn&#8217;t able to send the messages yet. If this number grows too large, the communication layer isn&#8217;t able to send them as fast as the application (daemon) wants the messages to be sent. </p>
<p> <i>number of connected clients:</i> This is the number of clients actually connected to this daemon, including the current qping connection. </p>
<p> <i>status:</i> The status value of the daemon. This value depends on the application which replies to the qping request. If the application does not provide any information, the status is 99999. Here are the possible status information values for the xxQS_NAMExx daemons: </p>
<p> qmaster: </p>
<p> <i>0</i> There is no unusual timing situation. </p>
<p> <i>1</i> One or more threads has reached warning timeout. This may happen when at least one thread does not increment its time stamp for an usually long time. A possible reason for this is a high workload for this thread.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <i>2</i> One or more threads has reached error timeout. This may happen when at least one thread has not incremented its time stamp for longer than 10 minutes. </p>
<p> <i>3</i> The time measurement is not initialized. </p>
<p> execd: </p>
<p> <i>0</i> There is no unusual timing situation. </p>
<p> <i>1</i> Dispatcher has reached warning timeout. This may happen when the dispatcher does not increment its time stamp for an unusually long time. A possible reason for this is a high workload.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <i>2</i> Dispatcher has reached error timeout. This may happen when the dispatcher has not incremented its time stamp for longer than 10 minutes. </p>
<p> <i>3</i> The time measurement is not initialized. </p>
<p> <i>info:</i> Status message of the daemon. This value depends on the application which replies to the qping request. If the application does not provide any information the info message is &quot;not available&quot;. Here are the possible status information values for the xxQS_NAMExx daemons: </p>
<p> qmaster: </p>
<p> The info message contains information about the qmaster threads, followed by a thread state and time information. Each time one of the known threads passes through its main loop the time information is updated. Since the qmaster has two message threads, every message thread updates the time. This means the timeout for the message thread (MT) can only occur when no message thread is active anymore: </p>
<p> THREAD_NAME: THREAD_STATE (THREAD_TIME) </p>
<p> THREAD_NAME: </p>
<pre>
MAIN: Main thread 
signaler: Signal thread 
event_master: Event master thread 
timer: Timer thread 
worker: Worker thread
listener: Listener thread
scheduler: Scheduler thread
jvm: Java thread 
</pre>
<p> The thread names above (other than MAIN) will be followed by a 3 digit number. </p>
<p> THREAD_STATE: </p>
<pre>
R: Running
W: Warning
E: Error
</pre>
<p> THREAD_TIME: </p>
<pre>
Time since last timestamp updating.
</pre>
<p> After the dispatcher information comes an additional information string which describes the complete application status. </p>
<p> execd: </p>
<p> The info message contains information for the execd job dispatcher: dispatcher: STATE (TIME) </p>
<p> STATE: </p>
<pre>
R: Running
W: Warning
E: Error
</pre>
<p> TIME: </p>
<pre>
Time since last timestamp updating.
</pre>
<p> After the thread information comes statistics on the <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) state, if available, e.g. using <i><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></i>(3). If xxQS_NAMExx is built with the allocator, the statistics are not printed by default because they are in a different, verbose format. See <code>print_malloc_info</code> in </p>
<p> <i>Monitor:</i> If available (see <code>MONITOR_TIME</code> In <code>qmaster_params</code> in displays statistics on threads. The data for each thread are displayed in one line. The format of this line can be changed at any time. Only the master implements monitoring.</p>
<h3><code>-help</code></h3>
<p> Prints a list of all options.</p>
<h3><code>-i interval</code></h3>
<p> Set qping interval. The default interval is one second. Qping will send a SIM (Status Information Message) after each interval.</p>
<h3><code>-info</code></h3>
<p> Show full status information (see <code>-f</code> for more information) and exit. The exit value 0 indicates no error. On errors qping returns with 1.</p>
<h3><code>-noalias</code></h3>
<p> Ignore host_aliases file, which is located at <i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/host_aliases.</i> If this option is used it is not necessary to set any xxQS_NAMExx environment variable.</p>
<h3><code>-ssl</code></h3>
<p> This option can be used to specify an SSL (Secure Socket Layer) configuration. qping will use the configuration to connect to services running SSL. If the xxQS_NAMExx settings file is not sourced, you have to use the <code>-noalias</code> option to bypass the need for the SGE_ROOT environment variable. The following environment variables are used to specify your certificates:<br />
&nbsp;<wbr>&nbsp;SSL_CA_CERT_FILE &#8211; CA certificate file<br />
&nbsp;<wbr>&nbsp;SSL_CERT_FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; certificates file<br />
&nbsp;<wbr>&nbsp;SSL_KEY_FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; key file<br />
&nbsp;<wbr>&nbsp;SSL_RAND_FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; rand file</p>
<h3><code>-tcp</code></h3>
<p> This option is used to select TCP/IP as the protocol used to connect to other services.</p>
<h3><code>-nonewline</code></h3>
<p> Dump output will not have a linebreak within a message, and binary messages are not unpacked.</p>
<h3><code>-dump</code></h3>
<p> This option allows an administrator to observe the communication protocol data flow of a xxQS_NAMExx service daemon. The command must be started as root, and on the host where the daemon to be observed is running. </p>
<p> The output is written to stdout. The environment variable &quot;SGE_QPING_OUTPUT_FORMAT&quot; can be set to hide columns, set a default column width, or to set a hostname output format. The value of the environment variable can be set to any combination of the following specifiers separated by a space character:</p>
<dl>
<dt>
<dd>
<pre><code>
"h:X"-&gt;hide column X
    "s:X"-&gt;show column X
    "w:X:Y"-&gt;set width of column X to Y
    "hn:X"-&gt;set hostname output parameter X.X values are "long" or
    "short"
</code></pre>
</dl>
<p> Run <code>qping -help</code> to see which columns are available.</p>
<h3><code>-dump_tag</code> <i>tag</i> [<i>param</i>]</h3>
<p> This option has the same meaning as -dump, but can provide more information by specifying the debug level and message types <i>qping</i> should print: <code>-dump_tag ALL</code> <i>debug level </i> This option shows all possible debug messages (APP+MSG) for the debug levels, ERROR, WARNING, INFO, DEBUG and DPRINTF. The contacted service must support this kind of debugging. This option is not currently implemented. <code>-dump_tag APP</code> <i>debug level </i> This option shows only application debug messages for the debug levels, ERROR, WARNING, INFO, DEBUG and DPRINTF. The contacted service must support this kind of debugging. This option is not currently implemented. <code>-dump_tag MSG</code> This option has the same behavior as the <code>-dump</code> option.</p>
<h3><i>host</i></h3>
<p> Host where daemon is running.</p>
<h3><i>port</i></h3>
<p> Port which daemon has bound (used xxqs_name_sxx_qmaster/xxqs_name_sxx_execd port number).</p>
<h3><i>name</i></h3>
<p> Name of communication endpoint (&quot;qmaster&quot; or &quot;execd&quot;). A communication endpoint is a triplet of hostname/endpoint name/endpoint id (e.g. hostA/qmaster/1 or subhost/qstat/4).</p>
<h3><code>id</code></h3>
<p> Id of communication endpoint (&quot;1&quot; for daemons)</p>
<h2>EXAMPLES</h2>
<pre>
&gt;qping master_host 31116 qmaster
08/24/2004 16:41:15 endpoint master_host/qmaster/1 at port 31116 is up since 365761 seconds
08/24/2004 16:41:16 endpoint master_host/qmaster/1 at port 31116 is up since 365762 seconds
08/24/2004 16:41:17 endpoint master_host/qmaster/1 at port 31116 is up since 365763 seconds
</pre>
<pre>
&gt; qping -info master_host 31116 qmaster 1
08/24/2004 16:42:47:
SIRM version:             0.1
SIRM message id:          1
start time:               08/20/2004 11:05:14 (1092992714)
run time [s]:             365853
messages in read buffer:  0
messages in write buffer: 0
no. of connected clients: 4
status:                   0
info:                     ok
</pre>
<pre>
&gt; qping -info execd_host 31117 execd 1
08/24/2004 16:43:45:
SIRM version:             0.1
SIRM message id:          1
start time:               08/20/2004 11:06:13 (1092992773)
run time [s]:             365852
messages in read buffer:  0
messages in write buffer: 0
no. of connected clients: 2
status:                   0
info:                     ok
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell.</p>
<dt><code>SGE_QPING_OUTPUT_FORMAT</code></p>
<dd> See <code>-dump</code> option above.</dl>
<p> The following apply when CSP security is used and can override the values deduced from the bootstrap file.</p>
<dl>
<dt><code>SSL_CA_CERT_FILE</code></p>
<dd> CA certificate file</p>
<dt><code>SSL_CERT_FILE</code></p>
<dd> Certificates file</p>
<dt><code>SSL_KEY_FILE</code></p>
<dd> Key file</p>
<dt><code>SSL_RAND_FILE</code></p>
<dd> Random seed file</dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbAT">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAU">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAV">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAW">COPYRIGHT</a></p>
<dd></dl>
