---
title: "pmiwrite(3)"
name: "pmiwrite"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiwrite/"
description: "pmiWrite – flush data to a LOGIMPORT archive"
---

<p><code>pmiWrite</code> &#8211; flush data to a LOGIMPORT archive</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiWrite(int </code><i>sec</i>, int <i>usec</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiWrite($</code><i>sec</i>, $<i>usec</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiWrite</code> forces accumulated data values out to the PCP archive. </p>
<p> The data values and associated metadata have previously been built up using calls to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) and <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3). </p>
<p> The current set of data values and any new metadata is written to the archive with a timestamp of <i>sec</i> and <i>usec</i> in the source timezone of the archive, see <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmiWrite</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) and <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3). </p>
