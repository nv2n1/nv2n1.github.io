---
title: "pmiputmark(3)"
name: "pmiputmark"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiputmark/"
description: "pmiPutMark – write a <mark> record to a PCP archive"
---

<p><code>pmiPutMark</code> &#8211; write a <i>&lt;mark&gt;</i> record to a PCP archive</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiPutMark(void); </p>
<p> cc &#8230; -lpcp_import -lpcp </code></p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiPutMark(); </code></p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiPutMark</code> writes a <code>&lt;mark&gt;</code> record to the current PCP output archive. This is required when there is a temporal discontinuity between the current input source and the next input source, if any, and should be called after the final call to <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) for the current input. If there is no next input to be processed or no temporal gap between sources, then the <code>&lt;mark&gt;</code> record is not required. </p>
<p> The <code>&lt;mark&gt;</code> record is used to signify a temporal gap, so that when replaying the output PCP archive, interpolation of metric values should not be performed between the last timestamp in the current input source to the first timestamp in the next input source, i.e. across the <code>&lt;mark&gt;</code> record.</p>
<h2>Diagnostics</h2>
<p><code>pmiPutMark</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) and <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3). </p>
