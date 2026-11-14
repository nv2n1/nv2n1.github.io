---
title: "pmevent(1)"
name: "pmevent"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmevent/"
description: "pmval, pmevent – arbitrary performance metrics value dumper"
---

<h2>NAME</h2>
<p> <code>pmval</code>, <code>pmevent</code> &#8211; arbitrary performance metrics value dumper</p>
<h2>SYNOPSIS</h2>
<p> <code>pmval</code> [<code>-dgLrvz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>] [<code>-f</code> <i>N</i>] [<code>-h</code> <i>host</i>] [<code>-i</code> <i>instances</i>] [<code>-K</code> <i>spec</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>offset</i>] [<code>-p</code> <i>port</i>] [<code>-S</code> <i>starttime</i>] [<code>-s</code> <i>samples</i>] [<code>-T</code> <i>endtime</i>] [<code>-t</code> <i>interval</i>] [<code>-U</code> <i>archive</i>] [<code>-w</code> <i>width</i>] [<code>-x</code> <i>pattern</i>] [<code>-Z</code> <i>timezone</i>] <i>metricname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmval</code> prints current or archived values for the nominated performance metric. The metric of interest is named in the <i>metricname</i> argument, subject to instance qualification with the <code>-i</code> flag as described below. </p>
<p> Unless directed to another host by the <code>-h</code> option, or to a set of archives by the <code>-a</code> or <code>-U</code> options, <code>pmval</code> will contact the Performance Metrics Collector Daemon (PMCD) on the local host to obtain the required information. </p>
<p> The <i>metricname</i> argument may also be given in the metric specification syntax, as described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), where the source, metric and instance may all be included in the <i>metricname</i>, e.g. thathost:kernel.all.load[&quot;1 minute&quot;]. When this format is used, none of the <code>-h</code> or <code>-a</code> or <code>-U</code> options may be specified. </p>
<p> When using the metric specification syntax, the &#8220;hostname&#8221; <code>@</code> is treated specially and causes <code>pmval</code> to use a local context to collect metrics from PMDAs on the local host without PMCD. Only some metrics are available in this mode. </p>
<p> When processing a set of archives, <code>pmval</code> may relinquish its own timing control, and operate as a &#8220;slave&#8221; of a <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) process that uses a GUI dialog to provide timing control. In this case, either the <code>-g</code> option should be used to start <code>pmval</code> as the sole slave of a new <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) instance, or <code>-p</code> should be used to attach <code>pmval</code> to an existing <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) instance via the IPC channel identified by the <i>port</i> argument. </p>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code> and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &#8220;natural&#8221; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of these options. </p>
<p> The other options which control the source, timing and layout of the information reported by <code>pmval</code> are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> Performance metric values are retrieved from the set of Performance Co-Pilot (PCP) archive logs identified. The argument is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. See also <code>-U</code>.</p>
<dt><code>-d</code></p>
<dd> When replaying from a set of archives, this option requests that the prevailing real-time delay be applied between samples (see <code>-t</code>) to effect a pause, rather than the default behaviour of replaying at full speed.</p>
<dt><code>-f</code></p>
<dd> Numbers are reported in &#8220;fixed point&#8221; notation, rather than the default scientific notation. Each number will be up to the column width determined by the default heuristics, else the <code>-w</code> option if specified, and include <i>N</i> digits after the decimal point. So, the options <code>-f 3 -w 8</code> would produce numbers of the form 9999.999. A value of zero for <i>N</i> omits the decimal point and any fractional digits.</p>
<dt><code>-g</code></p>
<dd> Start <code>pmval</code> as the slave of a new <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) process for replay of archived performance data using the <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) graphical user interface.</p>
<dt><code>-h</code></p>
<dd> Current performance metric values are retrieved from the nominated <i>host</i> machine.</p>
<dt><code>-i</code></p>
<dd> <i>instances</i> is a list of one or more instance names for the nominated performance metric &#8211; just these instances will be retrieved and reported (the default is to report all instances). The list must be a single argument, with elements of the list separated by commas and/or white space.</p>
<dl>
<dt>
<dd>
<p> The instance name may be quoted with single (&#8216;) or double (&quot;) quotes for those cases where the instance name contains white space or commas. </p>
<p> Multiple <code>-i</code> options are allowed as an alternative way of specifying more than one instance of interest. </p>
<p> As an example, the following are all equivalent: <code> </p>
<p> </code></p>
<pre>
$ pmval -i &quot;'1 minute','5 minute'&quot; kernel.all.load
$ pmval -i '&quot;1 minute&quot;,&quot;5 minute&quot;' kernel.all.load
$ pmval -i &quot;'1 minute' '5 minute'&quot; kernel.all.load
$ pmval -i &quot;'1 minute'&quot; -i &quot;'5 minute'&quot; kernel.all.load
$ pmval 'localhost:kernel.all.load[&quot;1 minute&quot;,&quot;5 minute&quot;]'
</pre>
</dl>
<dt><code>-K</code></p>
<dd> When fetching metrics from a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used.</p>
<dt><code>-n</code></p>
<dd> Normally <code>pmval</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile.</i></p>
<dt><code>-p</code></p>
<dd> Attach <code>pmval</code> to an existing <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) time control process instance via the IPC channel identified by the <i>port</i> argument. This option is normally only used by other tools, e.g. <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), when they launch <code>pmval</code> with synchronized time control.</p>
<dt><code>-r</code></p>
<dd> Print raw values for cumulative counter metrics. Normally cumulative counter metrics are converted to rates. For example, disk transfers are reported as number of disk transfers per second during the preceding sample interval, rather than the raw value of number of disk transfers since the machine was booted. If you specify this option, the raw metric values are printed.</p>
<dt><code>-s</code></p>
<dd> The argument <i>samples</i> defines the number of samples to be retrieved and reported. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pmval</code> will sample and report continuously (in real time mode) or until the end of the set of PCP archives (in archive mode).</p>
<dt><code>-t</code></p>
<dd> The default update <i>interval</i> may be set to something other than the default 1 second. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds).</p>
<dt><code>-U</code></p>
<dd> Performance metric values are retrieved from the set of Performance Co-Pilot (PCP) archive logs identified. The argument is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. However, unlike <code>-a</code> every recorded value in the archive for the selected metric and instances is reported (so no interpolation mode, and the sample interval (<code>-t</code> option) is ignored. See also <code>-a</code>.</p>
<dl>
<dt>
<dd>
<p> At most one of the options <code>-a</code> and <code>-U</code> may be specified.</dl>
<dt><code>-w</code></p>
<dd> Set the width of each column of output to be <i>width</i> columns. If not specified columns are wide enough to accommodate the largest value of the type being printed.</p>
<dt><code>-x</code></p>
<dd> The given <i>pattern</i> is sent to the performance metric domain agent for the requested <i>metricname</i> before any values are requested. This serves two purposes. Firstly, it provides a mechanism for server-side event filtering that is customisable for individual event streams. In addition, some performance metrics domain agents also use the PMCD store mechanism to provide a basic security model (e.g. for sensitive log files, only a client host with <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3) access would be able to access the event stream).</p>
<dl>
<dt>
<dd>
<p> As <i>pattern</i> may be processed by <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3) it should be a non-empty string. Use . (dot) for a &#8220;match all&#8221; <i>pattern</i>.</dl>
<dt><code>-Z</code></p>
<dd> By default, <code>pmval</code> reports the time of day according to the local timezone on the system where <code>pmval</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-z</code></p>
<dd> Change the reporting timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <i>metricname</i> or the <code>-h</code> or <code>-a</code> or <code>-U</code> options.</dl>
<p> The following symbols may occasionally appear, in place of a metric value, in <code>pmval</code> output: A question mark symbol (?) indicates that a value is no longer available for that metric instance. An exclamation mark (!) indicates that a 64-bit counter wrapped during the sample. </p>
<p> The output from <code>pmval</code> is directed to standard output.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error and are intended to be self-explanatory.</p>
<h2>CAVEATS</h2>
<p> By default, <code>pmval</code> attempts to display non-integer numeric values in a way that does not distort the inherent precision (rarely more than 4 significant digits), and tries to maintain a tabular format in the output. These goals are sometimes in conflict. </p>
<p> In the absence of the <code>-f</code> option (described above), the following table describes the formats used for different ranges of numeric values for any metric that is of type <code>PM_TYPE_FLOAT</code> or <code>PM_TYPE_DOUBLE</code>, or any metric that has the semantics of a counter (for which <code>pmval</code> reports the rate converted value): <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Format</td>
<td ALIGN=center>Value Range
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>!</td>
<td>No values available
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9.999E-99</td>
<td>&lt; 0.1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9.9999</td>
<td>&gt; 0 and &lt;= 0.9999
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9.999&nbsp;<wbr></td>
<td>&gt; 0.9999 and &lt; 9.999
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>99.99&nbsp;<wbr>&nbsp;<wbr></td>
<td>&gt; 9.999 and &lt; 99.99
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>999.9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>&gt; 99.99 and &lt; 999.9
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9999.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>&gt; 999.9 and &lt; 9999
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9.999E+99</td>
<td>&gt; 9999
</td>
</tr>
</table>
</table>
<p></center> </p>
<h2>Index</h2>
