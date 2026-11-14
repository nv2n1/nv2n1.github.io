---
title: "pmdadaemon(3)"
name: "pmdadaemon"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdadaemon/"
description: "pmdaDaemon – initialize the PMDA to run as a daemon"
---

<p><code>pmdaDaemon</code> &#8211; initialize the PMDA to run as a daemon</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> void pmdaDaemon(pmdaInterface *</code><i>dispatch</i>, int <i>interface</i>, char&nbsp;<wbr>*<i>name</i>, int&nbsp;<wbr><i>domain</i>, char&nbsp;<wbr>*<i>logfile</i>, char&nbsp;<wbr>*<i>helptext</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaDaemon</code> initializes the <code>pmdaInterface</code> structure to use the <i>interface</i> extensions assuming the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) is to be run as a daemon. The <code>pmdaInterface</code> structure is initialized with:</p>
<dl>
<dt><i>name</i></p>
<dd>The name of the agent.</p>
<dt><i>domain</i></p>
<dd>The default domain number of the agent which uniquely identifies this PMDA from other running PMDAs. This may be subsequently changed by a command line option <code>-d</code> (see <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3)).</p>
<dt><i>logfile</i></p>
<dd>The default path to the log file. This may be replaced by the <code>-l</code> command line option if using <code>pmdaGetOpt</code>.</p>
<dt><i>helptext</i></p>
<dd>The default path to the help text (see <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3). This may be replaced by the <code>-h</code> command line option if using <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3). If no help text is installed, or you are not using <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3), then this should be set to NULL.</dl>
<p> The callbacks are initialized to <code><a href="/docs/linux/man/3-pmdaprofile/">pmdaProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmdadesc/">pmdaDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3), <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3) and <code><a href="/docs/linux/man/3-pmdastore/">pmdaStore</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>Unable to allocate memory for pmdaExt structure</code></p>
<dd>In addition, the <i>dispatch-&gt;status</i> field is set to a value less than zero.</p>
<dt><code>PMDA interface version </code><i>interface</i><code> not supported</code></p>
<dd>The <i>interface</i> version is not supported by <code>pmdaDaemon</code>.</dl>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2</code> or later. </p>
<p> Once <code>pmdaDaemon</code> has been called, it is expected that the <code>pmdaInterface</code> structure pointed to by <i>dispatch</i> will remain accessible to the routines in <i>libpcp_pmda</i> (not reclaimed off the stack, not freed or oherwise released, etc.). If the caller needs to move or relocate the <code>pmdaInterface</code> structure for any reason, then after the move <code><a href="/docs/linux/man/3-pmdainterfacemoved/">pmdaInterfaceMoved</a></code>(3) must be called to resestablish the internal integrity of the <i>pmdaInterface</i> structure at the new location before any other routine in <i>libpcp_pmda</i> is called.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3), <code><a href="/docs/linux/man/3-pmdainterfacemoved/">pmdaInterfaceMoved</a></code>(3) and <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3). </p>
