---
title: "pmusecontext(3)"
name: "pmusecontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmusecontext/"
description: "pmUseContext – change current PMAPI context"
---

<p><code>pmUseContext</code> &#8211; change current PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmUseContext(int </code><i>handle</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>An application using the Performance Metrics Application Programming Interface (PMAPI) may manipulate several concurrent contexts, each associated with a source of performance metrics, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on some host, or an archive log of performance metrics as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Calling <code>pmUseContext</code> causes the current PMAPI context to be set to the context identified by <i>handle</i>. The value of <i>handle</i> must be one returned from an earlier call to <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) or <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3). </p>
<p> Below the PMAPI, all contexts used by an application are saved in their most recently modified state, so <code>pmUseContext</code> restores the context to the state it was in the last time the context was used, not the state of the context when it was established.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdestroycontext/">pmDestroyContext</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_NOCONTEXT</code></p>
<dl>
<dd><i>handle</i> does not identify a valid PMAPI context </p>
</dl>
