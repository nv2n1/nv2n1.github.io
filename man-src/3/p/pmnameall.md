---
title: "pmnameall(3)"
name: "pmnameall"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnameall/"
description: "pmNameAll – translate a PMID to a set of performance metric names"
---

<p><code>pmNameAll</code> &#8211; translate a PMID to a set of performance metric names</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmNameAll(pmID <i>pmid</i>, char ***<i>nameset</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a Performance Metric Identifier (PMID) via <i>pmid</i>, <code>pmNameAll</code> will determine all the corresponding metric names, if any, in the Performance Metrics Name Space (PMNS), and return these via <i>nameset</i>. </p>
<p> The resulting list of pointers <i>nameset</i> <code>and</code> the values (the relative names) that the pointers reference will have been allocated by <code>pmNameAll</code> with a single call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the <code>pmNameAll</code> caller to <i>free(nameset)</i> to release the space when it is no longer required. </p>
<p> In the absence of errors, <code>pmNameAll</code> returns the number of names in <i>nameset</i>. </p>
<p> For many examples of a PMNS, there will be a 1:1 mapping between a name and a PMID, and under these circumstances, <code><a href="/docs/linux/man/3-pmnameid/">pmNameID</a></code>(3) provides a slightly simpler interface in the absence of duplicate names for a particular PMID.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildrenstatus/">pmGetChildrenStatus</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), <code><a href="/docs/linux/man/3-pmnameid/">pmNameID</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>Failed to access a PMNS for operation. Note that if the application hasn&#8217;t a priori called <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) and wants to use the distributed PMNS, then a call to <code>pmNameAll</code> must be made after the creation of a context (see <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3)).</p>
<dt><code>PM_ERR_PMID</code></p>
<dd><i>pmid</i> does not correspond to a defined PMID in the PMNS.</p>
<dt><code>PM_ERR_*</code></p>
<dd>Other diagnostics are for protocol failures when accessing the distributed PMNS. </p>
</dl>
