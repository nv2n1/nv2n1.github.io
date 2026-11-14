---
title: "pmtraversepmns(3)"
name: "pmtraversepmns"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmtraversepmns/"
description: "pmTraversePMNS, pmTraversePMNS_r – traverse the performance metrics name space"
---

<p><code>pmTraversePMNS</code>, <code>pmTraversePMNS_r</code> &#8211; traverse the performance metrics name space</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmTraversePMNS(const char *<i>name</i>, void (*<i>dometric</i>)(const char *));
int pmTraversePMNS_r(const char *<i>name</i>, void (*<i>dometric_r</i>)(const char *, void *), void *<i>closure</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The routine <code>pmTraversePMNS</code> may be used to perform a depth-first traversal of the Performance Metrics Name Space (PMNS). </p>
<p> The traversal starts at the node identified by <i>name</i> &#8211; if <i>name</i> is an empty string (i.e. <code>&quot;&quot;</code>), the traversal starts at the root of the PMNS. Usually <i>name</i> would be the pathname of a non-leaf node in the PMNS. </p>
<p> For each leaf node (i.e. performance metric) found in the traversal, the user-supplied routine <i>dometric</i> is called with the full pathname of that metric in the PMNS as the single argument. This argument is null-byte terminated, and is constructed from a buffer that is managed internally to <code>pmTraversePMNS</code>. Consequently the value is only valid during the call to <i>dometric</i> &#8211; if the pathname needs to be retained, it should be copied using <code><a href="/docs/linux/man/3-strdup/">strdup</a></code>(3) before returning from <i>dometric</i>. </p>
<p> The <code>pmTraversePMNS_r</code> routine performs the same function, except the callback method <i>func_r</i> has an additional parameter that will be <i>closure</i> from the initial call to <code>pmTraversePMNS_r</code>. The additional parameter to <code>pmTraversePMNS_r</code> and the callback method allows the caller to pass context through <code>pmTraversePMNS_r</code> and into the callback method <i>func_r</i>, making the service more useful for multi-threaded applications where thread-private data can be accessed in the callback method via the <i>closure</i> argument. </p>
<p> On success <code>pmTraversePMNS</code> returns the number of children of <i>name</i>, which may be zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>Failed to access a PMNS for operation. Note that if the application hasn&#8217;t a priori called <a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a>(3) and wants to use the distributed PMNS, then a call to <code>pmTraversePMNS</code> must be made inside a current context.</p>
<dt><code>PM_ERR_NAME</code></p>
<dd>The initial pathname <i>name</i> is not valid in the current PMNS.</p>
<dt><code>PM_ERR_*</code></p>
<dd>Other diagnostics are for protocol failures when accessing the distributed PMNS. </p>
</dl>
