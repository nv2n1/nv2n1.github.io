---
title: "atmsigd(8)"
name: "atmsigd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmsigd/"
description: "atmsigd – ATM signaling demon"
---

<p>atmsigd &#8211; ATM signaling demon</p>
<h2>Synopsis</h2>
<p><code>atmsigd</code> [<code>-b</code>] [<code>-c&nbsp;<wbr></code><i>config_file</i>] [<code>-d</code>] [<code>-D&nbsp;<wbr></code><i>dump_dir</i>] [<code>-l&nbsp;<wbr></code><i>logfile</i>] [<code>-m&nbsp;<wbr></code><i>mode</i>] [<code>-n</code>] [<code>-q&nbsp;<wbr></code><i>qos</i>] [<code>-t&nbsp;<wbr></code><i>trace_length</i>] [<code>-u&nbsp;<wbr></code><i>uni_version</i>] [<code>[</code><i>itf</i>.]<i>vpi</i>.<i>vci</i> [<i>input output</i>]<code>]</code><br />
 <code>atmsigd</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>atmsigd</code> implements the ATM UNI signaling protocol. Requests to establish, accept, or close ATM SVCs are sent from the kernel (using a comparably simple protocol) to the signaling demon, which then performs the dialog with the network. </p>
<p> Note that <code>atmsigd</code> is not able to accept or establish connections until the local ATM address of the interface is configured by <code>ilmid</code> or manually using <code>atmaddr</code>. </p>
<p> The default signaling VC (interface 0, VPI 0, VCI 5) can be overridden on the command line by specifying a different PVC address. </p>
<p> When overriding the default VC, optionally a pair of named pipes to use for communicating with the user of signaling can be specified. Normally, the kernel is the user of signaling and <code>atmsigd</code> opens a special socket for communication with it. </p>
<p> If <code>atmsigd</code> is killed, all system calls requiring interaction with it will return with an error and set <code>errno</code> to <code>EUNATCH</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Run in background (i.e. in a forked child process) after initializing.</p>
<dt><code>-c&nbsp;<wbr></code><i>config_file</i></p>
<dd>Use the specified configuration file instead of <code>/etc/atmsigd.conf</code> If an option is specified in the configuration file and on the command line, the command line has priority.</p>
<dt><code>-d</code></p>
<dd>Enables (lots of) debugging output. By default, <code>atmsigd</code> is comparably quiet.</p>
<dt><code>-D&nbsp;<wbr></code><i>dump_dir</i></p>
<dd>Specifies the directory to which <code>atmsigd</code> will write status and trace dumps. If <code>-D</code> is not specified, dumps are written to /var/tmp.</p>
<dt><code>-l&nbsp;<wbr></code><i>logfile</i></p>
<dd>Write diagnostic messages to the specified file. The special name <code>syslog</code> is used to send diagnostics to the system logger, <code>stderr</code> is used to send diagnostics to standard error. If <code>-l</code> is absent, the setting in <code>atmsigd.conf</code> is used. If <code>atmsigd</code> doesn&#8217;t specify a destination either, messages are written to standard error.</p>
<dt><code>-m&nbsp;<wbr></code><i>mode</i></p>
<dd>Set the mode of operation. The following modes are available: <code>user</code> for the user side (the default), <code>network</code> for the network side (useful if you have two PCs but no switch), and <code>switch</code> for operation with a signaling relay in a switch.</p>
<dt><code>-n</code></p>
<dd>Prints addresses in numeric format only, i.e. no address to name translation is attempted.</p>
<dt><code>-q&nbsp;<wbr></code><i>qos</i></p>
<dd>Configures the signaling VC to use the specified quality of service (see <a href="/docs/linux/man/7-qos/">qos</a>(7) for the syntax). By default, UBR at link speed is used on the signaling VC.</p>
<dt><code>-t&nbsp;<wbr></code><i>trace_length</i></p>
<dd>Sets the number of entries that should be kept in the trace buffer. <code>-t 0</code> disables tracing. If <code>-t</code> is not specified, <code>atmsigd</code> uses a default of 20 trace entries.</p>
<dt><code>-u&nbsp;<wbr></code><i>uni_version</i></p>
<dd>Sets the signaling mode. The following modes are supported: <code>uni30</code> for UNI 3.0, <code>uni31</code> for UNI 3.1, <code>uni31+uni30</code> for UNI 3.1 with 3.0 compatibility, <code>uni40</code> for UNI 4.0, and <code>uni40+q.2963.1</code> for UNI 4.0 with Q.2963.1 peak cell rate renegotiation.</p>
<dt><code>-V</code></p>
<dd>Prints the version number of <code>atmsigd</code> on standard output and exits.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/atmsigd.conf</code></p>
<dd>default configuration file</p>
<dt><code>/var/tmp/atmsigd.</code><i>pid</i><code>.status.</code><i>version</i></p>
<dd>default location of status dumps</p>
<dt><code>/var/tmp/atmsigd.</code><i>pid</i><code>.trace.</code><i>version</i></p>
<dd>default location of signaling trace dumps</dl>
<h2>Debugging</h2>
<p>When receiving a <code>SIGUSR1</code> signal, <code>atmsigd</code> dumps the list of all internal socket descriptors. With <code>SIGUSR2</code>, it dumps the contents of the trace buffer. If a dump directory was set, dumps are written to files called <code>atmsigd.</code><i>pid</i><code>.status.</code><i>number</i> and <code>atmsigd.</code><i>pid</i><code>.trace.</code><i>number</i>, respectively, with <i>number</i> starting at zero and being incremented for every dump. If no dump directory is set, dumps are written to standard error. </p>
<p> Dumps are also generated whenever <code>atmsigd</code> detects a fatal error and terminates. No attempt is made to catch signals like <code>SIGSEGV</code>.</p>
<h2>Bugs</h2>
<p>The generation of traces is a comparably slow process which may already take several seconds for only 100 trace entries. To generate a trace dump, <code>atmsigd</code> therefore forks a child process that runs in parallel to the signaling demon.</p>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmaddr/">atmaddr</a>(8), <a href="/docs/linux/man/4-atmsigd-conf/">atmsigd.conf</a>(4), <a href="/docs/linux/man/8-ilmid/">ilmid</a>(8), <a href="/docs/linux/man/7-qos/">qos</a>(7) </p>
