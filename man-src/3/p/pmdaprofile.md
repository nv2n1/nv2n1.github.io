---
title: "pmdaprofile(3)"
name: "pmdaprofile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaprofile/"
description: "pmdaProfile – update instance profile for PMDA in preparation for the next fetch from PMCD"
---

<p><code>pmdaProfile</code> &#8211; update instance profile for PMDA in preparation for the next fetch from PMCD</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaProfile(__pmProfile *</code><i>prof</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaProfile</code> is the default callback which handles the receipt of a <code>__pmProfile</code> from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). A profile describes the instances that <code>pmcd</code> requires in the <code>pmResult</code> structure returned by the next fetch. <code>pmdaProfile</code> simply stores the new profile.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) and <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3). </p>
