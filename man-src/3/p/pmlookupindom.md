---
title: "pmlookupindom(3)"
name: "pmlookupindom"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlookupindom/"
description: "pmLookupInDom – translate an instance name into an instance identifier"
---

<p><code>pmLookupInDom</code> &#8211; translate an instance name into an instance identifier</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmLookupInDom(pmInDom <i>indom</i>, const char *<i>name</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>For the instance domain <i>indom</i>, in the current Performance Metrics Application Programming Interface (PMAPI) context, locate the instance with the external identification given by <i>name</i>, and return the internal instance identifier. </p>
<p> Only the leading non-space characters of <i>name</i> will be used to identify the instance. </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> <code>pmLookupInDom</code> will return a positive instance identifier on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomarchive/">pmLookupInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_INDOM</code></p>
<dd><i>indom</i> is not a valid instance domain identifier</p>
<dt><code>PM_ERR_INST</code></p>
<dd>The external instance <i>name</i> is not known for the instance domain <i>indom</i> in the current PMAPI context </p>
</dl>
