---
title: "sec(1)"
name: "sec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sec/"
description: "sec – simple event correlator"
---
<h2>NAME</h2>
<p> sec - simple event correlator  </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>sec</code></dt>
<dd> <p> [--conf=&lt;file pattern&gt; ...] <br />
 [--input=&lt;file pattern&gt;[=&lt;context&gt;] ...] <br />
 [--input-timeout=&lt;input timeout&gt;] <br />
 [--timeout-script=&lt;timeout script&gt;] <br />
 [--reopen-timeout=&lt;reopen timeout&gt;] <br />
 [--check-timeout=&lt;check timeout&gt;] <br />
 [--poll-timeout=&lt;poll timeout&gt;] <br />
 [--socket-timeout=&lt;socket timeout&gt;] <br />
 [--blocksize=&lt;io block size&gt;] <br />
 [--bufsize=&lt;input buffer size&gt;] <br />
 [--evstoresize=&lt;event store size&gt;] <br />
 [--cleantime=&lt;clean time&gt;] <br />
 [--log=&lt;logfile&gt;] <br />
 [--syslog=&lt;facility&gt;] <br />
 [--debug=&lt;debuglevel&gt;] <br />
 [--pid=&lt;pidfile&gt;] <br />
 [--dump=&lt;dumpfile&gt;] <br />
 [--user=&lt;username&gt;] <br />
 [--group=&lt;groupname&gt; ...] <br />
 [--umask=&lt;mode&gt;] <br />
 [--dumpfts | --nodumpfts] <br />
 [--quoting | --noquoting] <br />
 [--tail | --notail] <br />
 [--fromstart | --nofromstart] <br />
 [--detach | --nodetach] <br />
 [--jointbuf | --nojointbuf] <br />
 [--keepopen | --nokeepopen] <br />
 [--rwfifo | --norwfifo] <br />
 [--childterm | --nochildterm] <br />
 [--intevents | --nointevents] <br />
 [--intcontexts | --nointcontexts] <br />
 [--testonly | --notestonly] <br />
 [--help] [-?] <br />
 [--version] </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> SEC is an event correlation tool for advanced event processing which can be harnessed for event log monitoring, for network and security management, for fraud detection, and for any other task which involves event correlation. Event correlation is a procedure where a stream of events is processed, in order to detect (and act on) certain event groups that occur within predefined time windows. Unlike many other event correlation products which are heavyweight solutions, SEC is a lightweight and platform-independent event correlator which runs as a single process. The user can start it as a daemon, employ it in shell pipelines, execute it interactively in a terminal, run many SEC processes simultaneously for different tasks, and use it in a wide variety of other ways. </p>
<p> SEC reads lines from files, named pipes, or standard input, matches the lines with patterns (regular expressions, Perl subroutines, etc.) for recognizing input events, and correlates events according to the rules in its configuration file(s). Rules are matched against input in the order they are given in the configuration file. If there are two or more configuration files, rule sequence from every file is matched against input (unless explicitly specified otherwise). SEC can produce output by executing external programs (e.g., <code><a href="/docs/linux/man/1-snmptrap/">snmptrap</a></code>(1) or <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1)), by writing to files, by sending data to TCP and UDP based servers, by calling precompiled Perl subroutines, etc. </p>
<p> SEC can be run in various ways. For example, the following command line starts it as a daemon, in order to monitor events appended to the /var/log/messages syslog file with rules from /etc/sec/syslog.rules: </p>
<p> /usr/bin/sec --detach --conf=/etc/sec/syslog.rules \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/messages </p>
<p> Each time /var/log/messages is rotated, a new instance of /var/log/messages is opened and processed from the beginning. The following command line runs SEC in a shell pipeline, configuring it to process lines from standard input, and to exit when the /usr/bin/nc tool closes its standard output and exits: </p>
<p> /usr/bin/nc -l 8080 | /usr/bin/sec --notail --input=- \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--conf=/etc/sec/my.conf </p>
<p> Some SEC rules start event correlation operations, while other rules react immediately to input events or system clock. For example, suppose that SEC has been started with the following command line </p>
<p> /usr/bin/sec --conf=/etc/sec/sshd.rules --input=/var/log/secure </p>
<p> in order to monitor the /var/log/secure syslog file for sshd events. Also, suppose that the /etc/sec/sshd.rules configuration file contains the following rule for correlating SSH failed login syslog events: </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 <br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> The <i>pattern</i> field of the rule defines the pattern for recognizing input events, while the <i>ptype</i> field defines its type (regular expression). Suppose that user risto fails to log in over SSH and the following message is logged to /var/log/secure: </p>
<p> Dec 16 16:24:59 myserver sshd[13685]: Failed password for risto from 10.12.2.5 port 41063 ssh2 </p>
<p> This input message will match the regular expression pattern of the above rule, and the match variable $1 will be set to the string <i>risto </i> (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1) for details). After a match, SEC will evaluate the operation description string given with the <i>desc</i> field. This is done by substituting $1 with its current value which yields <i>Three SSH login failures within 1m for user risto</i>. SEC will then check if there already exists an event correlation operation identified with this string and triggered by the same rule. If the operation is not found, SEC will create a new operation for the user name risto, and the occurrence time of the input event will be recorded into the operation. Note that for event occurrence time SEC always uses the current time as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call, *not* the timestamp extracted from the event. Suppose that after 25 seconds, a similar SSH login failure event for the same user name is observed. In this case, a running operation will be found for the operation description string <i>Three SSH login failures within 1m for user risto</i>, and the occurrence time of the second event is recorded into the operation. If after 30 seconds a third event for the user name risto is observed, the operation has processed 3 events within 55 seconds. Since the threshold condition &quot;3 events within 60 seconds&quot; (as defined by the <i>thresh</i> and <i>window</i> fields) is now satisfied, SEC will execute the action defined with the <i>action </i> field -- it will fork a command </p>
<p> /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost </p>
<p> with a pipe connected to its standard input. Then, SEC writes the operation description string <i>Three SSH login failures within 1m for user risto</i> (held by the %s special variable) to the standard input of the command through the pipe. In other words, an e-mail warning is sent to the local root-user. Finally, since there are 5 seconds left until the end of the event correlation window, the operation will consume the following SSH login failure events for user risto without any further action, and finish after 5 seconds. </p>
<p> The above example illustrates that the <i>desc</i> field of a rule defines the scope of event correlation and influences the number of operations created by the rule. For example, if we set the <i>desc </i> field to <i>Three SSH login failures within 1m</i>, the root-user would be also alerted on 3 SSH login failure events for *different* users within 1 minute. In order to avoid clashes between operations started by different rules, operation ID contains not only the value set by the <i>desc</i> field, but also the rule file name and the rule number inside the file. For example, if the rule file /etc/sec/sshd.rules contains one rule </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 <br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> and the event </p>
<p> Dec 16 16:24:59 myserver sshd[13685]: Failed password for risto from 10.12.2.5 port 41063 ssh2 </p>
<p> is the first matching event for the above rule, this event will trigger a new event correlation operation with the ID </p>
<p> /etc/sec/sshd.rules | 0 | Three SSH login failures within 1m for user risto </p>
<p> (0 is the number assigned to the first rule in the file, see EVENT CORRELATION OPERATIONS section for more information). </p>
<p> The following simple example demonstrates that event correlation schemes can be defined by combining several rules. In this example, two rules harness contexts and synthetic events for achieving their goal: </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 <br />
 action=event 3_SSH_LOGIN_FAILURES_FOR_$1 <br />
 window=60 <br />
 thresh=3 </p>
<p> type=EventGroup <br />
 ptype=RegExp <br />
 pattern=3_SSH_LOGIN_FAILURES_FOR_(\S+) <br />
 context=!USER_$1_COUNTED &amp;&amp; !COUNTING_OFF <br />
 count=create USER_$1_COUNTED 60 <br />
 desc=Repeated SSH login failures for 30 distinct users within 1m <br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost; \ <br />
&nbsp;<wbr>create COUNTING_OFF 3600 <br />
 window=60 <br />
 thresh=30 </p>
<p> The first rule looks almost identical to the rule from the previous example, but its <i>action</i> field is different -- after three SSH login failures have been observed for the same user name within one minute by an event correlation operation, the operation will emit the synthetic event 3_SSH_LOGIN_FAILURES_FOR_&lt;username&gt;. Although synthetic events are created by SEC, they are treated like regular events received from input sources and are matched against rules. The regular expression pattern of the second rule will match the 3_SSH_LOGIN_FAILURES_FOR_&lt;username&gt; event and start a new event correlation operation if no such events have been previously seen. Also, each time a synthetic event for some user name has matched the rule, a context with the lifetime of 1 minute for that user name is created (see the <i>count</i> field). Note that this prevents further matches for the same user name, since a synthetic event for &lt;username&gt; can match the rule only if the context USER_&lt;username&gt;_COUNTED *does not* exist (as requested by the boolean expression in the <i>context</i> field; see CONTEXTS AND CONTEXT EXPRESSIONS section for more information). The operation started by the rule sends an e-mail warning to the local root-user if 30 synthetic events have been observed within 1 minute (see the <i>thresh</i> and <i>window</i> fields). Note that due to the use of the USER_&lt;username&gt;_COUNTED contexts, all synthetic events concern different user names. After sending an e-mail warning, the operation will also create the context COUNTING_OFF with the lifetime of 1 hour, and will continue to run until the 1 minute event correlation window expires. After the operation has finished, the presence of the COUNTING_OFF context will keep the second rule disabled (as requested by the boolean expression in the <i>context</i> field). Therefore, at most one e-mail warning per 1 hour is issued by above rules. </p>
<p> The above examples have presented the event correlation capabilities of SEC in a very brief fashion. The following sections will provide an in-depth discussion of SEC features.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--conf=&lt;file_pattern&gt;</code></dt>
<dd> <p> expand &lt;file_pattern&gt; to filenames (with the Perl <code>glob</code>() function) and read event correlation rules from every file. Multiple <code>--conf</code> options can be specified at command line. Each time SEC receives a signal that forces a configuration reload, &lt;file_pattern&gt; is re-evaluated. See also INPUT PROCESSING AND TIMING section for a discussion on rule processing order for multiple configuration files. </p>
 </dd>
<dt><code>--input=&lt;file_pattern&gt;[=&lt;context&gt;]</code></dt>
<dd> <p> expand &lt;file_pattern&gt; to filenames (with the Perl <code>glob</code>() function) and use the files as input sources. An input file can be a regular file, named pipe, or standard input if <code>-</code> was specified. Multiple <code>--input</code> options can be specified at command line. Each time SEC receives the <code>SIGHUP</code> or <code>SIGABRT</code> signal, &lt;file_pattern&gt; is re-evaluated. If SEC experiences a system error when reading from an input file, it will close the file (use the <code>--reopen-timeout</code> option for reopening the file). If &lt;context&gt; is given, SEC will set up the context &lt;context&gt; each time it reads a line from input files that correspond to &lt;file_pattern&gt;. This will help the user to write rules that match data from particular input source(s) only. When there is an <code>--input</code> option with &lt;context&gt; specified, it will automatically enable the <code>--intcontexts</code> option. See INTERNAL EVENTS AND CONTEXTS section for more information. </p>
 </dd>
<dt><code>--input-timeout=&lt;input_timeout&gt;</code>, <code>--timeout-script=&lt;timeout_script&gt;</code></dt>
<dd> <p> if SEC has not observed new data in an input file during &lt;input_timeout&gt; seconds (or the file was closed &lt;input_timeout&gt; seconds ago), &lt;timeout_script&gt; will be executed with command line parameters 1 and &lt;the name of the input file&gt;. If fresh data become available again, &lt;timeout_script&gt; will be executed with command line parameters 0 and &lt;the name of the input file&gt;. Setting &lt;input_timeout&gt; to 0 disables this behavior (this is also the default). Note that <code>--input_timeout </code> and <code>--timeout_script</code> options can be used as synonyms for <code>--input-timeout </code> and <code>--timeout-script</code>, respectively. </p>
 </dd>
<dt><code>--reopen-timeout=&lt;reopen_timeout&gt; </code></dt>
<dd> <p> if an input file is in the closed state (e.g., SEC fails to open the file at startup, because it has not been created yet), SEC will attempt to reopen the file after every &lt;reopen_timeout&gt; seconds until open succeeds. Setting &lt;reopen_timeout&gt; to 0 disables this behavior (this is also the default). This option has no meaning when the <code>--notail</code> option is also specified. Note that <code>--reopen_timeout</code> is a synonym for <code>--reopen-timeout</code>. </p>
 </dd>
<dt><code>--check-timeout=&lt;check_timeout&gt;</code></dt>
<dd> <p> if SEC has not observed new data in an input file, the file will not be polled (both for status and data) during the next &lt;check_timeout&gt; seconds. Setting &lt;check_timeout&gt; to 0 disables this behavior (this is also the default). Note that <code>--check_timeout</code> is a synonym for <code>--check-timeout</code>. </p>
 </dd>
<dt><code>--poll-timeout=&lt;poll_timeout&gt;</code></dt>
<dd> <p> a real number that specifies how many seconds SEC will sleep when no new data were read from input files. Default is 0.1 seconds. Note that <code>--poll_timeout</code> is a synonym for <code>--poll-timeout</code>. </p>
 </dd>
<dt><code>--socket-timeout=&lt;socket_timeout&gt;</code></dt>
<dd> <p> if a network connection to a remote peer can&#8217;t be established within &lt;socket_timeout&gt; seconds, give up. Default is 60 seconds. Note that <code>--socket_timeout</code> is a synonym for <code>--socket-timeout</code>. </p>
 </dd>
<dt><code>--blocksize=&lt;io_block_size&gt;</code></dt>
<dd> <p> the number of bytes SEC will attempt to read at once from an input file. Default is 8192 bytes (i.e., read from input files by 8KB blocks). </p>
 </dd>
<dt><code>--bufsize=&lt;input_buffer_size&gt;</code></dt>
<dd> <p> set all input buffers to hold &lt;input_buffer_size&gt; lines. The content of input buffers will be compared with patterns that are part of rule definitions (i.e., no more than &lt;input_buffer_size&gt; lines can be matched by a pattern at a time). If &lt;input_buffer_size&gt; is set to 0, SEC will determine the proper value for &lt;input_buffer_size&gt; by checking event matching patterns of all SEC rules. Default is 0 (i.e., determine the size of input buffers automatically). </p>
 </dd>
<dt><code>--evstoresize=&lt;event_store_size&gt;</code></dt>
<dd> <p> set an upper limit to the number of events in context event stores. Default is 0 which sets no limit. </p>
 </dd>
<dt><code>--cleantime=&lt;clean_time&gt;</code></dt>
<dd> <p> time interval in seconds that specifies how often internal event correlation and context lists are processed, in order to accomplish time-related tasks and to remove obsolete elements. See INPUT PROCESSING AND TIMING section for more information. Default is 1 second. </p>
 </dd>
<dt><code>--log=&lt;logfile&gt;</code></dt>
<dd> <p> use &lt;logfile&gt; for logging SEC activities. Note that if the SEC standard error is connected to a terminal, messages will also be logged there, in order to facilitate debugging. </p>
 </dd>
<dt><code>--syslog=&lt;facility&gt;</code></dt>
<dd> <p> use syslog for logging SEC activities. All messages will be logged with the facility &lt;facility&gt;, e.g., <i>local0</i> (see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for possible facility values). Warning: be careful with using this option if SEC is employed for monitoring syslog log files, because message loops might occur. </p>
 </dd>
<dt><code>--debug=&lt;debuglevel&gt;</code></dt>
<dd> <p> set logging verbosity for SEC. Setting debuglevel to &lt;debuglevel&gt; means that all messages of level &lt;debuglevel&gt; and lower are logged (e.g., if &lt;debuglevel&gt; is 3, messages from levels 1-3 are logged). The following levels are recognized by SEC: <br />
 1 - critical messages (severe faults that cause SEC to terminate, e.g., a failed system call) <br />
 2 - error messages (faults that need attention, e.g., an incorrect rule definition in a configuration file) <br />
 3 - warning messages (possible faults, e.g., a command forked from SEC terminated with a non-zero exit code) <br />
 4 - notification messages (normal system level events and interrupts, e.g., the reception of a signal) <br />
 5 - informative messages (information about external programs forked from SEC) <br />
 6 - debug messages (detailed information about all SEC activities) <br />
 Default &lt;debuglevel&gt; is 6 (i.e., log everything). See SIGNALS section for information on how to change &lt;debuglevel&gt; at runtime. </p>
 </dd>
<dt><code>--pid=&lt;pidfile&gt;</code></dt>
<dd> <p> SEC will store its process ID to &lt;pidfile&gt; at startup. </p>
 </dd>
<dt><code>--dump=&lt;dumpfile&gt;</code></dt>
<dd> <p> SEC will use &lt;dumpfile&gt; as its dump file for writing performance and debug data. With the <code>--dumpfts</code> option, a timestamp suffix is appended to the dump file name. See SIGNALS section for more information. Default is /tmp/sec.dump. </p>
 </dd>
<dt><code>--user=&lt;username&gt;</code>, <code>--group=&lt;groupname&gt;</code></dt>
<dd> <p> if SEC is started with effective user ID 0, it will drop root privileges by switching to user &lt;username&gt; and group &lt;groupname&gt;. The <code>--group</code> option can&#8217;t be used without the <code>--user</code> option. If the <code>--user</code> option is given without <code>--group</code>, primary group of the user &lt;username&gt; is assumed for &lt;groupname&gt;. If several groups are provided with multiple <code>--group</code> options, SEC switches to the first group with other groups as supplementary groups. </p>
 </dd>
<dt><code>--umask=&lt;mode&gt;</code></dt>
<dd> <p> set file mode creation mask to &lt;mode&gt; at SEC startup, where &lt;mode&gt; is a value from the range 0..0777 (see also <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)). Octal, decimal, hexadecimal, and binary values can be specified for &lt;mode&gt; (e.g., octal mask 0027 can also be expressed as 23, 0x17, and 0b000010111). </p>
 </dd>
<dt><code>--dumpfts</code>, <code>--nodumpfts</code></dt>
<dd> <p> if the <code>--dumpfts</code> option is specified, a timestamp suffix (seconds since Epoch) is appended to the dump file name that reflects the file creation time. Default is <code>--nodumpfts</code>. </p>
 </dd>
<dt><code>--quoting</code>, <code>--noquoting</code></dt>
<dd> <p> if the <code>--quoting</code> option is specified, operation description strings that are supplied to command lines of <i>shellcmd</i>, <i>spawn</i>, and <i>cspawn</i> actions will be put inside single quotes. Each single quote (&#8216;) that strings originally contain will be masked. This option prevents the shell from interpreting special symbols that operation description strings might contain. Default is <code>--noquoting</code>. </p>
 </dd>
<dt><code>--tail</code>, <code>--notail</code></dt>
<dd> <p> if the <code>--notail</code> option is specified, SEC will process all data that are currently available in input files and exit after reaching all EOFs. If all input is received from a pipe and the <code>--notail</code> option is given, SEC terminates when the last writer closes the pipe (EOF condition). Please note that with named pipes <code>--notail</code> should be used with <code>--norwfifo</code>. With the <code>--tail</code> option, SEC will jump to the end of input files and wait for new lines to arrive. Each input file is tracked both by its name and i-node, and input file rotations are handled seamlessly. If the input file is recreated or truncated, SEC will reopen it and process its content from the beginning. If the input file is removed (i.e., there is just an i-node left without a name), SEC will keep the i-node open and wait for the input file recreation. Default is <code>--tail</code>. </p>
 </dd>
<dt><code>--fromstart</code>, <code>--nofromstart</code></dt>
<dd> <p> these flags have no meaning when the <code>--notail</code> option is also specified. When used in combination with <code>--tail</code> (or alone, since <code>--tail</code> is enabled by default), <code>--fromstart</code> will force SEC to read and process input files from the beginning to the end, before the &#8216;tail&#8217; mode is entered. Default is <code>--nofromstart</code>. </p>
 </dd>
<dt><code>--detach</code>, <code>--nodetach</code></dt>
<dd> <p> if the <code>--detach</code> option is specified, SEC will disassociate itself from the controlling terminal and become a daemon at startup (note that SEC will close its standard input, standard output, and standard error, and change its working directory to the root directory). Default is <code>--nodetach</code>. </p>
 </dd>
<dt><code>--jointbuf</code>, <code>--nojointbuf</code></dt>
<dd> <p> if the <code>--jointbuf</code> option is specified, SEC uses joint input buffer for all input sources (the size of the buffer is set with the <code>--bufsize</code> option). The <code>--nojointbuf</code> option creates a separate input buffer for each input file, and a separate buffer for all synthetic and internal events (the sizes of all buffers are set with the <code>--bufsize</code> option). The <code>--jointbuf</code> option allows multiline patterns to match lines from several input sources, while the <code>--nojointbuf </code> pattern restricts the matching to lines from one input source only. See INPUT PROCESSING AND TIMING section for more information. If the size of input buffer(s) is 1 (either explicitly set with <code>--bufsize=1</code> or automatically determined from SEC rules), <code>--jointbuf</code> option is enabled, otherwise the default is <code>--nojointbuf</code>. </p>
 </dd>
<dt><code>--keepopen</code>, <code>--nokeepopen</code></dt>
<dd> <p> if the <code>--keepopen</code> option is specified, SEC will keep input files open across soft restarts. When the <code>SIGABRT</code> signal is received, SEC will not reopen input files which have been opened previously, but will only open input files which are in the closed state. The <code>--nokeepopen </code> option forces SEC to close and (re)open all input files during soft restarts. Default is <code>--keepopen</code>. </p>
 </dd>
<dt><code>--rwfifo</code>, <code>--norwfifo</code></dt>
<dd> <p> if the <code>--norwfifo</code> option is specified, named pipe input files are opened in read-only mode. In this mode, the named pipe has to be reopened when the last writer closes the pipe, in order to clear the EOF condition on the pipe. With the <code>--rwfifo</code> option, named pipe input files are opened in read-write mode, although SEC never writes to the pipes. In this mode, the pipe does not need to be reopened when an external writer closes it, since there is always at least one writer on the pipe and EOF will never appear. Therefore, if the <code>--notail</code> option has been given, <code>--norwfifo</code> should also be specified. Default is <code>--rwfifo</code>. </p>
 </dd>
<dt><code>--childterm</code>, <code>--nochildterm</code></dt>
<dd> <p> if the <code>--childterm</code> option is specified, SEC will send the SIGTERM signal to all its child processes when it terminates or goes through a full restart. Default is <code>--childterm</code>. </p>
 </dd>
<dt><code>--intevents</code>, <code>--nointevents</code></dt>
<dd> <p> SEC will generate internal events when it starts up, when it receives certain signals, and when it terminates gracefully. Specific rules can be written to match those internal events, in order to accomplish special tasks at SEC startup, restart, and shutdown. See INTERNAL EVENTS AND CONTEXTS section for more information. Default is <code>--nointevents</code>. </p>
 </dd>
<dt><code>--intcontexts</code>, <code>--nointcontexts</code></dt>
<dd> <p> SEC will create an internal context when it reads a line from an input file. This will help the user to write rules that match data from particular input source only. See INTERNAL EVENTS AND CONTEXTS section for more information. Default is <code>--nointcontexts</code>. </p>
 </dd>
<dt><code>--testonly</code>, <code>--notestonly</code></dt>
<dd> <p> if the <code>--testonly</code> option is specified, SEC will exit immediately after parsing the configuration file(s). If the configuration file(s) contained no faulty rules, SEC will exit with 0, otherwise with 1. Default is <code>--notestonly</code>. </p>
 </dd>
<dt><code>--help</code>, <code>-?</code></dt>
<dd> <p> SEC will output usage information and exit. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> SEC will output version information and exit. </p>
 </dd></dl>
<p> Note that options can be introduced both with the single dash (-) and double dash (--), and both the equal sign (=) and whitespace can be used for separating the option name from the option value. For example, <code>-conf=&lt;file_pattern&gt;</code> and <code>--conf &lt;file_pattern&gt;</code> options are equivalent.  </p>
<h2>CONFIGURATION FILES</h2>
<p> Each SEC configuration file consists of rule definitions which are separated by empty lines, whitespace lines and/or comment lines. Each rule definition consists of keyword=value fields, one keyword and value per line. Values are case insensitive only where character case is not important (like the values specifying rule types, e.g., &#8216;Single&#8217; and &#8216;single&#8217; are treated identically). The backslash character (\) may be used at the end of a line to continue the current rule field in the next line. Lines which begin with the number sign (#) are treated as comments and ignored (whitespace characters may precede #). Any comment line, empty line, whitespace line, or end of file will terminate the preceding rule definition. For inserting comments into rule definitions, the <i>rem</i> keyword can be used. For example, the following lines define two rules: </p>
<p> type=Single <br />
 rem=this rule matches any line which contains \ <br />
&nbsp;<wbr>three consecutive A characters and writes the string&nbsp;<wbr>\ <br />
&nbsp;<wbr>&quot;three A characters were observed&quot;&nbsp;<wbr>to standard output <br />
 ptype=SubStr <br />
 pattern=AAA <br />
 desc=Three A characters <br />
 action=write - three A characters were observed <br />
 # This comment line ends preceding rule definition. <br />
 # The following rule works like the previous rule, <br />
 # but looks for three consecutive B characters and <br />
 # writes the string &quot;three B characters were observed&quot; <br />
 # to standard output <br />
 type=Single <br />
 ptype=SubStr <br />
 pattern=BBB <br />
 desc=Three B characters <br />
 action=write - three B characters were observed </p>
<p> Apart from keywords that are part of rule definitions, <i>label</i> keywords may appear anywhere in the configuration file. The value of each <i>label</i> keyword will be treated as a label that can be referred to in rule definitions as a point-of-continue. This allows for continuing event processing at a rule that follows the label, after the current rule has matched and processed the event. </p>
<p> The points-of-continue are defined with <i>continue*</i> fields. Accepted values for these fields are: </p>
<dl>
<dt><i>TakeNext </i></dt>
<dd> <p> after an event has matched the rule, search for matching rules in the configuration file will continue from the next rule. </p>
 </dd>
<dt><i>GoTo &lt;label&gt;</i></dt>
<dd> <p> after an event has matched the rule, search for matching rules will continue from the location of &lt;label&gt; in the configuration file (&lt;label&gt; must be defined with the <i>label</i> keyword anywhere in the configuration file *after* the current rule definition). </p>
 </dd>
<dt><i>DontCont</i> (default value) </dt>
<dd> <p> after an event has matched the rule, search for matching rules ends in the *current* configuration file. </p>
 </dd>
<dt><i>EndMatch</i></dt>
<dd> <p> after an event has matched the rule, search for matching rules ends for *all* configuration files. </p>
 </dd></dl>
<p> SEC rules from the same configuration file are matched against input in the order they have been given in the file. For example, consider a configuration file which contains the following rule sequence: </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=AAA <br />
 rem=after this rule has matched, continue from last rule <br />
 continue=GoTo lastRule <br />
 desc=Three A characters <br />
 action=write - three A characters were observed </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=BBB <br />
 rem=after this rule has matched, don&#8217;t consider following rules, \ <br />
&nbsp;<wbr>since&nbsp;<wbr>&#8216;continue&#8217;&nbsp;<wbr>defaults to&nbsp;<wbr>&#8216;DontCont&#8217; <br />
 desc=Three B characters <br />
 action=write - three B characters were observed </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=CCC <br />
 rem=after this rule has matched, continue from next rule <br />
 continue=TakeNext <br />
 desc=Three C characters <br />
 action=write - three C characters were observed </p>
<p> label=lastRule </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=DDD <br />
 desc=Three D characters <br />
 action=write - three D characters were observed </p>
<p> For the input line &quot;AAABBBCCCDDD&quot;, this ruleset writes strings &quot;three A characters were observed&quot; and &quot;three D characters were observed&quot; to standard output. If the input line is &quot;BBBCCCDDD&quot;, the string &quot;three B characters were observed&quot; is written to standard output. For the input line &quot;CCCDDD&quot;, strings &quot;three C characters were observed&quot; and &quot;three D characters were observed&quot; are sent to standard output, while the input line &quot;DDD&quot; produces the output string &quot;three D characters were observed&quot;. </p>
<p> If there are two or more configuration files, rule sequence from every file is matched against input (unless explicitly specified otherwise). For example, suppose SEC is started with the command line </p>
<p> /usr/bin/sec --input=- \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--conf=/etc/sec/sec1.rules --conf=/etc/sec/sec2.rules </p>
<p> and the configuration file /etc/sec/sec1.rules has the following content: </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=AAA <br />
 desc=Three A characters <br />
 action=write - three A characters were observed </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=BBB <br />
 continue=EndMatch <br />
 desc=Three B characters <br />
 action=write - three B characters were observed </p>
<p> Also, suppose the configuration file /etc/sec/sec2.rules has the following content: </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=CCC <br />
 desc=Three C characters <br />
 action=write - three C characters were observed </p>
<p> If SEC receives the line &quot;AAABBBCCC&quot; from standard input, rules from both configuration files are tried, and as a result, the strings &quot;three A characters were observed&quot; and &quot;three C characters were observed&quot; are written to standard output. Note that rules from /etc/sec/sec1.rules are tried first against the input line, since the option <code>--conf=/etc/sec/sec1.rules </code> is given before <code>--conf=/etc/sec/sec2.rules </code> in the SEC command line (see also INPUT PROCESSING AND TIMING section for a more detailed discussion). If SEC receives the line &quot;BBBCCC&quot; from standard input, the second rule from /etc/sec/sec1.rules produces a match, and the string &quot;three B characters were observed&quot; is written to standard output. Since the rule contains <i>continue=EndMatch</i> statement, the search for matching rules will end for all configuration files, and rules from /etc/sec/sec2.rules will not be not tried. Without this statement, the search for matching rules would continue in /etc/sec/sec2.rules, and the first rule would write the string &quot;three C characters were observed&quot; to standard output.  </p>
<h2>PATTERNS, PATTERN TYPES AND MATCH VARIABLES</h2>
<p> Patterns and pattern types are defined with <i>pattern*</i> and <i>ptype*</i> rule fields. Many pattern types define the number of lines <i>N </i> which the pattern matches (if <i>N </i> is omitted, 1 is assumed). If <i>N</i> is greater than 1, the scope of matching is set with the <code>--jointbuf</code> and <code>--nojointbuf</code> options. With <code>--jointbuf</code>, the pattern is used for matching <i>N </i> last input lines taken from the joint input buffer (the lines can come from different input sources). With <code>--nojointbuf</code>, the source of the last input line is identified, and the pattern is matched with <i>N </i> last input lines from the input buffer of the identified source. </p>
<dl>
<dt><i>SubStr[N]</i></dt>
<dd> <p> pattern is a string that is searched in the last N input lines L1, L2, ..., LN. If N is greater than 1, the input lines are joined into a string &quot;L1&lt;NEWLINE&gt;L2&lt;NEWLINE&gt;...&lt;NEWLINE&gt;LN&quot;, and the pattern string will be searched from it. If the pattern string is found in input line(s), the pattern matches. Backslash sequences \t, \n, \r, \s, and \0 can be used in the pattern for denoting tabulation, newline, carriage return, space character, and empty string, respectively, while \\ denotes backslash itself. For example, consider the following pattern definition: </p>
<p> ptype=substr <br />
 pattern=Backup done:\tsuccess </p>
<p> The pattern matches lines containing &quot;Backup done:&lt;TAB&gt;success&quot;. </p>
<p> Note that since the <i>SubStr[N]</i> pattern type has been designed for fast matching, it does not support match variables. </p>
 </dd>
<dt><i>RegExp[N]</i></dt>
<dd> <p> pattern is a Perl regular expression (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1) for more information) for matching the last N input lines L1, L2, ..., LN. If N is greater than 1, the input lines are joined into a string &quot;L1&lt;NEWLINE&gt;L2&lt;NEWLINE&gt;...&lt;NEWLINE&gt;LN&quot;, and the regular expression is matched with this string. If the regular expression matches, match variables will be set, and these match variables can be used in other parts of the rule definition. </p>
<p> In addition to numbered match variables ($1, $2, etc.), SEC supports named match variables $+{name} and the $0 variable. The $0 variable holds the entire string of last N input lines that the regular expression has matched. Named match variables can be created in newer versions of Perl regular expression language, e.g., (?&lt;myvar&gt;AB|CD) sets $+{myvar} to AB or CD. The special named match variable $+{_inputsrc} is created by SEC and holds input file name(s) where matching line(s) came from. </p>
<p> For example, the following pattern matches the SSH &quot;Connection from&quot; event, and sets $0 to the entire event line, both $1 and $+{ip} to the IP address of the remote node, $2 to the port number at the remote node, and $+{_inputsrc} to the input file name: </p>
<p> ptype=RegExp <br />
 pattern=sshd\[\d+\]: Connection from (?&lt;ip&gt;[\d.]+) port (\d+) </p>
<p> Also, SEC allows for match caching and for the creation of additional named match variables through variable maps which are defined with the <i>varmap*</i> fields. Variable map is a list of <i>name=number </i> mappings separated by semicolons, where <i>name</i> is the name for the named variable and <i>number </i> identifies a numbered match variable that is set by the regular expression. Each name must begin with a letter and consist of letters, digits and underscores. After the regular expression has matched, named variables specified by the map are created from corresponding numbered variables. If the same named variable is set up both from the regular expression and variable map, the map takes precedence. </p>
<p> If <i>name</i> is not followed by the equal sign and number in the <i>varmap*</i> field, it is regarded as a common name for all match variables and their values from a successful match. This name is used for caching a successful match by the pattern -- match variables and their values are stored in the memory-based pattern match cache under <i>name</i>. Cached match results can be reused by <i>Cached</i> and <i>NCached</i> patterns. Note that before processing each new input line, previous content of the pattern match cache is cleared. Also note that a successful pattern match is cached even if the subsequent context expression evaluation yields FALSE (see INPUT PROCESSING AND TIMING section for more information). </p>
<p> For example, consider the following pattern definition: </p>
<p> ptype=regexp <br />
 pattern=(?i)(\S+\.mydomain).*printer: toner\/ink low <br />
 varmap=printer_toner_or_ink_low; message=0; hostname=1 </p>
<p> The pattern matches &quot;printer: toner/ink low&quot; messages in a case insensitive manner from printers belonging to .mydomain. Note that the printer hostname is assigned to $1 and $+{hostname}, while the whole message line is assigned to $0 and $+{message}. The name of the file where message line came from is assigned to $+{_inputsrc}. Also, these variables and their values are stored to the pattern match cache under the name &quot;printer_toner_or_ink_low&quot;. </p>
<p> The following pattern definition produces a match if the last two input lines are AAA and BBB: </p>
<p> ptype=regexp2 <br />
 pattern=^AAA\nBBB$ <br />
 varmap=aaa_bbb </p>
<p> Note that with the <code>--nojointbuf</code> option the pattern only matches if the matching lines are coming from the *same* input file, while the <code>--jointbuf</code> option lifts that restriction. </p>
<p> In the case of a match, $0 is set to &quot;AAA&lt;NEWLINE&gt;BBB&quot; and $+{_inputsrc} to file name(s) for matching lines. Also, these variable-value pairs are cached under the name &quot;aaa_bbb&quot;. </p>
 </dd>
<dt><i>PerlFunc[N]</i></dt>
<dd> <p> pattern is a Perl function for matching the last N input lines L1, L2, ..., LN. The Perl function is compiled at SEC startup with the Perl <code>eval</code>() function, and <code>eval</code>() must return a code reference for the pattern to be valid (see also PERL INTEGRATION section). The function is called in Perl list context, and with the <code>--jointbuf</code> option, lines L1, L2, ..., LN and the names of corresponding input files F1, F2, ..., FN are passed to the function as parameters: </p>
<p> function(L1, L2, ..., LN, F1, F2, ..., FN) </p>
<p> Note that with the <code>--nojointbuf</code> option, the function is called with a single file name parameter F, since lines L1, ..., LN are coming from the same input file: </p>
<p> function(L1, L2, ..., LN, F) </p>
<p> Also note that if the input line is a synthetic event, the input file name is Perl undefined value. </p>
<p> If the function returns several values or a single value that is true in Perl boolean context, the pattern matches. If the function returns no values or a single value that is false in Perl boolean context (0, empty string or undefined value), the pattern does not match. If the pattern matches, return values will be assigned to numbered match variables ($1, $2, etc.). Like with RegExp patterns, the $0 variable is set to matching input line(s), the $+{_inputsrc} variable is set to input file name(s), and named match variables can be created from variable maps. For example, consider the following pattern definition: </p>
<p> ptype=perlfunc2 <br />
 pattern=sub { return ($_[0] cmp $_[1]); } </p>
<p> The pattern compares last two input lines in a stringwise manner ($_[1] holds the last line and $_[0] the preceding one), and matches if the lines are different. Note that the result of the comparison is assigned to $1, while two matching lines are concatenated (with the newline character between them) and assigned to $0. The file name(s) for matching lines are assigned to $+{_inputsrc}. </p>
<p> The following pattern produces a match for any line, and sets $1, $2 and $3 variables to strings &quot;abc&quot;, &quot;def&quot; and &quot;ghi&quot;, respectively (also, $0 is set to the whole input line and $+{_inputsrc} to the input file name): </p>
<p> ptype=perlfunc <br />
 pattern=sub { return (&quot;abc&quot;, &quot;def&quot;, &quot;ghi&quot;); } </p>
<p> The following pattern definition produces a match if the input line is not a synthetic event and contains either the string &quot;abc&quot; or &quot;def&quot;. The $0 variable is set to the matching line, while $1, $+{file} and $+{_inputsrc} are set to the name of the input file: </p>
<p> ptype=perlfunc <br />
 pattern=sub { if (defined($_[1]) &amp;&amp; $_[0] =~ /abc|def/) \ <br />
 { return $_[1]; } return 0; } <br />
 varmap= file=1 </p>
<p> Finally, if a function pattern returns a single value which is a reference to a Perl hash, named match variables are created from key-value pairs in the hash. For example, the following pattern matches a line if it contains either the string &quot;three&quot; or &quot;four&quot;. Apart from setting $0 and $+{_inputsrc}, the pattern also creates match variables $+{three} and $+{four}, and sets them to 3 and 4, respectively: </p>
<p> ptype=perlfunc <br />
 pattern=sub { my(%hash); \ <br />
 if ($_[0] !~ /three|four/) { return 0; } \ <br />
 $hash{&quot;three&quot;} = 3; $hash{&quot;four&quot;} = 4; return \%hash; } </p>
 </dd>
<dt><i>Cached</i></dt>
<dd> <p> pattern is a name that is searched in the pattern match cache (entries are stored into the cache with the <i>varmap*</i> fields). If an entry with the given name is found in the cache, the pattern matches, and match variables and values are retrieved from the cache. For example, if the input line matches the following pattern </p>
<p> ptype=perlfunc <br />
 pattern=sub { if (defined($_[1]) &amp;&amp; $_[0] =~ /abc|def/) \ <br />
 { return $_[1]; } return 0; } <br />
 varmap=abc_or_def_found; file=1 </p>
<p> then the entry &quot;abc_or_def_found&quot; is created in the pattern match cache. Therefore, the pattern </p>
<p> ptype=cached <br />
 pattern=abc_or_def_found </p>
<p> will also produce a match for this input line, and set the $0, $1, $+{file}, and $+{_inputsrc} variables to values from the previous match. </p>
 </dd>
<dt><i>NSubStr[N]</i></dt>
<dd> <p> like <i>SubStr[N]</i>, except that the result of the match is negated. Note that this pattern type does not support match variables. </p>
 </dd>
<dt><i>NRegExp[N]</i></dt>
<dd> <p> like <i>RegExp[N]</i>, except that the result of the match is negated and variable maps are not supported. Note that the only match variables supported by this pattern type are $0 and $+{_inputsrc}. </p>
 </dd>
<dt><i>NPerlFunc[N]</i></dt>
<dd> <p> like <i>PerlFunc[N]</i>, except that the result of the match is negated and variable maps are not supported. Note that the only match variables supported by this pattern type are $0 and $+{_inputsrc}. </p>
 </dd>
<dt><i>NCached</i></dt>
<dd> <p> like <i>Cached</i>, except that the result of the match is negated. Note that this pattern type does not support match variables. </p>
 </dd>
<dt><i>TValue</i></dt>
<dd> <p> pattern is a truth value, with TRUE and FALSE being legitimate values. TRUE always matches an input line, while FALSE never matches anything. Note that this pattern type does not support match variables. </p>
 </dd></dl>
<p> When match variables are substituted, each &quot;$$&quot; sequence is interpreted as a literal dollar sign ($) which allows for masking match variables. For example, the string &quot;Received $$1&quot; becomes &quot;Received $1&quot; after substitution, while &quot;Received $$$1&quot; becomes &quot;Received $&lt;value_of_1st_var&gt;&quot;. In order to disambiguate numbered match variables from the following text, variable number must be enclosed in braces. For example, the string &quot;Received ${1}0&quot; becomes &quot;Received &lt;value_of_1st_var&gt;0&quot; after substitution, while the string &quot;Received $10&quot; would become &quot;Received &lt;value_of_10th_var&gt;&quot;. </p>
<p> If the match variable was not set by the pattern, it is substituted with an empty string (i.e., a zero-width string). Thus the string &quot;Received $10!&quot; becomes &quot;Received !&quot; after substitution if the pattern did not set $10. (Note that prior to SEC-2.6, unset variables were *not* substituted.) </p>
<p> In the current version of SEC, names of $+{name} match variables must comply with the following naming convention -- the first character can be a letter or underscore, while remaining characters can be letters, digits, underscores and exclamation marks (!). However, when setting named match variables from a pattern, it is recommended to begin the variable name with a letter, since names of special automatically created variables begin with an underscore (e.g., $+{_inputsrc}). </p>
<p> After the pattern has matched an event and match variables have been set, it is also possible to refer to previously cached match variables with the syntax <i>$:{entryname:varname}</i>, where <i>entryname</i> is the name of the pattern match cache entry, and <i>varname</i> is the name of the variable stored under the entry. For example, if the variable $+{ip} has been previously cached under the entry &quot;SSH&quot;, it can be referred as $:{SSH:ip}. For the reasons of efficiency, the $:{entryname:varname} syntax is not supported for fast pattern types which do not set match variables (i.e., SubStr, NSubStr, NCached and TValue). </p>
<p> Note that since Pair and PairWithWindow rules have two patterns, match variables of the first pattern are shadowed for some rule fields when the second pattern matches and sets variables. In order to refer to shadowed variables, their names must begin with % instead of $ (e.g., %1 refers to match variable $1 set by the first pattern). However, the use of the %-prefix is only valid under the following circumstances -- *both* pattern types support match variables *and* in the given rule field match variables from *both* patterns can be used. </p>
<p> The %-prefixed match variables are masked with the &quot;%%&quot; sequence (like regular match variables with &quot;$$&quot;). Similarly, the braces can be used for disambiguating the %-prefixed variables from the following text. </p>
<p> Finally, note that the second pattern of Pair and PairWithWindow rules may contain match variables if the second pattern is of type SubStr, NSubStr, Regexp, or NRegExp. The variables are substituted at runtime with the values set by the first pattern. If the pattern is a regular expression, all special characters inside substituted values are masked with the Perl <code>quotemeta</code>() function and the final expression is checked for correctness.  </p>
<h2>CONTEXTS AND CONTEXT EXPRESSIONS</h2>
<p> A SEC context is a memory based entity which has one or more names, a lifetime, and an event store. Also, an action list can be set up for a context which is executed immediately before the context expires. </p>
<p> For example, the action <i>create MYCONTEXT 3600 (report MYCONTEXT /bin/mail root [at] localhost)</i> creates the context <code>MYCONTEXT </code> which has a lifetime of 3600 seconds and empty event store. Also, immediately before <code>MYCONTEXT </code> expires and is dropped from memory, the action <i>report MYCONTEXT /bin/mail root [at] localhost</i> is executed which mails the event store of <code>MYCONTEXT </code> to root [at] localhost. </p>
<p> Contexts can be used for event aggregation and reporting. Suppose the following actions are executed in this order: </p>
<p> create MYCONTEXT <br />
 add MYCONTEXT This is a test <br />
 alias MYCONTEXT MYALIAS <br />
 add MYALIAS This is another test <br />
 report MYCONTEXT /bin/mail root [at] localhost <br />
 delete MYALIAS </p>
<p> The first action creates the context <code>MYCONTEXT </code> with infinite lifetime and empty event store. The second action appends the string &quot;This is a test&quot; to the event store of <code>MYCONTEXT</code>. The third action sets up an alias name <code>MYALIAS </code> for the context (names <code>MYCONTEXT </code> and <code>MYALIAS</code> refer to the same context data structure). The fourth action appends the string &quot;This is another test&quot; to the event store of the context. The fifth action writes the lines </p>
<p> This is a test <br />
 This is another test </p>
<p> to the standard input of the <i>/bin/mail root [at] localhost </i> command. The sixth action deletes the context data structure from memory and drops its names <code>MYCONTEXT </code> and <code>MYALIAS</code>. </p>
<p> Since contexts are accessible from all rules and event correlation operations, they can be used for data sharing and joining several rules into one event correlation scheme. In order to check for the presence of contexts from rules, context expressions can be employed. </p>
<p> Context expressions are boolean expressions that are defined with the <i>context*</i> rule fields. Context expressions can be used for restricting the matches produced by patterns, since if the expression evaluates FALSE, the rule will not match an input event. </p>
<p> The context expression accepts context names, Perl miniprograms, Perl functions, and pattern match cache lookups as operands. These operands can be combined with the following operators: <br />
 ! - logical NOT, <br />
 &amp;&amp; - short-circuit logical AND, <br />
 || - short-circuit logical OR. <br />
 In addition, parentheses can be used for grouping purposes. </p>
<p> If the operand does not contain any special operators (such as -&gt; or :&gt;, see below), it is treated as a context name. Context name operands may contain match variables, but may not contain whitespace. If the context name refers to an existing context, the operand evaluates TRUE, otherwise it evaluates FALSE. </p>
<p> For example, consider the following rule sequence: </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=Test: (\d+) <br />
 desc=test <br />
 action=create CONT_$1 </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=Test2: (\d+) (\d+) <br />
 context=CONT_$1 &amp;&amp; CONT_$2 <br />
 desc=test <br />
 action=write - Both $1 and $2 have been seen in the past </p>
<p> If the following input lines appear in this order </p>
<p> Test: 19 <br />
 Test: 261 <br />
 Test2: 19 787 <br />
 Test: 787 <br />
 Test2: 787 261 </p>
<p> the first input line matches the first rule which creates the context <code>CONT_19</code>, and similarly, the second input line triggers the creation of the context <code>CONT_261</code>. The third input line &quot;Test2: 19 787&quot; matches the regular expression </p>
<p> Test2: (\d+) (\d+) </p>
<p> but does not match the second rule, since the boolean expression </p>
<p> CONT_19 &amp;&amp; CONT_787 </p>
<p> evaluates FALSE (context <code>CONT_19</code> exists, but context <code>CONT_787</code> doesn&#8217;t). The fourth input line matches the first rule which creates the context <code>CONT_787</code>. The fifth input line &quot;Test2: 787 261&quot; matches the second rule, since the boolean expression </p>
<p> CONT_787 &amp;&amp; CONT_261 </p>
<p> evaluates TRUE (both context <code>CONT_787</code> and context <code>CONT_261</code> exist), and therefore the string &quot;Both 787 and 261 have been seen in the past&quot; is written to standard output. </p>
<p> If the context expression operand contains the arrow operator (-&gt;), the text following the arrow must be a valid Perl function definition that is compiled at SEC startup with the Perl <code>eval</code>() function. The <code>eval</code>() must return a code reference (see also PERL INTEGRATION section for more information). If any text precedes the arrow, it is treated as a list of parameters for the function. Parameters must be separated by whitespace and may contain match variables. In order to evaluate the context expression operand, the Perl function is called in the Perl scalar context. If the return value of the function is true in the Perl boolean context, the operand evaluates TRUE, otherwise it evaluates FALSE. </p>
<p> For example, the following rule matches an SSH login failure event if the login attempt comes from a privileged port of the client host: </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port (\d+) ssh2 <br />
 context=$2 -&gt; ( sub { $_[0] &lt; 1024 } ) <br />
 desc=SSH login failure for $1 priv port $2 <br />
 action=write - SSH login failure for user $1 from a privileged port $2 </p>
<p> When the following message from SSH daemon appears </p>
<p> Dec 16 16:24:59 myserver sshd[13685]: Failed password for risto from 10.12.2.5 port 41063 ssh2 </p>
<p> the regular expression of the rule matches this message, and the value of the $2 match variable (41063) is passed to the Perl function </p>
<p> sub { $_[0] &lt; 1024 } </p>
<p> This function returns true if its input parameter is less than 1024 and false otherwise, and therefore the above message will not match the rule. However, the following message </p>
<p> Dec 16 16:25:17 myserver sshd[13689]: Failed password for risto from 10.12.2.5 port 1023 ssh2 </p>
<p> matches the rule, and the string &quot;SSH login failure for user risto from a privileged port 1023&quot; is written to standard output. </p>
<p> As another example, the following context expression evaluates TRUE if the /var/log/messages file does not exist or was last modified more than 1 hour ago (note that the Perl function takes no parameters): </p>
<p> context= -&gt; ( sub { my(@stat) = stat(&quot;/var/log/messages&quot;); \ <br />
 return (!scalar(@stat) || time() - $stat[9] &gt; 3600); } ) </p>
<p> If the context expression operand contains the :&gt; operator, the text that follows :&gt; must be a valid Perl function definition that is compiled at SEC startup with the Perl <code>eval</code>() function. The <code>eval</code>() must return a code reference (see also PERL INTEGRATION section for more information). If any text precedes the :&gt; operator, it is treated as a list of parameters for the function. Parameters must be separated by whitespace and may contain match variables. It is assumed that each parameter is a name of an entry in the pattern match cache. If an entry with the given name does not exist, Perl undefined value is passed to the function. If an entry with the given name exists, a reference to the entry is passed to the Perl function. Internally, each pattern match cache entry is implemented as a Perl hash which contains all match variables for the given entry. In the hash, each key-value pair represents some variable name and value, e.g., if cached match variable $+{ip} is holding 10.1.1.1, the hash contains the value <code>10.1.1.1</code> with the key <code>ip</code>. In order to evaluate the context expression operand, the Perl function is called in the Perl scalar context. If the return value of the function is true in the Perl boolean context, the operand evaluates TRUE, otherwise it evaluates FALSE. </p>
<p> For example, consider the following rule sequence: </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: (?&lt;status&gt;Accepted|Failed) .+ \ <br />
 for (?&lt;invuser&gt;invalid user )?(?&lt;user&gt;\S+) from (?&lt;ip&gt;[\d.]+) \ <br />
 port (?&lt;port&gt;\d+) ssh2 <br />
 varmap=SSH <br />
 continue=TakeNext <br />
 desc=parse SSH login events and pass them to following rules <br />
 action=none </p>
<p> type=Single <br />
 ptype=Cached <br />
 pattern=SSH <br />
 context=SSH :&gt; ( sub { $_[0]-&gt;{&quot;status&quot;} eq &quot;Failed&quot; &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$_[0]-&gt;{&quot;port&quot;}&nbsp;<wbr>&lt;&nbsp;<wbr>1024&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>defined($_[0]-&gt;{&quot;invuser&quot;})&nbsp;<wbr>}&nbsp;<wbr>) <br />
 desc=Probe of invalid user $+{user} from privileged port of $+{ip} <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;SSH alert&#8217; root [at] localhost </p>
<p> The first rule matches and parses SSH login messages, and stores parsing results to the pattern match cache under the name <code>SSH</code>. The pattern of the second rule (defined with <i>ptype=Cached</i> and <i>pattern=SSH</i>) matches any input event for which the entry <code>SSH</code> has been previously created in the pattern match cache (in other words, the event has been recognized and parsed as an SSH login message). For each matching event, the second rule passes the reference to the <code>SSH</code> cache entry to the Perl function </p>
<p> sub { $_[0]-&gt;{&quot;status&quot;} eq &quot;Failed&quot; &amp;&amp; \ <br />
$_[0]-&gt;{&quot;port&quot;}&nbsp;<wbr>&lt;&nbsp;<wbr>1024&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>\ <br />
defined($_[0]-&gt;{&quot;invuser&quot;})&nbsp;<wbr>} </p>
<p> The function checks the values of $+{status}, $+{port}, and $+{invuser} match variables under the <code>SSH</code> entry, and returns true if $+{status} equals to the string &quot;Failed&quot; (i.e., login attempt failed), the value of $+{port} is less than 1024, and $+{invuser} holds a defined value (i.e., user account does not exist). If the function (and thus context expression) evaluates TRUE, the rule sends a warning e-mail to root [at] localhost that a non-existing user account was probed from a privileged port of a client host. </p>
<p> If the context expression operand begins with the <i>varset</i> keyword, the following string is treated as a name of an entry in the pattern match cache. The operand evaluates TRUE if the given entry exists, and FALSE otherwise. </p>
<p> For example, the following context expression definition evaluates TRUE if the pattern match cache entry <code>SSH</code> exists and under this entry, the value of the match variable $+{user} equals to the string &quot;risto&quot;: </p>
<p> context=varset SSH &amp;&amp; SSH :&gt; ( sub { $_[0]-&gt;{&quot;user&quot;} eq &quot;risto&quot; } ) </p>
<p> If the context expression operand begins with the equal sign (=), the following text must be a Perl miniprogram which is a valid parameter for the Perl <code>eval</code>() function. The miniprogram may contain match variables. In order to evaluate the Perl miniprogram operand, it will be compiled and executed by calling the Perl <code>eval</code>() function in the Perl scalar context (see also PERL INTEGRATION section). If the return value from <code>eval</code>() is true in the Perl boolean context, the operand evaluates TRUE, otherwise it evaluates FALSE. Please note that unlike Perl functions of -&gt; and :&gt; operators which are compiled once at SEC startup, Perl miniprograms are compiled before each execution, and their evaluation is thus considerably more expensive. </p>
<p> For example, the following context expression evaluates TRUE when neither the context <code>C1 </code> nor the context <code>C2 </code> exists and the value of the $1 variable equals to the string &quot;myhost.mydomain&quot;: </p>
<p> context=!(C1 || C2) &amp;&amp; =(&quot;$1&quot; eq &quot;myhost.mydomain&quot;) </p>
<p> Since &amp;&amp; is a short-circuiting operator, the Perl code </p>
<p> &quot;$1&quot; eq &quot;myhost.mydomain&quot; </p>
<p> is *not* evaluated if either <code>C1</code> or <code>C2</code> exists. </p>
<p> Note that since Perl functions and miniprograms may contain strings that clash with context expression operators (e.g., &#8216;!&#8216;), it is recommended to enclose them in parentheses, e.g., </p>
<p> context=$1 $2 -&gt; ( sub { $_[0] != $_[1] } ) </p>
<p> context= =({my($temp) = 0; !$temp;}) </p>
<p> Also, if function parameter lists contain such strings, they should be enclosed in parentheses in the similar way: </p>
<p> context=($1! $2) -&gt; ( sub { $_[0] eq $_[1] } ) </p>
<p> If the whole context expression is enclosed in square brackets [], e.g., [<code>MYCONTEXT1</code> &amp;&amp; !<code>MYCONTEXT2</code>], SEC evaluates the expression *before* pattern matching (normally, the pattern is matched with input line(s) first, so that match variables would be initialized and substituted before the expression is evaluated). However, if the expression does not contain match variables and many input events are known to match the pattern but not the expression, the []-operator could save substantial amount of CPU time.  </p>
<h2>ACTIONS, ACTION LISTS AND ACTION LIST VARIABLES</h2>
<p> Action lists are defined with the <i>action*</i> rule fields. An action list consists of action definitions that are separated by semicolons. Each action definition begins with a keyword specifying the action type. Depending on the action type, parameters may follow, and non-constant parameters may contain match variables. For instance, if the $1 and $2 match variables have the values &quot;test1&quot; and &quot;the second test&quot;, respectively, the action <i>create MYCONT_$1 60</i> creates the context <code>MYCONT_test1 </code> with the lifetime of 60 seconds, while the action <i>write - The names of tests: $1, $2</i> writes the string &quot;The names of tests: test1, the second test&quot; to standard output. In order to use semicolons inside a non-constant parameter, the parameter must be enclosed in parentheses (the outermost set of parentheses will be removed by SEC during configuration file parsing). </p>
<p> For example, the following action list consists of <i>delete</i> and <i>shellcmd</i> actions: </p>
<p> action=delete MYCONTEXT; shellcmd (rm /tmp/sec1.tmp; rm /tmp/sec2.tmp) </p>
<p> The <i>delete</i> action deletes the context <code>MYCONTEXT</code>, while the <i>shellcmd</i> action executes the command line <i>rm /tmp/sec1.tmp; rm /tmp/sec2.tmp</i>. Since the command line contains a semicolon, it has been enclosed in parentheses, since otherwise the semicolon would be mistakenly considered a separator between two actions. </p>
<p> Apart from match variables, SEC supports <i>action list variables</i> in action lists which facilitate data sharing between actions and Perl integration. Each action list variable has a name which must begin with a letter and consist of letters, digits and underscores. Names of built-in variables usually start with a punctuation mark (.), so that they can be distinguished from user defined variables. In order to refer to an action list variable, its name must be prefixed by a percent sign (%). Unlike match variables, action list variables can only be used in action lists and they are substituted with their values immediately before the action list execution. Also, action list variables continue to exist after the current action list has been executed and can be employed in action lists of other rules. </p>
<p> The following action list variables are predefined by SEC: </p>
<dl>
<dt><i>%s </i></dt>
<dd> <p> operation description string (the value of the <i>desc</i> field after match variables have been substituted with their values). Note that for the <i>action2</i> field of Pair and PairWithWindow rules, the %s variable is set by evaluating the <i>desc2</i> field of the rule. </p>
 </dd>
<dt><i>%t </i></dt>
<dd> <p> the time in human-readable format, as returned by the Perl <code>localtime</code>() function in the Perl scalar context (e.g., Fri Feb 19 17:54:18 2016). </p>
 </dd>
<dt><i>%u </i></dt>
<dd> <p> the time in seconds since Epoch, as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call. </p>
 </dd>
<dt><i>%.sec </i></dt>
<dd> <p> number of seconds after the minute, in the range 00-59 (the value consists of two digits and is zero padded on the left). </p>
 </dd>
<dt><i>%.min </i></dt>
<dd> <p> number of minutes after the hour, in the range 00-59 (the value consists of two digits and is zero padded on the left). </p>
 </dd>
<dt><i>%.hour </i></dt>
<dd> <p> number of hours past midnight, in the range 00-23 (the value consists of two digits and is zero padded on the left). </p>
 </dd>
<dt><i>%.hmsstr </i></dt>
<dd> <p> the time in HH:MM:SS format (hours, minutes and seconds separated by colons, e.g., 09:32:04 or 18:06:02). </p>
 </dd>
<dt><i>%.mday </i></dt>
<dd> <p> day of the month, in the range 01-31 (the value consists of two digits and is zero padded on the left). </p>
 </dd>
<dt><i>%.mdaystr </i></dt>
<dd> <p> day of the month as a string (the value consists of two characters and is space padded on the left, e.g., &quot; 1&quot;, &quot; 4&quot;, &quot; 9&quot;, or &quot;25&quot;). </p>
 </dd>
<dt><i>%.mon </i></dt>
<dd> <p> month, in the range 01-12 (the value consists of two digits and is zero padded on the left). </p>
 </dd>
<dt><i>%.monstr </i></dt>
<dd> <p> abbreviated name of the month according to the current locale, as returned by the %b specification of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library call (e.g., Jan, May, or Sep). </p>
 </dd>
<dt><i>%.year </i></dt>
<dd> <p> year (e.g., 1998 or 2016). </p>
 </dd>
<dt><i>%.wday </i></dt>
<dd> <p> day of the week, in the range 0-6 (0 denotes Sunday). </p>
 </dd>
<dt><i>%.wdaystr </i></dt>
<dd> <p> abbreviated name of the day of the week according to the current locale, as returned by the %a specification of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library call (e.g., Mon, Wed, or Sat). </p>
 </dd>
<dt><i>%.tzname </i></dt>
<dd> <p> name of the timezone according to the current locale, as returned by the %Z specification of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library call (e.g., UTC or EET). </p>
 </dd>
<dt><i>%.tzoff </i></dt>
<dd> <p> timezone offset from UTC, as returned by the %z specification of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library call (e.g., -0500 or +0200). </p>
 </dd>
<dt><i>%.tzoff2 </i></dt>
<dd> <p> timezone offset from UTC in +hh:mm/-hh:mm format (e.g., -05:00 or +02:00), provided that the %z specification of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library call returns the value in +hhmm/-hhmm format (if the value does not follow this format, %.tzoff2 is set to an empty string). </p>
 </dd>
<dt><i>%.nl </i></dt>
<dd> <p> newline character. </p>
 </dd>
<dt><i>%.cr </i></dt>
<dd> <p> carriage return character. </p>
 </dd>
<dt><i>%.tab </i></dt>
<dd> <p> tabulation character. </p>
 </dd>
<dt><i>%.chr0, ..., %.chr31</i></dt>
<dd> <p> ASCII 0..31 control characters (e.g., %.chr7 is bell and %.chr12 is form feed character). </p>
 </dd></dl>
<p> For example, the following action list assigns the current time in human readable format and the content of the $0 match variable to the %text action list variable, and mails the value of %text to root [at] localhost: </p>
<p> action=assign %text %t: $0; pipe &#8216;%text&#8217; /bin/mail root [at] localhost </p>
<p> If the action list is executed at Nov 19 10:58:51 2015 and the $0 match variable has the value &quot;This is a test event&quot;, the <i>assign</i> action sets the %text action list variable to the string &quot;Thu Nov 19 10:58:51 2015: This is a test event&quot;, while the <i>pipe</i> action mails this string to root [at] localhost. Note that unlike match variables, action list variables have a global scope, and accessing the value of the %text variable in action lists of other rules will thus yield the string &quot;Thu Nov 19 10:58:51 2015: This is a test event&quot; (until another value is assigned to %text). </p>
<p> In order to disambiguate the variable from the following text, the variable name must be enclosed in braces. For example, the following action </p>
<p> action=write - %{.year}-%{.mon}-%{.mday}T%{.hmsstr}%{.tzoff2} </p>
<p> writes a timestamp in ISO 8601 format to standard output, e.g., 2016-02-24T07:34:01+02:00 (replacing %{.mday} with %.mday in the above action would mistakenly create a reference to %.mdayT variable). </p>
<p> When action list variables are substituted with their values, each sequence &quot;%%&quot; is interpreted as a literal percent sign (%) which allows for masking the variables. For example, the string &quot;s%%t&quot; becomes &quot;s%t&quot; after substitution, not &quot;s%&lt;timestamp&gt;&quot;. </p>
<p> However, note that if %-prefixed match variables are supported for the <i>action2</i> field of the Pair or PairWithWindow rule, the sequence &quot;%%%&quot; must be used in <i>action2</i> for masking a variable, since the string goes through *two* variable substitution rounds (first for %-prefixed match variables and then for action list variables, e.g., the string &quot;s%%%t&quot; first becomes &quot;s%%t&quot; and finally &quot;s%t&quot;). </p>
<p> Whenever a rule field goes through several substitution rounds, the $ or % characters are masked inside values substituted during earlier rounds, in order to avoid unwanted side effects during later rounds. </p>
<p> If the action list variable has not been set, it is substituted with an empty string (i.e., a zero-width string). Thus the string &quot;Value of A is: %a&quot; becomes &quot;Value of A is: &quot; after substitution if the variable %a is unset. (Note that prior to SEC-2.6, unset variables were *not* substituted.) </p>
<p> Finally, the values are substituted as strings, therefore values of other types (e.g., references) lose their original meaning, unless explicitly noted otherwise (e.g., if a Perl function reference is stored to an action list variable, the function can later be invoked through this variable with the <i>call</i> action). </p>
<p> SEC supports the following actions (optional parameters are enclosed in square brackets): </p>
<dl>
<dt><i>none</i></dt>
<dd> <p> No action. </p>
 </dd>
<dt><i>logonly [&lt;string&gt;]</i></dt>
<dd> <p> Message &lt;string&gt; is logged to destinations given with the <code>--log</code> and <code>--syslog</code> options. The level of the log message is set to 4 (see the <code>--debug</code> option for more information on log message levels). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>write &lt;filename&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; with a terminating newline is written to the file &lt;filename&gt; (&lt;filename&gt; may not contain whitespace). File may be a regular file, named pipe, or standard output (denoted by <code>-</code>). If the file is a regular file, &lt;string&gt; is appended to the end of the file. If the file does not exist, it is created as a regular file before writing. Note that the file will not be closed after the action completes, and the following <i>write</i> actions will access an already open file. However, several signals cause the file to be closed and reopened (see SIGNALS section for more information). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>writen &lt;filename&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>write</i> action, except that the string &lt;string&gt; is written without a terminating newline. Note that <i>write</i> and <i>writen</i> actions share the same filehandle for accessing the file. </p>
 </dd>
<dt><i>closef &lt;filename&gt;</i></dt>
<dd> <p> Close the file &lt;filename&gt; that has been previously opened by the <i>write</i> or <i>writen</i> action (&lt;filename&gt; may not contain whitespace). </p>
 </dd>
<dt><i>owritecl &lt;filename&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>write </i> action, except that the file &lt;filename&gt; is opened and closed at each write. Also, the string &lt;string&gt; is written without a terminating newline. If the file has already been opened by a previous <i>write</i> action, <i>owritecl</i> does not use existing filehandle, but opens and closes the file separately. </p>
 </dd>
<dt><i>udgram &lt;filename&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; is written to the UNIX datagram socket &lt;filename&gt; (&lt;filename&gt; may not contain whitespace). Note that the socket will not be closed after the action completes, and the following <i>udgram</i> actions will access an already open socket. However, several signals cause the socket to be closed and reopened (see SIGNALS section for more information). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>closeudgr &lt;filename&gt;</i></dt>
<dd> <p> Close the UNIX datagram socket &lt;filename&gt; that has been previously opened by the <i>udgram</i> action (&lt;filename&gt; may not contain whitespace). </p>
 </dd>
<dt><i>ustream &lt;filename&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; is written to the UNIX stream socket &lt;filename&gt; (&lt;filename&gt; may not contain whitespace). Note that the socket will not be closed after the action completes, and the following <i>ustream</i> actions will access an already open socket. However, several signals cause the socket to be closed and reopened (see SIGNALS section for more information). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>closeustr &lt;filename&gt;</i></dt>
<dd> <p> Close the UNIX stream socket &lt;filename&gt; that has been previously opened by the <i>ustream</i> action (&lt;filename&gt; may not contain whitespace). </p>
 </dd>
<dt><i>udpsock &lt;host&gt;:&lt;port&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; is sent to the UDP port &lt;port&gt; of the host &lt;host&gt;. Note that the UDP socket which is used for communication will not be closed after the action completes, and the following <i>udpsock</i> actions for the same remote peer will use an already existing socket. However, several signals cause the socket to be closed and recreated (see SIGNALS section for more information). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>closeudp &lt;host&gt;:&lt;port&gt;</i></dt>
<dd> <p> Close the UDP socket for peer &lt;host&gt;:&lt;port&gt; that has been previously opened by the <i>udpsock</i> action. </p>
 </dd>
<dt><i>tcpsock &lt;host&gt;:&lt;port&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; is sent to the TCP port &lt;port&gt; of the host &lt;host&gt;. The timeout value given with the <code>--socket-timeout</code> option determines for how many seconds SEC will attempt to establish a connection to the remote peer. If the connection establishment does not succeed immediately, the <i>tcpsock</i> action buffers &lt;string&gt; in memory for later sending to the remote peer. Note that the relevant TCP socket will not be closed after &lt;string&gt; has been transmitted, and the following <i>tcpsock</i> actions for the same peer will use an already existing socket. However, several signals cause the socket to be closed and recreated (see SIGNALS section for more information). Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>closetcp &lt;host&gt;:&lt;port&gt;</i></dt>
<dd> <p> Close the TCP socket for peer &lt;host&gt;:&lt;port&gt; that has been previously opened by the <i>tcpsock</i> action. </p>
 </dd>
<dt><i>shellcmd &lt;cmdline&gt;</i></dt>
<dd> <p> Fork a process for executing command line &lt;cmdline&gt;. If the <code>--quoting</code> option was specified and &lt;cmdline&gt; contains %s variables, the value of %s is quoted with single quotes before substituting it into &lt;cmdline&gt;; if the value of %s contains single quotes, they are masked with backslashes (e.g., abc is converted to &#8216;abc&#8217; and aa&#8217;bb is converted to &#8216;aa&#8217;\&#8216;&#8216;bb&#8217;). For additional information, see INTERPROCESS COMMUNICATION section. </p>
 </dd>
<dt><i>spawn &lt;cmdline&gt;</i></dt>
<dd> <p> Similar to the <i>shellcmd</i> action, except that each line from the standard output of &lt;cmdline&gt; becomes a synthetic event and will be treated like a line from input file (see the <i>event</i> action for more information). If the <code>--intcontexts</code> command line option is given, internal context _INTERNAL_EVENT is set up before each synthetic event is processed (see INTERNAL EVENTS AND CONTEXTS section for more information). </p>
 </dd>
<dt><i>cspawn &lt;name&gt; &lt;cmdline&gt;</i></dt>
<dd> <p> Similar to the <i>spawn</i> action, except that if the <code>--intcontexts</code> command line option is given, internal context &lt;name&gt; is set up for each synthetic event. </p>
 </dd>
<dt><i>pipe &#8216;[&lt;string&gt;]&#8216; [&lt;cmdline&gt;]</i></dt>
<dd> <p> Fork a process for executing command line &lt;cmdline&gt;. The string &lt;string&gt; with a terminating newline is written to the standard input of &lt;cmdline&gt; (single quotes are used for disambiguating &lt;string&gt; from &lt;cmdline&gt;). If &lt;string&gt; contains semicolons, &lt;string&gt; must be enclosed in parentheses (e.g., <i>pipe &#8216;($1;$2)&#8216; /bin/cat</i>). Default value for &lt;string&gt; is %s. If &lt;cmdline&gt; is omitted, &lt;string&gt; is written to standard output. For additional information, see INTERPROCESS COMMUNICATION section. </p>
 </dd>
<dt><i>create [&lt;name&gt; [&lt;time&gt; [&lt;action list&gt;] ] ]</i></dt>
<dd> <p> Create a context with the name &lt;name&gt;, lifetime of &lt;time&gt; seconds, and empty event store. The &lt;name&gt; parameter may not contain whitespace and defaults to %s. The &lt;time&gt; parameter must evaluate to an unsigned integer at runtime. Specifying 0 for &lt;time&gt; or omitting the value means infinite lifetime. If &lt;action list&gt; is given, it will be executed when the context expires. If &lt;action list&gt; contains several actions, the list must be enclosed in parentheses. In &lt;action list&gt;, the internal context name _THIS may be used for referring to the current context (see INTERNAL EVENTS AND CONTEXTS section for a detailed discussion). If an already existing context is recreated with <i>create</i>, its remaining lifetime is set to &lt;time&gt; seconds, its action list is reinitialized, and its event store is emptied. </p>
 </dd>
<dt><i>delete [&lt;name&gt;]</i></dt>
<dd> <p> Delete the context &lt;name&gt;. The &lt;name&gt; parameter may not contain whitespace and defaults to %s. </p>
 </dd>
<dt><i>obsolete [&lt;name&gt;]</i></dt>
<dd> <p> Similar to the <i>delete </i> action, except that the action list of the context &lt;name&gt; (if present) is executed before deletion. </p>
 </dd>
<dt><i>set &lt;name&gt; &lt;time&gt; [&lt;action list&gt;]</i></dt>
<dd> <p> Change settings for the context &lt;name&gt;. The creation time of the context is set to the current time, and the lifetime of the context is set to &lt;time&gt; seconds. If the &lt;action list&gt; parameter is given, the context action list is set to &lt;action list&gt;. The &lt;name&gt; parameter may not contain whitespace and defaults to %s. The &lt;time&gt; parameter must evaluate to an unsigned integer or hyphen (-) at runtime. Specifying 0 for &lt;time&gt; means infinite lifetime. If &lt;time&gt; equals to -, the creation time and lifetime of the context are not changed. If &lt;action list&gt; contains several actions, the list must be enclosed in parentheses. In &lt;action list&gt;, the internal context name _THIS may be used for referring to the current context (see INTERNAL EVENTS AND CONTEXTS section for a detailed discussion). </p>
 </dd>
<dt><i>alias &lt;name&gt; [&lt;alias&gt;]</i></dt>
<dd> <p> Create an alias name &lt;alias&gt; for the context &lt;name&gt;. After creation, both &lt;alias&gt; and &lt;name&gt; will point to the same context data structure, and can thus be used interchangeably for referring to the context. The &lt;name&gt; and &lt;alias&gt; parameters may not contain whitespace, and &lt;alias&gt; defaults to %s. If the context &lt;name&gt; does not exist, the alias name is not created. If the <i>delete</i> action is called for one of the context names, the context data structure is destroyed, and all context names (which are now pointers to unallocated memory) cease to exist. Also note that when the context expires, its action list is executed only once, no matter how many names the context has. </p>
 </dd>
<dt><i>unalias [&lt;alias&gt;]</i></dt>
<dd> <p> Drop an existing context name &lt;alias&gt;, so that it can no longer be used for referring to the given context. The &lt;alias&gt; parameter may not contain whitespace and defaults to %s. If the name &lt;alias&gt; is the last reference to the context, the <i>unalias</i> action is identical to <i>delete</i>. </p>
 </dd>
<dt><i>add &lt;name&gt; [&lt;string&gt;]</i></dt>
<dd> <p> String &lt;string&gt; is appended to the end of the event store of the context &lt;name&gt;. The &lt;name&gt; parameter may not contain whitespace, and the &lt;string&gt; parameter defaults to %s. If the context &lt;name&gt; does not exist, the context is created with an infinite lifetime, empty action list and empty event store (as with <i>create &lt;name&gt;</i>) before adding the string to event store. If &lt;string&gt; is a multi-line string (i.e., it contains newlines), it is split into lines, and each line is appended to the event store separately. </p>
 </dd>
<dt><i>prepend &lt;name&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>add </i> action, except that the string &lt;string&gt; is prepended to the beginning of the event store of context &lt;name&gt;. </p>
 </dd>
<dt><i>fill &lt;name&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>add </i> action, except that the event store of the context &lt;name&gt; is emptied before &lt;string&gt; is added. </p>
 </dd>
<dt><i>report &lt;name&gt; [&lt;cmdline&gt;]</i></dt>
<dd> <p> Fork a process for executing command line &lt;cmdline&gt;, and write strings from the event store of the context &lt;name&gt; to the standard input of &lt;cmdline&gt;. Strings are written in the order they appear in the event store, with a terminating newline appended to each string. If the context &lt;name&gt; does not exist or its event store is empty, &lt;cmdline&gt; is not executed. The &lt;name&gt; parameter may not contain whitespace, and if &lt;cmdline&gt; is omitted, strings are written to standard output. For additional information, see INTERPROCESS COMMUNICATION section. </p>
 </dd>
<dt><i>copy &lt;name&gt; %&lt;var&gt;</i></dt>
<dd> <p> Strings s1,...,sn from the event store of the context &lt;name&gt; are joined into a multi-line string &quot;s1&lt;NEWLINE&gt;...&lt;NEWLINE&gt;sn&quot;, and this string is assigned to the action list variable %&lt;var&gt;. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>empty &lt;name&gt; [%&lt;var&gt;]</i></dt>
<dd> <p> Similar to the <i>copy</i> action, except that the event store of the context &lt;name&gt; will be emptied after the assignment. If %&lt;var&gt; is omitted, the content of the event store is dropped without an assignment. </p>
 </dd>
<dt><i>pop &lt;name&gt; %&lt;var&gt;</i></dt>
<dd> <p> Remove the last string from the event store of context &lt;name&gt;, and assign it to the action list variable %&lt;var&gt;. If the event store is empty, %&lt;var&gt; is set to empty string. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>shift &lt;name&gt; %&lt;var&gt;</i></dt>
<dd> <p> Remove the first string from the event store of context &lt;name&gt;, and assign it to the action list variable %&lt;var&gt;. If the event store is empty, %&lt;var&gt; is set to empty string. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>exists %&lt;var&gt; &lt;name&gt;</i></dt>
<dd> <p> If the context &lt;name&gt; exists, set the action list variable %&lt;var&gt; to 1, otherwise set %&lt;var&gt; to 0. </p>
 </dd>
<dt><i>getsize %&lt;var&gt; &lt;name&gt;</i></dt>
<dd> <p> Find the number of strings in the event store of context &lt;name&gt;, and assign this number to the action list variable %&lt;var&gt;. If the context &lt;name&gt; does not exist, %&lt;var&gt; is set to Perl undefined value. </p>
 </dd>
<dt><i>getaliases %&lt;var&gt; &lt;name&gt;</i></dt>
<dd> <p> Find all alias names for context &lt;name&gt;, join the names into a multi-line string &quot;alias1&lt;NEWLINE&gt;...&lt;NEWLINE&gt;aliasn&quot;, and assign this string to the action list variable %&lt;var&gt;. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>getltime %&lt;var&gt; &lt;name&gt;</i></dt>
<dd> <p> Find the lifetime of context &lt;name&gt;, and assign this number to the action list variable %&lt;var&gt;. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>getctime %&lt;var&gt; &lt;name&gt;</i></dt>
<dd> <p> Find the creation time of context &lt;name&gt;, and assign this number to the action list variable %&lt;var&gt;. If the context &lt;name&gt; does not exist, the value of %&lt;var&gt; does not change. </p>
 </dd>
<dt><i>setctime &lt;time&gt; &lt;name&gt;</i></dt>
<dd> <p> Set the creation time of context &lt;name&gt; to &lt;time&gt;. The &lt;time&gt; parameter must evaluate to seconds since Epoch (as reported by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call), and must reflect a time moment between the previous creation time and the current time (both endpoints included). </p>
 </dd>
<dt><i>event [&lt;time&gt;] [&lt;string&gt;]</i></dt>
<dd> <p> After &lt;time&gt; seconds, create a synthetic event &lt;string&gt;. If &lt;string&gt; is a multi-line string (i.e., it contains newlines), it is split into lines, and from each line a separate synthetic event is created. SEC will treat each synthetic event like a line from an input file -- the event will be matched against rules and it might trigger further actions. If the <code>--intcontexts </code> command line option is given, internal context _INTERNAL_EVENT is set up for synthetic event(s) (see INTERNAL EVENTS AND CONTEXTS section for more information). The &lt;time&gt; parameter is an integer constant. Specifying 0 for &lt;time&gt; or omitting the value means &quot;now&quot;. Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>tevent &lt;time&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>event</i> action, except that the &lt;time&gt; parameter may contain variables and must evaluate to an unsigned integer at runtime. </p>
 </dd>
<dt><i>cevent &lt;name&gt; &lt;time&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>tevent</i> action, except that if the <code>--intcontexts </code> command line option is given, internal context &lt;name&gt; is set up for synthetic event(s). </p>
 </dd>
<dt><i>reset [&lt;offset&gt;] [&lt;string&gt;]</i></dt>
<dd> <p> Terminate event correlation operation(s) with the operation description string &lt;string&gt;. Note that the <i>reset</i> action works only for operations started from the same configuration file. The &lt;offset&gt; parameter is used to refer to a specific rule in the configuration file. If &lt;offset&gt; is given, the operation started by the given rule is terminated (if it exists). If &lt;offset&gt; is an unsigned integer N, it refers to the N-th rule in the configuration file. If &lt;offset&gt; is 0, it refers to the current rule. If &lt;offset&gt; begins with the plus (+) or minus (-) sign, it specifies an offset from the current rule (e.g., -1 denotes the previous and +1 the next rule). Note that since Options rules are only processed when configuration files are loaded and they are not applied at runtime, Options rules are excluded when calculating &lt;offset&gt;. If &lt;offset&gt; is not given, SEC checks for each rule from the current configuration file if an operation with &lt;string&gt; has been started by this rule, and the operation is terminated if it exists. Default value for &lt;string&gt; is %s. For additional information, see EVENT CORRELATION OPERATIONS section. </p>
 </dd>
<dt><i>getwpos %&lt;var&gt; &lt;offset&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Find the beginning of the event correlation window for an event correlation operation, and set the action list variable %&lt;var&gt; to this timestamp. The value assigned to %&lt;var&gt; is measured in seconds since Epoch (as reported by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call). As with the <i>reset</i> action, the event correlation operation is identified by the operation description string &lt;string&gt; and the rule offset &lt;offset&gt;. If the operation does not exist, the value of %&lt;var&gt; does not change. Default value for &lt;string&gt; is %s. For additional information, see EVENT CORRELATION OPERATIONS section. </p>
 </dd>
<dt><i>setwpos &lt;time&gt; &lt;offset&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Set the beginning of the event correlation window to &lt;time&gt; for an event correlation operation (if it exists). The &lt;time&gt; parameter must evaluate to seconds since Epoch (as reported by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call), and must reflect a time moment between the previous window position and the current time (both endpoints included). As with the <i>reset</i> action, the event correlation operation is identified by the operation description string &lt;string&gt; and the rule offset &lt;offset&gt;. Default value for &lt;string&gt; is %s. For additional information, see EVENT CORRELATION OPERATIONS section. </p>
 </dd>
<dt><i>assign %&lt;var&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Assign string &lt;string&gt; to the action list variable %&lt;var&gt;. Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>assignsq %&lt;var&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Similar to the <i>assign</i> action, except that &lt;string&gt; is quoted with single quotes before assigning it to %&lt;var&gt;. If &lt;string&gt; contains single quotes, they are masked with backslashes (e.g., if the match variable $1 holds the value abc&#8217;123&#8217;xyz, the action <i>assignsq %myvar $1</i> assigns the value &#8216;abc&#8217;\&#8216;&#8216;123&#8217;\&#8216;&#8216;xyz&#8217; to the action list variable %myvar). This action is useful for disabling shell intepretation for the values of action list variables that appear in command lines executed by SEC. Default value for &lt;string&gt; is %s. </p>
 </dd>
<dt><i>free %&lt;var&gt;</i></dt>
<dd> <p> Unset the action list variable %&lt;var&gt;. </p>
 </dd>
<dt><i>eval %&lt;var&gt; &lt;code&gt;</i></dt>
<dd> <p> The parameter &lt;code&gt; is a Perl miniprogram that is compiled and executed by calling the Perl <code>eval</code>() function in the Perl list context. If the miniprogram returns a single value, it is assigned to the action list variable %&lt;var&gt;. If the miniprogram returns several values s1,...,sn, they are joined into a multi-line string &quot;s1&lt;NEWLINE&gt;...&lt;NEWLINE&gt;sn&quot;, and this string is assigned to %&lt;var&gt;. If no value is returned, %&lt;var&gt; is set to Perl undefined value. If <code>eval</code>() fails, the value of %&lt;var&gt; does not change. Since most Perl programs contain semicolons which are also employed by SEC as action separators, it is recommended to enclose the &lt;code&gt; parameter in parentheses, in order to mask the semicolons in &lt;code&gt;. For additional information, see PERL INTEGRATION section. </p>
 </dd>
<dt><i>call %&lt;var&gt; %&lt;ref&gt; [&lt;paramlist&gt;]</i></dt>
<dd> <p> Call the precompiled Perl function referenced by the action list variable %&lt;ref&gt;, and assign the result to the action list variable %&lt;var&gt;. The %&lt;ref&gt; parameter must be a code reference that has been previously created with the <i>eval</i> action. The &lt;paramlist&gt; parameter (if given) is a string which specifies parameters for the function. The parameters must be separated by whitespace in the &lt;paramlist&gt; string. If the function returns a single value, it is assigned to %&lt;var&gt;. If the function returns several values s1,...,sn, they are joined into a multi-line string &quot;s1&lt;NEWLINE&gt;...&lt;NEWLINE&gt;sn&quot;, and this string is assigned to %&lt;var&gt;. If no value is returned, %&lt;var&gt; is set to Perl undefined value. If the function encounters a fatal runtime error or %&lt;ref&gt; is not a code reference, the value of %&lt;var&gt; does not change. For additional information, see PERL INTEGRATION section. </p>
 </dd>
<dt><i>lcall %&lt;var&gt; [&lt;paramlist&gt;] -&gt; &lt;code&gt;</i></dt>
<dd> <p> Call the precompiled Perl function &lt;code&gt; and assign the result to the action list variable %&lt;var&gt;. The &lt;code&gt; parameter must be a valid Perl function definition that is compiled at SEC startup with the Perl <code>eval</code>() function, and <code>eval</code>() must return a code reference. The &lt;paramlist&gt; parameter (if given) is a string which specifies parameters for the function. The parameters must be separated by whitespace in the &lt;paramlist&gt; string. If the function returns a single value, it is assigned to %&lt;var&gt;. If the function returns several values s1,...,sn, they are joined into a multi-line string &quot;s1&lt;NEWLINE&gt;...&lt;NEWLINE&gt;sn&quot;, and this string is assigned to %&lt;var&gt;. If no value is returned, %&lt;var&gt; is set to Perl undefined value. If the function encounters a fatal runtime error, the value of %&lt;var&gt; does not change. Since most Perl functions contain semicolons which are also employed by SEC as action separators, it is recommended to enclose the &lt;code&gt; parameter in parentheses, in order to mask the semicolons in &lt;code&gt;. For additional information, see PERL INTEGRATION section. </p>
 </dd>
<dt><i>rewrite &lt;lnum&gt; [&lt;string&gt;]</i></dt>
<dd> <p> Replace last &lt;lnum&gt; lines in the input buffer with string &lt;string&gt;. If the <code>--nojointbuf </code> option was specified and the action is triggered by a matching event, the action modifies the buffer which holds this event. If the <code>--nojointbuf </code> option was specified and the action is triggered by the system clock (e.g., the action is executed from the Calendar rule), the action modifies the buffer which holds the last already processed event. With the <code>--jointbuf </code> option, the content of the joint input buffer is rewritten. The &lt;lnum&gt; parameter must evaluate to an unsigned integer at runtime. If &lt;lnum&gt; evaluates to 0, &lt;lnum&gt; is reset to the number of lines in &lt;string&gt;. If the value of &lt;lnum&gt; is greater than the buffer size N, &lt;lnum&gt; is reset to N. If &lt;string&gt; contains less than &lt;lnum&gt; lines, &lt;string&gt; will be padded with leading empty lines. If &lt;string&gt; contains more than &lt;lnum&gt; lines, only leading &lt;lnum&gt; lines from &lt;string&gt; are written into the buffer. Default value for &lt;string&gt; is %s. For additional information, see INPUT PROCESSING AND TIMING section. </p>
 </dd>
<dt><i>if %&lt;var&gt; ( &lt;action list&gt; ) [ else ( &lt;action list2&gt; ) ]</i></dt>
<dd> <p> If the action list variable %&lt;var&gt; evaluates true in the Perl boolean context (i.e., it holds a defined value which is neither 0 nor empty string), execute the action list &lt;action list&gt;. If the second action list &lt;action list2&gt; is given with the optional else-statement, it is executed if %&lt;var&gt; either does not exist or evaluates false (i.e., %&lt;var&gt; holds 0, empty string or Perl undefined value). </p>
 </dd>
<dt><i>while %&lt;var&gt; ( &lt;action list&gt; )</i></dt>
<dd> <p> Execute the action list &lt;action list&gt; repeatedly as long as the action list variable %&lt;var&gt; evaluates true in the Perl boolean context (i.e., it holds a defined value which is neither 0 nor empty string). </p>
 </dd>
<dt><i>break</i></dt>
<dd> <p> If used inside a while-loop, terminates its execution; otherwise terminates the execution of the entire action list. </p>
 </dd>
<dt><i>continue</i></dt>
<dd> <p> If used inside a while-loop, starts the next iteration of the loop; otherwise terminates the execution of the entire action list. </p>
 </dd></dl>
<p> <code>Examples:</code> </p>
<p> Follow the /var/log/trapd.log file and feed to SEC input all lines that are appended to the file: </p>
<p> action=spawn /bin/tail -f /var/log/trapd.log </p>
<p> Mail the timestamp and the value of the $0 variable to the local root: </p>
<p> action=pipe &#8216;%t: $0&#8217; /bin/mail -s &quot;alert message&quot; root [at] localhost </p>
<p> Add the value of the $0 variable to the event store of the context <code>ftp_&lt;the value of $1&gt;</code>, and set the context to expire after 30 minutes. When the context expires, its event store will be mailed to the local root: </p>
<p> action=add ftp_$1 $0; \ <br />
&nbsp;<wbr>set ftp_$1 1800&nbsp;<wbr>(report ftp_$1&nbsp;<wbr>/bin/mail root [at] localhost) </p>
<p> Create a subroutine for weeding out comment lines from the input list, and use this subroutine for removing comment lines from the event store of the context <code>C1</code>: </p>
<p> action=eval %funcptr ( sub { my(@buf) = split(/\n/, $_[0]); \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>my(@ret)&nbsp;<wbr>=&nbsp;<wbr>grep(!/^#/,&nbsp;<wbr>@buf);&nbsp;<wbr>return&nbsp;<wbr>@ret;&nbsp;<wbr>}&nbsp;<wbr>);&nbsp;<wbr>\ <br />
&nbsp;<wbr>copy C1&nbsp;<wbr>%in;&nbsp;<wbr>call&nbsp;<wbr>%out&nbsp;<wbr>%funcptr&nbsp;<wbr>%in;&nbsp;<wbr>fill C1&nbsp;<wbr>%out </p>
<p> The following action list achieves the same goal as the previous action list with <i>while </i> and <i>if </i> actions: </p>
<p> action=getsize %size C1; while %size ( shift C1 %event; \ <br />
&nbsp;<wbr>lcall&nbsp;<wbr>%nocomment&nbsp;<wbr>%event -&gt;&nbsp;<wbr>(&nbsp;<wbr>sub&nbsp;<wbr>{&nbsp;<wbr>$_[0]&nbsp;<wbr>!~&nbsp;<wbr>/^#/&nbsp;<wbr>}&nbsp;<wbr>);&nbsp;<wbr>\ <br />
&nbsp;<wbr>if&nbsp;<wbr>%nocomment&nbsp;<wbr>(&nbsp;<wbr>add C1&nbsp;<wbr>%event&nbsp;<wbr>);&nbsp;<wbr>\ <br />
&nbsp;<wbr>lcall&nbsp;<wbr>%size&nbsp;<wbr>%size -&gt;&nbsp;<wbr>(&nbsp;<wbr>sub&nbsp;<wbr>{&nbsp;<wbr>$_[0]-1;&nbsp;<wbr>}&nbsp;<wbr>)&nbsp;<wbr>)  </p>
<h2>PARSING ISSUES</h2>
<p> As already noted, SEC context expressions and action lists may contain parentheses which are used for grouping and masking purposes. When SEC parses its configuration, it checks whether parentheses in context expressions and action lists are balanced (i.e., whether each parenthesis has a counterpart), since unbalanced parentheses introduce ambiguity. This can cause SEC to reject some legitimate constructs, e.g., </p>
<p> action=eval %o (print &quot;)&quot;;) </p>
<p> is considered an invalid action list (however, note that <br />
 action=eval %o (print &quot;()&quot;;) <br />
 would be passed by SEC, since now parentheses are balanced). In order to avoid such parsing errors, each parenthesis without a counterpart must be masked with a backslash (the backslash will be removed by SEC during configuration file parsing). For example, the above action could be written as </p>
<p> action=eval %o (print &quot;\)&quot;;)  </p>
<h2>RULE TYPES</h2>
<p> This section provides a detailed discussion of SEC rule types.  </p>
<h3>SINGLE RULE</h3>
<p> The <code>Single</code> rule immediately executes an action list when an event has matched the rule. An event matches the rule if the pattern matches the event and the context expression (if given) evaluates TRUE. </p>
<p> The Single rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Single (value is case insensitive, so single or sIngLe can be used instead). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, and <i>action</i> fields. Also note that this rule does not start an event correlation operation, and the <i>desc</i> field is merely used for setting the %s action list variable. </p>
<p> <code>Examples:</code> </p>
<p> type=single <br />
 continue=takenext <br />
 ptype=regexp <br />
 pattern=ftpd\[(\d+)\]: \S+ \(ristov2.*FTP session opened <br />
 desc=ftp session opened for ristov2 pid $1 <br />
 action=create ftp_$1 </p>
<p> type=single <br />
 continue=takenext <br />
 ptype=regexp <br />
 pattern=ftpd\[(\d+)\]: <br />
 context=ftp_$1 <br />
 desc=ftp session event for ristov2 pid $1 <br />
 action=add ftp_$1 $0; set ftp_$1 1800 \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(report ftp_$1&nbsp;<wbr>/bin/mail root [at] localhost) </p>
<p> type=single <br />
 ptype=regexp <br />
 pattern=ftpd\[(\d+)\]: \S+ \(ristov2.*FTP session closed <br />
 desc=ftp session closed for ristov2 pid $1 <br />
 action=report ftp_$1 /bin/mail root [at] localhost; \ <br />
&nbsp;<wbr>delete ftp_$1 </p>
<p> This ruleset is created for monitoring the ftpd log file. The first rule creates the context <code>ftp_&lt;pid&gt;</code> when someone connects from host ristov2 over FTP and establishes a new ftp session (the session is identified by the PID of the process which has been created for handling this session). The second rule adds all further log file lines for the session &lt;pid&gt; to the event store of the context <code>ftp_&lt;pid&gt; </code> (before adding a line, the rule checks if the context exists). After adding a line, the rule extends context&#8217;s lifetime for 30 minutes and sets the action list that will be executed when the context expires. The third rule mails collected log file lines to root [at] localhost when the session &lt;pid&gt; is closed. Collected lines will also be mailed when the session &lt;pid&gt; has been inactive for 30 minutes (no log file lines observed for that session). </p>
<p> Note that the log file line that has matched the first rule is also matched against the second rule (since the first rule has the <i>continue</i> field set to TakeNext). Since the second rule always matches this line, it will become the first line in the event store of <code>ftp_&lt;pid&gt;</code>. The second rule has also its <i>continue</i> field set to TakeNext, since otherwise no log file lines would reach the third rule.  </p>
<h3>SINGLEWITHSCRIPT RULE</h3>
<p> The <code>SingleWithScript</code> rule forks a process for executing an external program when an event has matched the rule. The names of all currently existing contexts are written to the standard input of the program. After the program has been forked, the rule matching continues immediately, and the program status will be checked periodically until the program exits. If the program returns 0 exit status, the action list defined by the <i>action</i> field is executed; otherwise the action list defined by the <i>action2</i> field is executed (if given). </p>
<p> The SingleWithScript rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to SingleWithScript (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>script</i></dt>
<dd> <p> an external program. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>action2</i> (optional) </dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>script</i>, <i>desc</i>, <i>action</i>, and <i>action2</i> fields. Also note that this rule does not start an event correlation operation, and the <i>desc</i> field is merely used for setting the %s action list variable. </p>
<p> <code>Examples:</code> </p>
<p> type=SingleWithScript <br />
 ptype=RegExp <br />
 pattern=interface ([\d.]+) down <br />
 script=/bin/ping -c 3 -q $1 <br />
 desc=Check if $1 responds to ping <br />
 action=logonly Interface $1 reported down, but is pingable <br />
 action2=pipe &#8216;%t: Interface $1 is down&#8217; /bin/mail root [at] localhost </p>
<p> When &quot;interface &lt;ipaddress&gt; down&quot; line appears in input, the rule checks if &lt;ipaddress&gt; responds to ping. If &lt;ipaddress&gt; is pingable, the message &quot;Interface &lt;ipaddress&gt; reported down, but is pingable&quot; is logged; otherwise an e-mail warning containing a human-readable timestamp is sent to root [at] localhost.  </p>
<h3>SINGLEWITHSUPPRESS RULE</h3>
<p> The <code>SingleWithSuppress</code> rule runs event correlation operations for filtering repeated instances of the same event during T seconds. The value of T is defined by the <i>window</i> field. </p>
<p> When an event has matched the rule, SEC evaluates the operation description string given with the <i>desc</i> field. If the operation for the given string and rule does not exist, SEC will create it with the lifetime of T seconds, and the operation immediately executes an action list. If the operation exists, it consumes the matching event without any action. </p>
<p> The SingleWithSuppress rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to SingleWithSuppress (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, and <i>action</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> type=SingleWithSuppress <br />
 ptype=RegExp <br />
 pattern=(\S+): [fF]ile system full <br />
 desc=File system $1 full <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=900 </p>
<p> This rule runs event correlation operations for processing &quot;file system full&quot; syslog messages, e.g., </p>
<p> Dec 16 14:26:09 test ufs: [ID 845546 kern.notice] NOTICE: alloc: /var: file system full </p>
<p> When the first message for a file system is observed, an operation is created which sends an e-mail warning about this file system to root [at] localhost. The operation will then run for 900 seconds and silently consume further messages for the *same* file system. However, if a message for a different file system is observed, another operation will be started which sends a warning to root [at] localhost again (since the <i>desc</i> field contains the $1 match variable which evaluates to the file system name).  </p>
<h3>PAIR RULE</h3>
<p> The <code>Pair</code> rule runs event correlation operations for processing event pairs during T seconds. The value of T is defined by the <i>window</i> field. Default value is 0 which means infinity. </p>
<p> When an event has matched the conditions defined by the <i>pattern</i> and <i>context</i> field, SEC evaluates the operation description string given with the <i>desc</i> field. If the operation for the given string and rule exists, it consumes the matching event without any action. If the operation does not exist, SEC will create it with the lifetime of T seconds, and the operation immediately executes an action list defined by the <i>action</i> field. SEC will also copy the match conditions given with the <i>pattern2</i> and <i>context2</i> field into the operation, and substitute match variables with their values in copied conditions. </p>
<p> If the event does not match conditions defined by the <i>pattern</i> and <i>context</i> field, SEC will check the match conditions of all operations started by the given rule. Each matching operation executes the action list given with the <i>action2</i> field and finishes. </p>
<p> If match variables are set when the operation matches an event, they are made available as $-prefixed match variables in <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields of the rule definition. For example, if <i>pattern2</i> field is a regular expression, then $1 in the <i>desc2</i> field is set by <i>pattern2</i>. In order to access match variables set by <i>pattern</i>, %-prefixed match variables have to be used in <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields. For example, if <i>pattern</i> and <i>pattern2</i> are regular expressions, then %1 in the <i>desc2</i> field refers to the value set by the first capture group in <i>pattern</i> (i.e., it has the same value as $1 in the <i>desc</i> field). </p>
<p> The Pair rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Pair (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>pattern</i> and <i>context</i>. </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type for <i>pattern</i> (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map for <i>pattern</i>. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>pattern</i>. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>continue2</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>pattern2</i> and <i>context2</i>. </p>
 </dd>
<dt><i>ptype2</i></dt>
<dd> <p> pattern type for <i>pattern2</i> (value is case insensitive). </p>
 </dd>
<dt><i>pattern2</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap2</i> (optional) </dt>
<dd> <p> variable map for <i>pattern2</i>. </p>
 </dd>
<dt><i>context2</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>pattern2</i>. </p>
 </dd>
<dt><i>desc2</i></dt>
<dd> <p> format string that sets the %s variable for <i>action2</i>. </p>
 </dd>
<dt><i>action2</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window</i> (optional) </dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, <i>action</i>, <i>pattern2</i>, <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> type=Pair <br />
 ptype=RegExp <br />
 pattern=kernel: nfs: server (\S+) not responding, still trying <br />
 desc=Server $1 is not responding <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 ptype2=SubStr <br />
 pattern2=kernel: nfs: server $1 OK <br />
 desc2=Server $1 is responding again <br />
 action2=logonly <br />
 window=3600 </p>
<p> This rule runs event correlation operations for processing NFS &quot;server not responding&quot; and &quot;server OK&quot; syslog messages, e.g., </p>
<p> Dec 18 22:39:48 test kernel: nfs: server box1 not responding, still trying <br />
 Dec 18 22:42:27 test kernel: nfs: server box1 OK </p>
<p> When the &quot;server not responding&quot; message for an NFS server is observed, an operation is created for this server which sends an e-mail warning about the server to root [at] localhost. The operation will then run for 3600 seconds and silently consume further &quot;server not responding&quot; messages for the same server. If this operation observes &quot;server OK&quot; message for the *same* server, it will log the message &quot;Server &lt;servername&gt; is responding again&quot; and finish. </p>
<p> For example, if SEC observes the following event at 22:39:48 </p>
<p> Dec 18 22:39:48 test kernel: nfs: server box1 not responding, still trying </p>
<p> an event correlation operation is created for server box1 which issues an e-mail warning about this server immediately. After that, the operation will run for 3600 seconds (until 23:39:48), waiting for an event which would contain the substring &quot;kernel: nfs: server box1 OK&quot; (because the <i>pattern2</i> field contains the $1 match variable which evaluates to the server name). </p>
<p> If any further error messages appear for server box1 during the 3600 second lifetime of the operation, e.g., </p>
<p> Dec 18 22:40:28 test kernel: nfs: server box1 not responding, still trying <br />
 Dec 18 22:41:09 test kernel: nfs: server box1 not responding, still trying </p>
<p> these messages will be silently consumed by the operation. If before its expiration the operation observes an event which contains the substring &quot;kernel: nfs: server box1 OK&quot;, e.g., </p>
<p> Dec 18 22:42:27 test kernel: nfs: server box1 OK </p>
<p> the operation will log the message &quot;Server box1 is responding again&quot; and terminate immediately. If no such message appears during the 3600 second lifetime of the operation, the operation will expire without taking any action. Please note that if the <i>window</i> field would be either removed from the rule definition or set to 0, the operation would never silently expire, but would terminate only after observing an event which contains the substring &quot;kernel: nfs: server box1 OK&quot;. </p>
<p> If the above rule is modified in the following way </p>
<p> type=Pair <br />
 ptype=RegExp <br />
 pattern=^([[:alnum:]: ]+) \S+ kernel: nfs: server (\S+) not responding, still trying <br />
 desc=Server $2 is not responding <br />
 action=logonly <br />
 ptype2=RegExp <br />
 pattern2=^([[:alnum:]: ]+) \S+ kernel: nfs: server $2 OK <br />
 desc2=Server %2 was not accessible from %1 to $1 <br />
 action2=pipe &#8216;%s&#8217; /bin/mail root [at] localhost <br />
 window=86400 </p>
<p> this rule will run event correlation operations which report NFS server downtime to root [at] localhost via e-mail, provided that downtime does not exceed 24 hours (86400 seconds). </p>
<p> For example, if SEC observes the following event </p>
<p> Dec 18 23:01:17 test kernel: nfs: server box.test not responding, still trying </p>
<p> then the rule matches this event, sets $1 match variable to &quot;Dec 18 23:01:17&quot; and $2 to &quot;box.test&quot;, and creates an event correlation operation for server box.test. This operation will start its work by logging the message &quot;Server box.test is not responding&quot;, and will then run for 86400 seconds, waiting for an event which would match the regular expression </p>
<p> ^([[:alnum:]: ]+) \S+ kernel: nfs: server box\.test OK </p>
<p> Note that this expression was created from the regular expression template in the <i>pattern2</i> field by substituting the match variable $2 with its value. However, since the string &quot;box.test&quot; contains the dot (.) character which is a regular expression metacharacter, the dot is masked with the backslash in the regular expression. </p>
<p> Suppose SEC will then observe the event </p>
<p> Dec 18 23:09:54 test kernel: nfs: server box.test OK </p>
<p> This event matches the above regular expression which is used by the operation running for server box.test. Also, the regular expression match sets the $1 variable to &quot;Dec 18 23:09:54&quot; and unsets the $2 variable. In order to refer to their original values when the operation was created, %1 and %2 match variables have to be used in the <i>desc2 </i> field (%1 equals to &quot;Dec 18 23:01:17&quot; and %2 equals to &quot;box.test&quot;). Therefore, the operation will send the e-mail message &quot;Server box.test was not accessible from Dec 18 23:01:17 to Dec 18 23:09:54&quot; to root [at] localhost, and will terminate immediately.  </p>
<h3>PAIRWITHWINDOW RULE</h3>
<p> The <code>PairWithWindow</code> rule runs event correlation operations for processing event pairs during T seconds. The value of T is defined by the <i>window</i> field. </p>
<p> When an event has matched the conditions defined by the <i>pattern</i> and <i>context</i> field, SEC evaluates the operation description string given with the <i>desc</i> field. If the operation for the given string and rule exists, it consumes the matching event without any action. If the operation does not exist, SEC will create it with the lifetime of T seconds. SEC will also copy the match conditions given with the <i>pattern2</i> and <i>context2</i> field into the operation, and substitute match variables with their values in copied conditions. </p>
<p> If the event does not match conditions defined by the <i>pattern</i> and <i>context</i> field, SEC will check the match conditions of all operations started by the given rule. Each matching operation executes the action list given with the <i>action2</i> field and finishes. If the operation has not observed a matching event by the end of its lifetime, it executes the action list given with the <i>action</i> field before finishing. </p>
<p> If match variables are set when the operation matches an event, they are made available as $-prefixed match variables in <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields of the rule definition. For example, if <i>pattern2</i> field is a regular expression, then $1 in the <i>desc2</i> field is set by <i>pattern2</i>. In order to access match variables set by <i>pattern</i>, %-prefixed match variables have to be used in <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields. For example, if <i>pattern</i> and <i>pattern2</i> are regular expressions, then %1 in the <i>desc2</i> field refers to the value set by the first capture group in <i>pattern</i> (i.e., it has the same value as $1 in the <i>desc</i> field). </p>
<p> The PairWithWindow rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to PairWithWindow (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>pattern</i> and <i>context</i>. </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type for <i>pattern</i> (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map for <i>pattern</i>. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>pattern</i>. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>continue2</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>pattern2</i> and <i>context2</i>. </p>
 </dd>
<dt><i>ptype2</i></dt>
<dd> <p> pattern type for <i>pattern2</i> (value is case insensitive). </p>
 </dd>
<dt><i>pattern2</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap2</i> (optional) </dt>
<dd> <p> variable map for <i>pattern2</i>. </p>
 </dd>
<dt><i>context2</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>pattern2</i>. </p>
 </dd>
<dt><i>desc2</i></dt>
<dd> <p> format string that sets the %s variable for <i>action2</i>. </p>
 </dd>
<dt><i>action2</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, <i>action</i>, <i>pattern2</i>, <i>context2</i>, <i>desc2</i>, and <i>action2</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> type=PairWithWindow <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from ([\d.]+) port \d+ ssh2 <br />
 desc=User $1 has been unable to log in from $2 over SSH during 1 minute <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 ptype2=RegExp <br />
 pattern2=sshd\[\d+\]: Accepted .+ for $1 from $2 port \d+ ssh2 <br />
 desc2=SSH login successful for %1 from %2 after initial failure <br />
 action2=logonly <br />
 window=60 </p>
<p> This rule runs event correlation operations for processing SSH login events, e.g., </p>
<p> Dec 27 19:00:24 test sshd[10526]: Failed password for risto from 10.1.2.7 port 52622 ssh2 <br />
 Dec 27 19:00:27 test sshd[10526]: Accepted password for risto from 10.1.2.7 port 52622 ssh2 </p>
<p> When an SSH login failure is observed for a user name and a source IP address, an operation is created for this user name and IP address combination which will expect a successful login for the *same* user name and *same* IP address during 60 seconds. If the user will not log in from the same IP address during 60 seconds, the operation will send an e-mail warning to root [at] localhost before finishing, otherwise it will log the message &quot;SSH login successful for &lt;username&gt; from &lt;ipaddress&gt; after initial failure&quot; and finish. </p>
<p> Suppose the following events are generated by an SSH daemon, and each event timestamp reflects the time SEC observes the event: </p>
<p> Dec 30 13:02:01 test sshd[30517]: Failed password for risto from 10.1.2.7 port 42172 ssh2 <br />
 Dec 30 13:02:30 test sshd[30810]: Failed password for root from 192.168.1.104 port 46125 ssh2 <br />
 Dec 30 13:02:37 test sshd[30517]: Failed password for risto from 10.1.2.7 port 42172 ssh2 <br />
 Dec 30 13:02:59 test sshd[30810]: Failed password for root from 192.168.1.104 port 46125 ssh2 <br />
 Dec 30 13:03:04 test sshd[30810]: Accepted password for root from 192.168.1.104 port 46125 ssh2 </p>
<p> When the first event is observed at 13:02:01, an operation is started for user risto and IP address 10.1.2.7 which will expect a successful login for risto from 10.1.2.7. The operation will run for 60 seconds, waiting for an event which would match the regular expression </p>
<p> sshd\[\d+\]: Accepted .+ for risto from 10\.1\.2\.7 port \d+ ssh2 </p>
<p> Note that this expression was created from the regular expression template in the <i>pattern2</i> field by substituting match variables $1 and $2 with their values. However, since the value of $2 contains the dot (.) characters which are regular expression metacharacters, each dot is masked with the backslash in the regular expression. </p>
<p> When the second event is observed at 13:02:30, another operation is started for user root and IP address 192.168.1.104 which will expect root to log in successfully from 192.168.1.104. This operation will run for 60 seconds, waiting for an event matching the regular expression </p>
<p> sshd\[\d+\]: Accepted .+ for root from 192\.168\.1\.104 port \d+ ssh2 </p>
<p> The third event at 13:02:37 represents a second login failure for user risto and IP address 10.1.2.7, and is silently consumed by the first operation. Likewise, the fourth event at 13:02:59 is silently consumed by the second operation. The first operation will run until 13:03:01 and then expire without seeing a successful login for risto from 10.1.2.7. Before terminating, the operation will send an e-mail warning to root [at] localhost that user risto has not managed to log in from 10.1.2.7 during one minute. At 13:03:04, the second operation will observe an event which matches its regular expression </p>
<p> sshd\[\d+\]: Accepted .+ for root from 192\.168\.1\.104 port \d+ ssh2 </p>
<p> After seeing this event, the operation will log the message &quot;SSH login successful for root from 192.168.1.104 after initial failure&quot; and terminate immediately. Please note that the match by the regular expression </p>
<p> sshd\[\d+\]: Accepted .+ for root from 192\.168\.1\.104 port \d+ ssh2 </p>
<p> sets the $1 match variable to 1 and unsets $2. Therefore, the %1 and %2 match variables have to be used in the <i>desc2</i> field, in order to refer to the original values of $1 (root) and $2 (192.168.1.104) when the operation was created.  </p>
<h3>SINGLEWITHTHRESHOLD RULE</h3>
<p> The <code>SingleWithThreshold</code> rule runs event correlation operations for counting repeated instances of the same event during T seconds, and taking an action if N events are observed. The values of T and N are defined by the <i>window</i> and <i>thresh</i> field, respectively. </p>
<p> When an event has matched the rule, SEC evaluates the operation description string given with the <i>desc </i> field. If the operation for the given string and rule does not exist, SEC will create it with the lifetime of T seconds. The operation will memorize the occurrence time of the event (current time as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call), and compare the number of memorized occurrence times with the threshold N. If the operation has observed N events, it executes the action list defined by the <i>action</i> field, and consumes all further matching events without any action. If the rule has an optional action list defined with the <i>action2</i> field, the operation will execute it before finishing, provided that the action list given with <i>action</i> has been previously executed by the operation. Note that a sliding window is employed for event counting -- if the operation has observed less than N events by the end of its lifetime, it drops occurrence times which are older than T seconds, and extends its lifetime for T seconds from the earliest remaining occurrence time. If there are no remaining occurrence times, the operation finishes without executing an action list. </p>
<p> The SingleWithThreshold rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to SingleWithThreshold (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>action2</i> (optional) </dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>thresh</i></dt>
<dd> <p> counting threshold (value is an integer constant). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, <i>action</i>, and <i>action2</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> This rule runs event correlation operations for counting the number of SSH login failure events. Each operation counts events for one user name, and if the operation has observed three login failures within 60 seconds, it sends an e-mail warning to root [at] localhost. </p>
<p> Suppose the following events are generated by an SSH daemon, and each event timestamp reflects the time SEC observes the event: </p>
<p> Dec 28 01:42:21 test sshd[28132]: Failed password for risto from 10.1.2.7 port 42172 ssh2 <br />
 Dec 28 01:43:10 test sshd[28132]: Failed password for risto from 10.1.2.7 port 42172 ssh2 <br />
 Dec 28 01:43:29 test sshd[28132]: Failed password for risto from 10.1.2.7 port 42172 ssh2 <br />
 Dec 28 01:44:00 test sshd[28149]: Failed password for risto2 from 10.1.2.7 port 42176 ssh2 <br />
 Dec 28 01:44:03 test sshd[28211]: Failed password for risto from 10.1.2.7 port 42192 ssh2 <br />
 Dec 28 01:44:07 test sshd[28211]: Failed password for risto from 10.1.2.7 port 42192 ssh2 </p>
<p> When the first event is observed at 01:42:21, a counting operation is started for user risto, with its event correlation window ending at 01:43:21. Since by 01:43:21 two SSH login failures for user risto have occurred, the threshold condition remains unsatisfied for the operation. Therefore, the beginning of its event correlation window will be moved to 01:43:10 (the occurrence time of the second event), leaving the first event outside the window. At 01:44:00, another counting operation is started for user risto2. The threshold condition for the first operation will become satisfied at 01:44:03 (since the operation has seen three login failure events for user risto within 60 seconds), and thus an e-mail warning will be issued. Finally, the event occurring at 01:44:07 will be consumed silently by the first operation (the operation will run until 01:44:10). Since there will be no further login failure events for user risto2, the second operation will exist until 01:45:00 without taking any action.  </p>
<h3>SINGLEWITH2THRESHOLDS RULE</h3>
<p> The <code>SingleWith2Thresholds</code> rule runs event correlation operations which take action if N1 events have been observed in the window of T1 seconds, and then at most N2 events will be observed in the window of T2 seconds. The values of T1, N1, T2, and N2 are defined by the <i>window</i>, <i>thresh</i>, <i>window2</i>, and <i>thresh2</i> field, respectively. </p>
<p> When an event has matched the rule, SEC evaluates the operation description string given with the <i>desc </i> field. If the operation for the given string and rule does not exist, SEC will create it with the lifetime of T1 seconds. The operation will memorize the occurrence time of the event (current time as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call), and compare the number of memorized occurrence times with the threshold N1. If the operation has observed N1 events, it executes the action list defined by the <i>action</i> field, and starts another counting round for T2 seconds. If no more than N2 events have been observed by the end of the window, the operation executes the action list defined by the <i>action2</i> field and finishes. Note that both windows are sliding -- the first window slides like the window of the SingleWithThreshold operation, while the beginning of the second window is moved to the second earliest memorized event occurrence time when the threshold N2 is violated. </p>
<p> The SingleWith2Thresholds rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to SingleWith2Thresholds (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>thresh</i></dt>
<dd> <p> counting threshold. </p>
 </dd>
<dt><i>desc2</i></dt>
<dd> <p> format string that sets the %s variable for <i>action2</i>. </p>
 </dd>
<dt><i>action2</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>window2</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>thresh2</i></dt>
<dd> <p> counting threshold. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context</i>, <i>desc</i>, <i>action</i>, <i>desc2</i>, and <i>action2</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> type=SingleWith2Thresholds <br />
 ptype=RegExp <br />
 pattern=(\S+): %SYS-3-CPUHOG <br />
 desc=Router $1 CPU overload <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=300 <br />
 thresh=2 <br />
 desc2=Router $1 CPU load has been normal for 1h <br />
 action2=logonly <br />
 window2=3600 <br />
 thresh2=0 </p>
<p> When a SYS-3-CPUHOG syslog message is received from a router, the rule starts a counting operation for this router which sends an e-mail warning to root [at] localhost if another such message is received from the same router within 300 seconds. After sending the warning, the operation will continue to run until no SYS-3-CPUHOG syslog messages have been received from the router for 3600 seconds. When this condition becomes satisfied, the operation will log the message &quot;Router &lt;routername&gt; CPU load has been normal for 1h&quot; and finish. </p>
<p> Suppose the following events are generated by a router, and each event timestamp reflects the time SEC observes the event: </p>
<p> Dec 30 12:23:25 router1.mydomain Router1: %SYS-3-CPUHOG: cpu is hogged <br />
 Dec 30 12:25:38 router1.mydomain Router1: %SYS-3-CPUHOG: cpu is hogged <br />
 Dec 30 12:28:53 router1.mydomain Router1: %SYS-3-CPUHOG: cpu is hogged </p>
<p> When the first event is observed at 12:23:25, a counting operation is started for router Router1. The appearance of the second event at 12:25:38 fulfills the threshold condition given with the <i>thresh</i> and <i>window</i> fields (two events have been observed within 300 seconds). Therefore, the operation will send an e-mail warning about the CPU overload of Router1 to root [at] localhost. </p>
<p> After that, the operation will start another counting round, expecting to see no SYS-3-CPUHOG events (since <i>thresh2=0</i>) for Router1 during the following 3600 seconds (the beginning of the operation&#8217;s event correlation window will be moved to 12:25:38 for the second counting round). Since the appearance of the third event at 12:28:53 violates the threshold condition given with the <i>thresh2</i> and <i>window2</i> fields, the beginning of the event correlation window will be moved to 12:28:53. Since there will be no further SYS-3-CPUHOG messages for Router1, the operation will run until 13:28:53 and then expire, logging the message &quot;Router Router1 CPU load has been normal for 1h&quot; before finishing.  </p>
<h3>EVENTGROUP RULE</h3>
<p> The <code>EventGroup</code> rule runs event correlation operations for counting repeated instances of N different events e1,...,eN during T seconds, and taking an action if threshold conditions c1,...,cN for *all* events are satisfied (i.e., for each event eK there are at least cK event instances in the window). Note that the event correlation window of the EventGroup operation is sliding like the window of the SingleWithThreshold operation. </p>
<p> Event e1 is described with the <i>pattern</i> and <i>context</i> field, event e2 is described with the <i>pattern2</i> and <i>context2</i> field, etc. The values for N and T are defined by the <i>type</i> and <i>window</i> field, respectively. The value for c1 is given with the <i>thresh</i> field, the value for c2 is given with the <i>thresh2</i> field, etc. Values for N and c1,...,cN default to 1. </p>
<p> In order to match an event with the rule, <i>pattern</i> and <i>context</i> fields are evaluated first. If they don&#8217;t match the event, then <i>pattern2</i> and <i>context2</i> are evaluated, etc. If all N conditions are tried without a success, the event doesn&#8217;t match the rule. </p>
<p> When an event has matched the rule, SEC evaluates the operation description string given with the <i>desc </i> field. If the operation for the given string and rule does not exist, SEC will create it with the lifetime of T seconds. The operation will memorize the occurrence time of the event (current time as returned by the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call), and compare the number of memorized occurrence times for each eK with the threshold cK (i.e., the number of observed instances of eK is compared with the threshold cK). If all threshold confitions are satisfied, the operation executes the action list defined by the <i>action</i> field, and consumes all further matching events without re-executing the action list if the <i>multact</i> field is set to No (this is the default). However, if <i>multact</i> is set to Yes, the operation will re-evaluate the threshold conditions on every further matching event, re-executing the action list given with the <i>action</i> field if all conditions are satisfied, and sliding the event correlation window forward when the window is about to expire (if no events remain in the window, the operation will finish). </p>
<p> If the rule definition has an optional action list defined with the <i>countK</i> field for event eK, the operation executes it every time an instance of eK is observed (even if <i>multact</i> is set to No and the operation has already executed the action list given with <i>action</i>). </p>
<p> If the rule definition has an optional action list defined with the <i>init</i> field, the operation executes it immediately after the operation has been created. </p>
<p> If the rule definition has an optional action list defined with the <i>end</i> field, the operation executes it immediately before the operation finishes. Note that this action list is *not* executed when the operation is terminated with the <i>reset</i> action. </p>
<p> If the rule definition has an optional action list defined with the <i>slide</i> field, the operation executes it immediately after the event correlation window has slidden forward. However, note that moving the window with the <i>setwpos</i> action will *not* trigger the execution. </p>
<p> The EventGroup rule supports the following fields: </p>
<dl>
<dt><i>type </i></dt>
<dd> <p> <i></i>EventGroup[<i>N</i>] (value is case insensitive, N defaults to 1). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>pattern</i> and <i>context</i>. </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type for <i>pattern</i> (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map for <i>pattern</i>. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>pattern</i>. </p>
 </dd>
<dt><i>count</i> (optional) </dt>
<dd> <p> action list for execution after a match by <i>pattern</i> and <i>context</i>. </p>
 </dd>
<dt><i>thresh</i> (optional) </dt>
<dd> <p> counting threshold for events matched by <i>pattern</i> and <i>context </i> (value is an integer constant, default is 1). </p>
 </dd>
<dt><code>...</code></dt>
<dd>  </dd>
<dt><i>continueN</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). Specifies the point-of-continue after a match by <i>patternN</i> and <i>contextN</i>. </p>
 </dd>
<dt><i>ptypeN</i></dt>
<dd> <p> pattern type for <i>patternN</i> (value is case insensitive). </p>
 </dd>
<dt><i>patternN</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmapN</i> (optional) </dt>
<dd> <p> variable map for <i>patternN</i>. </p>
 </dd>
<dt><i>contextN</i> (optional) </dt>
<dd> <p> context expression, evaluated together with <i>patternN</i>. </p>
 </dd>
<dt><i>countN</i> (optional) </dt>
<dd> <p> action list for execution after a match by <i>patternN</i> and <i>contextN</i>. </p>
 </dd>
<dt><i>threshN</i> (optional) </dt>
<dd> <p> counting threshold for events matched by <i>patternN</i> and <i>contextN</i> (value is an integer constant, default is 1). </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>init</i> (optional) </dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>end</i> (optional) </dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>slide</i> (optional) </dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>multact</i> (optional) </dt>
<dd> <p> Yes or No (values are case insensitive, default is No). </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> event correlation window size (value is an integer constant). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in <i>context*</i>, <i>count*</i>, <i>desc</i>, <i>action</i>, <i>init</i>, <i>end</i>, and <i>slide</i> fields. </p>
<p> <code>Examples:</code> </p>
<p> The following example rule cross-correlates iptables events, Apache web server access log messages with 4xx response codes, and SSH login failure events: </p>
<p> type=EventGroup3 <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (?:invalid user )?\S+ from ([\d.]+) port \d+ ssh2 <br />
 thresh=2 <br />
 ptype2=RegExp <br />
 pattern2=^([\d.]+) \S+ \S+ \[.+?\] &quot;.+? HTTP\/[\d.]+&quot; 4\d+ <br />
 thresh2=3 <br />
 ptype3=RegExp <br />
 pattern3=kernel: iptables:.* SRC=([\d.]+) <br />
 thresh3=5 <br />
 desc=Repeated probing from host $1 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=120 </p>
<p> The rule starts an event correlation operation for an IP address if SSH login failure event, iptables event, or Apache 4xx event is observed for that IP address. The operation sends an e-mail warning to root [at] localhost if within 120 seconds three threshold conditions are satisfied for the IP address it tracks -- (1) at least two SSH login failure events have occurred for this client IP, (2) at least three Apache 4xx events have occured for this client IP, (3) at least five iptables events have been observed for this source IP. </p>
<p> Suppose the following events occur, and each event timestamp reflects the time SEC observes the event: </p>
<p> 192.168.1.104 - - [05/Jan/2014:01:11:22 +0200] &quot;GET /test.html HTTP/1.1&quot; 404 286 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 Jan 5 01:12:52 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=48422 DF PROTO=TCP SPT=46351 DPT=21 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 Jan 5 01:12:53 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=48423 DF PROTO=TCP SPT=46351 DPT=21 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 Jan 5 01:13:01 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=20048 DF PROTO=TCP SPT=44963 DPT=23 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 Jan 5 01:13:02 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=20049 DF PROTO=TCP SPT=44963 DPT=23 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 Jan 5 01:13:08 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=36362 DF PROTO=TCP SPT=56918 DPT=25 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 Jan 5 01:13:09 localhost kernel: iptables: IN=eth0 OUT= MAC=08:00:27:8e:a1:3a:00:1d:e0:7e:89:b1:08:00 SRC=192.168.1.104 DST=192.168.1.107 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=36363 DF PROTO=TCP SPT=56918 DPT=25 WINDOW=29200 RES=0x00 SYN URGP=0 <br />
 192.168.1.104 - - [05/Jan/2014:01:13:51 +0200] &quot;GET /test.html HTTP/1.1&quot; 404 286 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 192.168.1.104 - - [05/Jan/2014:01:13:54 +0200] &quot;GET /test.html HTTP/1.1&quot; 404 286 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 192.168.1.104 - - [05/Jan/2014:01:14:00 +0200] &quot;GET /login.html HTTP/1.1&quot; 404 287 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 192.168.1.104 - - [05/Jan/2014:01:14:03 +0200] &quot;GET /login.html HTTP/1.1&quot; 404 287 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 192.168.1.104 - - [05/Jan/2014:01:14:03 +0200] &quot;GET /login.html HTTP/1.1&quot; 404 287 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; <br />
 Jan 5 01:14:11 localhost sshd[1810]: Failed password for root from 192.168.1.104 port 46125 ssh2 <br />
 Jan 5 01:14:12 localhost sshd[1810]: Failed password for root from 192.168.1.104 port 46125 ssh2 <br />
 Jan 5 01:14:18 localhost sshd[1822]: Failed password for root from 192.168.1.104 port 46126 ssh2 <br />
 Jan 5 01:14:19 localhost sshd[1822]: Failed password for root from 192.168.1.104 port 46126 ssh2 <br />
 192.168.1.104 - - [05/Jan/2014:01:14:34 +0200] &quot;GET /test.html HTTP/1.1&quot; 404 286 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0&quot; </p>
<p> The Apache 4xx event at 01:11:22 starts an event correlation operation for 192.168.1.104 which has the event correlation window of 120 seconds, thus ending at 01:13:22. Between 01:12:52 and 01:13:09, six iptables events appear for 192.168.1.104, and the appearance of the fifth event at 01:13:08 fulfills the third threshold condition (within 120 seconds, at least five iptables events have been observed). </p>
<p> Since by 01:13:22 (the end of the event correlation window) no additional events have occurred, the first and second threshold condition remain unsatisfied. Therefore, the beginning of the event correlation window will be moved to 01:12:52 (the occurrence time of the earliest event which is at most 120 seconds old). As a result, the end of the window will move from 01:13:22 to 01:14:52. The only event which is left outside the window is the Apache 4xx event at 01:11:22, and thus the threshold condition for iptables events remains satisfied. </p>
<p> Between 01:13:51 and 01:14:03, five Apache 4xx events occur, and the appearance of the third event at 01:14:00 fulfills the second threshold condition (within 120 seconds, at least three Apache 4xx events have been observed). These events are followed by four SSH login failure events which occur between 01:14:11 and 01:14:19. The appearance of the second event at 01:14:12 fulfills the first threshold condition (within 120 seconds, at least two SSH login failure events have been observed). Since at this particular moment (01:14:12) the other two conditions are also fulfilled, the operation sends an e-mail warning about 192.168.1.104 to root [at] localhost. After that, the operation silently consumes all further matching events for 192.168.1.104 until 01:14:52, and then terminates. </p>
<p> Please note that if the above rule definition would contain <i>multact=yes</i> statement, the operation would continue sending e-mails at each matching event after 01:14:12, provided that all threshold conditions are satisfied. Therefore, the operation would send three additional e-mails at 01:14:18, 01:14:19, and 01:14:34. Also, the operation would not terminate after its window ends at 01:14:52, but would rather slide the window forward and expect new events. At the occurence of any iptables, SSH login failure or Apache 4xx event for 192.168.1.104, the operation would produce a warning e-mail if all threshold conditions are fulfilled. </p>
<p> The following example rule cross-correlates iptables events and SSH login events: </p>
<p> type=EventGroup3 <br />
 ptype=regexp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from ([\d.]+) port \d+ ssh2 <br />
 varmap= user=1; ip=2 <br />
 count=alias OPER_$+{ip} LOGIN_FAILED_$+{user}_$+{ip} <br />
 ptype2=regexp <br />
 pattern2=sshd\[\d+\]: Accepted .+ for (\S+) from ([\d.]+) port \d+ ssh2 <br />
 varmap2= user=1; ip=2 <br />
 context2=LOGIN_FAILED_$+{user}_$+{ip} <br />
 ptype3=regexp <br />
 pattern3=kernel: iptables:.* SRC=([\d.]+) <br />
 varmap3= ip=1 <br />
 desc=Client $+{ip} accessed a firewalled port and had difficulties with logging in <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 init=create OPER_$+{ip} <br />
 slide=delete OPER_$+{ip}; reset 0 <br />
 end=delete OPER_$+{ip} <br />
 window=120 </p>
<p> The rule starts an event correlation operation for an IP address if SSH login failure or iptables event was observed for that IP address. The operation exists for 120 seconds (since when the event correlation window slides forward, the operation terminates itself with the <i>reset </i> action as specified with the <i>slide</i> field). The operation sends an e-mail warning to root [at] localhost if within 120 seconds three threshold conditions are satisfied for the IP address it tracks -- (1) at least one iptables event has been observed for this source IP, (2) at least one SSH login failure has been observed for this client IP, (3) at least one successful SSH login has been observed for this client IP and for some user, provided that the operation has previously observed an SSH login failure for the same user and same client IP. </p>
<p> Suppose the following events occur, and each event timestamp reflects the time SEC observes the event: </p>
<p> Dec 27 19:00:06 test kernel: iptables: IN=eth0 OUT= MAC=00:13:72:8a:83:d2:00:1b:25:07:e2:1b:08:00 SRC=10.1.2.7 DST=10.2.5.5 LEN=60 TOS=0x00 PREC=0x00 TTL=62 ID=1881 DF PROTO=TCP SPT=34342 DPT=23 WINDOW=5840 RES=0x00 SYN URGP=0 <br />
 Dec 27 19:00:14 test sshd[10520]: Accepted password for root from 10.1.2.7 port 52609 ssh2 <br />
 Dec 27 19:00:24 test sshd[10526]: Failed password for risto from 10.1.2.7 port 52622 ssh2 <br />
 Dec 27 19:00:27 test sshd[10526]: Accepted password for risto from 10.1.2.7 port 52622 ssh2 </p>
<p> The iptables event at 19:00:06 starts an event correlation operation for 10.1.2.7 which has the event correlation window of 120 seconds. Immediately after the operation has been started, it creates the context OPER_10.1.2.7. The second event at 19:00:14 does not match the rule, since the context LOGIN_FAILED_root_10.1.2.7 does not exist. The third event at 19:00:24 matches the rule, and the operation which is running for 10.1.2.7 sets up the alias name LOGIN_FAILED_risto_10.1.2.7 for the context OPER_10.1.2.7. Finally, the fourth event at 19:00:27 matches the rule, since the context LOGIN_FAILED_risto_10.1.2.7 exists, and the event is therefore processed by the operation (the presence of the context indicates that the operation has previously observed a login failure for user risto from 10.1.2.7). At this particular moment (19:00:27), all three threshold conditions for the operation are fulfilled, and therefore it sends an e-mail warning about 10.1.2.7 to root [at] localhost. After that, the operation silently consumes all further matching events for 10.1.2.7 until 19:02:06, and then terminates. Immediately before termination, the operation deletes the context OPER_10.1.2.7 which also drops its alias name LOGIN_FAILED_risto_10.1.2.7. </p>
<h3>SUPPRESS RULE</h3>
<p> The <code>Suppress</code> rule takes no action when an event has matched the rule, and keeps matching events from being processed by later rules in the configuration file. </p>
<p> The Suppress rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Suppress (value is case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i> (optional) </dt>
<dd> <p> string for describing the rule. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in the <i>context</i> field. Also note that this rule does not start an event correlation operation, and the optional <i>desc</i> field is merely used for describing the rule. </p>
<p> <code>Examples:</code> </p>
<p> type=Suppress <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for \S+ from ([\d.]+) port \d+ ssh2 <br />
 context=SUPPRESS_IP_$1 </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from ([\d.]+) port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 from $2 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost; \ <br />
&nbsp;<wbr>create SUPPRESS_IP_$2 3600 <br />
 window=60 <br />
 thresh=3 </p>
<p> The first rule filters out SSH login failure events for an already reported source IP address, so that they will not be matched against the second rule during 3600 seconds after sending an e-mail warning.  </p>
<h3>CALENDAR RULE</h3>
<p> The <code>Calendar</code> rule was designed for executing actions at specific times. Unlike all other rules, this rule reacts only to the system clock, ignoring other input. The Calendar rule executes the action list given with the <i>action</i> field if the current time matches all conditions of the time specification given with the <i>time </i> field. The action list is executed only once for any matching minute. </p>
<p> The rule employs a time specification which closely resembles the <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) style, but there are some subtle differences. The time specification consists of five or six conditions separated by whitespace. The first condition matches minutes (allowed values are 0-59), the second condition matches hours (allowed values are 0-23), the third condition days (allowed values are 0-31, with 0 denoting the last day of the month), the fourth condition months (allowed values are 1-12), and the fifth condition weekdays (allowed values are 0-7, with 0 and 7 denoting Sunday). The sixth condition is optional and matches years (allowed values are 0-99 which denote the last two digits of the year). </p>
<p> Asterisks (*), ranges of numbers (e.g., 8-11), and lists (e.g., 2,5,7-9) are allowed as conditions. Asterisks and ranges may be augmented with step values (e.g., 47-55/2 means 47,49,51,53,55). </p>
<p> Note that unlike <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) time specification, the day and weekday conditions are *not* joined with logical OR, but rather with logical AND. Therefore, 0 1 25-31 10 7 means 1AM on last Sunday in October. On the other hand, with <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) the same specification means 1AM in every last seven days or every Sunday in October. </p>
<p> Also, unlike some versions of <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), SEC is not restricted to take action only during the first second of the current minute. For example, if SEC is started at the 22th second of a minute, the wildcard condition produces a match for this minute. As another example, if the time specification matches the current minute but the context expression evaluates FALSE during the first half of the minute, the Calendar rule will execute the action list in the middle of this minute when the expression value becomes TRUE. </p>
<p> The Calendar rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Calendar (value is case insensitive). </p>
 </dd>
<dt><i>time</i></dt>
<dd> <p> time specification. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>desc</i></dt>
<dd> <p> operation description string. </p>
 </dd>
<dt><i>action</i></dt>
<dd> <p> action list. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that this rule does not start event correlation operation, and the <i>desc</i> field is merely used for setting the %s action list variable. </p>
<p> <code>Examples:</code> </p>
<p> type=Calendar <br />
 time=0 2 25-31 3,12 6 <br />
 desc=Check if backup is done on last Saturday of Q1 and Q4 <br />
 action=event WAITING_FOR_BACKUP </p>
<p> type=Calendar <br />
 time=0 2 24-30 6,9 6 <br />
 desc=Check if backup is done on last Saturday of Q2 and Q3 <br />
 action=event WAITING_FOR_BACKUP </p>
<p> type=PairWithWindow <br />
 ptype=SubStr <br />
 pattern=WAITING_FOR_BACKUP <br />
 desc=Quarterly backup not completed on time! <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 ptype2=SubStr <br />
 pattern2=BACKUP READY <br />
 desc2=Quarterly backup successfully completed <br />
 action2=none <br />
 window=1800 </p>
<p> The first two rules create a synthetic event WAITING_FOR_BACKUP at 2AM on last Saturday of March, June, September and December. The third rule matches this event and starts an event correlation operation which waits for the BACKUP READY event for 1800 seconds. If this event has not arrived by 2:30AM, the operation sends an e-mail warning to root [at] localhost.  </p>
<h3>JUMP RULE</h3>
<p> The <code>Jump</code> rule submits matching events to specific ruleset(s) for further processing. If the event matches the rule, SEC continues the search for matching rules in configuration file set(s) given with the <i>cfset</i> field. Rules from every file are tried in the order of their appearance in the file. Configuration file sets can be created from Options rules with the <i>joincfset</i> field, with each set containing at least one configuration file. If more that one set name is given with <i>cfset</i>, sets are processed from left to right; a matching rule in one set doesn&#8217;t prevent SEC from processing the following sets. If the <i>constset</i> field is set to Yes, set names are assumed to be constants and will not be searched for match variables at runtime. </p>
<p> The Jump rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Jump (value is case insensitive). </p>
 </dd>
<dt><i>continue</i> (optional) </dt>
<dd> <p> TakeNext, DontCont, EndMatch or GoTo &lt;label&gt; (apart from &lt;label&gt;, values are case insensitive). </p>
 </dd>
<dt><i>ptype</i></dt>
<dd> <p> pattern type (value is case insensitive). </p>
 </dd>
<dt><i>pattern</i></dt>
<dd> <p> pattern. </p>
 </dd>
<dt><i>varmap</i> (optional) </dt>
<dd> <p> variable map. </p>
 </dd>
<dt><i>context</i> (optional) </dt>
<dd> <p> context expression. </p>
 </dd>
<dt><i>cfset</i> (optional) </dt>
<dd> <p> configuration file set names that are separated by whitespace. </p>
 </dd>
<dt><i>constset</i> (optional) </dt>
<dd> <p> Yes or No (values are case insensitive, default is Yes). </p>
 </dd>
<dt><i>desc</i> (optional) </dt>
<dd> <p> string for describing the rule. </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> Note that match variables may be used in the <i>context</i> field. They may also be used in the <i>cfset</i> field, provided that the <i>constset </i> field is set to No. Also note that this rule does not start event correlation operations, and the optional <i>desc</i> field is merely used for describing the rule. </p>
<p> Finally, if the <i>cfset</i> field is not present and the <i>continue</i> field is set to GoTo, the Jump rule can be used for skipping rules inside the current configuration file; if both <i>cfset</i> and <i>continue</i> are not present, Jump is identical to Suppress. </p>
<p> <code>Examples:</code> </p>
<p> type=Jump <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: <br />
 cfset=sshd-rules auth-rules </p>
<p> When an sshd syslog message appears in input, rules from configuration files of the set <code>sshd-rules</code> are first used for matching the message, and then rules from the configuration file set <code>auth-rules</code> are tried.  </p>
<h3>OPTIONS RULE</h3>
<p> The <code>Options</code> rule sets processing options for the ruleset in the current configuration file. If more than one Options rule is present in the configuration file, the last instance overrides all previous ones. Note that the Options rule is only processed when SEC (re)starts and reads in the configuration file. Since this rule is not applied at runtime, it can never match events, react to the system clock, or start event correlation operations. </p>
<p> The <i>joincfset</i> field lists the names of one or more configuration file sets, and the current configuration file will be added to each set. If a set doesn&#8217;t exist, it will be created and the current configuration file becomes its first member. If the <i>procallin</i> field is set to No, the rules from the configuration file will be used for matching input from Jump rules only. </p>
<p> The Options rule supports the following fields: </p>
<dl>
<dt><i>type</i></dt>
<dd> <p> fixed to Options (value is case insensitive). </p>
 </dd>
<dt><i>joincfset</i> (optional) </dt>
<dd> <p> configuration file set names that are separated by whitespace. </p>
 </dd>
<dt><i>procallin</i> (optional) </dt>
<dd> <p> Yes or No (values are case insensitive, default is Yes). </p>
 </dd>
<dt><i>rem</i> (optional, may appear more than once) </dt>
<dd> <p> remarks and comments. </p>
 </dd></dl>
<p> <code>Examples:</code> </p>
<p> The following rule adds the current configuration file to the set <code>sshd-rules</code> which is used for matching input from Jump rules only: </p>
<p> type=Options <br />
 joincfset=sshd-rules <br />
 procallin=no </p>
<p> The following rule adds the current configuration file to sets <code>linux</code> and <code>solaris</code> which are used for matching all input: </p>
<p> type=Options <br />
 joincfset=linux solaris  </p>
<h2>EVENT CORRELATION OPERATIONS</h2>
<p> Event correlation operations are dynamic entities created by rules. After creating an operation, the rule also feeds the operation with events that need to be correlated. Since each rule can create and feed many operations which are running simultaneously, each operation needs a unique ID. </p>
<p> In order to identify event correlation operations, SEC assigns an ID to every operation that is composed from the configuration file name, the rule number, and the operation description string (defined by the <i>desc</i> field of the rule). If there are N rules in the configuration file (excluding Options rules), the rule numbers belong to the range 0..N-1, and the number of the k-th rule is k-1. Since each Options rule is only processed when SEC reads in the configuration file and is not applied at runtime, the Options rules will not receive rule numbers. Note that since the configuration file name and rule number are part of the operation ID, different rules can have identical <i>desc</i> fields without a danger of a clash between operations. </p>
<p> For example, if the configuration file /etc/sec/my.conf contains only one rule </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=user (\S+) login failure on (\S+) <br />
 desc=Repeated login failures for user $1 on $2 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> then the number of this rule is 0. When this rule matches an input event &quot;user admin login failure on tty1&quot;, the <i>desc</i> field yields an operation description string <i>Repeated login failures for user admin on tty1</i>, and the event will be directed for further processing to the operation with the following ID: </p>
<p> /etc/sec/my.conf | 0 | Repeated login failures for user admin on tty1 </p>
<p> If the operation for this ID does not exist, the rule will create it. The newly created operation has its event counter initialized to 1, and it expects to receive two additional &quot;user admin login failure on tty1&quot; events from the rule within the following 60 seconds. If the operation receives such an event, its event counter is incremented, and if the counter reaches the value of 3, a warning e-mail is sent to root [at] localhost. </p>
<p> By tuning the <i>desc</i> field of the rule, the scope of individual event correlation operations can be changed. For instance, if the following events occur within 10 seconds </p>
<p> user admin login failure on tty1 <br />
 user admin login failure on tty5 <br />
 user admin login failure on tty2 </p>
<p> the above rule starts three event correlation operations. However, if the <i>desc</i> field of the rule is changed to <i>Repeated login failures for user $1</i>, these events are processed by the *same* event correlation operation (the operation sends a warning e-mail to root [at] localhost when it receives the third event). </p>
<p> Since rules from the same configuration file are matched against input in the order they are given, the rule ordering influences the creation and feeding of event correlation operations. Suppose the configuration file /etc/sec/my.conf contains the following rules: </p>
<p> type=Suppress <br />
 ptype=TValue <br />
 pattern=TRUE <br />
 context=MYCONTEXT </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=user (\S+) login failure on (\S+) <br />
 desc=Repeated login failures for user $1 on $2 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> The second rule is able to create and feed event correlation operations as long as the context MYCONTEXT does not exist. However, after MYCONTEXT has been created, no input event will reach the second rule, and the rule is thus unable to create new operations and feed existing ones with events. </p>
<p> Note that Pair and PairWithWindow rules can feed the same event to several operations. Suppose the configuration file /etc/sec/my2.conf contains the following rules: </p>
<p> type=Suppress <br />
 ptype=SubStr <br />
 pattern=test </p>
<p> type=Pair <br />
 ptype=RegExp <br />
 pattern=database (\S+) down <br />
 desc=Database $1 is down <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 ptype2=RegExp <br />
 pattern2=database $1 up|all databases up <br />
 desc2=Database %1 is up <br />
 action2=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=86400 </p>
<p> Since the following input events don&#8217;t contain the substring &quot;test&quot; </p>
<p> database mydb1 down <br />
 database mydb2 down <br />
 database mydb3 down </p>
<p> they are matched by the second rule of type Pair which creates three event correlation operations. Each operation is running for one particular database name, and the operations have the following IDs: </p>
<p> /etc/sec/my2.conf | 1 | Database mydb1 is down <br />
 /etc/sec/my2.conf | 1 | Database mydb2 is down <br />
 /etc/sec/my2.conf | 1 | Database mydb3 is down </p>
<p> Each newly created operation sends an e-mail notification to root [at] localhost about the &quot;database down&quot; condition, and will then wait for 86400 seconds (24 hours) for either of the following messages: <br />
 (a) &quot;database up&quot; message for the given database, <br />
 (b) &quot;all databases up&quot; message. </p>
<p> The operation with the ID </p>
<p> /etc/sec/my2.conf | 1 | Database mydb1 is down </p>
<p> uses the following regular expression for matching expected messages: </p>
<p> database mydb1 up|all databases up </p>
<p> The operation with the ID </p>
<p> /etc/sec/my2.conf | 1 | Database mydb2 is down </p>
<p> employs the following regular expression for matching expected messages: </p>
<p> database mydb2 up|all databases up </p>
<p> Finally, the operation with the ID </p>
<p> /etc/sec/my2.conf | 1 | Database mydb3 is down </p>
<p> uses the following regular expression: </p>
<p> database mydb3 up|all databases up </p>
<p> If the following input events appear after 10 minutes </p>
<p> database test up <br />
 admin logged in <br />
 database mydb3 up <br />
 all databases up </p>
<p> the first event &quot;database test up&quot; matches the first rule (Suppress) which does not pass the event further to the second rule (Pair). However, all following events reach the Pair rule. Since the messages don&#8217;t match the <i>pattern</i> field of the rule, the rule feeds them to all currently existing operations it has created, so that the operations can match these events with their regular expressions. Because regular expressions of all three operations don&#8217;t match the event &quot;admin logged in&quot;, the operations will continue to run. In the case of the &quot;database mydb3 up&quot; event, the regular expression of the operation </p>
<p> /etc/sec/my2.conf | 1 | Database mydb3 is down </p>
<p> produces a match. Therefore, the operation will send the e-mail notification &quot;Database mydb3 is up&quot; to root [at] localhost and terminate. However, the following event &quot;all databases up&quot; matches the regular expressions of two remaining operations. As a result, the operations will send e-mail notifications &quot;Database mydb1 is up&quot; and &quot;Database mydb2 is up&quot; to root [at] localhost and terminate. </p>
<p> Each operation has an event correlation window which defines its scope in time. The size of the window is defined by the <i>window*</i> field, and the beginning of the window can be obtained with the <i>getwpos</i> action. SingleWithThreshold, SingleWith2Thresholds and EventGroup operations can slide its window forward during event processing, while for all operations the window can also be moved explicitly with the <i>setwpos</i> action. Also, with the <i>reset</i> action event correlation operations can be terminated. Note that <i>getwpos</i>, <i>setwpos</i>, and <i>reset</i> actions only work for operations started by the rules from the same configuration file. </p>
<p> For example, consider the configuration file /etc/sec/sshd.rules that contains the following rules: </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=Three SSH login failures within 1m for user $1 <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=60 <br />
 thresh=3 </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Accepted .+ for (\S+) from [\d.]+ port \d+ ssh2 <br />
 desc=SSH login successful for user $1 <br />
 action=reset -1 Three SSH login failures within 1m for user $1 </p>
<p> Suppose the following events are generated by an SSH daemon, and each event timestamp reflects the time SEC observes the event: </p>
<p> Dec 29 15:00:03 test sshd[14129]: Failed password for risto from 10.1.2.7 port 31312 ssh2 <br />
 Dec 29 15:00:08 test sshd[14129]: Failed password for risto from 10.1.2.7 port 31312 ssh2 <br />
 Dec 29 15:00:17 test sshd[14129]: Accepted password for risto from 10.1.2.7 port 31312 ssh2 <br />
 Dec 29 15:00:52 test sshd[14142]: Failed password for risto from 10.1.1.2 port 17721 ssh2 </p>
<p> The first event at 15:00:03 starts an event correlation operation with the ID </p>
<p> /etc/sec/sshd.rules | 0 | Three SSH login failures within 1m for user risto </p>
<p> However, when the third event occurs at 15:00:17, the second rule matches it and terminates the operation with the action </p>
<p> reset -1 Three SSH login failures within 1m for user risto </p>
<p> The -1 parameter of <i>reset</i> restricts the action to operations started by the previous rule (i.e., the first rule that has a number 0), while the <i>Three SSH login failures within 1m for user risto</i> parameter refers to the operation description string. Together with the current configuration file name (/etc/sec/sshd.rules), the parameters yield the operation ID </p>
<p> /etc/sec/sshd.rules | 0 | Three SSH login failures within 1m for user risto </p>
<p> (If the operation with the given ID would not exist, <i>reset</i> would perform no operation.) </p>
<p> As a consequence, the fourth event at 15:00:52 starts another operation with the same ID as the terminated operation had. Without the second rule, the operation that was started at 15:00:03 would not be terminated, and the appearance of the fourth event would trigger a warning e-mail from that operation.  </p>
<h2>INPUT PROCESSING AND TIMING</h2>
<p> SEC processes input data iteratively by reading one line at each iteration, writing this line into a relevant input buffer, and matching the content of the updated buffer with rules from configuration files. If during the matching process an action list is executed which creates new input events (e.g., through the <i>event</i> action), they are *not* written to buffer(s) immediately, but rather consumed at following iterations. </p>
<p> Note that when both synthetic events and regular input are available for processing, synthetic events are always consumed first. When all synthetic events have been consumed iteratively, SEC will start processing new data from input files. </p>
<p> With the <code>--jointbuf</code> option, SEC employs a joint input buffer for all input sources which holds N last input lines (the value of N can be set with the <code>--bufsize</code> option). Updating the input buffer means that the new line becomes the first element of the buffer, while the last element (the oldest line) is removed from the end of the buffer. With the <code>--nojointbuf</code> option, SEC maintains a buffer of N lines for each input file, and if the input line comes from file F, the buffer of F is updated as described previously. There is also a separate buffer for synthetic and internal events. </p>
<p> Suppose SEC is started with the following command line </p>
<p> /usr/bin/sec --conf=/etc/sec/test-multiline.conf --jointbuf \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/prog1.log --input=/var/log/prog2.log </p>
<p> and the configuration file /etc/sec/test-multiline.conf has the following content: </p>
<p> type=Single <br />
 rem=this rule matches two consecutive lines where the first \ <br />
&nbsp;<wbr>line contains&nbsp;<wbr>&quot;test1&quot;&nbsp;<wbr>and the second line&nbsp;<wbr>&quot;test2&quot;, and&nbsp;<wbr>\ <br />
&nbsp;<wbr>writes the matching lines to standard output <br />
 ptype=RegExp2 <br />
 pattern=test1.*\n.*test2 <br />
 desc=two consecutive test lines <br />
 action=write - $0 </p>
<p> When the following lines appear in input files /var/log/prog1.log and /var/log/prog2.log </p>
<p> Dec 31 12:33:12 test prog1: test1 (file /var/log/prog1.log) <br />
 Dec 31 12:34:09 test prog2: test1 (file /var/log/prog2.log) <br />
 Dec 31 12:39:35 test prog1: test2 (file /var/log/prog1.log) <br />
 Dec 31 12:41:53 test prog2: test2 (file /var/log/prog2.log) </p>
<p> they are stored in a common input buffer. Therefore, rule fires after the third event has appeared, and writes the following lines to standard output: </p>
<p> Dec 31 12:34:09 test prog2: test1 (file /var/log/prog2.log) <br />
 Dec 31 12:39:35 test prog1: test2 (file /var/log/prog1.log) </p>
<p> However, if SEC is started with the <code>--nojointbuf </code> option, separate input buffers are set up for /var/log/prog1.log and /var/log/prog2.log. Therefore, the rule fires after the third event has occurred, and writes the following lines to standard output: </p>
<p> Dec 31 12:33:12 test prog1: test1 (file /var/log/prog1.log) <br />
 Dec 31 12:39:35 test prog1: test2 (file /var/log/prog1.log) </p>
<p> The rule also fires after the fourth event has occurred, producing the following output: </p>
<p> Dec 31 12:34:09 test prog2: test1 (file /var/log/prog2.log) <br />
 Dec 31 12:41:53 test prog2: test2 (file /var/log/prog2.log) </p>
<p> The content of input buffers can be modified with the <i>rewrite</i> action, and modifications become visible immediately during ongoing event processing iteration. Suppose SEC is started with the following command line </p>
<p> /usr/bin/sec --conf=/etc/sec/test-rewrite.conf \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=- --nojointbuf </p>
<p> and the configuration file /etc/sec/test-rewrite.conf has the following content: </p>
<p> type=Single <br />
 rem=this rule matches two consecutive lines where the first \ <br />
&nbsp;<wbr>line contains&nbsp;<wbr>&quot;test1&quot;&nbsp;<wbr>and the second line&nbsp;<wbr>&quot;test2&quot;, and&nbsp;<wbr>\ <br />
&nbsp;<wbr>joins these lines in the input buffer <br />
 ptype=RegExp2 <br />
 pattern=^(.*test1.*)\n(.*test2.*)$ <br />
 continue=TakeNext <br />
 desc=join two test lines <br />
 action=rewrite 2 Joined $1 and $2 </p>
<p> type=Single <br />
 rem=this rule matches a line which begins with &quot;Joined&quot;, \ <br />
&nbsp;<wbr>and writes this line to standard output <br />
 ptype=RegExp <br />
 pattern=^Joined <br />
 desc=output joined lines <br />
 action=write - $0 </p>
<p> When the following two lines appear in standard input </p>
<p> This is a test1 <br />
 This is a test2 </p>
<p> they are matched by the first rule which uses the <i>rewrite </i> action for replacing those two lines in the input buffer with a new content. The last line in the input buffer (&quot;This is a test2&quot;) is replaced with &quot;Joined This is a test1 and This is a test2&quot;, while the previous line in the input buffer (&quot;This is a test1&quot;) is replaced with an empty string. Since the rule contains <i>continue=TakeNext</i> statement, the matching process will continue from the following rule. This rule matches the last line in the input buffer if it begins with &quot;Joined&quot;, and writes the line to standard output, producing </p>
<p> Joined This is a test1 and This is a test2 </p>
<p> After each event processing iteration, the pattern match cache is cleared. In other words, if a match is cached with the rule <i>varmap*</i> field, it is available during ongoing iteration only. Note that results from a successful pattern matching are also cached when the subsequent context expression evaluation yields FALSE. This allows for reusing results from partial rule matches. For example, the following rule creates the cache entry &quot;ssh_failed_login&quot; for any SSH failed login event, even if the context ALERTING_ON does not exist: </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=sshd\[\d+\]: Failed .+ for (\S+) from ([\d.]+) port \d+ ssh2 <br />
 varmap=ssh_failed_login; user=1; ip=2 <br />
 context=ALERTING_ON <br />
 desc=SSH login failure for user $1 from $2 <br />
 action=pipe &#8216;%s&#8217; /bin/mail -s &#8216;SSH login alert&#8217; root [at] localhost </p>
<p> However, provided the context expression does not contain match variables, enclosing the expression in square brackets (e.g., [ALERTING_ON]) forces its evaluation before the pattern matching, and will thus prevent the matching and the creation of the cache entry if the evaluation yields FALSE. </p>
<p> Rules from the same configuration file are matched against the buffer content in the order they are given in that file. When multiple configuration files have been specified, rule sequences from all files are matched against the buffer content (unless specified otherwise with Options rules). The matching order is determined by the order of configuration files in SEC command line. For example, if the Perl <code>glob</code>() function returns filenames in ascending ASCII order, and configuration files /home/risto/A.conf, /home/risto/B.conf2, and /home/risto/C.conf are specified with <code>--conf=/home/risto/*.conf --conf=/home/risto/*.conf2</code> in SEC command line, then SEC first matches the input against the rule sequence from A.conf, then from C.conf, and finally from B.conf2. Also, note that even if A.conf contains a Suppress rule for a particular event, the event is still processed by rulesets in C.conf and B.conf2. However, note that <code>glob</code>() might return file names in different order if locale settings change. If you want to enforce a fixed order for configuration file application in a portable way, it is recommended to create a unique set for each file with the Options rule, and employ the Jump rule for defining the processing order for sets, e.g.: </p>
<p> # This rule appears in A.conf <br />
 type=Options <br />
 joincfset=FileA <br />
 procallin=no </p>
<p> # This rule appears in B.conf2 <br />
 type=Options <br />
 joincfset=FileB <br />
 procallin=no </p>
<p> # This rule appears in C.conf <br />
 type=Options <br />
 joincfset=FileC <br />
 procallin=no </p>
<p> # This rule appears in main.conf <br />
 type=Jump <br />
 ptype=TValue <br />
 pattern=TRUE <br />
 cfset=FileA FileC FileB </p>
<p> After the relevant input buffer has been updated and its content has been matched by the rules, SEC handles caught signals and checks the status of child processes. When the timeout specified with the <code>--cleantime</code> option has expired, SEC also checks the status of contexts and event correlation operations. Therefore, relatively small values should be specified with the <code>--cleantime</code> option, in order to retain the accuracy of the event correlation process. If the <code>--cleantime</code> option is set to 0, SEC checks event correlation operations and contexts after processing every input line, but this consumes more CPU time. If the <code>--poll-timeout</code> option value exceeds the value given with <code>--cleantime</code>, the <code>--poll-timeout</code> option value takes precedence (i.e., sleeps after unsuccessful polls will not be shortened). </p>
<p> Finally, note that apart from the sleeps after unsuccessful polls, SEC measures all time intervals and occurrence times in seconds, and always uses the <code><a href="/docs/linux/man/2-time/">time</a></code>(2) system call for obtaining the current time. Also, for input event occurrence time SEC always uses the time it observed the event, *not* the timestamp extracted from the event.  </p>
<h2>INTERNAL EVENTS AND CONTEXTS</h2>
<p> In the action list of a context, the context can also be referred with the internal context name _THIS. The name _THIS is created and deleted dynamically by SEC and it points to the context only during its action list execution. This feature is useful when the context has had several names during its lifetime (created with the <i>alias</i> action), and it is hard to determine which names exist when the context expires. For example, if the context is created with <i>create A 60 (report A /bin/mail root) </i> which is immediately followed by <i>alias A B</i> and <i>unalias A</i>, the <i>report</i> action will fail since the name A no longer refers to the context. However, replacing the first action with <i>create A 60 (report _THIS /bin/mail root)</i> will produce the correct result. </p>
<p> If the <code>--intevents</code> command line option is given, SEC will generate internal events when it is started up, when it receives certain signals, and when it terminates normally. Inside SEC, internal event is treated as if it was a line that was read from a SEC input file. Specific rules can be written to match internal events, in order to take some action (e.g., start an external event correlation module with <i>spawn</i> when SEC starts up). The following internal events are supported: </p>
<p> SEC_STARTUP - generated when SEC is started (this event will always be the first event that SEC sees) </p>
<p> SEC_PRE_RESTART - generated before processing of the <code>SIGHUP</code> signal (this event will be the last event that SEC sees before clearing all internal data structures and reloading its configuration) </p>
<p> SEC_RESTART - generated after processing of the <code>SIGHUP</code> signal (this event will be the first event that SEC sees after clearing all internal data structures and reloading its configuration) </p>
<p> SEC_PRE_SOFTRESTART - generated before processing of the <code>SIGABRT</code> signal (this event will be the last event that SEC sees before reloading its configuration) </p>
<p> SEC_SOFTRESTART - generated after processing of the <code>SIGABRT</code> signal (this event will be the first event that SEC sees after reloading its configuration) </p>
<p> SEC_PRE_LOGROTATE - generated before processing of the <code>SIGUSR2</code> signal (this event will be the last event that SEC sees before reopening its log file and closing its outputs) </p>
<p> SEC_LOGROTATE - generated after processing of the <code>SIGUSR2</code> signal (this event will be the first event that SEC sees after reopening its log file and closing its outputs) </p>
<p> SEC_SHUTDOWN - generated when SEC receives the <code>SIGTERM</code> signal, or when SEC reaches all EOFs of input files after being started with the <code>--notail</code> option. With the <code>--childterm</code> option, SEC sleeps for 3 seconds after generating SEC_SHUTDOWN event, and then sends SIGTERM to its child processes (if a child process was triggered by SEC_SHUTDOWN, this delay leaves the process enough time for setting a signal handler for SIGTERM). </p>
<p> Before generating an internal event, SEC sets up a context named SEC_INTERNAL_EVENT, in order to disambiguate internal events from regular input. The SEC_INTERNAL_EVENT context is deleted immediately after the internal event has been matched against all rules. </p>
<p> If the <code>--intcontexts</code> command line option is given, or there is an <code>--input</code> option with a context specified, SEC creates an internal context each time it reads a line from an input file or a synthetic event. The internal context is deleted immediately after the line has been matched against all rules. For all input files that have the context name explicitly set with <code>--input=&lt;file_pattern&gt;=&lt;context&gt;</code>, the name of the internal context is &lt;context&gt;. If the line was read from the input file &lt;filename&gt; for which there is no context name set, the name of the internal context is _FILE_EVENT_&lt;filename&gt;. For synthetic events, the name of the internal context defaults to _INTERNAL_EVENT, but <i>cspawn</i> and <i>cevent</i> actions can be used for generating synthetic events with custom internal context names. This allows for writing rules that match data from one particular input source only. For example, the rule </p>
<p> type=Suppress <br />
 ptype=TValue <br />
 pattern=TRUE <br />
 context=[!_FILE_EVENT_/dev/logpipe] </p>
<p> passes only the lines that were read from /dev/logpipe, and also synthetic events that were generated with the _FILE_EVENT_/dev/logpipe internal context (e.g., with the action <i>cevent _FILE_EVENT_/dev/logpipe 0 This is a test event</i>). As another example, if SEC has been started with the command line </p>
<p> /usr/bin/sec --intevents --intcontexts --conf=/etc/sec/my.conf \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/messages=MESSAGES&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/secure=SECURE&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/cron=CRON&nbsp;<wbr> </p>
<p> and the rule file /etc/sec/my.conf contains the following rules </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=^(?:SEC_STARTUP|SEC_RESTART)$ <br />
 context=[SEC_INTERNAL_EVENT] <br />
 desc=listen on 10514/tcp for incoming events <br />
 action=cspawn MESSAGES /usr/bin/nc -l -k 10514 </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=. <br />
 context=[MESSAGES] <br />
 desc=echo everything from 10514/tcp and /var/log/messages <br />
 action=write - $0 </p>
<p> then SEC will receive input lines from the log files /var/log/messages, /var/log/secure, and /var/log/cron, and will also run /usr/bin/nc for receiving input lines from the port 10514/tcp. All input lines from /var/log/messages and 10514/tcp are matched by the second rule and written to standard output.  </p>
<h2>INTERPROCESS COMMUNICATION</h2>
<p> The SingleWithScript rule and <i>shellcmd</i>, <i>spawn</i>, <i>cspawn</i>, <i>pipe</i>, and <i>report</i> actions fork a child process for executing an external program. If the program command line contains shell metacharacters, the command line is first parsed by the shell which then starts the program. SEC communicates with its child processes through pipes (created with the <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) system call). When the child process is at the read end of the pipe, data have to be written to the pipe in blocking mode which ensures reliable data transmission. In order to avoid being blocked, SEC forks another child process for writing data to the pipe reliably. </p>
<p> After forking an external program, SEC continues immediately, and checks the program status periodically until the program exits. The running time of a child process is not limited in any way. With the <code>--childterm</code> option, SEC sends the <code>SIGTERM </code> signal to all child processes when it terminates. If some special exit procedures need to be accomplished in the child process (or the child wishes to ignore <code>SIGTERM</code>), then the child must install a handler for the <code>SIGTERM </code> signal. Note that if the program command line contains shell metacharacters, the parsing shell will run as a child process of SEC and the parent process of the program. Therefore, the <code>SIGTERM</code> signal will be sent to the shell, *not* the program. In order to avoid this, the shell&#8217;s builtin <i>exec</i> command can be used (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) for more information) which replaces the shell with the program without forking a new process, e.g., </p>
<p> action=spawn exec /usr/local/bin/myscript.pl 2&gt;/var/log/myscript.log </p>
<p> Note that if an action list includes two actions which fork external programs, the execution order these programs is not determined by the order of actions in the list, since both programs are running asynchronously. In order to address this issue, the execution order must be specified explicitly (e.g., instead of writing <i>action=shellcmd cmd1; shellcmd cmd2</i>, use the shell &amp;&amp; operator and write <i>action=shellcmd cmd1 &amp;&amp; cmd2</i>). </p>
<p> Sometimes it is desireable to start an external program and provide it with data from several rules. In order to create such setup, named pipes can be harnessed. For example, if /var/log/pipe is a named pipe, then </p>
<p> action=shellcmd /usr/bin/logger -f /var/log/pipe -p user.notice </p>
<p> starts the /usr/bin/logger utility which sends all lines read from /var/log/pipe to the local syslog daemon with the &quot;user&quot; facility and &quot;notice&quot; level. In order to feed events to /usr/bin/logger, the <i>write</i> action can be used (e.g., <i>write /var/log/pipe This is my event</i>). Although SEC keeps the named pipe open across different <i>write</i> actions, the pipe will be closed on the reception of SIGHUP, SIGABRT and SIGUSR2 signals. Since many UNIX tools terminate on receiving EOF from standard input, they need restarting after such signals have arrived. For this purpose, the <code>--intevents</code> option and SEC internal events can be used. For example, the following rule starts the /usr/bin/logger utility at SEC startup, and also restarts it after the reception of relevant signals: </p>
<p> type=Single <br />
 ptype=RegExp <br />
 pattern=^(?:SEC_STARTUP|SEC_RESTART|SEC_SOFTRESTART|SEC_LOGROTATE)$ <br />
 context=SEC_INTERNAL_EVENT <br />
 desc=start the logger tool <br />
 action=free %emptystring; owritecl /var/log/pipe %emptystring; \ <br />
&nbsp;<wbr>shellcmd&nbsp;<wbr>/usr/bin/logger -f&nbsp;<wbr>/var/log/pipe -p user.notice </p>
<p> Note that if /var/log/pipe is never opened for writing by a <i>write</i> action, /usr/bin/logger will never see EOF and will thus not terminate. The <i>owritecl</i> action opens and closes /var/log/pipe without writing any bytes, in order to ensure the presence of EOF in such cases. This allows any previous /usr/bin/logger process to terminate before the new process is started.  </p>
<h2>PERL INTEGRATION</h2>
<p> SEC supports patterns, context expressions, and actions which involve calls to the Perl <code>eval</code>() function or the execution of precompiled Perl code. The use of Perl code in SEC patterns and context expressions allows for creating proper match conditions for scenarios which can&#8217;t be handled by a simple regular expression match. For example, consider the following iptables syslog events: </p>
<p> May 27 10:00:15 box1 kernel: iptables: IN=eth0 OUT= MAC=08:00:27:be:9e:2f:00:10:db:ff:20:03:08:00 SRC=10.6.4.14 DST=10.1.8.2 LEN=84 TOS=0x00 PREC=0x00 TTL=251 ID=61426 PROTO=ICMP TYPE=8 CODE=0 ID=11670 SEQ=2 <br />
 May 27 10:02:22 box1 kernel: iptables: IN=eth0 OUT= MAC=08:00:27:be:9e:2f:00:10:db:ff:20:03:08:00 SRC=10.6.4.14 DST=10.1.8.2 LEN=52 TOS=0x00 PREC=0x00 TTL=60 ID=61441 DF PROTO=TCP SPT=53125 DPT=23 WINDOW=49640 RES=0x00 SYN URGP=0 </p>
<p> Depending on the protocol and the nature of the traffic, events can have a wide variety of fields, and parsing out all event data with one regular expression is infeasible. For addressing this issue, a PerlFunc pattern can be used which creates match variables from all fields of the matching event, stores them in one Perl hash, and returns a reference to this hash. Outside the PerlFunc pattern, match variables are initialized from the key-value pairs in the returned hash. Suppose the following Jump rule with a PerlFunc pattern is defined in the main.rules rule file: </p>
<p> type=Jump <br />
 ptype=PerlFunc <br />
 pattern=sub { my(%var); my($line) = $_[0]; \ <br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>($line&nbsp;<wbr>!~&nbsp;<wbr>/kernel: iptables:/g)&nbsp;<wbr>{&nbsp;<wbr>return 0;&nbsp;<wbr>}&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>while&nbsp;<wbr>($line&nbsp;<wbr>=~&nbsp;<wbr>/\G\s*([A-Z]+)(?:=(\S*))?/g)&nbsp;<wbr>{&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$var{$1}&nbsp;<wbr>=&nbsp;<wbr>defined($2)?$2:1;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>return&nbsp;<wbr>\%var;&nbsp;<wbr>} <br />
 varmap=IPTABLES <br />
 desc=parse iptables event <br />
 cfset=iptables </p>
<p> For example, if the iptables event contains the fields SRC=10.6.4.14, DST=10.1.8.2 and SYN, the above PerlFunc pattern sets up match variable $+{SRC} which holds 10.6.4.14, match variable $+{DST} which holds 10.1.8.2, and match variable $+{SYN} which holds 1. The Jump rule caches all created match variables under the name IPTABLES, and submits the matching event to <code>iptables</code> ruleset for further processing. Suppose the <code>iptables</code> ruleset is defined in the iptables.rules rule file: </p>
<p> type=Options <br />
 procallin=no <br />
 joincfset=iptables </p>
<p> type=SingleWithThreshold <br />
 ptype=Cached <br />
 pattern=IPTABLES <br />
 context=IPTABLES :&gt; ( sub { return $_[0]-&gt;{&quot;PROTO&quot;} eq &quot;ICMP&quot;; } ) <br />
 desc=ICMP flood type $+{TYPE} code $+{CODE} from host $+{SRC} <br />
 action=logonly <br />
 window=10 <br />
 thresh=100 </p>
<p> type=SingleWithThreshold <br />
 ptype=Cached <br />
 pattern=IPTABLES <br />
 context=IPTABLES :&gt; ( sub { return exists($_[0]-&gt;{&quot;SYN&quot;}) &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exists($_[0]-&gt;{&quot;FIN&quot;})&nbsp;<wbr>;&nbsp;<wbr>}&nbsp;<wbr>) <br />
 desc=SYN+FIN flood from host $+{SRC} <br />
 action=logonly <br />
 window=10 <br />
 thresh=100 </p>
<p> The two SingleWithThreshold rules employ Cached patterns for matching iptables events by looking up the IPTABLES entry in the pattern match cache (created by the above Jump rule for each iptables event). In order to narrow down the match to specific iptables events, the rules employ precompiled Perl functions in context expressions. The :&gt; operator is used for speeding up the matching, providing the function with a single parameter which refers to the hash of variable name-value pairs for the IPTABLES cache entry. </p>
<p> The first SingleWithThreshold rule logs a warning message if within 10 seconds 100 iptables events have been observed for ICMP packets with the same type, code, and source IP address. The second SingleWithThreshold rule logs a warning message if within 10 seconds 100 iptables events have been observed for TCP packets coming from the same host, and having both SYN and FIN flag set in each packet. </p>
<p> Apart from using action list variables for data sharing between rules, Perl variables created in Perl code can be employed for the same purpose. For example, when SEC has executed the following action </p>
<p> action=eval %a ($b = 1) </p>
<p> the variable $b and its value become visible in the following context expression </p>
<p> context= =(++$b &gt; 10) </p>
<p> (with that expression one can implement event counting implicitly). In order to avoid possible clashes with variables inside the SEC code itself, user-defined Perl code is executed in the main::SEC namespace (i.e., inside the special package main::SEC). By using the main:: prefix, SEC data structures can be accessed and modified. For example, the following rules restore and save contexts on SEC startup and shutdown (SEC keeps all contexts in %main::context_list hash): </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=SEC_STARTUP <br />
 context=SEC_INTERNAL_EVENT <br />
 continue=TakeNext <br />
 desc=Load the Storable module and terminate if it is not found <br />
 action=eval %ret (require Storable); \ <br />
&nbsp;<wbr>if&nbsp;<wbr>%ret&nbsp;<wbr>(&nbsp;<wbr>logonly Storabe loaded&nbsp;<wbr>)&nbsp;<wbr>else&nbsp;<wbr>(&nbsp;<wbr>eval&nbsp;<wbr>%o&nbsp;<wbr><a href="/docs/linux/man/1-exit/">exit</a>(1)&nbsp;<wbr>)&nbsp;<wbr> </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=SEC_STARTUP <br />
 context=SEC_INTERNAL_EVENT <br />
 desc=Restore all SEC contexts from /var/lib/sec/SEC_CONTEXTS on startup <br />
 action=lcall %ret -&gt; ( sub { \ <br />
&nbsp;<wbr>my&nbsp;<wbr>$ptr&nbsp;<wbr>=&nbsp;<wbr>$main::context_list{&quot;SEC_INTERNAL_EVENT&quot;};&nbsp;<wbr>\ <br />
&nbsp;<wbr>%main::context_list&nbsp;<wbr>=&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{Storable::retrieve(&quot;/var/lib/sec/SEC_CONTEXTS&quot;)};&nbsp;<wbr>\ <br />
&nbsp;<wbr>$main::context_list{&quot;SEC_INTERNAL_EVENT&quot;}&nbsp;<wbr>=&nbsp;<wbr>$ptr;&nbsp;<wbr>}&nbsp;<wbr>) </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=SEC_SHUTDOWN <br />
 context=SEC_INTERNAL_EVENT <br />
 desc=Save all SEC contexts into /var/lib/sec/SEC_CONTEXTS on shutdown <br />
 action=lcall %ret -&gt; ( sub { \ <br />
&nbsp;<wbr>Storable::store(\%main::context_list,&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/var/lib/sec/SEC_CONTEXTS&quot;);&nbsp;<wbr>}&nbsp;<wbr>) </p>
<p> However, note that modifying data structures within SEC code is recommended only for advanced users who have carefully studied relevant parts of the code. </p>
<p> Finally, sometimes larger chunks of Perl code have to be used for event processing and correlation. However, writing many lines of code directly into a rule is cumbersome and may decrease its readability. In such cases it is recommended to separate the code into a custom Perl module which is loaded at SEC startup, and use the code through the module interface (see <code><a href="/docs/linux/man/1-perlmod/">perlmod</a></code>(1) for further details): </p>
<p> type=Single <br />
 ptype=SubStr <br />
 pattern=SEC_STARTUP <br />
 context=SEC_INTERNAL_EVENT <br />
 desc=Load the SecStuff module <br />
 action=eval %ret (require &#8216;/usr/local/sec/SecStuff.pm&#8217;); \ <br />
&nbsp;<wbr>if&nbsp;<wbr>%ret&nbsp;<wbr>(&nbsp;<wbr>none&nbsp;<wbr>)&nbsp;<wbr>else&nbsp;<wbr>(&nbsp;<wbr>eval&nbsp;<wbr>%o&nbsp;<wbr><a href="/docs/linux/man/1-exit/">exit</a>(1)&nbsp;<wbr>) </p>
<p> type=Single <br />
 ptype=PerlFunc <br />
 pattern=sub { return SecStuff::my_match($_[0]); } <br />
 desc=event &#8216;$0&#8217; was matched by my_match() <br />
 action=write - %s  </p>
<h2>EXAMPLES</h2>
<h3>Example 1 - a ruleset for Cisco events</h3>
<p> This section presents an example rulebase for managing Cisco devices. It is assumed that the managed devices have syslog logging enabled, and that all syslog messages are sent to a central host and written to log file(s) that are monitored by SEC. </p>
<p> # Set up contexts NIGHT and WEEKEND for nights <br />
 # and weekends. The context NIGHT has a lifetime <br />
 # of 8 hours and the context WEEKEND 2 days </p>
<p> type=Calendar <br />
 time=0 23 * * * <br />
 desc=NIGHT <br />
 action=create %s 28800 </p>
<p> type=Calendar <br />
 time=0 0 * * 6 <br />
 desc=WEEKEND <br />
 action=create %s 172800 </p>
<p> # If a router does not come up within 5 minutes <br />
 # after it was rebooted, generate event <br />
 # &quot;&lt;router&gt; REBOOT FAILURE&quot;. The next rule matches <br />
 # this event, checks the router with ping and sends <br />
 # a notification if there is no response. </p>
<p> type=PairWithWindow <br />
 ptype=RegExp <br />
 pattern=\s([\w.-]+) \d+: %SYS-5-RELOAD <br />
 desc=$1 REBOOT FAILURE <br />
 action=event %s <br />
 ptype2=RegExp <br />
 pattern2=\s$1 \d+: %SYS-5-RESTART <br />
 desc2=%1 successful reboot <br />
 action2=logonly <br />
 window=300 </p>
<p> type=SingleWithScript <br />
 ptype=RegExp <br />
 pattern=^([\w.-]+) REBOOT FAILURE <br />
 script=/bin/ping -c 3 -q $1 <br />
 desc=$1 did not come up after reboot <br />
 action=logonly $1 is pingable after reboot <br />
 action2=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost </p>
<p> # Send a notification if CPU load of a router is too <br />
 # high (two CPUHOG messages are received within 5 <br />
 # minutes); send another notification if the load is <br />
 # normal again (no CPUHOG messages within last 15 <br />
 # minutes). Rule is not active at night or weekend. </p>
<p> type=SingleWith2Thresholds <br />
 ptype=RegExp <br />
 pattern=\s([\w.-]+) \d+: %SYS-3-CPUHOG <br />
 context=!(NIGHT || WEEKEND) <br />
 desc=$1 CPU overload <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=300 <br />
 thresh=2 <br />
 desc2=$1 CPU load normal <br />
 action2=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window2=900 <br />
 thresh2=0 </p>
<p> # If a router interface is in down state for less <br />
 # than 15 seconds, generate event <br />
 # &quot;&lt;router&gt; INTERFACE &lt;interface&gt; SHORT OUTAGE&quot;; <br />
 # otherwise generate event <br />
 # &quot;&lt;router&gt; INTERFACE &lt;interface&gt; DOWN&quot;. </p>
<p> type=PairWithWindow <br />
 ptype=RegExp <br />
 pattern=\s([\w.-]+) \d+: %LINK-3-UPDOWN: Interface ([\w.-]+), changed state to down <br />
 desc=$1 INTERFACE $2 DOWN <br />
 action=event %s <br />
 ptype2=RegExp <br />
 pattern2=\s$1 \d+: %LINK-3-UPDOWN: Interface $2, changed state to up <br />
 desc2=%1 INTERFACE %2 SHORT OUTAGE <br />
 action2=event %s <br />
 window=15 </p>
<p> # If &quot;&lt;router&gt; INTERFACE &lt;interface&gt; DOWN&quot; event is <br />
 # received, send a notification and wait for <br />
 # &quot;interface up&quot; event from the same router interface <br />
 # for the next 24 hours </p>
<p> type=Pair <br />
 ptype=RegExp <br />
 pattern=^([\w.-]+) INTERFACE ([\w.-]+) DOWN <br />
 desc=$1 interface $2 is down <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 ptype2=RegExp <br />
 pattern2=\s$1 \d+: %LINK-3-UPDOWN: Interface $2, changed state to up <br />
 desc2=%1 interface %2 is up <br />
 action2=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=86400 </p>
<p> # If ten &quot;short outage&quot; events have been observed <br />
 # in the window of 6 hours, send a notification </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=^([\w.-]+) INTERFACE ([\w.-]+) SHORT OUTAGE <br />
 desc=Interface $2 at node $1 is unstable <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail root [at] localhost <br />
 window=21600 <br />
 thresh=10  </p>
<h3>Example 2 - hierarchically organized rulesets for iptables and sshd events</h3>
<p> This section presents an example of hierarchically organized rules for processing Linux iptables events from /var/log/messages and SSH login events from /var/log/secure. It is assumed that all rule files reside in the /etc/sec directory and that the rule hierarchy has two levels. The file /etc/sec/main.rules contains first-level Jump rules for matching and parsing events from input files and submitting them to proper rulesets for further processing. All other rule files in the /etc/sec directory contain second-level rules which receive their input from first-level Jump rules. Also, the example assumes that SEC is started with the following command line: </p>
<p> /usr/bin/sec --conf=/etc/sec/*.rules --intcontexts \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>--input=/var/log/messages --input=/var/log/secure </p>
<p> # <br />
 # the content of /etc/sec/main.rules <br />
 # </p>
<p> type=Jump <br />
 context=[ _FILE_EVENT_/var/log/messages ] <br />
 ptype=PerlFunc <br />
 pattern=sub { my(%var); my($line) = $_[0]; \ <br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>($line&nbsp;<wbr>!~&nbsp;<wbr>/kernel: iptables:/g)&nbsp;<wbr>{&nbsp;<wbr>return 0;&nbsp;<wbr>}&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>while&nbsp;<wbr>($line&nbsp;<wbr>=~&nbsp;<wbr>/\G\s*([A-Z]+)(?:=(\S*))?/g)&nbsp;<wbr>{&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$var{$1}&nbsp;<wbr>=&nbsp;<wbr>defined($2)?$2:1;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>return&nbsp;<wbr>\%var;&nbsp;<wbr>} <br />
 varmap=IPTABLES <br />
 desc=parse iptables events and direct to relevant ruleset <br />
 cfset=iptables </p>
<p> type=Jump <br />
 context=[ _FILE_EVENT_/var/log/secure ] <br />
 ptype=RegExp <br />
 pattern=sshd\[(?&lt;pid&gt;\d+)\]: (?&lt;status&gt;Accepted|Failed) \ <br />
 (?&lt;authmethod&gt;[\w-]+) for (?&lt;invuser&gt;invalid user )?\ <br />
 (?&lt;user&gt;[\w-]+) from (?&lt;srcip&gt;[\d.]+) port (?&lt;srcport&gt;\d+) ssh2$ <br />
 varmap=SSH_LOGIN <br />
 desc=parse SSH login events and direct to relevant ruleset <br />
 cfset=ssh-login </p>
<p> type=Jump <br />
 context=[ SSH_EVENT ] <br />
 ptype=TValue <br />
 pattern=True <br />
 desc=direct SSH synthetic events to relevant ruleset <br />
 cfset=ssh-events </p>
<p> # <br />
 # the content of /etc/sec/iptables.rules <br />
 # </p>
<p> type=Options <br />
 procallin=no <br />
 joincfset=iptables </p>
<p> type=SingleWithThreshold <br />
 ptype=Cached <br />
 pattern=IPTABLES <br />
 context=IPTABLES :&gt; ( sub { return exists($_[0]-&gt;{&quot;SYN&quot;}) &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exists($_[0]-&gt;{&quot;FIN&quot;})&nbsp;<wbr>;&nbsp;<wbr>}&nbsp;<wbr>)&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>!SUPPRESS_IP_$+{SRC} <br />
 desc=SYN+FIN flood from host $+{SRC} <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;iptables alert&#8217; root [at] localhost; \ <br />
&nbsp;<wbr>create SUPPRESS_IP_$+{SRC}&nbsp;<wbr>3600 <br />
 window=10 <br />
 thresh=100 </p>
<p> type=SingleWithThreshold <br />
 ptype=Cached <br />
 pattern=IPTABLES <br />
 context=IPTABLES :&gt; ( sub { return exists($_[0]-&gt;{&quot;SYN&quot;}) &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>!exists($_[0]-&gt;{&quot;ACK&quot;})&nbsp;<wbr>;&nbsp;<wbr>}&nbsp;<wbr>)&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>!SUPPRESS_IP_$+{SRC} <br />
 desc=SYN flood from host $+{SRC} <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;iptables alert&#8217; root [at] localhost; \ <br />
&nbsp;<wbr>create SUPPRESS_IP_$+{SRC}&nbsp;<wbr>3600 <br />
 window=10 <br />
 thresh=100 </p>
<p> # <br />
 # the content of /etc/sec/ssh-login.rules <br />
 # </p>
<p> type=Options <br />
 procallin=no <br />
 joincfset=ssh-login </p>
<p> type=Single <br />
 ptype=Cached <br />
 pattern=SSH_LOGIN <br />
 context=SSH_LOGIN :&gt; ( sub { return $_[0]-&gt;{&quot;status&quot;} eq &quot;Failed&quot; &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$_[0]-&gt;{&quot;srcport&quot;}&nbsp;<wbr>&lt;&nbsp;<wbr>1024&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>defined($_[0]-&gt;{&quot;invuser&quot;});&nbsp;<wbr>}&nbsp;<wbr>) <br />
 continue=TakeNext <br />
 desc=Probe of invalid user $+{user} from privileged port of $+{srcip} <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;SSH alert&#8217; root [at] localhost </p>
<p> type=SingleWithThreshold <br />
 ptype=Cached <br />
 pattern=SSH_LOGIN <br />
 context=SSH_LOGIN :&gt; ( sub { return $_[0]-&gt;{&quot;status&quot;} eq &quot;Failed&quot; &amp;&amp; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>defined($_[0]-&gt;{&quot;invuser&quot;});&nbsp;<wbr>}&nbsp;<wbr>) <br />
 desc=Ten login probes for invalid users from $+{srcip} within 60s <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;SSH alert&#8217; root [at] localhost <br />
 thresh=10 <br />
 window=60 </p>
<p> type=PairWithWindow <br />
 ptype=Cached <br />
 pattern=SSH_LOGIN <br />
 context=SSH_LOGIN :&gt; ( sub { return $_[0]-&gt;{&quot;status&quot;} eq &quot;Failed&quot;; } ) <br />
 desc=User $+{user} failed to log in from $+{srcip} within 60s <br />
 action=cevent SSH_EVENT 0 %s <br />
 ptype2=Cached <br />
 pattern2=SSH_LOGIN <br />
 context2=SSH_LOGIN :&gt; \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(&nbsp;<wbr>sub&nbsp;<wbr>{&nbsp;<wbr>return&nbsp;<wbr>$_[0]-&gt;{&quot;status&quot;}&nbsp;<wbr>eq&nbsp;<wbr>&quot;Accepted&quot;;&nbsp;<wbr>}&nbsp;<wbr>)&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$+{user}&nbsp;<wbr>%+{user}&nbsp;<wbr>$+{srcip}&nbsp;<wbr>%+{srcip}&nbsp;<wbr>-&gt;&nbsp;<wbr>\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(&nbsp;<wbr>sub&nbsp;<wbr>{&nbsp;<wbr>return&nbsp;<wbr>$_[0]&nbsp;<wbr>eq&nbsp;<wbr>$_[1]&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>&nbsp;<wbr>$_[2]&nbsp;<wbr>eq&nbsp;<wbr>$_[3];&nbsp;<wbr>}&nbsp;<wbr>&nbsp;<wbr>) <br />
 desc2=User $+{user} logged in successfully from $+{srcip} within 60s <br />
 action2=logonly <br />
 window=60 </p>
<p> # <br />
 # the content of /etc/sec/ssh-events.rules <br />
 # </p>
<p> type=Options <br />
 procallin=no <br />
 joincfset=ssh-events </p>
<p> type=SingleWithThreshold <br />
 ptype=RegExp <br />
 pattern=User ([\w-]+) failed to log in from [\d.]+ within 60s <br />
 desc=Ten login failures for user $1 within 1h <br />
 action=pipe &#8216;%t: %s&#8217; /bin/mail -s &#8216;SSH alert&#8217; root [at] localhost <br />
 thresh=10 <br />
 window=3600  </p>
<h2>ENVIRONMENT</h2>
<p> If the <code>SECRC </code> environment variable is set, SEC expects it to contain the name of its resource file. Resource file lines which are empty or which begin with the number sign (#) are ignored (whitespace may precede #). Each remaining line is appended to the <code>argv</code> array of SEC as a *single* element. Also, the lines are appended to <code>argv</code> in the order they appear in the resource file. Therefore, if the SEC command line option has a value, the option name and the value must either be separated by the equal sign (=) or a newline. Here is a simple resource file example: </p>
<p> # read events from standard input <br />
 --input=- </p>
<p> # rules are stored in /etc/sec/test.conf <br />
 --conf <br />
 /etc/sec/test.conf </p>
<p> Note that although SEC rereads its resource file at the reception of the <code>SIGHUP</code> or <code>SIGABRT</code> signal, adding an option that specifies a certain startup procedure (e.g., <code>--pid</code> or <code>--detach</code>) will not produce the desired effect at runtime. Also note that the resource file content is *not* parsed by shell, therefore shell metacharacters are passed to SEC as-is.  </p>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></dt>
<dd> <p> full restart -- SEC will reinterpret its command line and resource file options, reopen its log and input files, close its output files and sockets (these will be reopened on demand), reload its configuration, and drop *all* event correlation state (all event correlation operations will be terminated, all contexts will be deleted, all action list variables will be erased, etc.). With the <code>--childterm</code> option, SEC will also send the <code>SIGTERM </code> signal to its child processes. </p>
 </dd>
<dt><code>SIGABRT</code></dt>
<dd> <p> soft restart -- SEC will reinterpret its command line and resource file options, reopen its log file, and close its output files and sockets (these will be reopened on demand). If the <code>--keepopen</code> option is specified, previously opened input files will remain open across soft restart, otherwise all input files will be reopened. SEC will (re)load configuration from rule files which have been modified (file modification time returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) has changed) or created after the previous configuration load. SEC will also terminate event correlation operations started from rule files that have been modified or removed after the previous configuration load. Other operations and previously loaded configuration from unmodified rule files will remain intact. Note that on some systems <code>SIGIOT</code> is used in place of <code>SIGABRT</code>. </p>
 </dd>
<dt><code>SIGUSR1</code></dt>
<dd> <p> detailed information about the current state of SEC (performance and rule matching statistics, running event correlation operations, created contexts, etc.) will be written to the SEC dump file. </p>
 </dd>
<dt><code>SIGUSR2</code></dt>
<dd> <p> SEC will reopen its log file (useful for log file rotation), and also close its output files and sockets which will be reopened on demand. </p>
 </dd>
<dt><code>SIGINT</code></dt>
<dd> <p> SEC will increase its logging level by one; if the current level is 6, the level will be set back to 1. Please note this feature is available only if SEC is running non-interactively (e.g., in daemon mode). </p>
 </dd>
<dt><code>SIGTERM</code></dt>
<dd> <p> SEC will terminate gracefully. With the <code>--childterm</code> option, all SEC child processes will receive <code>SIGTERM</code>. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> With some locale settings, single quotes (&#8216;) in this man page might be displayed incorrectly. As a workaround, set the LANG environment variable to C when reading this man page (e.g., env LANG=C man sec).  </p>
<h2>AUTHOR</h2>
<p> Risto Vaarandi (ristov at users d0t s0urcef0rge d0t net)  </p>
<h2>ACKNOWLEDGMENTS</h2>
<p> This work is supported by SEB. The author thanks the following people for supplying software patches, documentation fixes, and suggesting new features: Al Sorrell, Brian Mielke, David Lang, James Brown, Jon Frazier, Mark D. Nagel, Peter Eckel, Rick Casey, and William Gertz. Last but not least, the author expresses his profound gratitute to John P. Rouillard for many great ideas and creative discussions that have helped to develop SEC.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-perlmod/">perlmod</a></code>(1), <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-snmptrap/">snmptrap</a></code>(1), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">CONFIGURATION FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">PATTERNS, PATTERN TYPES AND MATCH VARIABLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">CONTEXTS AND CONTEXT EXPRESSIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">ACTIONS, ACTION LISTS AND ACTION LIST VARIABLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">PARSING ISSUES</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">RULE TYPES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAL">SINGLE RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">SINGLEWITHSCRIPT RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">SINGLEWITHSUPPRESS RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">PAIR RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">PAIRWITHWINDOW RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">SINGLEWITHTHRESHOLD RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">SINGLEWITH2THRESHOLDS RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">EVENTGROUP RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">SUPPRESS RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">CALENDAR RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">JUMP RULE</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">OPTIONS RULE</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAX">EVENT CORRELATION OPERATIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">INPUT PROCESSING AND TIMING</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">INTERNAL EVENTS AND CONTEXTS</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">INTERPROCESS COMMUNICATION</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">PERL INTEGRATION</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">EXAMPLES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbBD">Example 1 - a ruleset for Cisco events</a></dt>
<dd>  </dd>
<dt><a href="#lbBE">Example 2 - hierarchically organized rulesets for iptables and sshd events</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbBF">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbBG">SIGNALS</a></dt>
<dd>  </dd>
<dt><a href="#lbBH">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbBI">AUTHOR</a></dt>
<dd>  </dd>
<dt><a href="#lbBJ">ACKNOWLEDGMENTS</a></dt>
<dd>  </dd>
<dt><a href="#lbBK">SEE ALSO</a></dt>
<dd>  </dd></dl>
