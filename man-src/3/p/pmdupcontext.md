---
title: "pmdupcontext(3)"
name: "pmdupcontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdupcontext/"
description: "pmDupContext – duplicate a PMAPI context"
---

<p><code>pmDupContext</code> &#8211; duplicate a PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmDupContext(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>An application using the Performance Metrics Application Programming Interface (PMAPI) may manipulate several concurrent contexts, each associated with a source of performance metrics, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on some host, or a set of archive logs of performance metrics as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Calling <code>pmDupContext</code> will replicate the current PMAPI context, returning a handle for the new context that may be used with subsequent calls to <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3). </p>
<p> Once created, the duplicated context and the original context have independent existence, and so their instance profiles and collection time (relevant only for archive contexts) may be independently varied. </p>
<p> The newly replicated context becomes the current context.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3). </p>
