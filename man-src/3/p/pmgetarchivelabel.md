---
title: "pmgetarchivelabel(3)"
name: "pmgetarchivelabel"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetarchivelabel/"
description: "pmGetArchiveLabel – fetch the label record from a set of performance metrics archive logs"
---

<p><code>pmGetArchiveLabel</code> &#8211; fetch the label record from a set of performance metrics archive logs</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetArchiveLabel(pmLogLabel *</code><i>lp</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Within the framework of the Performance Co-Pilot (PCP), archive logs of performance metrics values may be accumulated and saved using the program <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> The routine <code>pmGetArchiveLabel</code> may be used to fetch the label record from a set of archive logs that has already been opened using <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), or <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), and thereby associated with the current Performance Metrics Application Programming Interface (PMAPI) context. </p>
<p> The result returned via the pointer <i>lp</i> is a structure that must be pre-allocated by the caller and has the following format (defined in <code>pmapi.h</code>). </p>
<pre>/*
 * Label Record at the start of every log file
 */
typedef struct {
 int ll_magic; /* PM_LOG_MAGIC | log format version no. */
 pid_t ll_pid; /* PID of logger */
 struct timeval ll_start;/* start of this log */
 char ll_hostname[PM_LOG_MAXHOSTLEN]; /* name of collection host */
 char ll_tz[40]; /* $TZ at collection host */
} pmLogLabel;</pre>
<p>For an application, the most useful information from the archive label is likely to be in the fields <i>ll_start</i>, <i>ll_hostname</i> or <i>ll_tz</i>. </p>
<p> Note that the size of the <i>ll_hostname</i> field is <i>PM_LOG_MAXHOSTLEN</i> (64 bytes) which is less than <code>MAXHOSTNAMELEN</code> (see <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3)) on some platforms. These semantics are necessary to retain backwards compatibility with the PCP archive file format. </p>
<p> <code>pmGetArchiveLabel</code> returns zero for success.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOCONTEXT</code></p>
<dd>the current PMAPI context is either invalid, or not associated with a set of archive logs </p>
</dl>
