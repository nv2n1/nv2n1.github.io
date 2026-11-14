---
title: "sec(1)"
name: "sec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sec/"
description: "sec – simple event correlator"
---

<h2>NAME</h2>
<p> sec &#8211; simple event correlator</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>sec</code></p>
<dd> [&#8211;conf=&lt;file pattern&gt; &#8230;]<br />
 [&#8211;input=&lt;file pattern&gt;[=&lt;context&gt;] &#8230;]<br />
 [&#8211;input-timeout=&lt;input timeout&gt;]<br />
 [&#8211;timeout-script=&lt;timeout script&gt;]<br />
 [&#8211;reopen-timeout=&lt;reopen timeout&gt;]<br />
 [&#8211;check-timeout=&lt;check timeout&gt;]<br />
 [&#8211;poll-timeout=&lt;poll timeout&gt;]<br />
 [&#8211;socket-timeout=&lt;socket timeout&gt;]<br />
 [&#8211;blocksize=&lt;io block size&gt;]<br />
 [&#8211;bufsize=&lt;input buffer size&gt;]<br />
 [&#8211;evstoresize=&lt;event store size&gt;]<br />
 [&#8211;cleantime=&lt;clean time&gt;]<br />
 [&#8211;log=&lt;logfile&gt;]<br />
 [&#8211;syslog=&lt;facility&gt;]<br />
 [&#8211;debug=&lt;debuglevel&gt;]<br />
 [&#8211;pid=&lt;pidfile&gt;]<br />
 [&#8211;dump=&lt;dumpfile&gt;]<br />
 [&#8211;user=&lt;username&gt;]<br />
 [&#8211;group=&lt;groupname&gt; &#8230;]<br />
 [&#8211;umask=&lt;mode&gt;]<br />
 [&#8211;dumpfts | &#8211;nodumpfts]<br />
 [&#8211;quoting | &#8211;noquoting]<br />
 [&#8211;tail | &#8211;notail]<br />
 [&#8211;fromstart | &#8211;nofromstart]<br />
 [&#8211;detach | &#8211;nodetach]<br />
 [&#8211;jointbuf | &#8211;nojointbuf]<br />
 [&#8211;keepopen | &#8211;nokeepopen]<br />
 [&#8211;rwfifo | &#8211;norwfifo]<br />
 [&#8211;childterm | &#8211;nochildterm]<br />
 [&#8211;intevents | &#8211;nointevents]<br />
 [&#8211;intcontexts | &#8211;nointcontexts]<br />
 [&#8211;testonly | &#8211;notestonly]<br />
 [&#8211;help] [-?]<br />
 [&#8211;version]</dl>
<h2>DESCRIPTION</h2>
<p> SEC is an event correlation tool for advanced event processing which can be harnessed for event log monitoring, for network and security management, for fraud detection, and for any other task which involves event correlation. Event correlation is a procedure where a stream of events is processed, in order to detect (and act on) certain event groups that occur within predefined time windows. Unlike many other event correlation products which are heavyweight solutions, SEC is a lightweight and platform-independent event correlator which runs as a single process. The user can start it as a daemon, employ it in shell pipelines, execute it interactively in a terminal, run many SEC processes simultaneously for different tasks, and use it in a wide variety of other ways. </p>
<p> SEC reads lines from files, named pipes, or standard input, matches the lines with patterns (regular expressions, Perl subroutines, etc.) for recognizing input events, and correlates events according to the rules in its configuration file(s). Rules are matched against input in the order they are given in the configuration file. If there are two or more configuration files, rule sequence from every file is matched against input (unless explicitly specified otherwise). SEC can produce output by executing external programs (e.g., <code><a href="/docs/linux/man/1-snmptrap/">snmptrap</a></code>(1) or <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1)), by writing to files, by sending data to TCP and UDP based servers, by calling precompiled Perl subroutines, etc. </p>
<p> SEC can be run in various ways. For example, the following command line starts it as a daemon, in order to monitor events appended to the /var/log/messages syslog file with rules from /etc/sec/syslog.rules: </p>
<p> /usr/bin/sec &#8211;detach &#8211;conf=/etc/sec/syslog.rules \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;input=/var/log/messages </p>
<p> Each time /var/log/messages is rotated, a new instance of /var/log/messages is opened and processed from the beginning. The following command line runs SEC in a shell pipeline, configuring it to process lines from standard input, and to exit when the /usr/bin/nc tool closes its standard output and exits: </p>
<p> /usr/bin/nc -l 8080 | /usr/bin/sec &#8211;notail &#8211;input=- \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;conf=/etc/sec/my.conf </p>
<p> Some SEC rules start event correlation operations, while other rules react immediately to input events or system clock. For example, suppose that SEC has been started with the following command line </p>
<p> /usr/bin/sec &#8211;conf=/etc/sec/sshd.rules &#8211;input=/var/log/secure </p>
<p> in order to monitor the /var/log/secure syslog file for sshd events. Also, suppose that the /etc/sec/sshd.rules configuration file contains the following rule for correlating SSH failed login syslog events: </p>
<p> type=SingleWithThreshold<br />
 ptype=RegExp<br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2<br />
 desc=Three SSH login failures within 1m for user $1<br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost<br />
 window=60<br />
 thresh=3 </p>
<p> The <i>pattern</i> field of the rule defines the pattern for recognizing input events, while the <i>ptype</i> field defines its type (regular expression). Suppose that user risto fails to log in over SSH and the following message is logged to /var/log/secure: </p>
<p> Dec 16 16:24:59 myserver sshd[13685]: Failed password for risto from 10.12.2.5 port 41063 ssh2 </p>
<p> This input message will match the regular expression pattern of the above rule, and the match variable $1 will be set to the string <i>risto </i> (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1) for details). After a match, SEC will evaluate the operation description string given with the <i>desc</i> field. This is done by substituting $1 with its current value which yields <i>Three SSH login failures within 1m for user risto</i>. SEC will then check if there already exists an event correlation operation identified with this string and triggered by the same rule. If the operation is not found, SEC will create a new operation for the user name risto, and the occurrence time of the input event will be recorded into the operation. Note that for event occurrence time SEC always uses the current time as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call, *not* the timestamp extracted from the event. Suppose that after 25 seconds, a similar SSH login failure event for the same user name is observed. In this case, a running operation will be found for the operation description string <i>Three SSH login failures within 1m for user risto</i>, and the occurrence time of the second event is recorded into the operation. If after 30 seconds a third event for the user name risto is observed, the operation has processed 3 events within 55 seconds. Since the threshold condition &quot;3 events within 60 seconds&quot; (as defined by the <i>thresh</i> and <i>window</i> fields) is now satisfied, SEC will execute the action defined with the <i>action </i> field &#8212; it will fork a command </p>
<p> /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost </p>
<p> with a pipe connected to its standard input. Then, SEC writes the operation description string <i>Three SSH login failures within 1m for user risto</i> (held by the %s special variable) to the standard input of the command through the pipe. In other words, an e-mail warning is sent to the local root-user. Finally, since there are 5 seconds left until the end of the event correlation window, the operation will consume the following SSH login failure events for user risto without any further action, and finish after 5 seconds. </p>
<p> The above example illustrates that the <i>desc</i> field of a rule defines the scope of event correlation and influences the number of operations created by the rule. For example, if we set the <i>desc </i> field to <i>Three SSH login failures within 1m</i>, the root-user would be also alerted on 3 SSH login failure events for *different* users within 1 minute. In order to avoid clashes between operations started by different rules, operation ID contains not only the value set by the <i>desc</i> field, but also the rule file name and the rule number inside the file. For example, if the rule file /etc/sec/sshd.rules contains one rule </p>
<p> type=SingleWithThreshold<br />
 ptype=RegExp<br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2<br />
 desc=Three SSH login failures within 1m for user $1<br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost<br />
 window=60<br />
 thresh=3 </p>
<p> and the event </p>
<p> Dec 16 16:24:59 myserver sshd[13685]: Failed password for risto from 10.12.2.5 port 41063 ssh2 </p>
<p> is the first matching event for the above rule, this event will trigger a new event correlation operation with the ID </p>
<p> /etc/sec/sshd.rules | 0 | Three SSH login failures within 1m for user risto </p>
<p> (0 is the number assigned to the first rule in the file, see EVENT CORRELATION OPERATIONS section for more information). </p>
<p> The following simple example demonstrates that event correlation schemes can be defined by combining several rules. In this example, two rules harness contexts and synthetic events for achieving their goal: </p>
<p> type=SingleWithThreshold<br />
 ptype=RegExp<br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2<br />
 desc=Three SSH login failures within 1m for user $1<br />
 action=event 3_SSH_LOGIN_FAILURES_FOR_$1<br />
 window=60<br />
 thresh=3 </p>
<p> type=EventGroup<br />
 ptype=RegExp<br />
 pattern=3_SSH_LOGIN_FAILURES_FOR_(\S+)<br />
 context=!USER_$1_COUNTED &amp;&amp; !COUNTING_OFF<br />
 count=create USER_$1_COUNTED 60<br />
 desc=Repeated SSH login failures for 30 distinct users within 1m<br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost; \<br />
&nbsp;<wbr>create COUNTING_OFF 3600<br />
 window=60<br />
 thresh=30 </p>
<p> The first rule looks almost identical to the rule from the previous example, but its <i>action</i> field is different &#8212; after three SSH login failures have been observed for the same user name within one minute by an event correlation operation, the operation will emit the synthetic event 3_SSH_LOGIN_FAILURES_FOR_&lt;username&gt;. Although synthetic events are created by SEC, they are treated like regular events received from input sources and are matched against rules. The regular expression pattern of the second rule will match the 3_SSH_LOGIN_FAILURES_FOR_&lt;username&gt; event and start a new event correlation operation if no such events have been previously seen. Also, each time a synthetic event for some user name has matched the rule, a context with the lifetime of 1 minute for that user name is created (see the <i>count</i> field). Note that this prevents further matches for the same user name, since a synthetic event for &lt;username&gt; can match the rule only if the context USER_&lt;username&gt;_COUNTED *does not* exist (as requested by the boolean expression in the <i>context</i> field; see CONTEXTS AND CONTEXT EXPRESSIONS section for more information). The operation started by the rule sends an e-mail warning to the local root-user if 30 synthetic events have been observed within 1 minute (see the <i>thresh</i> and <i>window</i> fields). Note that due to the use of the USER_&lt;username&gt;_COUNTED contexts, all synthetic events concern different user names. After sending an e-mail warning, the operation will also create the context COUNTING_OFF with the lifetime of 1 hour, and will continue to run until the 1 minute event correlation window expires. After the operation has finished, the presence of the COUNTING_OFF context will keep the second rule disabled (as requested by the boolean expression in the <i>context</i> field). Therefore, at most one e-mail warning per 1 hour is issued by above rules. </p>
<p> The above examples have presented the event correlation capabilities of SEC in a very brief fashion. The following sections will provide an in-depth discussion of SEC features.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;conf=&lt;file_pattern&gt;</code></p>
<dd> expand &lt;file_pattern&gt; to filenames (with the Perl <code>glob</code>() function) and read event correlation rules from every file. Multiple <code>&#8211;conf</code> options can be specified at command line. Each time SEC receives a signal that forces a configuration reload, &lt;file_pattern&gt; is re-evaluated. See also INPUT PROCESSING AND TIMING section for a discussion on rule processing order for multiple configuration files.</p>
<dt><code>&#8211;input=&lt;file_pattern&gt;[=&lt;context&gt;]</code></p>
<dd> expand &lt;file_pattern&gt; to filenames (with the Perl <code>glob</code>() function) and use the files as input sources. An input file can be a regular file, named pipe, or standard input if <code>&#8211;</code> was specified. Multiple <code>&#8211;input</code> options can be specified at command line. Each time SEC receives the <code>SIGHUP</code> or <code>SIGABRT</code> signal, &lt;file_pattern&gt; is re-evaluated. If SEC experiences a system error when reading from an input file, it will close the file (use the <code>&#8211;reopen-timeout</code> option for reopening the file). If &lt;context&gt; is given, SEC will set up the context &lt;context&gt; each time it reads a line from input files that correspond to &lt;file_pattern&gt;. This will help the user to write rules that match data from particular input source(s) only. When there is an <code>&#8211;input</code> option with &lt;context&gt; specified, it will automatically enable the <code>&#8211;intcontexts</code> option. See INTERNAL EVENTS AND CONTEXTS section for more information.</p>
<dt><code>&#8211;input-timeout=&lt;input_timeout&gt;</code>, <code>&#8211;timeout-script=&lt;timeout_script&gt;</code></p>
<dd> if SEC has not observed new data in an input file during &lt;input_timeout&gt; seconds (or the file was closed &lt;input_timeout&gt; seconds ago), &lt;timeout_script&gt; will be executed with command line parameters 1 and &lt;the name of the input file&gt;. If fresh data become available again, &lt;timeout_script&gt; will be executed with command line parameters 0 and &lt;the name of the input file&gt;. Setting &lt;input_timeout&gt; to 0 disables this behavior (this is also the default). Note that <code>&#8211;input_timeout </code> and <code>&#8211;timeout_script</code> options can be used as synonyms for <code>&#8211;input-timeout </code> and <code>&#8211;timeout-script</code>, respectively.</p>
<dt><code>&#8211;reopen-timeout=&lt;reopen_timeout&gt; </code></p>
<dd> if an input file is in the closed state (e.g., SEC fails to open the file at startup, because it has not been created yet), SEC will attempt to reopen the file after every &lt;reopen_timeout&gt; seconds until open succeeds. Setting &lt;reopen_timeout&gt; to 0 disables this behavior (this is also the default). This option has no meaning when the <code>&#8211;notail</code> option is also specified. Note that <code>&#8211;reopen_timeout</code> is a synonym for <code>&#8211;reopen-timeout</code>.</p>
<dt><code>&#8211;check-timeout=&lt;check_timeout&gt;</code></p>
<dd> if SEC has not observed new data in an input file, the file will not be polled (both for status and data) during the next &lt;check_timeout&gt; seconds. Setting &lt;check_timeout&gt; to 0 disables this behavior (this is also the default). Note that <code>&#8211;check_timeout</code> is a synonym for <code>&#8211;check-timeout</code>.</p>
<dt><code>&#8211;poll-timeout=&lt;poll_timeout&gt;</code></p>
<dd> a real number that specifies how many seconds SEC will sleep when no new data were read from input files. Default is 0.1 seconds. Note that <code>&#8211;poll_timeout</code> is a synonym for <code>&#8211;poll-timeout</code>.</p>
<dt><code>&#8211;socket-timeout=&lt;socket_timeout&gt;</code></p>
<dd> if a network connection to a remote peer can&#8217;t be established within &lt;socket_timeout&gt; seconds, give up. Default is 60 seconds. Note that <code>&#8211;socket_timeout</code> is a synonym for <code>&#8211;socket-timeout</code>.</p>
<dt><code>&#8211;blocksize=&lt;io_block_size&gt;</code></p>
<dd> the number of bytes SEC will attempt to read at once from an input file. Default is 8192 bytes (i.e., read from input files by 8KB blocks).</p>
<dt><code>&#8211;bufsize=&lt;input_buffer_size&gt;</code></p>
<dd> set all input buffers to hold &lt;input_buffer_size&gt; lines. The content of input buffers will be compared with patterns that are part of rule definitions (i.e., no more than &lt;input_buffer_size&gt; lines can be matched by a pattern at a time). If &lt;input_buffer_size&gt; is set to 0, SEC will determine the proper value for &lt;input_buffer_size&gt; by checking event matching patterns of all SEC rules. Default is 0 (i.e., determine the size of input buffers automatically).</p>
<dt><code>&#8211;evstoresize=&lt;event_store_size&gt;</code></p>
<dd> set an upper limit to the number of events in context event stores. Default is 0 which sets no limit.</p>
<dt><code>&#8211;cleantime=&lt;clean_time&gt;</code></p>
<dd> time interval in seconds that specifies how often internal event correlation and context lists are processed, in order to accomplish time-related tasks and to remove obsolete elements. See INPUT PROCESSING AND TIMING section for more information. Default is 1 second.</p>
<dt><code>&#8211;log=&lt;logfile&gt;</code></p>
<dd> use &lt;logfile&gt; for logging SEC activities. Note that if the SEC standard error is connected to a terminal, messages will also be logged there, in order to facilitate debugging.</p>
<dt><code>&#8211;syslog=&lt;facility&gt;</code></p>
<dd> use syslog for logging SEC activities. All messages will be logged with the facility &lt;facility&gt;, e.g., <i>local0</i> (see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for possible facility values). Warning: be careful with using this option if SEC is employed for monitoring syslog log files, because message loops might occur.</p>
<dt><code>&#8211;debug=&lt;debuglevel&gt;</code></p>
<dd> set logging verbosity for SEC. Setting debuglevel to &lt;debuglevel&gt; means that all messages of level &lt;debuglevel&gt; and lower are logged (e.g., if &lt;debuglevel&gt; is 3, messages from levels 1-3 are logged). The following levels are recognized by SEC:<br />
 1 &#8211; critical messages (severe faults that cause SEC to terminate, e.g., a failed system call)<br />
 2 &#8211; error messages (faults that need attention, e.g., an incorrect rule definition in a configuration file)<br />
 3 &#8211; warning messages (possible faults, e.g., a command forked from SEC terminated with a non-zero exit code)<br />
 4 &#8211; notification messages (normal system level events and interrupts, e.g., the reception of a signal)<br />
 5 &#8211; informative messages (information about external programs forked from SEC)<br />
 6 &#8211; debug messages (detailed information about all SEC activities)<br />
 Default &lt;debuglevel&gt; is 6 (i.e., log everything). See SIGNALS section for information on how to change &lt;debuglevel&gt; at runtime.</p>
<dt><code>&#8211;pid=&lt;pidfile&gt;</code></p>
<dd> SEC will store its process ID to &lt;pidfile&gt; at startup.</p>
<dt><code>&#8211;dump=&lt;dumpfile&gt;</code></p>
<dd> SEC will use &lt;dumpfile&gt; as its dump file for writing performance and debug data. With the <code>&#8211;dumpfts</code> option, a timestamp suffix is appended to the dump file name. See SIGNALS section for more information. Default is /tmp/sec.dump.</p>
<dt><code>&#8211;user=&lt;username&gt;</code>, <code>&#8211;group=&lt;groupname&gt;</code></p>
<dd> if SEC is started with effective user ID 0, it will drop root privileges by switching to user &lt;username&gt; and group &lt;groupname&gt;. The <code>&#8211;group</code> option can&#8217;t be used without the <code>&#8211;user</code> option. If the <code>&#8211;user</code> option is given without <code>&#8211;group</code>, primary group of the user &lt;username&gt; is assumed for &lt;groupname&gt;. If several groups are provided with multiple <code>&#8211;group</code> options, SEC switches to the first group with other groups as supplementary groups.</p>
<dt><code>&#8211;umask=&lt;mode&gt;</code></p>
<dd> set file mode creation mask to &lt;mode&gt; at SEC startup, where &lt;mode&gt; is a value from the range 0..0777 (see also <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)). Octal, decimal, hexadecimal, and binary values can be specified for &lt;mode&gt; (e.g., octal mask 0027 can also be expressed as 23, 0x17, and 0b000010111).</p>
<dt><code>&#8211;dumpfts</code>, <code>&#8211;nodumpfts</code></p>
<dd> if the <code>&#8211;dumpfts</code> option is specified, a timestamp suffix (seconds since Epoch) is appended to the dump file name that reflects the file creation time. Default is <code>&#8211;nodumpfts</code>.</p>
<dt><code>&#8211;quoting</code>, <code>&#8211;noquoting</code></p>
<dd> if the <code>&#8211;quoting</code> option is specified, operation description strings that are supplied to command lines of <i>shellcmd</i>, <i>spawn</i>, and <i>cspawn</i> actions will be put inside single quotes. Each single quote (&#8216;) that strings originally contain will be masked. This option prevents the shell from interpreting special symbols that operation description strings might contain. Default is <code>&#8211;noquoting</code>.</p>
<dt><code>&#8211;tail</code>, <code>&#8211;notail</code></p>
<dd> if the <code>&#8211;notail</code> option is specified, SEC will process all data that are currently available in input files and exit after reaching all EOFs. If all input is received from a pipe and the <code>&#8211;notail</code> option is given, SEC terminates when the last writer closes the pipe (EOF condition). Please note that with named pipes <code>&#8211;notail</code> should be used with <code>&#8211;norwfifo</code>. With the <code>&#8211;tail</code> option, SEC will jump to the end of input files and wait for new lines to arrive. Each input file is tracked both by its name and i-node, and input file rotations are handled seamlessly. If the input file is recreated or truncated, SEC will reopen it and process its content from the beginning. If the input file is removed (i.e., there is just an i-node left without a name), SEC will keep the i-node open and wait for the input file recreation. Default is <code>&#8211;tail</code>.</p>
<dt><code>&#8211;fromstart</code>, <code>&#8211;nofromstart</code></p>
<dd> these flags have no meaning when the <code>&#8211;notail</code> option is also specified. When used in combination with <code>&#8211;tail</code> (or alone, since <code>&#8211;tail</code> is enabled by default), <code>&#8211;fromstart</code> will force SEC to read and process input files from the beginning to the end, before the &#8216;tail&#8217; mode is entered. Default is <code>&#8211;nofromstart</code>.</p>
<dt><code>&#8211;detach</code>, <code>&#8211;nodetach</code></p>
<dd> if the <code>&#8211;detach</code> option is specified, SEC will disassociate itself from the controlling terminal and become a daemon at startup (note that SEC will close its standard input, standard output, and standard error, and change its working directory to the root directory). Default is <code>&#8211;nodetach</code>.</p>
<dt><code>&#8211;jointbuf</code>, <code>&#8211;nojointbuf</code></p>
<dd> if the <code>&#8211;jointbuf</code> option is specified, SEC uses joint input buffer for all input sources (the size of the buffer is set with the <code>&#8211;bufsize</code> option). The <code>&#8211;nojointbuf</code> option creates a separate input buffer for each input file, and a separate buffer for all synthetic and internal events (the sizes of all buffers are set with the <code>&#8211;bufsize</code> option). The <code>&#8211;jointbuf</code> option allows multiline patterns to match lines from several input sources, while the <code>&#8211;nojointbuf </code> pattern restricts the matching to lines from one input source only. See INPUT PROCESSING AND TIMING section for more information. If the size of input buffer(s) is 1 (either explicitly set with <code>&#8211;bufsize=1</code> or automatically determined from SEC rules), <code>&#8211;jointbuf</code> option is enabled, otherwise the default is <code>&#8211;nojointbuf</code>.</p>
<dt><code>&#8211;keepopen</code>, <code>&#8211;nokeepopen</code></p>
<dd> if the <code>&#8211;keepopen</code> option is specified, SEC will keep input files open across soft restarts. When the <code>SIGABRT</code> signal is received, SEC will not reopen input files which have been opened previously, but will only open input files which are in the closed state. The <code>&#8211;nokeepopen </code> option forces SEC to close and (re)open all input files during soft restarts. Default is <code>&#8211;keepopen</code>.</p>
<dt><code>&#8211;rwfifo</code>, <code>&#8211;norwfifo</code></p>
<dd> if the <code>&#8211;norwfifo</code> option is specified, named pipe input files are opened in read-only mode. In this mode, the named pipe has to be reopened when the last writer closes the pipe, in order to clear the EOF condition on the pipe. With the <code>&#8211;rwfifo</code> option, named pipe input files are opened in read-write mode, although SEC never writes to the pipes. In this mode, the pipe does not need to be reopened when an external writer closes it, since there is always at least one writer on the pipe and EOF will never appear. Therefore, if the <code>&#8211;notail</code> option has been given, <code>&#8211;norwfifo</code> should also be specified. Default is <code>&#8211;rwfifo</code>.</p>
<dt><code>&#8211;childterm</code>, <code>&#8211;nochildterm</code></p>
<dd> if the <code>&#8211;childterm</code> option is specified, SEC will send the SIGTERM signal to all its child processes when it terminates or goes through a full restart. Default is <code>&#8211;childterm</code>.</p>
<dt><code>&#8211;intevents</code>, <code>&#8211;nointevents</code></p>
<dd> SEC will generate internal events when it starts up, when it receives certain signals, and when it terminates gracefully. Specific rules can be written to match those internal events, in order to accomplish special tasks at SEC startup, restart, and shutdown. See INTERNAL EVENTS AND CONTEXTS section for more information. Default is <code>&#8211;nointevents</code>.</p>
<dt><code>&#8211;intcontexts</code>, <code>&#8211;nointcontexts</code></p>
<dd> SEC will create an internal context when it reads a line from an input file. This will help the user to write rules that match data from particular input source only. See INTERNAL EVENTS AND CONTEXTS section for more information. Default is <code>&#8211;nointcontexts</code>.</p>
<dt><code>&#8211;testonly</code>, <code>&#8211;notestonly</code></p>
<dd> if the <code>&#8211;testonly</code> option is specified, SEC will exit immediately after parsing the configuration file(s). If the configuration file(s) contained no faulty rules, SEC will exit with 0, otherwise with 1. Default is <code>&#8211;notestonly</code>.</p>
<dt><code>&#8211;help</code>, <code>-?</code></p>
<dd> SEC will output usage information and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> SEC will output version information and exit.</dl>
<p> Note that options can be introduced both with the single dash (-) and double dash (&#8211;), and both the equal sign (=) and whitespace can be used for separating the option name from the option value. For example, <code>-conf=&lt;file_pattern&gt;</code> and <code>&#8211;conf &lt;file_pattern&gt;</code> options are equivalent.</p>
<h2>CONFIGURATION FILES</h2>
<p> Each SEC configuration file consists of rule definitions which are separated by empty lines, whitespace lines and/or comment lines. Each rule definition consists of keyword=value fields, one keyword and value per line. Values are case insensitive only where character case is not important (like the values specifying rule types, e.g., &#8216;Single&#8217; and &#8216;single&#8217; are treated identically). The backslash character (\) may be used at the end of a line to continue the current rule field in the next line. Lines which begin with the number sign (#) are treated as comments and ignored (whitespace characters may precede #). Any comment line, empty line, whitespace line, or end of file will terminate the preceding rule definition. For inserting comments into rule definitions, the <i>rem</i> keyword can be used. For example, the following lines define two rules: </p>
<p> type=Single<br />
 rem=this rule matches any line which contains \<br />
&nbsp;<wbr>three consecutive A characters and writes the string&nbsp;<wbr>\<br />
&nbsp;<wbr>&quot;three A characters were observed&quot;&nbsp;<wbr>to standard output<br />
 ptype=SubStr<br />
 pattern=AAA<br />
 desc=Three A characters<br />
 action=write &#8211; three A characters were observed<br />
 # This comment line ends preceding rule definition.<br />
 # The following rule works like the previous rule,<br />
 # but looks for three consecutive B characters and<br />
 # writes the string &quot;three B characters were observed&quot;<br />
 # to standard output<br />
 type=Single<br />
 ptype=SubStr<br />
 pattern=BBB<br />
 desc=Three B characters<br />
 action=write &#8211; three B characters were observed </p>
<p> Apart from keywords that are part of rule definitions, <i>label</i> keywords may appear anywhere in the configuration file. The value of each <i>label</i> keyword will be treated as a label that can be referred to in rule definitions as a point-of-continue. This allows for continuing event processing at a rule that follows the label, after the current rule has matched and processed the event. </p>
<p> The points-of-continue are defined with <i>continue*</i> fields. Accepted values for these fields are:</p>
<dl>
<dt><i>TakeNext </i></p>
<dd> after an event has matched the rule, search for matching rules in the configuration file will continue from the next rule.</p>
<dt><i>GoTo &lt;label&gt;</i></p>
<dd> after an event has matched the rule, search for matching rules will continue from the location of &lt;label&gt; in the configuration file (&lt;label&gt; must be defined with the <i>label</i> keyword anywhere in the configuration file *after* the current rule definition).</p>
<dt><i>DontCont</i> (default value)</p>
<dd> after an event has matched the rule, search for matching rules ends in the *current* configuration file.</p>
<dt><i>EndMatch</i></p>
<dd> after an event has matched the rule, search for matching rules ends for *all* configuration files.</dl>
<p> SEC rules from the same configuration file are matched against input in the order they have been given in the file. For example, consider a configuration file which contains the following rule sequence: </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=AAA<br />
 rem=after this rule has matched, continue from last rule<br />
 continue=GoTo lastRule<br />
 desc=Three A characters<br />
 action=write &#8211; three A characters were observed </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=BBB<br />
 rem=after this rule has matched, don&#8217;t consider following rules, \<br />
&nbsp;<wbr>since&nbsp;<wbr>&#8216;continue&#8217;&nbsp;<wbr>defaults to&nbsp;<wbr>&#8216;DontCont&#8217;<br />
 desc=Three B characters<br />
 action=write &#8211; three B characters were observed </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=CCC<br />
 rem=after this rule has matched, continue from next rule<br />
 continue=TakeNext<br />
 desc=Three C characters<br />
 action=write &#8211; three C characters were observed </p>
<p> label=lastRule </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=DDD<br />
 desc=Three D characters<br />
 action=write &#8211; three D characters were observed </p>
<p> For the input line &quot;AAABBBCCCDDD&quot;, this ruleset writes strings &quot;three A characters were observed&quot; and &quot;three D characters were observed&quot; to standard output. If the input line is &quot;BBBCCCDDD&quot;, the string &quot;three B characters were observed&quot; is written to standard output. For the input line &quot;CCCDDD&quot;, strings &quot;three C characters were observed&quot; and &quot;three D characters were observed&quot; are sent to standard output, while the input line &quot;DDD&quot; produces the output string &quot;three D characters were observed&quot;. </p>
<p> If there are two or more configuration files, rule sequence from every file is matched against input (unless explicitly specified otherwise). For example, suppose SEC is started with the command line </p>
<p> /usr/bin/sec &#8211;input=- \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;conf=/etc/sec/sec1.rules &#8211;conf=/etc/sec/sec2.rules </p>
<p> and the configuration file /etc/sec/sec1.rules has the following content: </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=AAA<br />
 desc=Three A characters<br />
 action=write &#8211; three A characters were observed </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=BBB<br />
 continue=EndMatch<br />
 desc=Three B characters<br />
 action=write &#8211; three B characters were observed </p>
<p> Also, suppose the configuration file /etc/sec/sec2.rules has the following content: </p>
<p> type=Single<br />
 ptype=SubStr<br />
 pattern=CCC<br />
 desc=Three C characters<br />
 action=write &#8211; three C characters were observed </p>
<p> If SEC receives the line &quot;AAABBBCCC&quot; from standard input, rules from both configuration files are tried, and as a result, the strings &quot;three A characters were observed&quot; and &quot;three C characters were observed&quot; are written to standard output. Note that rules from /etc/sec/sec1.rules are tried first against the input line, since the option <code>&#8211;conf=/etc/sec/sec1.rules </code> is given before <code>&#8211;conf=/etc/sec/sec2.rules </code> in the SEC command line (see also INPUT PROCESSING AND TIMING section for a more detailed discussion). If SEC receives the line &quot;BBBCCC&quot; from standard input, the second rule from /etc/sec/sec1.rules produces a match, and the string &quot;three B characters were observed&quot; is written to standard output. Since the rule contains <i>continue=EndMatch</i> statement, the search for matching rules will end for all configuration files, and rules from /etc/sec/sec2.rules will not be not tried. Without this statement, the search for matching rules would continue in /etc/sec/sec2.rules, and the first rule would write the string &quot;three C characters were observed&quot; to standard output.</p>
<h2>PATTERNS, PATTERN TYPES AND MATCH VARIABLES</h2>
<p> Patterns and pattern types are defined with <i>pattern*</i> and <i>ptype*</i> rule fields. Many pattern types define the number of lines <i>N </i> which the pattern matches (if <i>N </i> is omitted, 1 is assumed). If <i>N</i> is greater than 1, the scope of matching is set with the <code>&#8211;jointbuf</code> and <code>&#8211;nojointbuf</code> options. With <code>&#8211;jointbuf</code>, the pattern is used for matching <i>N </i> last input lines taken from the joint input buffer (the lines can come from different input sources). With <code>&#8211;nojointbuf</code>, the source of the last input line is identified, and the pattern is matched with <i>N </i> last input lines from the input buffer of the identified source.</p>
<dl>
<dt><i>SubStr[N]</i></p>
<dd> pattern is a string that is searched in the last N input lines L1, L2, &#8230;, LN. If N is greater than 1, the input lines are joined into a string &quot;L1&lt;NEWLINE&gt;L2&lt;NEWLINE&gt;&#8230;&lt;NEWLINE&gt;LN&quot;, and the pattern string will be searched from it. If the pattern string is found in input line(s), the pattern matches. Backslash sequences 	, 
, , \s, and 
