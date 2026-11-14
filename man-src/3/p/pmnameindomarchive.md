---
title: "pmnameindomarchive(3)"
name: "pmnameindomarchive"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnameindomarchive/"
description: "pmNameInDomArchive – translate an instance identifier into an instance name"
---

<p><code>pmNameInDomArchive</code> &#8211; translate an instance identifier into an instance name</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmNameInDomArchive(pmInDom </code><i>indom</i>, int <i>inst</i>, char **<i>name</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Provided that the current Performance Metrics Application Programming Interface (PMAPI) context is associated with a set of archive logs, <code>pmNameInDomArchive</code> will scan the union of all the instance domain metadata for the instance domain <i>indom</i>, locate the first instance with the internal instance identifier given by <i>inst</i>, and return the full external instance identification via <i>name</i>. </p>
<p> This routine is a specialized version of the more general PMAPI routine <code>pmNameInDom</code>. </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The space for the value of <i>name</i> will have been allocated in <code>pmNameInDomArchive</code> with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the caller to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the space when it is no longer required. </p>
<p> <code>pmNameInDomArchive</code> returns zero on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindomarchive/">pmGetInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomarchive/">pmLookupInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOTARCHIVE</code></p>
<dd>the current PMAPI context is not associated with a set of archive logs</p>
<dt><code>PM_ERR_INDOM_LOG</code></p>
<dd><i>indom</i> is not a defined instance domain identifier for the set of archive logs</p>
<dt><code>PM_ERR_INST_LOG</code></p>
<dd>the instance identifier <i>inst</i> is not known for the instance domain <i>indom</i> in the set of archive logs </p>
</dl>
