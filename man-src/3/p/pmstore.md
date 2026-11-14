---
title: "pmstore(3)"
name: "pmstore"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmstore/"
description: "pmStore – modify values of performance metrics"
---

<p><code>pmStore</code> &#8211; modify values of performance metrics</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmStore(const pmResult *<i>result</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>In some special cases it may be helpful to modify the current values of performance metrics, e.g. to reset a counter to zero, or to modify a &#8220;metric&#8221; which is a control variable for some agent collecting performance metrics. </p>
<p> The routine <code>pmStore</code> is a lightweight inverse of <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
<p> The caller must build the <i>pmResult</i> data structure (of course, this could have been returned from an earlier <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) call) and then call <code>pmStore</code>. </p>
<p> It is an error to pass a request to <code>pmStore</code> in which the <i>numval</i> field within any of the <code>pmValueSet</code> structure has a value less than one. </p>
<p> The current Performance Metrics Application Programming Interface (PMAPI) context must be one with a host as the source of metrics, and the current value of the nominated metrics will be changed, i.e. <code>pmStore</code> cannot be used to make retrospective changes to information in either the archive logs, or in the recent past for real-time sources of metrics. </p>
<p> The return code from <code>pmStore</code> is zero for success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) and <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_GENERIC</code></p>
<dd>At least one of the modifications was rejected. No other status is available from below the PMAPI (this is the lightweight part of the functionality!). In cases where the outcome of <code>pmStore</code> for individual metrics is important, the caller should make one call to <code>pmStore</code> for each metric. On the other hand, a bulk modification can be performed in a single <code>pmStore</code> call for situations in which the outcome is not critical.</p>
<dt><code>PM_ERR_NOTHOST</code></p>
<dd>The current PMAPI context is an archive rather than a host, or it is a host that is not set to the current time, i.e. has been &#8220;rewound&#8221; to the recent past using <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3).</p>
<dt><code>PM_ERR_TOOSMALL</code></p>
<dd>The number of metrics specified in <i>result</i> is less than one.</p>
<dt><code>PM_ERR_VALUE</code></p>
<dd>One or more of the <i>pmValueSet</i>s in <i>result</i> has a <i>numval</i> field with a value less than one. </p>
</dl>
