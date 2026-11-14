---
title: "pmgetindomarchive(3)"
name: "pmgetindomarchive"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetindomarchive/"
description: "pmGetInDomArchive – get instance identifiers for a performance metrics instance domain"
---

<p><code>pmGetInDomArchive</code> &#8211; get instance identifiers for a performance metrics instance domain</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetInDomArchive(pmInDom </code><i>indom</i>, int **<i>instlist</i>, char ***<i>namelist</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Provided the current Performance Metrics Application Programming Interface (PMAPI) context is associated with a set of archive logs, <code>pmGetInDomArchive</code> will scan the union of all the instance domain metadata for the instance domain <i>indom</i>, and return via <i>instlist</i> the internal instance identifiers for all instances, and via <i>namelist</i> the full external identifiers for all instances. </p>
<p> This routine is a specialized version of the more general PMAPI routine <code>pmGetInDom</code>. </p>
<p> The number of instances found is returned as the function value (else less than zero to indicate an error). </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The resulting lists of instance identifiers (<i>instlist</i> and <i>namelist</i>), and the names that the elements of <i>namelist</i> point to, will have been allocated by <code>pmGetInDomArchive</code> with two calls to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the caller to <i>free(instlist)</i> and <i>free(namelist)</i> to release the space when it is no longer required. </p>
<p> When the result of <code>pmGetInDomArchive</code> is less than one, both <i>instlist</i> and <i>namelist</i> are undefined (no space will have been allocated, and so calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) is a singularly bad idea).</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomarchive/">pmLookupInDomArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmnameindomarchive/">pmNameInDomArchive</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOTARCHIVE</code></p>
<dd>the current PMAPI context is not associated with a set of archive logs</p>
<dt><code>PM_ERR_INDOM_LOG</code></p>
<dd><i>indom</i> is not a defined instance domain identifier for the set of archive logs </p>
</dl>
