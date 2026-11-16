---
title: "snmptrapd(8)"
name: "snmptrapd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snmptrapd/"
description: "snmptrapd – Receive and log SNMP trap messages."
---

<p>snmptrapd &#8211; Receive and log SNMP trap messages.</p>
<h2>Synopsis</h2>
<p><code>snmptrapd</code> [OPTIONS] [LISTENING ADDRESSES]</p>
<h2>Description</h2>
<p><code>snmptrapd</code> is an SNMP application that receives and logs SNMP TRAP and INFORM messages. </p>
<p> Note: the default is to listen on UDP port 162 on all IPv4 interfaces. Since 162 is a privileged port, <code>snmptrapd</code> must typically be run as root.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd>Ignore authenticationFailure traps.</dd>
<dt><code>-A</code></dt>
<dd>Append to the log file rather than truncating it. </dd>
<p> Note that this needs to come <i>before</i> any -Lf options that it should apply to.</p>
<dt><code>-c</code><i> FILE</i></dt>
<dd>Read <i>FILE</i> as a configuration file (or a comma-separated list of configuration files).</dd>
<dt><code>-C</code></dt>
<dd>Do not read any configuration files except the one optionally specified by the <code>-c </code> option.</dd>
<dt><code>-d</code></dt>
<dd>Dump (in hexadecimal) the sent and received SNMP packets.</dd>
<dt><code>-D[TOKEN[,&#8230;]]</code></dt>
<dd>Turn on debugging output for the given <i>TOKEN</i>(s). Try <i>ALL</i> for extremely verbose output.</dd>
<dt><code>-f</code></dt>
<dd>Do not fork() from the calling shell.</dd>
<dt><code>-F</code><i> FORMAT</i></dt>
<dd>When logging to standard output, use the format in the string <i>FORMAT</i>. See the section <code>FORMAT SPECIFICATIONS</code> below for more details.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display a brief usage message and then exit.</dd>
<dt><code>-H</code></dt>
<dd>Display a list of configuration file directives understood by the trap daemon and then exit.</dd>
<dt><code>-I </code><i>[-]INITLIST</i></dt>
<dd>Specifies which modules should (or should not) be initialized when snmptrapd starts up. If the comma-separated <i>INITLIST</i> is preceded with a &#8216;-&#8216;, it is the list of modules that should <i>not</i> be started. Otherwise this is the list of the <i>only</i> modules that should be started. </dd>
<p> To get a list of compiled modules, run snmptrapd with the arguments <i>-Dmib_init -H</i> (assuming debugging support has been compiled in).</p>
<dt><code>-L[efos]</code></dt>
<dd>Specify where logging output should be directed (standard error or output, to a file or via syslog). See LOGGING OPTIONS in <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</dd>
<dt><code>-m</code> <i>MIBLIST</i></dt>
<dd>Specifies a colon separated list of MIB modules to load for this application. This overrides the environment variable MIBS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</dd>
<dt><code>-M</code> <i>DIRLIST</i></dt>
<dd>Specifies a colon separated list of directories to search for MIBs. This overrides the environment variable MIBDIRS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</dd>
<dt><code>-n</code></dt>
<dd>Do not attempt to translate source addresses of incoming packets into hostnames.</dd>
<dt><code>-p</code><i> FILE</i></dt>
<dd>Save the process ID of the trap daemon in <i>FILE</i>.</dd>
<dt><code>-O</code><i> [abeEfnqQsStTuUvxX]</i></dt>
<dd>Specifies how MIB objects and other output should be displayed. See the section <code>OUTPUT OPTIONS</code> in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for details.</dd>
<dt><code>-t</code></dt>
<dd>Do not log traps to syslog. This disables logging to syslog. This is useful if you want the snmptrapd application to <code>only</code> run traphandle hooks and not to log any traps to any location.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Print version information for the trap daemon and then exit.</dd>
<dt><code>-x </code><i>ADDRESS</i></dt>
<dd>Connect to the AgentX master agent on the specified address, rather than the default &quot;/var/agentx/master&quot;. See <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> for details of the format of such addresses.</dd>
<dt><code>&#8212;</code><i>name=value</i></dt>
<dd>Allows one to specify any token (&quot;name&quot;) supported in the <i>snmptrapd.conf</i> file and sets its value to &quot;value&quot;. Overrides the corresponding token in the <i>snmptrapd.conf</i> file. See <i><a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)</i> for the full list of tokens.</dd></dl>
<h2>Format Specifications</h2>
<p><code>snmptrapd</code> interprets format strings similarly to <i><a href="/docs/linux/man/3-printf/">printf</a>(3)</i>. It understands the following formatting sequences:</p>
<dl>
<dd>
</dd><dl>
<dt><code>%%</code></dt>
<dd>a literal %</dd>
<dt><code>%a</code></dt>
<dd>the contents of the agent-addr field of the PDU (v1 TRAPs only)</dd>
<dt><code>%A</code></dt>
<dd>the hostname corresponding to the contents of the agent-addr field of the PDU, if available, otherwise the contents of the agent-addr field of the PDU (v1 TRAPs only).</dd>
<dt><code>%b</code></dt>
<dd>PDU source address (Note: this is not necessarily an IPv4 address)</dd>
<dt><code>%B</code></dt>
<dd>PDU source hostname if available, otherwise PDU source address (see note above)</dd>
<dt><code>%h</code></dt>
<dd>current hour on the local system</dd>
<dt><code>%H</code></dt>
<dd>the hour field from the sysUpTime.0 varbind</dd>
<dt><code>%j</code></dt>
<dd>current minute on the local system</dd>
<dt><code>%J</code></dt>
<dd>the minute field from the sysUpTime.0 varbind</dd>
<dt><code>%k</code></dt>
<dd>current second on the local system</dd>
<dt><code>%K</code></dt>
<dd>the seconds field from the sysUpTime.0 varbind</dd>
<dt><code>%l</code></dt>
<dd>current day of month on the local system</dd>
<dt><code>%L</code></dt>
<dd>the day of month field from the sysUpTime.0 varbind</dd>
<dt><code>%m</code></dt>
<dd>current (numeric) month on the local system</dd>
<dt><code>%M</code></dt>
<dd>the numeric month field from the sysUpTime.0 varbind</dd>
<dt><code>%N</code></dt>
<dd>enterprise string</dd>
<dt><code>%q</code></dt>
<dd>trap sub-type (numeric, in decimal)</dd>
<dt><code>%P</code></dt>
<dd>security information from the PDU (community name for v1/v2c, user and context for v3)</dd>
<dt><code>%t</code></dt>
<dd>decimal number of seconds since the operating system epoch (as returned by <i><a href="/docs/linux/man/2-time/">time</a>(2)</i>)</dd>
<dt><code>%T</code></dt>
<dd>the value of the sysUpTime.0 varbind in seconds</dd>
<dt><code>%v</code></dt>
<dd>list of variable-bindings from the notification payload. These will be separated by a tab, or by a comma and a blank if the alternate form is requested See also %V</dd>
<dt><code>%V</code></dt>
<dd>specifies the variable-bindings separator. This takes a sequence of characters, up to the next % (to embed a % in the string, use \%)</dd>
<dt><code>%w</code></dt>
<dd>trap type (numeric, in decimal)</dd>
<dt><code>%W</code></dt>
<dd>trap description</dd>
<dt><code>%y</code></dt>
<dd>current year on the local system</dd>
<dt><code>%Y</code></dt>
<dd>the year field from the sysUpTime.0 varbind</dd></dl>
</dl>
<p> In addition to these values, an optional field width and precision may also be specified , just as in <i><a href="/docs/linux/man/3-printf/">printf</a>(3)</i>, and a flag value. The following flags are supported:</p>
<dl>
<dd>
</dd><dl>
<dt><code>&#8211;</code></dt>
<dd>left justify</dd>
<dt><code>0</code></dt>
<dd>use leading zeros</dd>
<dt><code>#</code></dt>
<dd>use alternate form</dd></dl>
</dl>
<p> The &quot;use alternate form&quot; flag changes the behavior of various format string sequences:</p>
<dl>
<dd>Time information will be displayed based on GMT (rather than the local timezone)</dd>
<dd>The variable-bindings will be a comma-separated list (rather than a tab-separated one)</dd>
<dd>The system uptime will be broken down into a human-meaningful format (rather than being a simple integer)</dd></dl>
<h3>Examples:</h3>
<p>To get a message like &quot;14:03 TRAP3.1 from humpty.ucd.edu&quot; you could use something like this: </p>
<dl>
<dd>
<pre>snmptrapd -P -F &quot;%02.2h:%02.2j TRAP%w.%q from %A
&quot;</pre>
</dd></dl>
<p> If you want the same thing but in GMT rather than local time, use </p>
<dl>
<dd>
<pre>snmptrapd -P -F &quot;%#02.2h:%#02.2j TRAP%w.%q from %A
&quot;</pre>
</dd></dl>
<h2>Listening Addresses</h2>
<p>By default, <code>snmptrapd</code> listens for incoming SNMP TRAP and INFORM packets on UDP port 162 on all IPv4 interfaces. However, it is possible to modify this behaviour by specifying one or more listening addresses as arguments to <code>snmptrapd</code>. See the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</p>
<h2>Notification-Log-Mib Support</h2>
<p>As of net-snmp 5.0, the snmptrapd application supports the NOTIFICATION-LOG-MIB. It does this by opening an AgentX subagent connection to the master snmpd agent and registering the notification log tables. As long as the snmpd application is started first, it will attach itself to it and thus you should be able to view the last recorded notifications via the nlmLogTable and nlmLogVariableTable. See the snmptrapd.conf file and the &quot;doNotRetainNotificationLogs&quot; token for turning off this support. See the NOTIFICATION-LOG-MIB for more details about the MIB itself.</p>
<h2>Extensibility And Configuration</h2>
<p>See the <i><a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)</i> manual page.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/8-snmpd/">snmpd</a>(8), <a href="/docs/linux/man/3-printf/">printf</a>(3), <a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5), syslog(8), <a href="/docs/linux/man/5-variables/">variables</a>(5) </p>
