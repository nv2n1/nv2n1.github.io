---
title: "pmiputresult(3)"
name: "pmiputresult"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiputresult/"
description: "pmiPutResult – add a data record to a LOGIMPORT archive"
---

<p><code>pmiPutResult</code> &#8211; add a data record to a LOGIMPORT archive</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiPutResult(const pmResult *</code><i>result</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiPutResult</code> provides an interface for developers familiar with the internal PCP data structures to create output archives directly. </p>
<p> By building the <code>pmResult</code> data structure directly, then calling <code>pmiPutResult</code> the developer avoids calls to <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) and/or <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) followed by a call to <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) for each record written to the archive. </p>
<p> Any metrics and instances appearing in the <i>result</i> must have been defined by prior calls to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3) and <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3). </p>
<p> <code>pmiPutResult</code> will arrange for any new metadata (metrics and/or instance domain changes) covered by <i>result</i> to be also written to the PCP archive. </p>
<p> Because of the complexity of the <code>pmResult</code> data structure, this routine is not available in the Perl interface to the LOGIMPORT services.</p>
<h2>Diagnostics</h2>
<p><code>pmiPutResult</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3) and <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3). </p>
