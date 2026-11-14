---
title: "pmiputvaluehandle(3)"
name: "pmiputvaluehandle"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiputvaluehandle/"
description: "pmiPutValueHandle – add a value for a metric-instance pair via a handle"
---

<p><code>pmiPutValueHandle</code> &#8211; add a value for a metric-instance pair via a handle</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiPutValueHandle(int </code><i>handle</i>, const char *<i>value</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiPutValueHandle($</code><i>handle</i>, $<i>value</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiPutValueHandle</code> adds a single value to the current output record for a given metric and instance, using the <i>handle</i> defined by an earlier call to <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3). </p>
<p> The <i>value</i> should be in a format consistent with the metric&#8217;s type as defined in the call to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3). </p>
<p> No data will be written until <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) is called, so multiple calls to <code>pmiPutValueHandle</code> or <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) are typically used to accumulate data values for several metric-instance pairs before calling <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmiPutValueHandle</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) and <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3). </p>
