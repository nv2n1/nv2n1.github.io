---
title: "pmgetarchiveend(3)"
name: "pmgetarchiveend"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetarchiveend/"
description: "pmGetArchiveEnd – locate logical end of file for a set of archive logs"
---

<p><code>pmGetArchiveEnd</code> &#8211; locate logical end of file for a set of archive logs</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetArchiveEnd(struct timeval *</code><i>tvp</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Assuming the current PMAPI context is associated with a set of archive logs, <code>pmGetArchiveEnd</code> will attempt to find the logical end of file (after the last complete record in the set of archives), and return the last recorded timestamp via <i>tvp</i>. This timestamp may be passed to <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3) to reliably position the context at the last valid log record, e.g. in preparation for subsequent reading in reverse chronological order. </p>
<p> For archive logs that are not concurrently being written, the physical end of file and the logical end of file are co-incident. However if an archive log is being written by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) at the same time an application is trying to read the archive, the logical end of file may be before the physical end of file due to write buffering that is not aligned with the logical record boundaries. </p>
<p> <code>pmGetArchiveEnd</code> returns an error less than zero if the context is neither valid, nor associated with a set of archives, or the set of archives is seriously corrupted. Otherwise, the return value is 0 if there has been no change of state since the last call, or 1 if the logical end of file has advanced since the last call. </p>
<p> In the absence of an error, the result returned via <i>tvp</i> is well-defined. </p>
<p> <code>pmGetArchiveEnd</code> preserves the positioning state of the log file prior to this function call.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmfetcharchive/">pmFetchArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmgetarchivelabel/">pmGetArchiveLabel</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOCONTEXT</code></p>
<dd>the current PMAPI context is either invalid, or not associated with an set of archive logs</p>
<dt><code>PM_ERR_LOGREC</code></p>
<dd>the set of archives is sufficiently damaged, that not a single valid record can be found </p>
</dl>
