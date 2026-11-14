---
title: "pmdastore(3)"
name: "pmdastore"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdastore/"
description: "pmdaStore – store a value into a metric for a PMDA"
---

<p><code>pmdaStore</code> &#8211; store a value into a metric for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaStore(pmResult *</code><i>result</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaStore</code> is the generic callback for storing a value into a metric. <code>pmdaStore</code> is usually a no-op as, by default, no metrics can be altered. Also, the implementation of a store callback which does permit metrics to be altered by <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) is very application dependent.</p>
<h2>Diagnostics</h2>
<p><code>pmdaStore</code> returns <code>PM_ERR_PERMISSION</code> to indicate that no metrics may be modified.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) and <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3). </p>
