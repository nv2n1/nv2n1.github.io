---
title: "pmnameid(3)"
name: "pmnameid"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnameid/"
description: "pmNameID – translate a PMID to a performance metric name"
---

<p><code>pmNameID</code> &#8211; translate a PMID to a performance metric name</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmNameID(pmID <i>pmid</i>, char **<i>name</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a Performance Metric Identifier (PMID) via <i>pmid</i>, <code>pmNameID</code> will determine the corresponding metric name, if any, in the Performance Metrics Name Space (PMNS), and return this via <i>name</i>. </p>
<p> If the PMNS contains multiple names associated with the requested PMID, one of these will be returned via <i>name</i>, but there is no way to determine which of the duplicate names this will be. See <code><a href="/docs/linux/man/3-pmnameall/">pmNameAll</a></code>(3) if all of the corresponding names are required. </p>
<p> As of Version 3.10.3 of PCP, duplicate names for the same PMID <code>are</code> allowed in the PMNS, so using <code><a href="/docs/linux/man/3-pmnameall/">pmNameAll</a></code>(3) is recommended over <code>pmnameID</code>. </p>
<p> <i>name</i> is a null-byte terminated string, allocated by <code>pmNameID</code> using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and it is the caller&#8217;s responsibility to call <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to release the storage when the value is no longer required. </p>
<p> In the absence of errors, <code>pmNameID</code> returns zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildrenstatus/">pmGetChildrenStatus</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), <code><a href="/docs/linux/man/3-pmnameall/">pmNameAll</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>Failed to access a PMNS for operation. Note that if the application hasn&#8217;t a priori called <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) and wants to use the distributed PMNS, then a call to <code>pmNameID</code> must be made after the creation of a context (see <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3)).</p>
<dt><code>PM_ERR_PMID</code></p>
<dd><i>pmid</i> does not correspond to a defined PMID in the PMNS.</p>
<dt><code>PM_ERR_*</code></p>
<dd>Other diagnostics are for protocol failures when accessing the distributed PMNS. </p>
</dl>
