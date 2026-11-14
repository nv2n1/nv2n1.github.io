---
title: "pmigethandle(3)"
name: "pmigethandle"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmigethandle/"
description: "pmiGetHandle – define a handle for a metric-instance pair"
---

<p><code>pmiGetHandle</code> &#8211; define a handle for a metric-instance pair</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiGetHandle(const char *</code><i>name</i>, const char *<i>instance</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> $</code><i>handle</i> = pmiGetHandle($<i>name</i>, $<i>instance</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiGetHandle</code> creates a handle for a given metric and instance. The handle is returned as the value from the <code>pmiGetHandle</code> call and can be used in subsequent calls to <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3). </p>
<p> The metric&#8217;s <i>name</i> should match one defined earlier in a call to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3). </p>
<p> For singular metrics (those defined with an instance domain of <code>PM_INDOM_NULL</code>), the <i>instance</i> should be NULL or an empty string, otherwise <i>instance</i> should match the name of an instance defined earlier in a call to <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3) for the metric&#8217;s instance domain. </p>
<p> When combined with <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3), the use of handles provide a performance improvement over the alternative lookup for a metric name and an instance name for each data value that is required for <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>On failure <code>pmiGetHandle</code> returns a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3). </p>
