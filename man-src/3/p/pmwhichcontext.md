---
title: "pmwhichcontext(3)"
name: "pmwhichcontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmwhichcontext/"
description: "pmWhichContext – identify the current PMAPI context"
---

<p><code>pmWhichContext</code> &#8211; identify the current PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmWhichContext(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>An application using the Performance Metrics Application Programming Interface (PMAPI) may manipulate several concurrent contexts, each associated with a source of performance metrics, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on some host, or an archive log of performance metrics as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> <code>pmWhichContext</code> returns a handle for the current PMAPI context, that may be used in the associated PMAPI routines that require a handle to identify a PMAPI context.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdestroycontext/">pmDestroyContext</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOCONTEXT</code></p>
<dd>no current context </p>
</dl>
