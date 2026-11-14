---
title: "pmiaddmetric(3)"
name: "pmiaddmetric"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiaddmetric/"
description: "pmiAddMetric – add a new metric definition to a LOGIMPORT context"
---

<p><code>pmiAddMetric</code> &#8211; add a new metric definition to a LOGIMPORT context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiAddMetric(const char *</code><i>name</i>, pmID <i>pmid</i>, int&nbsp;<wbr><i>type</i>, pmInDom&nbsp;<wbr><i>indom</i>, int&nbsp;<wbr><i>sem</i>, pmUnits&nbsp;<wbr><i>units</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiAddMetric($</code><i>name</i>, $<i>pmid</i>, $<i>type</i>, $<i>indom</i>, $<i>sem</i>, $<i>units</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiAddMetric</code> is used to define a new metric. The metric&#8217;s <i>name</i> must follow the naming conventions described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and should be unique for each LOGIMPORT context. </p>
<p> The other arguments are in effect the fields of a <code>pmDesc</code> structure. Refer to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a complete description of the values and semantics of the components of this structure, and hence the valid argument values for <code>pmiAddMetrics</code>. </p>
<p> The internal identifier for the metric may be given using the <i>pmid</i> argument and must be unique for each LOGIMPORT context. The value for <i>pmid</i> which would typically be constructed using the <code>pmid_build</code> macro, e.g. pmid_build(PMI_DOMAIN, 0, 3) for the fourth metric in first &#8220;cluster&#8221; of metrics in the Performance Metrics Domain PMI_DOMAIN (which is the default for all meta data created by the LOGIMPORT library). Alternatively, <i>pmid</i> may be <code>PM_IN_NULL</code> and <code>pmiAddMetric</code> will assign a unique <i>pmid</i> (although this means the <i>pmid</i> remains opaque and the application must use <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) or <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3) and cannot use <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3) to add data values to the PCP archive). </p>
<p> <i>type</i> defines the data type of the metric and must be one of the <code>PM_TYPE_&#8230;</code> values defined in <code>&lt;pcp/import.h&gt;</code>. </p>
<p> The instance domain for the metric is defined by <i>indom</i> and may be <code>PM_INDOM_NULL</code> for a metric with a singular value, else the value for <i>indom</i> would normally be constructed using the <code>pmInDom_build</code> macro, e.g. pmInDom_build(LOGIMPORT,0) for the first instance domain in the Performance Metrics Domain LOGIMPORT (which is the default for all meta data created by the LOGIMPORT library). Multiple metrics can share the same instance domain if they have values for a similar (or more usually, identical) set of instances. </p>
<p> The semantics of the metric (counter, instantaneous value, etc.) is specified by the <i>sem</i> argument which would normally be the result of a call to the convenience constructor method <code><a href="/docs/linux/man/3-pmiunits/">pmiUnits</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmiAddMetric</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmiunits/">pmiUnits</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
