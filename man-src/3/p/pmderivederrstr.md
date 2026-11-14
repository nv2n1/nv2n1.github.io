---
title: "pmderivederrstr(3)"
name: "pmderivederrstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmderivederrstr/"
description: "pmDerivedErrStr – return error message from failure to parse derived metric definition"
---

<p><code>pmDerivedErrStr</code> &#8211; return error message from failure to parse derived metric definition</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> char *pmDerivedErrStr(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>When <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3) is called to add a new derived metric definition and an error occurs, <code>pmDerivedErrStr</code> may be called to return the associated error message. </p>
<p> The <code>pmRegisterDerivedMetric</code> interface provides a convenience wrapper around both <code>pmRegisterDerived</code> and <code>pmDerivedErrStr</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3). </p>
