---
title: "pmsortinstances(3)"
name: "pmsortinstances"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmsortinstances/"
description: "pmSortInstances – sort performance metric values on instance identifier"
---

<p><code>pmSortInstances</code> &#8211; sort performance metric values on instance identifier</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> void pmSortInstances(pmResult *</code><i>result</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The routine <code>pmSortInstances</code> may be used to guarantee that for each performance metric in the <i>result</i> from <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), the instances are in ascending instance identifier sequence. </p>
<p> This is most useful when trying to compute rates from two consecutive <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>None.</p>
