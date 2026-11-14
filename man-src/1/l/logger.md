---
title: "logger(1)"
name: "logger"
section: "1"
letter: "l"
url: "/docs/linux/man/1-logger/"
description: "logger – enter messages into the system log"
---

<h2 class="name">NAME</h2>
<p> logger &#8211; enter messages into the system log </p>
<h2>SYNOPSIS</h2>
<p> <code>logger</code> [options] <i>message</i></p>
<h2>DESCRIPTION</h2>
<p> <code>logger</code> makes entries in the system log. </p>
<p> When the optional <i>message</i> argument is present, it is written to the log. If it is not present, and the <code>-f</code> option is not given either, then standard input is logged.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code>, <code>&#8211;udp</code></p>
<dl>
<dt>
<dd> Use datagrams (UDP) only. By default the connection is tried to the syslog port defined in <i>/etc/services</i>, which is often 514. </p>
<p> See also <code>&#8211;server</code> and <code>&#8211;socket</code> to specify where to connect.</dl>
<p> <code>-e</code>, <code>&#8211;skip-empty</code></p>
<dl>
<dt>
<dd> Ignore empty lines when processing files. An empty line is defined to be a line without any characters. Thus a line consisting only of whitespace is NOT considered empty. Note that when the <code>&#8211;prio-prefix</code> option is specified, the priority is not part of the line. Thus an empty line in this mode is a line that does not have any characters after the priority prefix (e.g., <code>&lt;13&gt;</code>).</dl>
<p> <code>-f</code>, <code>&#8211;file</code> <i>file</i></p>
<dl>
<dt>
<dd> Log the contents of the specified <i>file</i>. This option cannot be combined with a command-line message.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Log the PID of the <code>logger</code> process with each line.</dl>
<p> <code>&#8211;id</code>[<code>=</code><i>id</i>]</p>
<dl>
<dt>
<dd> Log the PID of the <code>logger</code> process with each line. When the optional argument <i>id</i> is specified, then it is used instead of the <code>logger</code> command&#8217;s PID. The use of <code>&#8211;id=$$</code> (PPID) is recommended in scripts that send several messages. </p>
<p> Note that the system logging infrastructure (for example <code>systemd</code> when listening on <i>/dev/log</i>) may follow local socket credentials to overwrite the PID specified in the message. <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) is able to set those socket credentials to the given <i>id</i>, but only if you have root permissions and a process with the specified PID exists, otherwise the socket credentials are not modified and the problem is silently ignored.</dl>
<p> <code>&#8211;journald</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Write a systemd journal entry. The entry is read from the given <i>file</i>, when specified, otherwise from standard input. Each line must begin with a field that is accepted by journald; see <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7) for details. The use of a MESSAGE_ID field is generally a good idea, as it makes finding entries easy. Examples:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
logger --journald &lt;&lt;end
MESSAGE_ID=67feb6ffbaf24c5cbec13c008dd72309
MESSAGE=The dogs bark, but the caravan goes on.
DOGS=bark
CARAVAN=goes on
end
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
logger --journald=entry.txt
</pre>
</dl>
</dl>
<p> Notice that <code>&#8211;journald</code> will ignore values of other options, such as priority. If priority is needed it must be within input, and use PRIORITY field. The simple execution of <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) will display MESSAGE field. Use <code>journalctl &#8211;output json-pretty</code> to see rest of the fields. </p>
<p> + To include newlines in MESSAGE, specify MESSAGE several times. This is handled as a special case, other fields will be stored as an array in the journal if they appear multiple times. </p>
<p> <code>&#8211;msgid</code> <i>msgid</i></p>
<dl>
<dt>
<dd> Sets the <i>RFC 5424</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc5424">https://tools.ietf.org/html/rfc5424</a>&gt; MSGID field. Note that the space character is not permitted inside of <i>msgid</i>. This option is only used if <code>&#8211;rfc5424</code> is specified as well; otherwise, it is silently ignored.</dl>
<p> <code>-n</code>, <code>&#8211;server</code> <i>server</i></p>
<dl>
<dt>
<dd> Write to the specified remote syslog <i>server</i> instead of to the system log socket. Unless <code>&#8211;udp</code> or <code>&#8211;tcp</code> is specified, <code>logger</code> will first try to use UDP, but if this fails a TCP connection is attempted.</dl>
<p> <code>&#8211;no-act</code></p>
<dl>
<dt>
<dd> Causes everything to be done except for writing the log message to the system log, and removing the connection or the journal. This option can be used together with <code>&#8211;stderr</code> for testing purposes.</dl>
<p> <code>&#8211;octet-count</code></p>
<dl>
<dt>
<dd> Use the <i>RFC 6587</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc6587">https://tools.ietf.org/html/rfc6587</a>&gt; octet counting framing method for sending messages. When this option is not used, the default is no framing on UDP, and RFC6587 non-transparent framing (also known as octet stuffing) on TCP.</dl>
<p> <code>-P</code>, <code>&#8211;port</code> <i>port</i></p>
<dl>
<dt>
<dd> Use the specified <i>port</i>. When this option is not specified, the port defaults to syslog for udp and to syslog-conn for tcp connections.</dl>
<p> <code>-p</code>, <code>&#8211;priority</code> <i>priority</i></p>
<dl>
<dt>
<dd> Enter the message into the log with the specified <i>priority</i>. The priority may be specified numerically or as a <i>facility</i>.<i>level</i> pair. For example, <code>-p local3.info</code> logs the message as informational in the local3 facility. The default is <code>user.notice</code>.</dl>
<p> <code>&#8211;prio-prefix</code></p>
<dl>
<dt>
<dd> Look for a syslog prefix on every line read from standard input. This prefix is a decimal number within angle brackets that encodes both the facility and the level. The number is constructed by multiplying the facility by 8 and then adding the level. For example, <code>local0.info</code>, meaning facility=16 and level=6, becomes <code>&lt;134&gt;</code>. </p>
<p> If the prefix contains no facility, the facility defaults to what is specified by the <code>-p</code> option. Similarly, if no prefix is provided, the line is logged using the <i>priority</i> given with <code>-p</code>. </p>
<p> This option doesn&#8217;t affect a command-line message.</dl>
<p> <code>&#8211;rfc3164</code></p>
<dl>
<dt>
<dd> Use the <i>RFC 3164</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc3164">https://tools.ietf.org/html/rfc3164</a>&gt; BSD syslog protocol to submit messages to a remote server.</dl>
<p> <code>&#8211;rfc5424</code>[<code>=</code><i>without</i>]</p>
<dl>
<dt>
<dd> Use the <i>RFC 5424</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc5424">https://tools.ietf.org/html/rfc5424</a>&gt; syslog protocol to submit messages to a remote server. The optional <i>without</i> argument can be a comma-separated list of the following values: <code>notq</code>, <code>notime</code>, <code>nohost</code>. </p>
<p> The <code>notq</code> value suppresses the time-quality structured data from the submitted message. The time-quality information shows whether the local clock was synchronized plus the maximum number of microseconds the timestamp might be off. The time quality is also automatically suppressed when <code>&#8211;sd-id timeQuality</code> is specified. </p>
<p> The <code>notime</code> value (which implies <code>notq</code>) suppresses the complete sender timestamp that is in ISO-8601 format, including microseconds and timezone. </p>
<p> The <code>nohost</code> value suppresses <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2) information from the message header. </p>
<p> The RFC 5424 protocol has been the default for <code>logger</code> since version 2.26.</dl>
<p> <code>-s</code>, <code>&#8211;stderr</code></p>
<dl>
<dt>
<dd> Output the message to standard error as well as to the system log.</dl>
<p> <code>&#8211;sd-id</code> <i>name</i>[<code>@</code><i>digits</i>]</p>
<dl>
<dt>
<dd> Specifies a structured data element ID for an RFC 5424 message header. The option has to be used before <code>&#8211;sd-param</code> to introduce a new element. The number of structured data elements is unlimited. The ID (<i>name</i> plus possibly <code>@</code><i>digits</i>) is case-sensitive and uniquely identifies the type and purpose of the element. The same ID must not exist more than once in a message. The <code>@</code><i>digits</i> part is required for user-defined non-standardized IDs. </p>
<p> <code>logger</code> currently generates the <code>timeQuality</code> standardized element only. RFC 5424 also describes the elements <code>origin</code> (with parameters ip, enterpriseId, software and swVersion) and <code>meta</code> (with parameters sequenceId, sysUpTime and language). These element IDs may be specified without the <code>@</code><i>digits</i> suffix.</dl>
<p> <code>&#8211;sd-param</code> <i>name</i>=<i>value</i></p>
<dl>
<dt>
<dd> Specifies a structured data element parameter, a name and value pair. The option has to be used after <code>&#8211;sd-id</code> and may be specified more than once for the same element. Note that the quotation marks around <i>value</i> are required and must be escaped on the command line. </p>
<dl>
<dt>
<dd>
<pre><code>
logger-- rfc5424-- sd - id zoo @123 --sd - param tiger = "hungry" --sd - param zebra = "running" --sd - id manager @123 --sd - param onMeeting = "yes"
                                                                                                                                                 "this is message"
</code></pre>
</dl>
<p> produces: </p>
<p> <code>&lt;13&gt;1 2015-10-01T14:07:59.168662+02:00 ws kzak &#8211; &#8211; [timeQuality tzKnown=&quot;1&quot; isSynced=&quot;1&quot; syncAccuracy=&quot;218616&quot;][zoo@123 tiger=&quot;hungry&quot; zebra=&quot;running&quot;][manager@123 onMeeting=&quot;yes&quot;] this is message</code></dl>
<p> <code>-S</code>, <code>&#8211;size</code> <i>size</i></p>
<dl>
<dt>
<dd> Sets the maximum permitted message size to <i>size</i>. The default is 1KiB characters, which is the limit traditionally used and specified in RFC 3164. With RFC 5424, this limit has become flexible. A good assumption is that RFC 5424 receivers can at least process 4KiB messages. </p>
<p> Most receivers accept messages larger than 1KiB over any type of syslog protocol. As such, the <code>&#8211;size</code> option affects <code>logger</code> in all cases (not only when <code>&#8211;rfc5424</code> was used). </p>
<p> Note: the message-size limit limits the overall message size, including the syslog header. Header sizes vary depending on the selected options and the hostname length. As a rule of thumb, headers are usually not longer than 50 to 80 characters. When selecting a maximum message size, it is important to ensure that the receiver supports the max size as well, otherwise messages may become truncated. Again, as a rule of thumb two to four KiB message size should generally be OK, whereas anything larger should be verified to work.</dl>
<p> <code>&#8211;socket-errors</code>[<code>=</code><i>mode</i>]</p>
<dl>
<dt>
<dd> Print errors about Unix socket connections. The <i>mode</i> can be a value of <code>off</code>, <code>on</code>, or <code>auto</code>. When the mode is <code>auto</code>, then <code>logger</code> will detect if the init process is <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), and if so assumption is made <i>/dev/log</i> can be used early at boot. Other init systems lack of <i>/dev/log</i> will not cause errors that is identical with messaging using <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3) system call. The <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) before version 2.26 used openlog, and hence was unable to detected loss of messages sent to Unix sockets. </p>
<p> The default mode is <code>auto</code>. When errors are not enabled lost messages are not communicated and will result to successful exit status of <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) invocation.</dl>
<p> <code>-T</code>, <code>&#8211;tcp</code></p>
<dl>
<dt>
<dd> Use stream (TCP) only. By default the connection is tried to the <i>syslog-conn</i> port defined in <i>/etc/services</i>, which is often <i>601</i>. </p>
<p> See also <code>&#8211;server</code> and <code>&#8211;socket</code> to specify where to connect.</dl>
<p> <code>-t</code>, <code>&#8211;tag</code> <i>tag</i></p>
<dl>
<dt>
<dd> Mark every line to be logged with the specified <i>tag</i>. The default tag is the name of the user logged in on the terminal (or a user name based on effective user ID).</dl>
<p> <code>-u</code>, <code>&#8211;socket</code> <i>socket</i></p>
<dl>
<dt>
<dd> Write to the specified <i>socket</i> instead of to the system log socket.</dl>
<p> <code>&#8212;</code></p>
<dl>
<dt>
<dd> End the argument list. This allows the <i>message</i> to start with a hyphen (-).</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>logger</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>FACILITIES AND LEVELS</h2>
<p> Valid facility names are: </p>
<p> <code>auth</code><br />
 <code>authpriv</code> for security information of a sensitive nature<br />
 <code>cron</code> </p>
<p> <code>daemon</code><br />
 <code>ftp</code><br />
 <code>kern</code> cannot be generated from userspace process, automatically converted to <code>user</code> </p>
<p> <code>lpr</code><br />
 <code>mail</code><br />
 <code>news</code><br />
 <code>syslog</code><br />
 <code>user</code><br />
 <code>uucp</code><br />
 <code>local0</code><br />
 to<br />
 <code>local7</code><br />
 <code>security</code> deprecated synonym for <code>auth</code> </p>
<p> Valid level names are: </p>
<p> <code>emerg</code><br />
 <code>alert</code><br />
 <code>crit</code><br />
 <code>err</code><br />
 <code>warning</code><br />
 <code>notice</code><br />
 <code>info</code><br />
 <code>debug</code><br />
 <code>panic</code> deprecated synonym for <code>emerg</code><br />
 <code>error</code> deprecated synonym for <code>err</code><br />
 <code>warn</code> deprecated synonym for <code>warning</code> </p>
<p> For the priority order and intended purposes of these facilities and levels, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>CONFORMING TO</h2>
<p> The <code>logger</code> command is expected to be IEEE Std 1003.2 (&quot;POSIX.2&quot;) compatible.</p>
<h2>EXAMPLES</h2>
<p> <code>logger System rebooted</code> <code>logger -p local0.notice -t HOSTIDM -f /dev/idmc</code> <code>logger -n loghost.example.com System rebooted</code></p>
<h2>AUTHORS</h2>
<p> The <code>logger</code> command was originally written by University of California in 1983-1993 and later rewritten by and</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>logger</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
