---
title: "pmdadesc(3)"
name: "pmdadesc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdadesc/"
description: "pmdaDesc – get the description of a metric from a PMDA"
---

<p><code>pmdaDesc</code> &#8211; get the description of a metric from a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaDesc(pmID </code><i>pmid</i>, pmDesc *<i>desc</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaDesc</code> uses the standard <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) data structures to return the <code>pmDesc</code> description in <i>desc</i> for the metric identified by <i>pmid</i>.</p>
<h2>Diagnostics</h2>
<p>If the <i>pmid</i> does not correspond to any metric supported by this PMDA, <code>pmdaDesc</code> returns <code>PM_ERR_PMID</code>.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
