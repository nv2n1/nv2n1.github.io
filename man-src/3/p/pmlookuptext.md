---
title: "pmlookuptext(3)"
name: "pmlookuptext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlookuptext/"
description: "pmLookupText – return text describing a performance metric"
---

<p><code>pmLookupText</code> &#8211; return text describing a performance metric</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmLookupText(pmID <i>pmid</i>, int <i>level</i>, char **<i>buffer</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Provided the source of metrics from the current Performance Metrics Application Programming Interface (PMAPI) context is a host, retrieve descriptive text about the performance metric identified by <i>pmid</i>. </p>
<p> The argument <i>level</i> should be <code>PM_TEXT_ONELINE</code> for a one-line summary, else <code>PM_TEXT_HELP</code> for a more verbose description, suited to a help dialog. </p>
<p> The space pointed to by <i>buffer</i> will have been allocated in <code>pmLookupText</code> with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the caller to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the space when it is no longer required. </p>
<p> <code>pmLookupText</code> returns zero on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chkhelp/">chkhelp</a></code>(1), <code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomtext/">pmLookupInDomText</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOTHOST</code></p>
<dd>if the current PMAPI context is an archive log (help and one-line text is not maintained in the archive logs) </p>
</dl>
