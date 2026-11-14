---
title: "telnet-probe(1)"
name: "telnet-probe"
section: "1"
letter: "t"
url: "/docs/linux/man/1-telnet-probe/"
description: "telnet-probe – lightweight telnet-like port probe"
---

<h2>NAME</h2>
<p> <code>telnet-probe</code> &#8211; lightweight telnet-like port probe</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/telnet-probe</code> [<code>-c</code>] [<code>-v</code>] <i>host</i> <i>port</i></p>
<h2>DESCRIPTION</h2>
<p> <code>telnet-probe</code> allows the <code><a href="/docs/linux/man/1-pmdashping/">pmdashping</a></code>(1) daemons to establish connections to arbitrary local and remote service-providing daemons so that response time and service availability information can be obtained. </p>
<p> The required <i>host</i> and <i>port</i> number arguments have the same meaning as their <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1) equivalents. </p>
<p> The <code>-c</code> option causes <code>telnet-probe</code> to perform a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) only. This skips the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) exercise that would otherwise be done after connecting (see below). </p>
<p> The <code>-v</code> option causes <code>telnet-probe</code> to be verbose while operating. </p>
<p> Once the telnet connection has been established, <code>telnet-probe</code> reads from <i>stdin</i> until end-of-file, and writes all the input data to the telnet connection. Next, <code>telnet-probe</code> will read from the telnet connection until end-of-file, discarding whatever data it receives. Then <code>telnet-probe</code> exits. </p>
<p> To operate successfully, the input passed via <code>telnet-probe</code> to the remote service must be sufficient to cause the remote service to close the connection when the last line of input has been processed, e.g. ending with &#8220;quit&#8221; when probing SMTP on port 25. </p>
<p> By default <code>telnet-probe</code> will not produce any output, unless there is an error in which case a diagnostic message can be displayed (in verbose mode only) and the exit status will be non-zero indicating a failure.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>telnet-probe</code> succeeds, then 0 will be returned. If the attempt to establish a connection fails or is terminated, then a non-zero exit status is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPintro</a></code>(1), <code><a href="/docs/linux/man/1-pmdashping/">pmdashping</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2). </p>
<h2>Index</h2>
