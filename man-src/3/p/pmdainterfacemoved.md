---
title: "pmdainterfacemoved(3)"
name: "pmdainterfacemoved"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdainterfacemoved/"
description: "pmdaInterfaceMoved – reset internal state of a pmdaInterface structure"
---

<p><code>pmdaInterfaceMoved</code> &#8211; reset internal state of a <i>pmdaInterface</i> structure</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> void pmdaInterfaceMoved(pmdaInterface *</code><i>dispatch</i>) </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>After a call to either <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) to initialize the <code>pmdaInterface</code> structure, if the caller needs to relocate or move the structure for any reason then <code>pmdaInterfaceMoved</code> needs to be called with the new base address of the <i>pmdaInterface</i> routine as specified by <i>dispatch</i>. </p>
<p> <code>pmdaInterfaceMoved</code> will re-establish the internal integrity of the <i>pmdaInterface</i> structure at the new location before any other routine in <i>libpcp_pmda</i> called.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2</code> or later.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) and <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3). </p>
