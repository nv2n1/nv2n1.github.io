---
title: "pmindomstr(3)"
name: "pmindomstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmindomstr/"
description: "pmInDomStr, pmInDomStr_r – convert a performance metric instance domain identifier into a string"
---

<p><code>pmInDomStr</code>, <code>pmInDomStr_r</code> &#8211; convert a performance metric instance domain identifier into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmInDomStr(pmInDom </code><i>indom</i>);<br />
 char *pmInDomStr_r(pmInDom <i>indom</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>For use in error and diagnostic messages, <code>pmInDomStr</code> return a &#8216;human readable&#8217; version of the specified instance domain identifier. The <code>pmInDomStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 20 bytes. </p>
<p> The value for the instance domain <i>indom</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> Internally, an instance domain identifier is encoded as follows; </p>
<pre>typedef struct {
 int pad:2;
 unsigned int domain:8; /* the administrative PMD */
 unsigned int serial:22; /* unique within PMD */
} __pmInDom_int;</pre>
<p><code>pmInDomStr</code> returns a string with each of the <i>domain</i> and <i>serial</i> subfields appearing as decimal numbers, separated by periods. </p>
<p> The string value returned by <code>pmInDomStr</code> is held in a single static buffer, so the returned value is only valid until the next call to <code>pmInDomStr</code>.</p>
<h2>Notes</h2>
<p><code>pmInDomStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmInDomStr_r</code> instead.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmidstr/">pmIDStr</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
