---
title: "pmdaconnect(3)"
name: "pmdaconnect"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaconnect/"
description: "pmdaConnect – establish a connection between a daemon PMDA and PMCD"
---

<p><code>pmdaConnect</code> &#8211; establish a connection between a daemon PMDA and PMCD</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> void pmdaConnect(pmdaInterface *</code><i>dispatch</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaConnect</code> initializes an IPC channel between a <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) and the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) process on the local host. The type of the connection is dependent on the <i>e_io</i> field of the <code>pmdaExt</code> structure:</p>
<dl>
<dt><code>pmdaPipe</code></p>
<dd>Use <code>stdin</code>/<code>stdout</code> to communicate; assumes this is a pipe created by <code>pmcd</code> before the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) was launched.</p>
<dt><code>pmdaInet</code></p>
<dd>Assume <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) will establish a connection to an IPv4 internet domain socket set up by the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3). The name or number of the port must be specified in the <i>e_sockname</i> or <i>e_port</i> fields of the <code>pmdaExt</code> structure, respectively.</p>
<dt><code>pmdaIPv6</code></p>
<dd>Assume <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) will establish a connection to an IPv6 internet domain socket set up by the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3). The name or number of the port must be specified in the <i>e_sockname</i> or <i>e_port</i> fields of the <code>pmdaExt</code> structure, respectively.</p>
<dt><code>pmdaUnix</code></p>
<dd>Assume <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) will establish a connection to a unix domain socket set up by the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3). The port number must be specified in the <i>e_port</i> field of the <code>pmdaExt structure.</code></p>
<dt><code>pmdaUnknown</code></p>
<dd>The initial value of <i>e_io</i> which defaults to using <code>stdin</code>/<code>stdout</code>.</dl>
<p> The relevant <code>pmdaExt</code> fields are initialized by <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) and set by <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3) or <code><a href="/docs/linux/man/3-pmdagetoptions/">pmdaGetOptions</a></code>(3) so most PMDAs should not need to access or modify them. </p>
<p> Traditionally most PMDAs have called <code>pmdaConnect</code> after calls to <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetoptions/">pmdaGetOptions</a></code>(3) (or <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3)) and <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3). If the PMDA requires significant processing at startup to identify the available metrics and/or instance domains before <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3) can be called, then it risks timing out during the handshake protocol that starts as soon as <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) launches the PMDA and does not conclude until <code>pmdaConnect</code> is called. In this case, it is advisable to move the <code>pmdaConnect</code> call, so that it comes <i>after</i> the call to <code><a href="/docs/linux/man/3-pmdagetoptions/">pmdaGetOptions</a></code>(3) (or <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3)) and <i>before</i> the call to <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmdaConnect</code> will log the type of connection made to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) if the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) debug control variable (<code>pmDebug</code>) has the <code>DBG_TRACE_LIBPMDA</code> flag set. </p>
<p> If an error occurs that is unrecoverable, <i>dispatch-&gt;status</i> is set to a value less than 0, otherwise it is zero or positive.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetoptions/">pmdaGetOptions</a></code>(3) and <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3). </p>
