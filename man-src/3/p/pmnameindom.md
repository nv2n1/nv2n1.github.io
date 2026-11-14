---
title: "pmnameindom(3)"
name: "pmnameindom"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnameindom/"
description: "pmNameInDom – translate an instance identifier into an instance name"
---

<p><code>pmNameInDom</code> &#8211; translate an instance identifier into an instance name</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmNameInDom(pmInDom <i>indom</i>, int <i>inst</i>, char **<i>name</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>For the instance domain <i>indom</i>, in the current Performance Metrics Application Programming Interface (PMAPI) context, locate the instance with the internal instance identifier given by <i>inst</i>, and return the full external instance identification via <i>name</i>. </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The space for the value of <i>name</i> will have been allocated in <code>pmNameInDom</code> with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the caller to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the space when it is no longer required. </p>
<p> <code>pmNameInDom</code> returns zero on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindomarchive/">pmNameInDomArchive</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_INDOM</code></p>
<dd><i>indom</i> is not a valid instance domain identifier</p>
<dt><code>PM_ERR_INST</code></p>
<dd>The instance identifier <i>inst</i> is not known for the instance domain <i>indom</i> in the current PMAPI context </p>
</dl>
