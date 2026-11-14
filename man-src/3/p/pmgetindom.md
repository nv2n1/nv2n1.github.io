---
title: "pmgetindom(3)"
name: "pmgetindom"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetindom/"
description: "pmGetInDom – get instance identifiers for a performance metrics instance domain"
---

<p><code>pmGetInDom</code> &#8211; get instance identifiers for a performance metrics instance domain</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmGetInDom(pmInDom <i>indom</i>, int **<i>instlist</i>, char ***<i>namelist</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>In the current Performance Metrics Application Programming Interface (PMAPI) context, locate the description of the instance domain <i>indom</i>, and return via <i>instlist</i> the internal instance identifiers for all instances, and via <i>namelist</i> the full external identifiers for all instances. The number of instances found is returned as the function value (else less than zero to indicate an error). </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The resulting lists of instance identifiers (<i>instlist</i> and <i>namelist</i>), and the names that the elements of <i>namelist</i> point to, will have been allocated by <code>pmGetInDom</code> with two calls to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the caller to <i>free(instlist)</i> and <i>free(namelist)</i> to release the space when it is no longer required. </p>
<p> When the result of <code>pmGetInDom</code> is less than one, both <i>instlist</i> and <i>namelist</i> are undefined (no space will have been allocated, and so calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) is a singularly bad idea).</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindomarchive/">pmGetInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_INDOM</code></p>
<dd><i>indom</i> is not a valid instance domain identifier </p>
</dl>
