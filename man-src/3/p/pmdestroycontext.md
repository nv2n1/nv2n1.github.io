---
title: "pmdestroycontext(3)"
name: "pmdestroycontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdestroycontext/"
description: "pmDestroyContext – destroy a PMAPI context"
---

<p><code>pmDestroyContext</code> &#8211; destroy a PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmDestroyContext(int </code><i>handle</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>An application using the Performance Metrics Application Programming Interface (PMAPI) may manipulate several concurrent contexts, each associated with a source of performance metrics, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on some host, or an archive log of performance metrics as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> <code>pmDestroyContext</code> destroys the PMAPI context identified by <i>handle</i>. Typically this would imply some termination of a connection to a PMCD or closing an archive log file, and orderly clean-up. </p>
<p> The context must have been previously created using <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) or <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3). </p>
<p> On success, <code>pmDestroyContext</code> returns zero. If <i>handle</i> was the current PMAPI context, then the current context becomes undefined. This means the application must explicitly re-establish a valid PMAPI context with <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3), or create a new context with <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) or <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), before the next PMAPI operation that requires a PMAPI context.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_NOCONTEXT</code></p>
<dl>
<dd><i>handle</i> does not identify a valid PMAPI context </p>
</dl>
