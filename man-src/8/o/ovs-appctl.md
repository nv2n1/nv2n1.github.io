---
title: "ovs-appctl(8)"
name: "ovs-appctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-appctl/"
description: "ovs-appctl – utility for configuring running Open vSwitch daemons"
---

<p>ovs-appctl &#8211; utility for configuring running Open vSwitch daemons</p>
<h2>Synopsis</h2>
<p><code>ovs-appctl</code> [<code>&#8211;target=</code><i>target</i> | <code>-t</code> <i>target</i>] <i>command </i>[<i>arg</i>&#8230;]<br />
 <code>ovs-appctl</code> &#8211;help<br />
 <code>ovs-appctl</code> &#8211;version</p>
<h2>Description</h2>
<p>Open vSwitch daemons accept certain commands at runtime to control their behavior and query their settings. Every daemon accepts a common set of commands documented under <code>COMMON COMMANDS</code> below. Some daemons support additional commands documented in their own manpages. <code>ovs-vswitchd</code> in particular accepts a number of additional commands documented in <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8). </p>
<p> The <code>ovs-appctl</code> program provides a simple way to invoke these commands. The command to be sent is specified on <code>ovs-appctl</code>&#8216;s command line as non-option arguments. <code>ovs-appctl</code> sends the command and prints the daemon&#8217;s response on standard output. </p>
<p> In normal use only a single option is accepted:</p>
<dl>
<dt><code>-t </code><i>target</i></p>
<dd>
<dt><code>&#8211;target=</code><i>target</i></p>
<dd>Tells <code>ovs-appctl</code> which daemon to contact.</p>
<dd>If <i>target</i> begins with <code>/</code> it must name a Unix domain socket on which an Open vSwitch daemon is listening for control channel connections. By default, each daemon listens on a Unix domain socket named <code>/var/run/openvswitch/</code><i>program</i><code>.</code><i>pid</i><code>.ctl</code>, where <i>program</i> is the program&#8217;s name and <i>pid</i> is its process ID. For example, if <code>ovs-vswitchd</code> has PID 123, it would listen on <code>/var/run/openvswitch/ovs-vswitchd.123.ctl</code>.</p>
<dd>Otherwise, <code>ovs-appctl</code> looks for a pidfile, that is, a file whose contents are the process ID of a running process as a decimal number, named <code>/var/run/openvswitch/</code><i>target</i><code>.pid</code>. (The <code>&#8211;pidfile</code> option makes an Open vSwitch daemon create a pidfile.) <code>ovs-appctl</code> reads the pidfile, then looks for a Unix socket named <code>/var/run/openvswitch/</code><i>target</i><code>.</code><i>pid</i><code>.ctl</code>, where <i>pid</i> is replaced by the process ID read from the pidfile, and uses that file as if it had been specified directly as the target.</p>
<dd>On Windows, <i>target</i> can be an absolute path to a file that contains a localhost TCP port on which an Open vSwitch daemon is listening for control channel connections. By default, each daemon writes the TCP port on which it is listening for control connection into the file <i>program</i><code>.ctl</code> located inside the configured <i>OVS_RUNDIR</i> directory. If <i>target</i> is not an absolute path, <code>ovs-appctl</code> looks for a file named <i>target</i><code>.ctl</code> in the configured <i>OVS_RUNDIR</i> directory.</p>
<dd>The default target is <code>ovs-vswitchd</code>.</dl>
<h2>Common Commands</h2>
<p>Every Open vSwitch daemon supports a common set of commands, which are documented in this section.</p>
<h3>General Commands</h3>
<p>These commands display daemon-specific commands and the running version. Note that these commands are different from the <code>&#8211;help</code> and <code>&#8211;version</code> options that return information about the <code>ovs-appctl</code> utility itself.</p>
<dl>
<dt><code>list-commands</code></p>
<dd>Lists the commands supported by the target.</p>
<dt><code>version</code></p>
<dd>Displays the version and compilation date of the target.</dl>
<h3>Logging Commands</h3>
<p>Open vSwitch has several log levels. The highest-severity log level is:</p>
<dl>
<dt><code>off</code></p>
<dd>No message is ever logged at this level, so setting a logging destination&#8217;s log level to <code>off</code> disables logging to that destination.</dl>
<p> The following log levels, in order of descending severity, are available:</p>
<dl>
<dt><code>emer</code></p>
<dd>A major failure forced a process to abort.</p>
<dt><code>err</code></p>
<dd>A high-level operation or a subsystem failed. Attention is warranted.</p>
<dt><code>warn</code></p>
<dd>A low-level operation failed, but higher-level subsystems may be able to recover.</p>
<dt><code>info</code></p>
<dd>Information that may be useful in retrospect when investigating a problem.</p>
<dt><code>dbg</code></p>
<dd>Information useful only to someone with intricate knowledge of the system, or that would commonly cause too-voluminous log output. Log messages at this level are not logged by default.</dl>
<p> Every Open vSwitch daemon supports the following commands for examining and adjusting log levels.</p>
<dl>
<dt><code>vlog/list</code></p>
<dd>Lists the known logging modules and their current levels.</p>
<dt><code>vlog/list-pattern</code></p>
<dd>Lists logging pattern used for each destination.</p>
<dt><code>vlog/set</code> [<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively.</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful if the <i>target</i> was started with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless the target application was invoked with the <code>&#8211;log-file</code> option.</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>vlog/set PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Each time a message is logged to <i>destination</i>, <i>pattern</i> determines the message&#8217;s formatting. Most characters in <i>pattern</i> are copied literally to the log, but special escapes beginning with <code>%</code> are expanded as follows:</p>
<dl>
<dd>
<dl>
<dt><code>%A</code></p>
<dd>The name of the application logging the message, e.g. <code>ovs-vswitchd</code>.</p>
<dt><code>%B</code></p>
<dd>The RFC5424 syslog PRI of the message.</p>
<dt><code>%c</code></p>
<dd>The name of the module (as shown by <code>ovs-appctl &#8211;list</code>) logging the message.</p>
<dt><code>%d</code></p>
<dd>The current date and time in ISO 8601 format (YYYY-MM-DD HH:MM:SS).</p>
<dt><code>%d{</code><i>format</i><code>}</code></p>
<dd>The current date and time in the specified <i>format</i>, which takes the same format as the <i>template</i> argument to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). As an extension, any <code>#</code> characters in <i>format</i> will be replaced by fractional seconds, e.g. use <code>%H:%M:%S.###</code> for the time to the nearest millisecond. Sub-second times are only approximate and currently decimal places after the third will always be reported as zero.</p>
<dt><code>%D</code></p>
<dd>The current UTC date and time in ISO 8601 format (YYYY-MM-DD HH:MM:SS).</p>
<dt><code>%D{</code><i>format</i><code>}</code></p>
<dd>The current UTC date and time in the specified <i>format</i>, which takes the same format as the <i>template</i> argument to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). Supports the same extension for sub-second resolution as <code>%d{</code>&#8230;<code>}</code>.</p>
<dt><code>%E</code></p>
<dd>The hostname of the node running the application.</p>
<dt><code>%m</code></p>
<dd>The message being logged.</p>
<dt><code>%N</code></p>
<dd>A serial number for this message within this run of the program, as a decimal number. The first message a program logs has serial number 1, the second one has serial number 2, and so on.</p>
<dt><code>%n</code></p>
<dd>A new-line.</p>
<dt><code>%p</code></p>
<dd>The level at which the message is logged, e.g. <code>DBG</code>.</p>
<dt><code>%P</code></p>
<dd>The program&#8217;s process ID (pid), as a decimal number.</p>
<dt><code>%r</code></p>
<dd>The number of milliseconds elapsed from the start of the application to the time the message was logged.</p>
<dt><code>%t</code></p>
<dd>The subprogram name, that is, an identifying name for the process or thread that emitted the log message, such as <code>monitor</code> for the process used for <code>&#8211;monitor</code> or <code>main</code> for the primary process or thread in a program.</p>
<dt><code>%T</code></p>
<dd>The subprogram name enclosed in parentheses, e.g. <code>(monitor)</code>, or the empty string for the primary process or thread in a program.</p>
<dt><code>%%</code></p>
<dd>A literal <code>%</code>.</dl>
</dl>
<dd>A few options may appear between the <code>%</code> and the format specifier character, in this order:</p>
<dl>
<dd>
<dl>
<dt><code>&#8211;</code></p>
<dd>Left justify the escape&#8217;s expansion within its field width. Right justification is the default.</p>
<dt><code>0</code></p>
<dd>Pad the field to the field width with <code>0</code>s. Padding with spaces is the default.</p>
<dt><i>width</i></p>
<dd>A number specifies the minimum field width. If the escape expands to fewer characters than <i>width</i> then it is padded to fill the field width. (A field wider than <i>width</i> is not truncated to fit.)</dl>
</dl>
<dd>The default pattern for console and file output is <code>%D{%Y-%m-%dT %H:%M:%SZ}|%05N|%c|%p|%m</code>; for syslog output, <code>%05N|%c|%p|%m</code>.</p>
<dd>Daemons written in Python (e.g. <code>ovs-xapi-sync</code>, <code>ovs-monitor-ipsec) do not allow control over the log pattern.</p>
<dt>vlog/set</code> FACILITY:<i>facility</i></p>
<dd>Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>.</p>
<dt><code>vlog/reopen</code></p>
<dd>Causes the daemon to close and reopen its log file. (This is useful after rotating log files, to cause a new log file to be used.)</p>
<dd>This has no effect if the target application was not invoked with the <code>&#8211;log-file</code> option.</dl>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</dl>
<h2>See Also</h2>
<p><code>ovs-appctl</code> can control all Open vSwitch daemons, including: <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8), and <code><a href="/docs/linux/man/8-ovsdb-server/">ovsdb-server</a></code>(8). </p>
