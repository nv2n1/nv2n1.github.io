---
title: "pmfreeresult(3)"
name: "pmfreeresult"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfreeresult/"
description: "pmFreeResult – release storage allocated for performance metrics values"
---

<p><code>pmFreeResult</code> &#8211; release storage allocated for performance metrics values</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> void pmFreeResult(pmResult *</code><i>result</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The variable sized results returned by <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) are allocated below the Performance Metrics Application Programming Interface (PMAPI) using a combination of dynamic (i.e. <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)) and specialized allocation strategies. </p>
<p> Applications should call <code>pmFreeResult</code> to release the storage previously allocated for <i>result</i> by <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), when the application no longer requires access to the <i>pmResult</i> structure. </p>
<p> Under <code>no</code> circumstances should an application use <i>free(result)</i> to release storage previously allocated for a <i>pmResult</i> by <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
