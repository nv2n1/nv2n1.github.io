---
title: "pmrep(1)"
name: "pmrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmrep/"
description: "pmrep – performance metrics reporter"
---

<h2>NAME</h2>
<p> <code>pmrep</code> &#8211; performance metrics reporter</p>
<h2>SYNOPSIS</h2>
<p> <code>pmrep</code> [<code>-CdGHLpruUVxz?</code>] [<code>-a</code> <i>archive</i>] [<code>-A</code> <i>align</i>] [<code>-b</code> <i>space-scale</i>] [<code>-c</code> <i>config</i>] [<code>-e</code> <i>derived</i>] [<code>-E</code> <i>lines</i>] [<code>-f</code> <i>format</i>] [<code>-F</code> <i>outfile</i>] [<code>-h</code> <i>host</i>] [<code>-K</code> <i>spec</i>] [<code>-l</code> <i>delimiter</i>] [<code>-o</code> <i>output</i>] [<code>-O</code> <i>origin</i>] [<code>-P</code> <i>precision</i>] [<code>-q</code> <i>count-scale</i>] [<code>-s</code> <i>samples</i>] [<code>-S</code> <i>starttime</i>] [<code>-t</code> <i>interval</i>] [<code>-T</code> <i>endtime</i>] [<code>-w</code> <i>width</i>] [<code>-y</code> <i>time-scale</i>] [<code>-Z</code> <i>timezone</i>] <i>metricspec [&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmrep</code> is a customizable performance metrics reporting tool. Any available performance metric, live or archived, system and/or application, can be selected for reporting using one of the output alternatives listed below together with applicable formatting options. </p>
<p> <code>pmrep</code> collects the selected metric values through the facilities of the Performance Co-Pilot (PCP), see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). The metrics to be reported are specified on the command line, in a configuration file, or both. Metrics can be automatically converted and scaled using the PCP facilities, either by default or by per-metric scaling specifications. In addition to the existing metrics, derived metrics can be defined using the arithmetic expressions described in <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3). </p>
<p> Unless directed to another host by the <code>-h</code> option, <code>pmrep</code> will contact the Performance Metrics Collector Daemon (PMCD, see <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1)) on the local host. </p>
<p> The <code>-a</code> option causes <code>pmrep</code> to use the specified set of archive logs rather than connecting to a PMCD. The <code>-a</code> and <code>-h</code> options are mutually exclusive. </p>
<p> The <code>-L</code> option causes <code>pmrep</code> to use a local context to collect metrics from DSO PMDAs (Performance Metrics Domain Agents, &#8220;plugins&#8221;) on the local host without PMCD. Only some metrics are available in this mode. The <code>-a</code>, <code>-h</code>, and <code>-L</code> options are mutually exclusive. </p>
<p> The metrics of interest are named in the <i>metricspec</i> argument(s). If a metricspec specifies a non-leaf node in the Performance Metrics Name Space (PMNS), then <code>pmrep</code> will recursively descend the PMNS and report on all leaf nodes (i.e., metrics) for that metricspec. (Use for example <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1) to list all the leaf nodes and their descriptions.) </p>
<p> A <i>metricspec</i> has three different forms. First, on the command line it can start with a colon (&#8220;:&#8221;) to indicate a <i>metricset</i> to be read from a <code>pmrep</code> configuration file (see <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5)) which can then consist of any number of metricspecs. Second, a <i>metricspec</i> starting with non-colon specifies a PMNS node as described above, optionally followed by metric formatting definitions (applicable only to leaf nodes). This so-called <i>compact form</i> of a metricspec is defined as follows: </p>
<pre><code>
metric[, label[, instance[, unit / scale[, type[, width]]]]]
</code></pre>
<p> A valid PMNS node (<i>metric</i>) is mandatory. It can be followed by a text <i>label</i> used by supporting output targets (such as <i>csv</i> and <i>stdout</i>, see below). The optional <i>instance</i> definition is currently unimplemented. An optional <i>unit/scale</i> is applicable for dimension-compatible, non-string, and (currently) non-raw metrics. (See below for supported <i>unit/scale</i> specifications.) By default, cumulative counter metrics are converted to rates. If the optional <i>type</i> field is set to <code>raw</code> then this rate conversion is disabled, unit/scale specification is (currently) ignored and raw values are reported instead. Finally, for supporting output targets (currently: <i>stdout</i>) a numeric <i>width</i> can be used to set the width of the output column for this metric. Too-wide numeric values for output will not be printed (apart from decimal places, numeric values will never be silently truncated). Too-wide strings will be truncated. </p>
<p> The following <i>metricspec</i> requests the metric <code>kernel.all.sysfork</code> to be reported under the label <code>forks</code>, converting to the default rate count/s in an <code>8</code> wide column. Although the definitions in this <i>compact form</i> are optional, they must always be provided in the order specified above. </p>
<pre>
kernel.all.sysfork,forks,,,,8
</pre>
<p> The third form of a metricspec is valid only in <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5). </p>
<p> Derived metrics are specified like PMNS leaf node metrics. </p>
<p> Configuration file parameters override the corresponding built-in default values (if any). Command line parameters override the corresponding configuration file parameters (if any).</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The available command line options are:</p>
<dl>
<dt><code>-a</code></p>
<dd> Performance metric values are retrieved from the set of Performance Co-Pilot (PCP) archive log files identified by the argument <i>archive</i>, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. See also <code>-u</code>.</p>
<dt><code>&#8211;archive-folio</code></p>
<dd> Read metric source archives from the PCP archive <i>folio</i> (see <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1)).</p>
<dt><code>-A</code></p>
<dd> When reporting archived metrics, force the initial sample to be aligned on the boundary of a natural time unit <i>align</i>. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>align</i>.</p>
<dt><code>-b</code></p>
<dd> <i>Unit/scale</i> for space (byte) metrics, possible values include <code>bytes</code>, <code>Kbytes</code>, <code>KB</code>, <code>Mbytes</code>, <code>MB</code>, and so forth up to <code>Ebytes</code>. This option will <i>not</i> override possible per-metric specifications. See also <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3).</p>
<dt><code>-c</code></p>
<dd> Specify the <i>config</i> file to use. The default is <code>./pmrep.conf</code>. See <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5).</p>
<dt><code>-C</code></p>
<dd> Exit before reporting any values, but after parsing the configuration and metrics and printing possible headers.</p>
<dt><code>-d</code></p>
<dd> When replaying from an archive, this option requests that the prevailing real-time delay be applied between samples (see <code>-t</code>) to effect a pause, rather than the default behaviour of replaying at full speed.</p>
<dt><code>-e</code></p>
<dd> Specify <i>derived</i> performance metrics. If <i>derived</i> starts with a slash (&#8220;/&#8221;) or with a dot (&#8220;.&#8221;) it will be interpreted as a derived metrics configuration file, otherwise it will be interpreted as comma-separated derived metric expressions. For details see <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3) and <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3).</p>
<dt><code>-E</code></p>
<dd> Repeat the header every <i>lines</i> of output.</p>
<dt><code>-f</code></p>
<dd> Use the <i>format</i> string for formatting the timestamp. The format will be used with Python&#8217;s <code>datetime.strftime</code> method which is mostly the same as that described in <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). An empty <i>format</i> string (i.e., &#8221;) will remove the timestamps from the output. The default with stdout is <code>%H:%M:%S</code>. The default with csv is <code>%Y-%m-%d %H:%M:%S</code>.</p>
<dt><code>-F</code></p>
<dd> Specify the output file <i>outfile</i>. See <code>-o</code>.</p>
<dt><code>-G</code></p>
<dd> Do not include global metrics in reporting (see <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5)).</p>
<dt><code>-h</code></p>
<dd> Fetch performance metrics from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on <i>host</i>, rather than the default localhost.</p>
<dt><code>-H</code></p>
<dd> Do not print any headers.</p>
<dt><code>-K</code></p>
<dd> When fetching metrics from a local context (see <code>-L</code>), the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a>(3).</code> More than one <code>-K</code> option may be used.</p>
<dt><code>-l</code></p>
<dd> Specify the <i>delimiter</i> that separates each column of <i>csv</i> or <i>stdout</i> output. The <i>delimiter</i> may only be a single character. The default for <i>stdout</i> is two spaces (&#8220; &#8221;) and comma (&#8220;,&#8221;) for <i>csv</i>.</p>
<dt><code>-L</code></p>
<dd> Use a local context to collect metrics from DSO PMDAs on the local host without PMCD. See also <code>-K</code>.</p>
<dt><code>-o</code></p>
<dd> Use <i>output</i> target for reporting. The default target is <i>stdout</i>. The available target alternatives are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>archive</i></p>
<dd> Record metrics into a PCP archive which can later be replayed with PCP tools, including <code>pmrep</code> itself. See <code><a href="/docs/linux/man/5-pcp-archive/">pcp-archive</a></code>(5) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for details about PCP archive files. Requires <code>-F</code>.</p>
<dt><i>csv</i></p>
<dd> Print metrics in CSV format (subject to formatting options).</p>
<dt><i>stdout</i></p>
<dd> Print metrics to stdout (format subject to formatting options).</p>
<dt><i>zabbix</i></p>
<dd> Send metrics to a Zabbix server. See <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5) for the needed Zabbix configuration parameters. This target is currently <i>experimental</i>.</dl>
</dl>
<dt><code>-O</code></p>
<dd> When reporting archived metrics, start reporting at <i>origin</i> within the time window (see <code>-S</code> and <code>-T</code>). Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>origin</i>.</p>
<dt><code>-p</code></p>
<dd> Print timestamps. By default no timestamps are printed.</p>
<dt><code>-P</code></p>
<dd> Use <i>precision</i> for numeric non-integer output values. If the value is too wide for its column width, <i>precision</i> is reduced one by one until the value fits, or not printed at all if it does not. The default is to use 3 decimal places (when applicable).</p>
<dt><code>-q</code></p>
<dd> <i>Unit/scale</i> for count metrics, possible values include <code>count x 10^-1</code>, <code>count</code>, <code>count x 10</code>, <code>count x 10^2</code>, and so forth from <code>10^-8</code> to <code>10^7</code>. (These values are currently space-sensitive.) This option will <i>not</i> override possible per-metric specifications. See also <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3).</p>
<dt><code>-r</code></p>
<dd> Output raw metric values, do not convert cumulative counters to rates. This option <i>will</i> override possible per-metric specifications.</p>
<dt><code>-s</code></p>
<dd> The argument <i>samples</i> defines the number of samples to be retrieved and reported. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pmrep</code> will sample and report continuously (in real time mode) or until the end of the set of PCP archives (in archive mode). See also <code>-T</code>.</p>
<dt><code>-S</code></p>
<dd> When reporting archived metrics, the report will be restricted to those records logged at or after <i>starttime</i>. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>starttime</i>.</p>
<dt><code>-t</code></p>
<dd> The default update <i>interval</i> may be set to something other than the default 1 second. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). See also the <code>-T</code> and <code>-u</code> options.</p>
<dt><code>-T</code></p>
<dd> When reporting archived metrics, the report will be restricted to those records logged before or at <i>endtime</i>. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>endtime</i>.</p>
<dl>
<dt>
<dd>
<p> When used to define the runtime before <code>pmrep</code> will exit, if no <i>samples</i> is given (see <code>-s</code>) then the number of reported samples depends on <i>interval</i> (see <code>-t</code>). If <i>samples</i> is given then <i>interval</i> will be adjusted to allow reporting of <i>samples</i> during runtime. In case all of <code>-T</code>, <code>-s</code>, and <code>-t</code> are given, <i>endtime</i> determines the actual time <code>pmrep</code> will run.</dl>
<dt><code>-u</code></p>
<dd> When reporting archived metrics, by default values are reported according to the selected sample interval (<code>-t</code> option), not according to the actual record interval in an archive. To this effect PCP interpolates the values to be reported based on the records in the archive. With the <code>-u</code> option uninterpolated reporting is enabled, every recorded value for the selected metrics is reported and the requested sample interval (<code>-t</code>) is ignored.</p>
<dl>
<dt>
<dd>
<p> So for example, if a PCP archive contains recorded values for every 10 seconds and the requested sample interval is 1 hour, by default <code>pmrep</code> will use an interpolation scheme to compute the values of the requested metrics from the values recorded in the proximity of these requested metrics and values for every 1 hour are reported. With <code>-u</code> every record every 10 seconds are used as such (the reported values are still subject to rate conversion, use <code>-r</code> to disable).</dl>
<dt><code>-U</code></p>
<dd> Omit unit information from of headers.</p>
<dt><code>-V</code></p>
<dd> Display version number and exit.</p>
<dt><code>-w</code></p>
<dd> Set the stdout output column <i>width</i>. Strings will be truncated to this width. The default <i>width</i> is the shortest that can fit the metric label, the forced minimum is 3. This option will <i>not</i> override possible per-metric specifications.</p>
<dt><code>-x</code></p>
<dd> Print extended header.</p>
<dt><code>-y</code></p>
<dd> <i>Unit/scale</i> for time metrics, possible values include <code>nanosec</code>, <code>ns</code>, <code>microsec</code>, <code>us</code>, <code>millisec</code>, and so forth up to <code>hours</code>, <code>hr</code>. This option will <i>not</i> override possible per-metric specifications. See also <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3).</p>
<dt><code>-z</code></p>
<dd> Use the local timezone of the host that is the source of the performance metrics, as identified by either the <code>-h</code> or the <code>-a</code> options. The default is to use the timezone of the local host.</p>
<dt><code>-Z</code></p>
<dd> Use <i>timezone</i> when displaying the date and time. <i>Timezone</i> is in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-?</code></p>
<dd> Display usage message and exit.</dl>
<h2>EXAMPLES</h2>
<p> The following examples use the PCP facilities for collecting the metric values, no external utilities are needed. The examples expect the default configuration file to contain the <i>metricset</i> specifications. </p>
<p> Display network interface statistics on the local host:</p>
<dl>
<dt>
<dd>
<pre>
$ pmrep network.interface.total.bytes
</pre>
</dl>
<p> Display per-device disk reads and writes from the host <i>server1</i> using two seconds interval and CSV output format:</p>
<dl>
<dt>
<dd>
<pre>
$ pmrep -h server1 -o csv -t 2s disk.dev.read disk.dev.write
</pre>
</dl>
<p> Display timestamped <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8) like information using MBs instead of bytes and also include the number of in-use inodes:</p>
<dl>
<dt>
<dd>
<pre>
$ pmrep -p -b MB vfs.inodes.count :vmstat
</pre>
</dl>
<p> Display <code>sar -w</code> and <code>sar -W</code> like information at the same time from the PCP archive <i>./20150921.09.13</i> showing values recorded between 3 &#8211; 5 PM:</p>
<dl>
<dt>
<dd>
<pre>
$ pmrep -a ./20150921.09.13 -S @15:00 -T @17:00 :sar-w :sar-W
</pre>
</dl>
<p> Record all 389 Directory Server, XFS file system and CPU/disk/memory related metrics every five seconds for the next five minutes to the PCP archive <i>./a</i>:</p>
<dl>
<dt>
<dd>
<pre>
$ pmrep -o archive -F ./a -t 5s -T 5m ds389 xfs kernel.all.cpu disk mem
</pre>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>./pmrep.conf</code></p>
<dd> Default configuration file.</p>
<dt><code>/etc/pcp/pmrep/pmrep.conf</code></p>
<dd> Example configuration file.</dl>
<h2>BUGS</h2>
<p> No command line option can follow metrics. </p>
<p> Specifying instances is not yet supported.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parametrize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pcp-atop/">pcp-atop</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmcollectl/">pmcollectl</a></code>(1), <code><a href="/docs/linux/man/1-pmdiff/">pmdiff</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmiostat/">pmiostat</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1), <code><a href="/docs/linux/man/1-pmstat/">pmstat</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3), <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/5-pcp-archive/">pcp-archive</a></code>(5), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), <code><a href="/docs/linux/man/5-pmrep-conf/">pmrep.conf</a></code>(5), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) and <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8). </p>
<h2>Index</h2>
