---
title: "cyrus-master(8)"
name: "cyrus-master"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyrus-master/"
description: "cyrus-master – cyrus-master Cyrus process"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyrus-master &#8211; cyrus-master Cyrus process</p>
<h2>Synopsis</h2>
<p><code>cyrus-master</code> [ <code>-C</code> <i>alternate imapd.conf</i> ] [ <code>-M</code> <i>alternate cyrus.conf</i> ] [ <code>-l</code> <i>listen queue</i> ] [ <code>-p</code> <i>pidfile</i> ] [ <code>-P</code> <i>snmp agentx ping interval</i> ] [ <code>-j</code> <i>janitor period</i> ] [ <code>-d</code> ] [ <code>-D</code> ] [ <code>-x</code> <i>snmp agentx socket</i> ]</p>
<h2>Description</h2>
<p><i>Cyrus-master</i> is the process that controls all of the Cyrus processes. This process is responsible for creating all imapd, pop3d, lmtpd and sieved child processes. This process also initializes the Berkeley DB code and performs scheduled cleanup/maintenance. </p>
<p> If this process dies, then no new sessions will be started. </p>
<p> It kills itself and all child processes when it receives a SIGTERM.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> alternate imapd.conf</i></p>
<dd>Specifies an alternate imapd.conf for use by cyrus-master (note that this will not affect any sub-processes spawned by cyrus-master, you should specify those specifically in the respective entries in cyrus.conf).</p>
<dt><code>-M</code><i> alternate cyrus.conf</i></p>
<dd>Specifies an alternate cyrus.conf for use by cyrus-master.</p>
<dt><code>-l</code><i> listen queue backlog</i></p>
<dd>Increase the listen queue backlog. By default, the listen queue is set to 32. On systems with a high connection rate, it may be desirable to increase this value. refer to <code><a href="/docs/linux/man/2-listen/">listen</a>(2)</code> for details.</p>
<dt><code>-j</code><i> janitor full-sweeps per second</i></p>
<dd>Sets the amount of times per second the janitor should sweep the entire child table. Leave it at the default of 1 unless you have a really high fork rate (and you have not increased the child hash table size when you compiled Cyrus from its default of 10000 entries).</p>
<dt><code>-p</code><i> pidfile</i></p>
<dd>Use <i>pidfile</i> as the pidfile. If not specified, defaults to /var/run/cyrus-master.pid</p>
<dt><code>-P</code><i> snmp agentx ping interval</i></p>
<dd>Sets the amount on time in seconds the subagent will try and reconnect to the cyrus-master agent (snmpd) if it ever becomes (or starts) disconnected. Requires net-snmp 5.0 or higher.</p>
<dt><code>-d</code></p>
<dd>Start in daemon mode (run in background and disconnect from controlling terminal).</p>
<dt><code>-D</code></p>
<dd>Don&#8217;t close stdin/stdout/stderr. Primiarly useful for debugging.</p>
<dt><code>-x</code><i> snmp agentx socket</i></p>
<dd>Address the cyrus-master agent (most likely snmpd) listens on. Requires net-snmp 5.0 or higher.</dl>
<h2>Configuration</h2>
<p>Upon execution, <i>cyrus-master</i> reads its configuration information out of the <i><a href="/docs/linux/man/5-cyrus-conf/">cyrus.conf</a></i>(5) file. </p>
<p> <i>Cyrus-master</i> rereads its configuration file when it receives a hangup signal, SIGHUP. Services and events may be added, deleted or modified when the configuration file is reread. Any active services removed from the configuration file will be allowed to run until completion.</p>
<h2>Notes</h2>
<p>The environment variable <code>CYRUS_VERBOSE</code> can be set to log additional debugging information. Setting the value to 1 results in base level logging. Setting it higher results in more log messages being generated.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/cyrus.conf, /etc/imapd.conf, /var/run/cyrus-master.pid</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cyrus-conf/">cyrus.conf</a>(5)</code>, <code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-imapd/">imapd</a>(8)</code>, <code><a href="/docs/linux/man/8-pop3d/">pop3d</a>(8)</code>, <code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8)</code>, <code><a href="/docs/linux/man/8-timsieved/">timsieved</a>(8)</code>, <code><a href="/docs/linux/man/8-idled/">idled</a>(8)</code> </p>
