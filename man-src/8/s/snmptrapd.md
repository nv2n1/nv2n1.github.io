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
<dt><code>-a</code></p>
<dd>Ignore authenticationFailure traps.</p>
<dt><code>-A</code></p>
<dd>Append to the log file rather than truncating it. </p>
<p> Note that this needs to come <i>before</i> any -Lf options that it should apply to.</p>
<dt><code>-c</code><i> FILE</i></p>
<dd>Read <i>FILE</i> as a configuration file (or a comma-separated list of configuration files).</p>
<dt><code>-C</code></p>
<dd>Do not read any configuration files except the one optionally specified by the <code>-c </code> option.</p>
<dt><code>-d</code></p>
<dd>Dump (in hexadecimal) the sent and received SNMP packets.</p>
<dt><code>-D[TOKEN[,&#8230;]]</code></p>
<dd>Turn on debugging output for the given <i>TOKEN</i>(s). Try <i>ALL</i> for extremely verbose output.</p>
<dt><code>-f</code></p>
<dd>Do not fork() from the calling shell.</p>
<dt><code>-F</code><i> FORMAT</i></p>
<dd>When logging to standard output, use the format in the string <i>FORMAT</i>. See the section <code>FORMAT SPECIFICATIONS</code> below for more details.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display a brief usage message and then exit.</p>
<dt><code>-H</code></p>
<dd>Display a list of configuration file directives understood by the trap daemon and then exit.</p>
<dt><code>-I </code><i>[-]INITLIST</i></p>
<dd>Specifies which modules should (or should not) be initialized when snmptrapd starts up. If the comma-separated <i>INITLIST</i> is preceded with a &#8216;-&#8216;, it is the list of modules that should <i>not</i> be started. Otherwise this is the list of the <i>only</i> modules that should be started. </p>
<p> To get a list of compiled modules, run snmptrapd with the arguments <i>-Dmib_init -H</i> (assuming debugging support has been compiled in).</p>
<dt><code>-L[efos]</code></p>
<dd>Specify where logging output should be directed (standard error or output, to a file or via syslog). See LOGGING OPTIONS in <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</p>
<dt><code>-m</code> <i>MIBLIST</i></p>
<dd>Specifies a colon separated list of MIB modules to load for this application. This overrides the environment variable MIBS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</p>
<dt><code>-M</code> <i>DIRLIST</i></p>
<dd>Specifies a colon separated list of directories to search for MIBs. This overrides the environment variable MIBDIRS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</p>
<dt><code>-n</code></p>
<dd>Do not attempt to translate source addresses of incoming packets into hostnames.</p>
<dt><code>-p</code><i> FILE</i></p>
<dd>Save the process ID of the trap daemon in <i>FILE</i>.</p>
<dt><code>-O</code><i> [abeEfnqQsStTuUvxX]</i></p>
<dd>Specifies how MIB objects and other output should be displayed. See the section <code>OUTPUT OPTIONS</code> in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for details.</p>
<dt><code>-t</code></p>
<dd>Do not log traps to syslog. This disables logging to syslog. This is useful if you want the snmptrapd application to <code>only</code> run traphandle hooks and not to log any traps to any location.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Print version information for the trap daemon and then exit.</p>
<dt><code>-x </code><i>ADDRESS</i></p>
<dd>Connect to the AgentX master agent on the specified address, rather than the default &quot;/var/agentx/master&quot;. See <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> for details of the format of such addresses.</p>
<dt><code>&#8212;</code><i>name=value</i></p>
<dd>Allows one to specify any token (&quot;name&quot;) supported in the <i>snmptrapd.conf</i> file and sets its value to &quot;value&quot;. Overrides the corresponding token in the <i>snmptrapd.conf</i> file. See <i><a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)</i> for the full list of tokens.</dl>
<h2>Format Specifications</h2>
<p><code>snmptrapd</code> interprets format strings similarly to <i><a href="/docs/linux/man/3-printf/">printf</a>(3)</i>. It understands the following formatting sequences:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>a literal %</p>
<dt><code>%a</code></p>
<dd>the contents of the agent-addr field of the PDU (v1 TRAPs only)</p>
<dt><code>%A</code></p>
<dd>the hostname corresponding to the contents of the agent-addr field of the PDU, if available, otherwise the contents of the agent-addr field of the PDU (v1 TRAPs only).</p>
<dt><code>%b</code></p>
<dd>PDU source address (Note: this is not necessarily an IPv4 address)</p>
<dt><code>%B</code></p>
<dd>PDU source hostname if available, otherwise PDU source address (see note above)</p>
<dt><code>%h</code></p>
<dd>current hour on the local system</p>
<dt><code>%H</code></p>
<dd>the hour field from the sysUpTime.0 varbind</p>
<dt><code>%j</code></p>
<dd>current minute on the local system</p>
<dt><code>%J</code></p>
<dd>the minute field from the sysUpTime.0 varbind</p>
<dt><code>%k</code></p>
<dd>current second on the local system</p>
<dt><code>%K</code></p>
<dd>the seconds field from the sysUpTime.0 varbind</p>
<dt><code>%l</code></p>
<dd>current day of month on the local system</p>
<dt><code>%L</code></p>
<dd>the day of month field from the sysUpTime.0 varbind</p>
<dt><code>%m</code></p>
<dd>current (numeric) month on the local system</p>
<dt><code>%M</code></p>
<dd>the numeric month field from the sysUpTime.0 varbind</p>
<dt><code>%N</code></p>
<dd>enterprise string</p>
<dt><code>%q</code></p>
<dd>trap sub-type (numeric, in decimal)</p>
<dt><code>%P</code></p>
<dd>security information from the PDU (community name for v1/v2c, user and context for v3)</p>
<dt><code>%t</code></p>
<dd>decimal number of seconds since the operating system epoch (as returned by <i><a href="/docs/linux/man/2-time/">time</a>(2)</i>)</p>
<dt><code>%T</code></p>
<dd>the value of the sysUpTime.0 varbind in seconds</p>
<dt><code>%v</code></p>
<dd>list of variable-bindings from the notification payload. These will be separated by a tab, or by a comma and a blank if the alternate form is requested See also %V</p>
<dt><code>%V</code></p>
<dd>specifies the variable-bindings separator. This takes a sequence of characters, up to the next % (to embed a % in the string, use \%)</p>
<dt><code>%w</code></p>
<dd>trap type (numeric, in decimal)</p>
<dt><code>%W</code></p>
<dd>trap description</p>
<dt><code>%y</code></p>
<dd>current year on the local system</p>
<dt><code>%Y</code></p>
<dd>the year field from the sysUpTime.0 varbind</dl>
</dl>
<p> In addition to these values, an optional field width and precision may also be specified , just as in <i><a href="/docs/linux/man/3-printf/">printf</a>(3)</i>, and a flag value. The following flags are supported:</p>
<dl>
<dd>
<dl>
<dt><code>&#8211;</code></p>
<dd>left justify</p>
<dt><code>0</code></p>
<dd>use leading zeros</p>
<dt><code>#</code></p>
<dd>use alternate form</dl>
</dl>
<p> The &quot;use alternate form&quot; flag changes the behavior of various format string sequences:</p>
<dl>
<dd>Time information will be displayed based on GMT (rather than the local timezone)</p>
<dd>The variable-bindings will be a comma-separated list (rather than a tab-separated one)</p>
<dd>The system uptime will be broken down into a human-meaningful format (rather than being a simple integer)</dl>
<h3>Examples:</h3>
<p>To get a message like &quot;14:03 TRAP3.1 from humpty.ucd.edu&quot; you could use something like this: </p>
<dl>
<dd>
<pre>snmptrapd -P -F &quot;%02.2h:%02.2j TRAP%w.%q from %A
&quot;</pre>
</dl>
<p> If you want the same thing but in GMT rather than local time, use </p>
<dl>
<dd>
<pre>snmptrapd -P -F &quot;%#02.2h:%#02.2j TRAP%w.%q from %A
&quot;</pre>
</dl>
<h2>Listening Addresses</h2>
<p>By default, <code>snmptrapd</code> listens for incoming SNMP TRAP and INFORM packets on UDP port 162 on all IPv4 interfaces. However, it is possible to modify this behaviour by specifying one or more listening addresses as arguments to <code>snmptrapd</code>. See the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</p>
<h2>Notification-Log-Mib Support</h2>
<p>As of net-snmp 5.0, the snmptrapd application supports the NOTIFICATION-LOG-MIB. It does this by opening an AgentX subagent connection to the master snmpd agent and registering the notification log tables. As long as the snmpd application is started first, it will attach itself to it and thus you should be able to view the last recorded notifications via the nlmLogTable and nlmLogVariableTable. See the snmptrapd.conf file and the &quot;doNotRetainNotificationLogs&quot; token for turning off this support. See the NOTIFICATION-LOG-MIB for more details about the MIB itself.</p>
<h2>Extensibility And Configuration</h2>
<p>See the <i><a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)</i> manual page.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/8-snmpd/">snmpd</a>(8), <a href="/docs/linux/man/3-printf/">printf</a>(3), <a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5), <a href="/docs/linux/man/8-syslog/">syslog</a>(8), <a href="/docs/linux/man/5-variables/">variables</a>(5) </p>
