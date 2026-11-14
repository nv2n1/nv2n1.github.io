---
title: "pmlookupindomarchive(3)"
name: "pmlookupindomarchive"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlookupindomarchive/"
description: "pmLookupInDomArchive – translate an instance name into an instance identifier"
---

<p><code>pmLookupInDomArchive</code> &#8211; translate an instance name into an instance identifier</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmLookupInDomArchive(pmInDom </code><i>indom</i>, const char *<i>name</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Provided the current Performance Metrics Application Programming Interface (PMAPI) context is associated with a set of archive logs, <code>pmLookupInDomArchive</code> will scan the union of all the instance domain metadata for the instance domain <i>indom</i>, locate the first instance with the external identification given by <i>name</i>, and return the internal instance identifier. </p>
<p> This routine is a specialized version of the more general PMAPI routine <code>pmLookupInDom</code>. </p>
<p> Only the leading non-space characters of <i>name</i> will be used to identify the instance. </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> <code>pmLookupInDomArchive</code> will return a positive instance identifier on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindomarchive/">pmGetInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindomarchive/">pmNameInDomArchive</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOTARCHIVE</code></p>
<dd>the current PMAPI context is not associated with a set of archive logs</p>
<dt><code>PM_ERR_INDOM_LOG</code></p>
<dd><i>indom</i> is not a defined instance domain identifier for the set of archive logs</p>
<dt><code>PM_ERR_INST_LOG</code></p>
<dd>the external instance <i>name</i> is not known for the instance domain <i>indom</i> in the set of archive logs </p>
</dl>
