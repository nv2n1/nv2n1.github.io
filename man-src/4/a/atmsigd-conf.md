---
title: "atmsigd-conf(4)"
name: "atmsigd-conf"
section: "4"
letter: "a"
url: "/docs/linux/man/4-atmsigd-conf/"
description: "atmsigd.conf – configuration file for the ATM signaling demon"
---

<p>atmsigd.conf &#8211; configuration file for the ATM signaling demon</p>
<h2>Synopsis</h2>
<p><code>/etc/atmsigd.conf</code></p>
<h2>Description</h2>
<p><code>atmsigd.conf</code> contains configuration data for <code>atmsigd</code>. <code>atmsigd</code> reads <code>atmsigd.conf</code> after parsing the command line options, before connecting to the ATM network. </p>
<p> Configuration parameters are arranged in functional groups. In order to set a parameter, the name of the group, the name of the parameter, and the parameter value(s) have to be specified, e.g. </p>
<pre> sig level debug</pre>
<p>decreases the logging threshold for messages related to signaling to the <code>debug</code> level. The following options are recognized:</p>
<dl>
<dt><code>debug dump&nbsp;<wbr></code><i>path</i></p>
<dd>Specifies the directory to which <code>atmsigd</code> will write status and trace dumps. If tracing is not yet enabled, the trace size is automatically set to a (small) default value.</p>
<dt><code>debug level&nbsp;<wbr></code><i>level</i></p>
<dd>Sets the default debug level to <i>level</i>. <i>level</i> can be any of <code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>, and <code>fatal</code>. Only messages with the same or a higher priority than the debug level are printed. Note that the command-line option <code>-d</code> generates even more output (e.g. hexdumps of all packets passing between <code>atmsigd</code> and the network) than <code>debug level debug</code>.</p>
<dt><code>debug log&nbsp;<wbr></code><i>path</i></p>
<dd>Specifies the file to which <code>atmsigd</code> writes logging messages. When using the special file name <code>syslog</code>, messages are send to the system logger instead. Log messages are written to standard output if no log file is specified. Writing to standard output can also be explicitly requested by using the special file name <code>stderr</code>.</p>
<dt><code>debug trace&nbsp;<wbr></code>[<i>number</i>]</p>
<dd>Enables tracing and optionally sets the number of entries that should be kept in the trace buffer. A (small) default is used if the number is omitted.</p>
<dt><code>io level&nbsp;<wbr></code><i>level</i></p>
<dd>Sets the debug level for IO-related messages to <i>level</i>.</p>
<dt><code>io max_rate&nbsp;<wbr></code><i>rate</i></p>
<dd>Sets the rate to signal if an application requests the &quot;maximum&quot;. See <a href="/docs/linux/man/7-qos/">qos</a>(7) for the syntax to use for expressing the rate. The default maximum rate is 353207 cells/second (OC3). (Note that the value of <code>max_rate</code> does not constrain the rates an application can explicitly request.)</p>
<dt><code>io qos&nbsp;<wbr></code><i>qos</i></p>
<dd>Configures the signaling VC to use the specified QOS (see <a href="/docs/linux/man/7-qos/">qos</a>(7) for the syntax). By default, UBR at link speed is used on the signaling VC.</p>
<dt><code>io vc&nbsp;<wbr></code>[<i>itf</i><code>.</code>]<i>vpi</i><code>.</code><i>vci</i></p>
<dd>Uses the specified VC for signaling messages instead of the usual 0.0.5.</p>
<dt><code>saal level&nbsp;<wbr></code><i>level</i></p>
<dd>Sets the debug level for messages related to SAAL (i.e. SSCF and SSCOP) to <i>level</i>.</p>
<dt><code>sig level&nbsp;<wbr></code><i>level</i></p>
<dd>Sets the debug level for messages related to signaling (Q.2931 or ISP) to <i>level</i>.</p>
<dt><code>sig mode&nbsp;<wbr></code><i>mode</i></p>
<dd>Set the mode of operation. The following modes are available: <code>user</code> for the user side, <code>network</code> for the network side, and <code>switch</code> for operation in a switch. The default behaviour is <code>user</code>.</p>
<dt><code>sig uni30</code></p>
<dd>Use UNI 3.0 signaling. If specified together with <code>sig uni31</code>, this option sets UNI 3.1 signaling with a few backwards-compatibility extensions.</p>
<dt><code>sig uni31</code></p>
<dd>Use UNI 3.1 signaling. This option can be combined with <code>sig uni30</code> (see above).</p>
<dt><code>sig uni40</code></p>
<dd>Use UNI 4.0 signaling. This option can be combined with <code>sig q.2963.1</code> (see below).</p>
<dt><code>sig q.2963.1</code></p>
<dd>Enable peak cell rate renegotiation. This option is only available with UNI 4.0 signaling.</p>
<dt><code>sig vpci&nbsp;<wbr></code><i>vpci</i><code>&nbsp;<wbr>itf&nbsp;<wbr></code><i>itf</i></p>
<dd>Sets up a very simplistic type of routing. All calls with VPCI values equal to or greater than <i>vpci</i> will be routed to <i>itf</i>, and their VPI values will be set to the signaled VPCI minus <i>vpci</i>. Multiple <code>sig vpci</code> entries can be used to support an arbitrary number of interfaces. Example: with <code>sig vpci 4 itf 1</code>, a call signaled for VPCI/VCI 0.x is routed to 0.0.x, a call signaled for 6.y is routed to 1.2.y, etc.</p>
<dt><code>policy level&nbsp;<wbr></code><i>level</i></p>
<dd>Sets the debug level for messages related to policy decisions to <i>level</i>.</p>
<dt><code>policy&nbsp;<wbr></code><i>decision direction address</i></p>
<dd>Takes the specified <i>decision</i> for calls from or to <i>address</i>. <i>decision</i> can be either <code>allow</code> or <code>reject</code>. <i>direction</i> is either <code>from</code> or <code>to</code>. The <i>address</i> may be wildcarded by prepending a slash and the number of significant bits (NSAP) or digits (E.164). The rules are searched in the order in which they appear in <code>atmsigd.conf</code> until the first match. If no rule matches, the call is allowed.</p>
<dt><code>entity&nbsp;<wbr></code>[<i>itf</i><code>.</code>]<i>vpi</i><code>.</code><i>vci</i>&nbsp;<wbr>{&nbsp;<wbr><i>options &#8230;</i>&nbsp;<wbr>}</p>
<dd>Activates a signaling entity on that specific VC. Multiple <code>entity</code> clauses can appear in the same configuration. When using <code>entity</code>, the option <code>io vc</code> is not available. <code>entity</code> is optionally followed by the following options, enclosed in curly braces: <code>vpci</code> (corresponds to <code>sig vpci</code>), <code>mode</code> (corresponds to <code>sig mode</code>), <code>qos</code> (corresponds to <code>vc qos</code>), <code>route</code>, and <code>default</code>. The last two options determine how outbound calls are routed. The <code>route</code> option is followed by an address in the format used for addresses in <code>policy</code>. If no route entry matches the called party number of an outbound call, the entry marked with <code>default</code> is selected.</dl>
<p> When setting multiple parameters in the same group, the group name doesn&#8217;t have to be repeated if it is followed by the parameters in curly braces. Example: </p>
<pre> debug {
 level warn
 dump /var/tmp
 log syslog
 trace 100
 }</pre>
<p>Line breaks can be inserted in <code>atmsigd.conf</code> wherever spaces or tabs are allowed. Everything between a `#&#8217; and the end of the line is considered a comment. The `#&#8217; character cannot be escaped. </p>
<p> If an option is specified in <code>atmsigd.conf</code> and on the command line, the command line has priority.</p>
<h2>Compatibility</h2>
<p>Certain options used by past versions of <code>atmsigd</code> but no longer documented on the man page are still recognized and supported, but they also yield a warning message. Future versions of <code>atmsigd</code> will not recognize those options.</p>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8), <a href="/docs/linux/man/7-qos/">qos</a>(7), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) </p>
