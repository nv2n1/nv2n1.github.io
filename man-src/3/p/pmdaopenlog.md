---
title: "pmdaopenlog(3)"
name: "pmdaopenlog"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaopenlog/"
description: "pmdaOpenLog – redirect stderr to a logfile"
---

<p><code>pmdaOpenLog</code> &#8211; redirect stderr to a logfile</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> void pmdaOpenLog(pmdaInterface * </code><i>dispatch</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaOpenLog</code> redirects <i>stderr</i> to the logfile specified in the <i>dispatch</i> structure, set by the previous call to <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) or <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3). The first line of the log file will detail the name of the calling process, the host the process is running on, and the current time. In addition, the log is appended with the exit time of the process by a routine registered with <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3).</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <i><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></i>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/2-atexit/">atexit</a></code>(2), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) and <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3). </p>
