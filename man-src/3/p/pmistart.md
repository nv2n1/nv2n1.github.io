---
title: "pmistart(3)"
name: "pmistart"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmistart/"
description: "pmiStart – establish a new LOGIMPORT context"
---

<p><code>pmiStart</code> &#8211; establish a new LOGIMPORT context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiStart(const char *</code><i>archive</i>, int <i>inherit</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiStart($</code><i>archive</i>, $<i>inherit</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiStart</code> creates a new context. Each context maintains the following state and metadata:</p>
<dl>
<dt>&bull;</p>
<dd>The base name (<i>archive</i>) for the physical files that constitute the output PCP archive.</p>
<dt>&bull;</p>
<dd>The source hostname for the data that will be written to the PCP archive. Defaults to the hostname of the localhost, but can be set using <code><a href="/docs/linux/man/3-pmisethostname/">pmiSetHostname</a></code>(3).</p>
<dt>&bull;</p>
<dd>The source timezone for the PCP archive. Defaults to the timezone of the localhost, but can be set using <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3).</p>
<dt>&bull;</p>
<dd>Metrics and instance domains, as defined by <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3).</p>
<dt>&bull;</p>
<dd>Instances for each instance domain, as defined by <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3).</p>
<dt>&bull;</p>
<dd>Handles as defined by <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3). Each handle is a metric-instance pair, and each metric-instance pair may have an associated value in each record written to the output PCP archive.</p>
<dt>&bull;</p>
<dd>An optional set of data values for one or more metric-instance pairs (ready for the next record to be written to the output PCP archive) as defined by calls to <code><a href="/docs/linux/man/3-pmputvalue/">pmPutValue</a></code>(3) or <code><a href="/docs/linux/man/3-pmputvaluehandle/">pmPutValuehandle</a></code>(3).</dl>
<p> If <i>inherit</i> is true, then the new context will inherit any and all metadata (metrics, instance domains, instances and handles) from the current context, otherwise the new context is created with no metadata. The basename for the output PCP archive, the source hostname, the source timezone and any data values from the current context are <code>not</code> inherited. If this is the first call to <code>pmiStart</code> the metadata will be empty independent of the value of <i>inherit</i>. </p>
<p> Since no physical files for the output PCP archive will be created until the first call to <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) or <code><a href="/docs/linux/man/3-pmiputrecord/">pmiPutRecord</a>(3),</code> <i>archive</i> could be NULL to create a convenience context that is populated with metadata to be inherited by subsequent contexts. </p>
<p> The return value is a context identifier that could be used in a subsequent call to <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) and the new context becomes the current context which persists for all subsequent calls up to either another <code>pmiStart</code> call or a call to <code><a href="/docs/linux/man/3-pmiusecontext/">pmiUseContext</a></code>(3) or a call to <code><a href="/docs/linux/man/3-pmiend/">pmiEnd</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>It is an error if the physical files <i>archive</i>.<code>0</code> and/or <i>archive</i>.<code>index</code> and/or <i>archive</i>.<code>meta</code> already exist, but this is not discovered until the first attempt is made to output some data by calling <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3) or <code><a href="/docs/linux/man/3-pmiputrecord/">pmiPutRecord</a>(3),</code> so <code>pmiStart</code> always returns a positive context identifier.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmiend/">pmiEnd</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmiputresult/">pmiPutResult</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvaluehandle/">pmiPutValueHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmisethostname/">pmiSetHostname</a></code>(3), <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3), <code><a href="/docs/linux/man/3-pmiusecontext/">pmiUseContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmiwrite/">pmiWrite</a></code>(3). </p>
