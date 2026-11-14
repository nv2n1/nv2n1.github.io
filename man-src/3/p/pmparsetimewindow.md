---
title: "pmparsetimewindow(3)"
name: "pmparsetimewindow"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmparsetimewindow/"
description: "pmParseTimeWindow – parse time window command line arguments"
---

<p><code>pmParseTimeWindow</code> &#8211; parse time window command line arguments</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmParseTimeWindow(const char *</code><i>swStart</i>, const char&nbsp;<wbr>*<i>swEnd</i>, const char&nbsp;<wbr>*<i>swAlign</i>, const char&nbsp;<wbr>*<i>swOffset</i>, const struct timeval&nbsp;<wbr>*<i>logStart</i>, const struct timeval&nbsp;<wbr>*<i>logEnd</i>, struct timeval&nbsp;<wbr>*<i>rsltStart</i>, struct timeval&nbsp;<wbr>*<i>rsltEnd</i>, struct timeval&nbsp;<wbr>*<i>rsltOffset</i>, char&nbsp;<wbr>**<i>errMsg</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmParseTimeWindow</code> is designed to encapsulate the interpretation of the <code>-S</code>, <code>-T</code>, <code>-A</code> and <code>-O</code> command line options used by Performance Co-Pilot (PCP) applications to define a time window of interest. The time window is defined by a start time and an end time that constrains the time interval during which the PCP application will retrieve and display performance metrics. In the absence of the <code>-O</code> and <code>-A</code> options to specify an initial sample time origin and time alignment (see below), the PCP application will retrieve the first sample at the start of the time window. </p>
<p> The syntax and meaning of the various argument formats for these options is described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1).</p>
<h2>Usage</h2>
<p><code>pmParseTimeWindow</code> expects to be called with the argument of the <code>-S</code> option as <code>swStart</code>, the argument of the <code>-T</code> option as <code>swEnd</code>, the argument of the <code>-A</code> option as <code>swAlign</code>, and the argument of the <code>-O</code> option as <code>swOffset</code>. Any or all of these parameters may be NULL to indicate that the corresponding command line option was not present. </p>
<p> If the application is using a set of PCP archive logs as the source of performance metrics, you also need to supply the time of the first archive log entry as <code>logStart</code>, and the time of the last archive log entry as <code>logEnd</code>. See <code><a href="/docs/linux/man/3-pmgetarchivelabel/">pmGetArchiveLabel</a></code>(3) and <code><a href="/docs/linux/man/3-pmgetarchiveend/">pmGetArchiveEnd</a></code>(3) for how to obtain values for these times. </p>
<p> If the application is manipulating multiple concurrent archive logs, then the caller must resolve how the default time window is to be defined (the union of the time intervals in all archive logs is a likely interpretation). </p>
<p> If the application is using a live feed of performance data, <code>logStart</code> should be the current time (but could be aligned on the next second for example), while <code>logEnd</code> should have its <i>tv_sec</i> component set to <code>INT_MAX</code>. </p>
<p> The <code>rsltStart</code>, <code>rsltEnd</code> and <code>rsltOffset</code> structures must be allocated before calling <code>pmParseTimeWindow</code>. </p>
<p> You also need to set the current PCP reporting time zone to correctly reflect the <code>-z</code> and <code>-Z</code> command line parameters before calling <code>pmParseTimeWindow</code>. See <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3) and friends for information on how this is done.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetarchiveend/">pmGetArchiveEnd</a></code>(3), <code><a href="/docs/linux/man/3-pmgetarchivelabel/">pmGetArchiveLabel</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3), <code><a href="/docs/linux/man/3-pmparseinterval/">pmParseInterval</a></code>(3) and <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>If the conversion is successful, <code>pmParseTimeWindow</code> returns 1 and fills in <code>rsltStart</code>, <code>rsltEnd</code> and <code>rsltOffset</code> with the start, end, and offset times for the time window defined by the input parameters. The <code>errMsg</code> parameter is not changed when <code>pmParseTimeWindow</code> returns 1. </p>
<p> If the conversion is successful, but the requested alignment could not be performed (e.g. the set of PCP archive logs is too short) the alignment is ignored, <code>rsltStart</code>, <code>rsltEnd</code> and <code>rsltOffset</code> are filled in and <code>pmParseTimeWindow</code> returns 0. In this case, <code>errMsg</code> will point to a warning message in an internal static buffer. This buffer should not be freed. </p>
<p> If the argument strings could not be parsed, <code>pmParseTimeWindow</code> returns -1. In this case, <code>errMsg</code> will point to an error message in a static internal buffer.</p>
