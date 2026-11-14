---
title: "sudo_logsrv-proto(5)"
name: "sudo_logsrv-proto"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudo_logsrv-proto/"
description: "sudo_logsrv.proto – Sudo log server protocol"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo_logsrv.proto</code> &#8211; Sudo log server protocol</p>
<h2>Description</h2>
<p>Starting with version 1.9.0, <code>sudo</code> supports sending event and I/O logs to a log server. The protocol used is written in Google&#8217;s Protocol Buffers domain specific language. The Sx EXAMPLES section includes a complete description of the protocol in Protocol Buffers format. </p>
<p> Because there is no way to determine message boundaries when using Protocol Buffers, the wire size of each message is sent immediately preceding the message itself as a 32-bit unsigned integer in network byte order. This is referred to as &#8220;length-prefix framing&#8221; and is how Google suggests handling the lack of message delimiters. </p>
<p> The protocol is made up of two basic messages, <i>ClientMessage</i> and <i>ServerMessage</i> described below. The server must accept messages up to two megabytes in size. The server may return an error if the client tries to send a message larger than two megabytes.</p>
<h2>Client Messages</h2>
<p>A <i>ClientMessage</i> is a container used to encapsulate all the possible message types a client may send to the server. </p>
<pre>message ClientMessage {
 oneof type {
 AcceptMessage accept_msg = 1;
 RejectMessage reject_msg = 2;
 ExitMessage exit_msg = 3;
 RestartMessage restart_msg = 4;
 AlertMessage alert_msg = 5;
 IoBuffer ttyin_buf = 6;
 IoBuffer ttyout_buf = 7;
 IoBuffer stdin_buf = 8;
 IoBuffer stdout_buf = 9;
 IoBuffer stderr_buf = 10;
 ChangeWindowSize winsize_event = 11;
 CommandSuspend suspend_event = 12;
 ClientHello hello_msg = 13;
 }
}</pre>
<p>The different <i>ClientMessage</i> sub-messages the client may sent to the server are described below.</p>
<h3>TimeSpec</h3>
<pre>message TimeSpec {
 int64 tv_sec = 1;
 int32 tv_nsec = 2;
}</pre>
<p>A <i>TimeSpec</i> is the equivalent of a POSIX <code>struct timespec</code> containing seconds and nanoseconds members. The <i>tv_sec</i> member is a 64-bit integer to support dates after the year 2038.</p>
<h3>InfoMessage</h3>
<pre>message InfoMessage {
 message StringList {
 repeated string strings = 1;
 }
 message NumberList {
 repeated int64 numbers = 1;
 }
 string key = 1;
 oneof value {
 int64 numval = 2;
 string strval = 3;
 StringList strlistval = 4;
 NumberList numlistval = 5;
 }
}</pre>
<p>An <i>InfoMessage</i> is used to represent information about the invoking user as well as the execution environment the command runs in the form of key-value pairs. The key is always a string but the value may be a 64-bit integer, a string, an array of strings, or an array of 64-bit integers. The event log data is composed of <i>InfoMessage</i> entries. See the Sx EVENT LOG VARIABLES section for more information.</p>
<h3>ClientHello hello_msg</h3>
<pre>message ClientHello {
 string client_id = 1;
}</pre>
<p>A <i>ClientHello</i> message consists of client information that may be sent to the server when the client first connects.</p>
<dl>
<dt><code>client_id</code></p>
<dd>A free-form client description. This usually includes the name and version of the client implementation.</dl>
<h3>AcceptMessage accept_msg</h3>
<pre>message AcceptMessage {
 TimeSpec submit_time = 1;
 repeated InfoMessage info_msgs = 2;
 bool expect_iobufs = 3;
}</pre>
<p>An <i>AcceptMessage</i> is sent by the client when a command is allowed by the security policy. It contains the following members:</p>
<dl>
<dt><code>submit_time</code></p>
<dd>The wall clock time when the command was submitted to the security policy.</p>
<dt><code>info_msgs</code></p>
<dd>An array of <i>InfoMessage</i> describing the user who submitted the command as well as the execution environment of the command. This information is used to generate an event log entry and may also be used by server to determine where and how the I/O log is stored.</p>
<dt><code>expect_iobufs</code></p>
<dd>Set to true if the server should expect <i>IoBuffer</i> messages to follow (for I/O logging) or false if the server should only store the event log.</dl>
<p> If an <i>AcceptMessage</i> is sent, the client must not send a <i>RejectMessage</i> or <i>RestartMessage</i></p>
<h3>RejectMessage reject_msg</h3>
<pre>message RejectMessage {
 TimeSpec submit_time = 1;
 string reason = 2;
 repeated InfoMessage info_msgs = 3;
}</pre>
<p>A <i>RejectMessage</i> is sent by the client when a command is denied by the security policy. It contains the following members:</p>
<dl>
<dt><code>submit_time</code></p>
<dd>The wall clock time when the command was submitted to the security policy.</p>
<dt><code>reason</code></p>
<dd>The reason the security policy gave for denying the command.</p>
<dt><code>info_msgs</code></p>
<dd>An array of <i>InfoMessage</i> describing the user who submitted the command as well as the execution environment of the command. This information is used to generate an event log entry.</dl>
<p> If a <i>RejectMessage</i> is sent, the client must not send an <i>AcceptMessage</i> or <i>RestartMessage</i></p>
<h3>ExitMessage exit_msg</h3>
<pre>message ExitMessage {
 TimeSpec run_time = 1;
 int32 exit_value = 2;
 bool dumped_core = 3;
 string signal = 4;
 string error = 5;
}</pre>
<p>An <i>ExitMessage</i> is sent by the client after the command has exited or has been terminated by a signal. It contains the following members:</p>
<dl>
<dt><code>run_time</code></p>
<dd>The total amount of elapsed time since the command started, calculated using a monotonic clock where possible. This is not the wall clock time.</p>
<dt><code>exit_value</code></p>
<dd>The command&#8217;s exit value in the range 0-255.</p>
<dt><code>dumped_core</code></p>
<dd>True if the command was terminated by a signal and dumped core.</p>
<dt><code>signal</code></p>
<dd>If the command was terminated by a signal, this is set to the name of the signal without the leading &#8220;SIG&#8221; For example, <code>INT</code> <code>TERM</code> <code>KILL</code> <code>SEGV</code></p>
<dt><code>error</code></p>
<dd>A message from the client indicating that the command was terminated unexpectedly due to an error.</dl>
<p> When performing I/O logging, the client should wait for a <i>commit_point</i> corresponding to the final <i>IoBuffer</i> before closing the connection unless the final <i>commit_point</i> has already been received.</p>
<h3>RestartMessage restart_msg</h3>
<pre>message RestartMessage {
 string log_id = 1;
 TimeSpec resume_point = 2;
}</pre>
<p>A <i>RestartMessage</i> is sent by the client to resume sending an existing I/O log that was previously interrupted. It contains the following members:</p>
<dl>
<dt><code>log_id</code></p>
<dd>The the server-side name for an I/O log that was previously sent to the client by the server. This may be a path name on the server or some other kind of server-side identifier.</p>
<dt><code>resume_point</code></p>
<dd>The point in time after which to resume the I/O log. This is in the form of a <i>TimeSpec</i> representing the amount of time since the command started, not the wall clock time. The <i>resume_point</i> should correspond to a <i>commit_point</i> previously sent to the client by the server. If the server receives a <i>RestartMessage</i> containing a <i>resume_point</i> it has not previously seen, an error will be returned to the client and the connection will be dropped.</dl>
<p> If a <i>RestartMessage</i> is sent, the client must not send an <i>AcceptMessage</i> or <i>RejectMessage</i></p>
<h3>AlertMessage alert_msg</h3>
<pre>message AlertMessage {
 TimeSpec alert_time = 1;
 string reason = 2;
 repeated InfoMessage info_msgs = 3;
}</pre>
<p>An <i>AlertMessage</i> is sent by the client to indicate a problem detected by the security policy while the command is running that should be stored in the event log. It contains the following members:</p>
<dl>
<dt><code>alert_time</code></p>
<dd>The wall clock time when the alert occurred.</p>
<dt><code>reason</code></p>
<dd>The reason for the alert.</p>
<dt><code>info_msgs</code></p>
<dd>An optional array of <i>InfoMessage</i> describing the user who submitted the command as well as the execution environment of the command. This information is used to generate an event log entry.</dl>
<h3>IoBuffer ttyin_buf | ttyout_buf | stdin_buf | stdout_buf | stderr_buf</h3>
<pre>message IoBuffer {
 TimeSpec delay = 1;
 bytes data = 2;
}</pre>
<p>An <i>IoBuffer</i> is used to represent data from terminal input, terminal output, standard input, standard output, or standard error. It contains the following members:</p>
<dl>
<dt><code>delay</code></p>
<dd>The elapsed time since the last record in the form of a <i>TimeSpec</i> The <i>delay</i> should be calculated using a monotonic clock where possible.</p>
<dt><code>data</code></p>
<dd>The binary I/O log data from terminal input, terminal output, standard input, standard output, or standard error.</dl>
<h3>ChangeWindowSize winsize_event</h3>
<pre>message ChangeWindowSize {
 TimeSpec delay = 1;
 int32 rows = 2;
 int32 cols = 3;
}</pre>
<p>A <i>ChangeWindowSize</i> message is sent by the client when the terminal running the command changes size. It contains the following members:</p>
<dl>
<dt><code>delay</code></p>
<dd>The elapsed time since the last record in the form of a <i>TimeSpec</i> The <i>delay</i> should be calculated using a monotonic clock where possible.</p>
<dt><code>rows</code></p>
<dd>The new number of terminal rows.</p>
<dt><code>cols</code></p>
<dd>The new number of terminal columns.</dl>
<h3>CommandSuspend suspend_event</h3>
<pre>message CommandSuspend {
 TimeSpec delay = 1;
 string signal = 2;
}</pre>
<p>A <i>CommandSuspend</i> message is sent by the client when the command is either suspended or resumed. It contains the following members:</p>
<dl>
<dt><code>delay</code></p>
<dd>The elapsed time since the last record in the form of a <i>TimeSpec</i> The <i>delay</i> should be calculated using a monotonic clock where possible.</p>
<dt><code>signal</code></p>
<dd>The signal name without the leading &#8220;SIG&#8221; For example, <code>STOP</code> <code>TSTP</code> <code>CONT</code></dl>
<h2>Server Messages</h2>
<p>A <i>ServerMessage</i> is a container used to encapsulate all the possible message types the server may send to a client. </p>
<pre>message ServerMessage {
 oneof type {
 ServerHello hello = 1;
 TimeSpec commit_point = 2;
 string log_id = 3;
 string error = 4;
 string abort = 5;
 }
}</pre>
<p>The different <i>ServerMessage</i> sub-messages the server may sent to the client are described below.</p>
<h3>ServerHello hello</h3>
<pre>message ServerHello {
 string server_id = 1;
 string redirect = 2;
 repeated string servers = 3;
 bool subcommands = 4;
}</pre>
<p>The <i>ServerHello</i> message consists of server information sent when the client first connects. It contains the following members:</p>
<dl>
<dt><code>server_id</code></p>
<dd>A free-form server description. Usually this includes the name and version of the implementation running on the log server. This member is always present.</p>
<dt><code>redirect</code></p>
<dd>A host and port separated by a colon (`:&#8217; ) that the client should connect to instead. The host may be a host name, an IPv4 address, or an IPv6 address in square brackets. This may be used for server load balancing. The server will disconnect after sending the <i>ServerHello</i> when it includes a <code>redirect</code></p>
<dt><code>servers</code></p>
<dd>A list of other known log servers. This can be used to implement log server redundancy and allows the client to discover all other log servers simply by connecting to one known server. This member may be omitted when there is only a single log server.</p>
<dt><code>subcommands</code></p>
<dd>If set, the server supports logging additional commands during a session. The client may send an <i>AcceptMessage</i> or <i>RejectMessage</i> when <code>sudo</code> is running in <i>intercept</i> mode. In this mode, commands spawned from the initial command authorized by <code>sudo</code> are subject to policy restrictions and/or are logged. If <i>subcommands</i> is false, the client must not attempt to log additional commands.</dl>
<h3>TimeSpec commit_point</h3>
<p>A periodic time stamp sent by the server to indicate when I/O log buffers have been committed to storage. This message is not sent after every <i>IoBuffer</i> but rather at a server-configurable interval. When the server receives an <i>ExitMessage</i> it will respond with a <i>commit_point</i> corresponding to the last received <i>IoBuffer</i> before closing the connection.</p>
<h3>string log_id</h3>
<p>The server-side ID of the I/O log being stored, sent in response to an <i>AcceptMessage</i> where <i>expect_iobufs</i> is true.</p>
<h3>string error</h3>
<p>A fatal server-side error. The server will close the connection after sending the <i>error</i> message.</p>
<h3>string abort</h3>
<p>An <i>abort</i> message from the server indicates that the client should kill the command and terminate the session. It may be used to implement simple server-side policy. The server will close the connection after sending the <i>abort</i> message.</p>
<h2>Protocol flow of control</h2>
<p>The expected protocol flow is as follows: </p>
<ol>
<li> Client connects to the first available server. If the client is configured to use TLS, a TLS handshake will be attempted.
<li> Client sends <i>ClientHello</i> This is currently optional but allows the server to detect a non-TLS connection on the TLS port.
<li> Server sends <i>ServerHello</i>
<li> Client responds with either <i>AcceptMessage</i> <i>RejectMessage</i> or <i>RestartMessage</i>
<li> If client sent a <i>AcceptMessage</i> with <i>expect_iobufs</i> set, server creates a new I/O log and responds with a <i>log_id</i>
<li> Client sends zero or more <i>IoBuffer</i> messages.
<li> Server periodically responds to <i>IoBuffer</i> messages with a <i>commit_point</i>
<li> Client sends an <i>ExitMessage</i> when the command exits or is killed.
<li> Server sends the final <i>commit_point</i> if one is pending.
<li> Server closes the connection. After receiving the final <i>commit_point</i> the client shuts down its side of the TLS connection if TLS is in use, and closes the connection.
<li> Server shuts down its side of the TLS connection if TLS is in use, and closes the connection. </ol>
<p> At any point, the server may send an <i>error</i> or <i>abort</i> message to the client at which point the server will close the connection. If an <i>abort</i> message is received, the client should terminate the running command.</p>
<h2>Event Log Variables</h2>
<p><i>AcceptMessage</i> <i>AlertMessage</i> and <i>RejectMessage</i> classes contain an array of <i>InfoMessage</i> that should contain information about the user who submitted the command as well as information about the execution environment of the command if it was accepted. </p>
<p> Some variables have a <i>client</i> <i>run</i> or <i>submit</i> prefix. These prefixes are used to eliminate ambiguity for variables that could apply to the client program, the user submitting the command, or the command being run. Variables with a <i>client</i> prefix pertain to the program performing the connection to the log server, for example <code>sudo</code> Variables with a <i>run</i> prefix pertain to the command that the user requested be run. Variables with a <i>submit</i> prefix pertain to the user submitting the request (the user running <code>sudo</code> ) </p>
<p> The following <i>InfoMessage</i> entries are required:</p>
<dl>
<dt><code>Key Ta </code><code>Type Ta </code><code>Description</code></p>
<dd>
<dt><code>command Ta </code>string Ta command that was submitted</p>
<dd>
<dt><code>runuser Ta </code>string Ta name of user the command was run as</p>
<dd>
<dt><code>submithost Ta </code>string Ta name of host the command was submitted on</p>
<dd>
<dt><code>submituser Ta </code>string Ta name of user submitting the command</p>
<dd></dl>
<p> The following <i>InfoMessage</i> entries are recognized, but not required:</p>
<dl>
<dt><code>Key Ta </code><code>Type Ta </code><code>Description</code></p>
<dd>
<dt><code>clientargv Ta </code>StringList Ta client&#8217;s original argument vector</p>
<dd>
<dt><code>clientpid Ta </code>int64 Ta client&#8217;s process ID</p>
<dd>
<dt><code>clientppid Ta </code>int64 Ta client&#8217;s parent process ID</p>
<dd>
<dt><code>clientsid Ta </code>int64 Ta client&#8217;s terminal session ID</p>
<dd>
<dt><code>columns Ta </code>int64 Ta number of columns in the terminal</p>
<dd>
<dt><code>lines Ta </code>int64 Ta number of lines in the terminal</p>
<dd>
<dt><code>runargv Ta </code>StringList Ta argument vector of command to run</p>
<dd>
<dt><code>runchroot Ta </code>string Ta root directory of command to run</p>
<dd>
<dt><code>runcwd Ta </code>string Ta running command&#8217;s working directory</p>
<dd>
<dt><code>runenv Ta </code>StringList Ta the running command&#8217;s environment</p>
<dd>
<dt><code>rungid Ta </code>int64 Ta primary group-ID of the command</p>
<dd>
<dt><code>rungids Ta </code>NumberList Ta supplementary group-IDs for the command</p>
<dd>
<dt><code>rungroup Ta </code>string Ta primary group name of the command</p>
<dd>
<dt><code>rungroups Ta </code>StringList Ta supplementary group names for the command</p>
<dd>
<dt><code>runuid Ta </code>int64 Ta run user&#8217;s user-ID</p>
<dd>
<dt><code>submitcwd Ta </code>string Ta submit user&#8217;s current working directory</p>
<dd>
<dt><code>submitenv Ta </code>StringList Ta the submit user&#8217;s environment</p>
<dd>
<dt><code>submitgid Ta </code>int64 Ta submit user&#8217;s primary group-ID</p>
<dd>
<dt><code>submitgids Ta </code>NumberList Ta submit user&#8217;s supplementary group-IDs</p>
<dt><code>submitgroup Ta </code>string Ta submitting user&#8217;s primary group name</p>
<dd>
<dd>
<dt><code>submitgroups Ta </code>StringList Ta submit user&#8217;s supplementary group names</p>
<dd>
<dt><code>submituid Ta </code>int64 Ta submit user&#8217;s user-ID</p>
<dd>
<dt><code>ttyname Ta </code>string Ta the terminal the command was submitted from</p>
<dd></dl>
<p> The server must accept other variables not listed above but may ignore them.</p>
<h2>Examples</h2>
<p>The Protocol Buffers description of the log server protocol is included in full below. Note that this uses the newer &#8220;proto3&#8221; syntax. </p>
<pre>syntax = &quot;proto3&quot;;
/*
 * Client message to the server. Messages on the wire are
 * prefixed with a 32-bit size in network byte order.
 */
message ClientMessage {
 oneof type {
 AcceptMessage accept_msg = 1;
 RejectMessage reject_msg = 2;
 ExitMessage exit_msg = 3;
 RestartMessage restart_msg = 4;
 AlertMessage alert_msg = 5;
 IoBuffer ttyin_buf = 6;
 IoBuffer ttyout_buf = 7;
 IoBuffer stdin_buf = 8;
 IoBuffer stdout_buf = 9;
 IoBuffer stderr_buf = 10;
 ChangeWindowSize winsize_event = 11;
 CommandSuspend suspend_event = 12;
 }
}
/* Equivalent of POSIX struct timespec */
message TimeSpec {
 int64 tv_sec = 1; /* seconds */
 int32 tv_nsec = 2; /* nanoseconds */
}
/* I/O buffer with keystroke data */
message IoBuffer {
 TimeSpec delay = 1; /* elapsed time since last record */
 bytes data = 2; /* keystroke data */
}
/*
 * Key/value pairs, like Privilege Manager struct info.
 * The value may be a number, a string, or a list of strings.
 */
message InfoMessage {
 message StringList {
 repeated string strings = 1;
 }
 message NumberList {
 repeated int64 numbers = 1;
 }
 string key = 1;
 oneof value {
 int64 numval = 2;
 string strval = 3;
 StringList strlistval = 4;
 NumberList numlistval = 5;
 }
}
/*
 * Event log data for command accepted by the policy.
 */
message AcceptMessage {
 TimeSpec submit_time = 1; /* when command was submitted */
 repeated InfoMessage info_msgs = 2; /* key,value event log data */
 bool expect_iobufs = 3; /* true if I/O logging enabled */
}
/*
 * Event log data for command rejected by the policy.
 */
message RejectMessage {
 TimeSpec submit_time = 1; /* when command was submitted */
 string reason = 2; /* reason command was rejected */
 repeated InfoMessage info_msgs = 3; /* key,value event log data */
}
/* Message sent by client when command exits. */
/* Might revisit runtime and use end_time instead */
message ExitMessage {
 TimeSpec run_time = 1; /* total elapsed run time */
 int32 exit_value = 2; /* 0-255 */
 bool dumped_core = 3; /* true if command dumped core */
 string signal = 4; /* signal name if killed by signal */
 string error = 5; /* if killed due to other error */
}
/* Alert message, policy module-specific. */
message AlertMessage {
 TimeSpec alert_time = 1; /* time alert message occurred */
 string reason = 2; /* policy alert error string */
 repeated InfoMessage info_msgs = 3; /* key,value event log data */
}
/* Used to restart an existing I/O log on the server. */
message RestartMessage {
 string log_id = 1; /* ID of log being restarted */
 TimeSpec resume_point = 2; /* resume point (elapsed time) */
}
/* Window size change event. */
message ChangeWindowSize {
 TimeSpec delay = 1; /* elapsed time since last record */
 int32 rows = 2; /* new number of rows */
 int32 cols = 3; /* new number of columns */
}
/* Command suspend/resume event. */
message CommandSuspend {
 TimeSpec delay = 1; /* elapsed time since last record */
 string signal = 2; /* signal that caused suspend/resume */
}
/*
 * Server messages to the client. Messages on the wire are
 * prefixed with a 32-bit size in network byte order.
 */
message ServerMessage {
 oneof type {
 ServerHello hello = 1; /* server hello message */
 TimeSpec commit_point = 2; /* cumulative time of records stored */
 string log_id = 3; /* ID of server-side I/O log */
 string error = 4; /* error message from server */
 string abort = 5; /* abort message, kill command */
 }
}
/* Hello message from server when client connects. */
message ServerHello {
 string server_id = 1; /* free-form server description */
 string redirect = 2; /* optional redirect if busy */
 repeated string servers = 3; /* optional list of known servers */
}</pre>
<h2>See Also</h2>
<p>sudo_logsrvd.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8), sudo_logsrvd8</p>
<dl>
<dd><i>Protocol Buffers</i></dl>
<h2>History</h2>
<p>See the HISTORY file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/history.html)">https://www.sudo.ws/history.html)</a> for a brief history of sudo.</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
