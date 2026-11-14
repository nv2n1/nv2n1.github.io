---
title: "qmccontext(3)"
name: "qmccontext"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmccontext/"
description: "QmcContext – container for a PMAPI context and its metrics"
---

<p><code>QmcContext</code> &#8211; container for a PMAPI context and its metrics</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QmcContext.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>A <code>QmcContext</code> object is a container for a single <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) context. The object maintains a list of all the metric descriptors (<code>QmcDesc</code>), instance domains (<code>QmcIndom</code>) and metrics (<code>QmcMetric</code>) using the context to minimize the duplication of these objects.</p>
<h2>Constructors</h2>
<p>A <code>QmcContext</code> object should be constructed through the <code>QmcGroup::use</code> interface.</p>
<h2>Descriptor Lookup</h2>
<p>The metric and instance domain descriptors are cached by the <code>QmcContext</code> object to reduce duplicate <code><a href="/docs/linux/man/3-qmcdesc/">QmcDesc</a></code>(3) and <code><a href="/docs/linux/man/3-qmcindom/">QmcIndom</a></code>(3) objects and <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) calls required to create them. Also the mapping from metrics names to <code>pmID</code>s is also maintained to avoid <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3) calls.</p>
<dl COMPACT>
<dt><code>int lookupDesc(const char *name, pmID&amp; id);</code></p>
<dd>Search for the metric <i>name</i> in the name list and set <code>id</code> to the known <code>pmID</code>. If not found, use <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3) to get the mapping. If this call fails, the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error code will be returned.</p>
<dt><code>int lookupDesc(const char *name, uint_t&amp; desc, uint_t&amp; indom);</code></p>
<dd>Find the index <i>desc</i> and <i>indom</i> to the <code>QmcDesc</code> object and the <code>QmcIndom</code> object for the metric <i>name</i>. The indexes can then be used with <code>QmcContext::desc</code> and <code>QmcContext::indom</code> to obtain references to the real objects. The methods will return a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error code if the metric descriptor or instance domain could not be obtained.</p>
<dt><code>int lookupDesc(pmID pmid, uint_t&amp; desc, uint_t&amp; indom);</code></p>
<dd>Find the index <i>desc</i> and <i>indom</i> to the <code>QmcDesc</code> object and the <code>QmcIndom</code> object for the metric <i>pmid</i>. The indexes can then be used with <code>QmcContext::desc</code> and <code>QmcContext::indom</code> to obtain references to the real objects. The methods will return a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error code if the metric descriptor or instance domain could not be obtained.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-qmcdesc/">QmcDesc</a></code>(3), <code><a href="/docs/linux/man/3-qmcgroup/">QmcGroup</a></code>(3), <code><a href="/docs/linux/man/3-qmcindom/">QmcIndom</a></code>(3), <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> and <code>DBG_TRACE_OPTFETCH</code> to the global <i>pmDebug</i>.</p>
