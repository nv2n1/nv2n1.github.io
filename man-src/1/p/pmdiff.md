---
title: "pmdiff(1)"
name: "pmdiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdiff/"
description: "pmdiff – compares archives and report significant differences"
---

<h2>NAME</h2>
<p> <code>pmdiff</code> &#8211; compares archives and report significant differences</p>
<h2>SYNOPSIS</h2>
<p> <code>pmdiff</code> [<code>-d</code>/<code>&#8211;keep</code>] [<code>-z</code>/<code>&#8211;hostzone</code>] [<code>-p</code>/<code>&#8211;precision</code> <i>precision</i>] [<code>-q</code>/<code>&#8211;threshold</code> <i>thres</i>] [<code>-S</code>/<code>&#8211;start</code> <i>starttime</i>] [<code>-T</code>/<code>&#8211;finish</code> <i>endtime</i>] [<code>-B</code>/<code>&#8211;begin</code> <i>starttime</i>] [<code>-E</code>/<code>&#8211;end</code> <i>endtime</i>] [<code>-x</code> <i>metric</i>] [<code>-X</code> <i>file</i>] [<code>&#8211;skip-excluded</code>] [<code>&#8211;skip-missing</code>] [<code>-Z</code>/<code>&#8211;timezone</code> <i>timezone</i>] <i>archive1</i> [<i>archive2</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdiff</code> compares the average values for every metric in either one or two sets of archives, in a given time window, for changes that are likely to be of interest when searching for performance regressions. </p>
<p> The archive specifiers <i>archive1</i> and <i>archive2</i> may be comma-separated lists of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. Each archive in the resulting set of archives must have been previously created using <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). The <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1) utility is used to obtain the average values used for comparison. </p>
<p> There are two sorts of invocation of the tool: with either one or two sets of archives. </p>
<p> In the first case, the only sensible command line requires use of all four time window arguments. These are specified using the same time window format described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and are <code>-S</code>/<code>&#8211;start</code> and <code>-T</code>/<code>&#8211;finish</code> for the start and end times of the first time window of interest in the archive set, and <code>-B</code>/<code>&#8211;before</code> and <code>-E</code>/<code>&#8211;end</code> for the start and end times of the second time window of interest. </p>
<p> In the second case, with two sets of archives, the <code>-B</code>/<code>&#8211;before</code> and <code>-E</code>/<code>&#8211;end</code> options might be unnecessary. This might be the case, for example, when comparing the same time window of two consecutive days (usually two separate sets of archives), or a time window on the same day of different weeks. </p>
<p> In either case, <code>pmdiff</code> produces a sorted summary of those metrics in the specified window whose values have deviated the most from a minimal threshold. The level of deviation is calculated by dividing the average value of each metric in both logs, and then calculating whether the ratio falls outside of a range considered normal. This ratio can be adjusted using the <code>-q</code>/<code>&#8211;threshold</code> option, and by default it is 2 (i.e. report all metrics with average values that have more than doubled in the two time windows or more than halved in the two time windows). </p>
<p> If the baseline value is zero and the comparison value is non-zero, the ratio is reported as &#8220;|+|&#8221; (infinitely large). If the comparison value is zero and the baseline value is non-zero, the ratio is reported as &#8220;|-|&#8221; (infinitely small). </p>
<p> Reported metrics are sorted in ascending ratio order. </p>
<p> Should any metrics be present in one window but missing from the other, a diagnostic will be displayed listing each missing metric and the archive set from which it was missing. </p>
<p> The remaining options control the specific information to be reported. Metrics with counter semantics are converted to rates before being evaluated.</p>
<dl>
<dt><code>-p</code>/<code>&#8211;precision</code></p>
<dd> Print all floating point numbers with <i>precision</i> digits after the decimal place.</p>
<dt><code>&#8211;skip-excluded</code></p>
<dd> Cull the list of names of metrics being excluded from the output.</p>
<dt><code>&#8211;skip-missing</code></p>
<dd> By default, <code>pmdiff</code> will report the names of any metrics that are in one archive set but not the other. This option suppresses that reporting.</p>
<dt><code>-x</code></p>
<dd> Compare each metric in each archive set in the time windows specified to a given <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) pattern, excluding those that match from the report output.</p>
<dt><code>-X</code></p>
<dd> Allows a <i>file</i> to be specified which containing <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) patterns which are applied to the metric names to optionally exclude some from the report.</p>
<dt><code>-z</code></p>
<dd> Use the local timezone from the given archive set.</p>
<dt><code>-Z</code>/<code>&#8211;timezone</code></p>
<dd> Changes the timezone in the archive labels to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dl>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> Default directory for PCP archives containing performance metric values collected from the host <i>hostname</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
