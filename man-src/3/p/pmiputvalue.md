---
title: "pmiputvalue(3)"
name: "pmiputvalue"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiputvalue/"
description: "pmiPutValue – add a value for a metric-instance pair"
---

<p><code>pmiPutValue</code> &#8211; add a value for a metric-instance pair</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiPutValue(const char *</code><i>name</i>, const char *<i>instance</i>, const char&nbsp;<wbr>*<i>value</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiPutValue($</code><i>name</i>, $<i>instance</i>, $<i>value</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiPutValue</code> adds a single value to the current output record for a given metric and instance. </p>
<p> The metric&#8217;s <i>name</i> should match one defined earlier in a call to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3). </p>
<p> For singular metrics (those defined with an instance domain of <code>PM_INDOM_NULL</code>), the <i>instance</i> should be NULL or an empty string, otherwise <i>instance</i> should match the name of an instance defined earlier in a call to <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3) for the metric&#8217;s instance domain. </p>
<p> The <i>value</i> should be in a format consistent with the metric&#8217;s type as defined in the call to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3). </p>
<p> No data will be written until <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) is called, so multiple calls to <code>pmiPutValue</code> or <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) are typically used to accumulate data values for several metric-instance pairs before calling <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmiPutValue</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) and <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3). </p>
