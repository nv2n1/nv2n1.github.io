---
title: "qmcsource(3)"
name: "qmcsource"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmcsource/"
description: "QmcSource – manages contexts created by all groups"
---

<p><code>QmcSource </code> &#8211; manages contexts created by all groups</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QmcSource.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>The <code>QmcSource</code> class maintains a unique list of all metric sources in use to minimize the creation of new contexts (see <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3)) when the context could have been duplicated (see <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3)). This also reduces the duplication of descriptions of each source. </p>
<p> In general, <code>QMC</code> users should only need to access <code>QmcSource</code> methods to obtain source descriptions for a <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3) object. All context creation by the user should be handled through <code><a href="/docs/linux/man/3-qmcgroup/">QmcGroup</a></code>(3).</p>
<h2>Destructor</h2>
<dl COMPACT>
<dt><code>~QmcSource();</code></p>
<dd>Destructor.</dl>
<h2>Constructors</h2>
<dl COMPACT>
<dt><code>static QmcSource* getSource(int type, const char* source,</code></p>
<dd><code>bool matchHosts)</code> </p>
<p> This method will return a <code>QmcSource</code> object that represents a context of <i>type</i> to <i>source</i>. The <code>QmcSource</code> object may be a new object if the <i>source</i> has not been previously requested. Memory management of the <code>QmcSource</code> objects is handled by <code>QmcSource</code>. If all <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3)s to the <code>QmcSource</code> have been deleted, the <code>QmcSource</code> object will also be deleted. </p>
<p> The <i>matchHosts</i> flag controls the algorithm that is used to match hosts to archives. If <i>matchHosts</i> is equal to <code>false</code> then no attempt will be made by this method to match a host context to an existing source context. A <code>QmcSource</code> object will always be returned in this case, although the <code>QmcSource::status</code> method may indicate that a context to <i>source</i> failed. </p>
<p> If <i>matchHosts</i> is equal to <code>true</code>, host contexts will be matched to a pre-defined archive source collected from that <i>source</i>. If no archive sources for the <i>source</i> have been previous specified, <code>getSource</code> will return a NULL pointer.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3), <code><a href="/docs/linux/man/3-qmcgroup/">QmcGroup</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> to the global <i>pmDebug</i>.</p>
