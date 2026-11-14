---
title: "pmfetcharchive(3)"
name: "pmfetcharchive"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfetcharchive/"
description: "pmFetchArchive – get performance metrics directly from a set if archive logs"
---

<p><code>pmFetchArchive</code> &#8211; get performance metrics directly from a set if archive logs</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmFetchArchive(pmResult **</code><i>result</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmFetchArchive</code> is a variant of <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) that may only be used when the current Performance Metrics Application Programming Interface (PMAPI) context is associated with a set of archive logs. </p>
<p> The <i>result</i> is instantiated with all of the metrics (and instances) from the next archive record, consequently there is no notion of a list of desired metrics, and the instance profile of the PMAPI context is ignored. </p>
<p> <code>pmFetchArchive</code> may return a <i>result</i> in which <i>numpmid</i> is zero. This is a <i>&lt;mark&gt;</i> record that indicates a temporal discontinuity in the time series of performance metrics. This can happen at the boundary between archive logs in a set or if the archive log associated with the current PMAPI context was created using <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1) to concatenate two or more PCP archive logs, and the <i>&lt;mark&gt;</i> record marks a point in time between the end of one input archive and the start of the next input archive. </p>
<p> It is expected that <code>pmFetchArchive</code> would be used to create utilities that scan sets of archive logs, while the more common access to the archives would be via the <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) interface. </p>
<p> To skip records within the set of archive logs, use <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3) to change the collection time within the current PMAPI context, then call <code>pmFetchArchive.</code> </p>
<p> Note that the <i>result</i> returned by <code>pmFetchArchive</code> is dynamically allocated, and must be released using <code><a href="/docs/linux/man/3-pmfreeresult/">pmFreeResult</a></code>(3), not <code><a href="/docs/linux/man/3-free/">free</a></code>(3). See <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) and <code><a href="/docs/linux/man/3-pmfreeresult/">pmFreeResult</a></code>(3) for further details. </p>
<p> <code>pmFetchArchive</code> returns zero on success.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmfreeresult/">pmFreeResult</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3) and <code><a href="/docs/linux/man/3-pmtrimnamespace/">pmTrimNameSpace</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOTARCHIVE</code></p>
<dd>the current PMAPI context is not associated with a set of archive logs </p>
</dl>
