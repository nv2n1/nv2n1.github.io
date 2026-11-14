---
title: "pcp-iostat(1)"
name: "pcp-iostat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-iostat/"
description: "pmiostat, pcp-iostat – performance metrics i/o statistics tool"
---

<h2>NAME</h2>
<p> <code>pmiostat</code>, <code>pcp-iostat</code> &#8211; performance metrics i/o statistics tool</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp iostat</code> [<code>-A</code> <i>align</i> <code>&#8211;align=</code><i>TIME</i>] [<code>-a</code> <i>archive</i> <code>&#8211;archive=</code><i>FILE</i>] [<code>-G</code> <i>method</i> <code>&#8211;aggregate=</code><i>method</i>] [<code>-h</code> <i>host</i> <code>&#8211;host=</code><i>HOST</i>] [<code>-O</code> <i>offset</i> <code>&#8211;origin=</code><i>TIME</i>] [<code>-S</code> <i>starttime</i> <code>&#8211;start=</code><i>TIME</i>] [<code>-s</code> <i>samples</i> <code>&#8211;samples=</code><i>N</i>] [<code>-T</code> <i>endtime</i> <code>&#8211;finish=</code><i>TIME</i>] [<code>-t</code> <i>interval</i> <code>&#8211;interval=</code><i>DELTA</i>] [<code>-P</code> <i>precision</i> <code>&#8211;precision=</code><i>N</i>] [<code>-R</code> <i>pattern</i> <code>&#8211;regex=</code><i>pattern</i>] [<code>-u</code> <code>&#8211;no-interpolate</code>] [<code>-Z</code> <i>timezone</i> <code>&#8211;timezone=</code><i>TZ</i>] [<code>-z</code> <code>&#8211;hostzone</code>] [<code>-?</code> <code>&#8211;help</code>] [<code>-x</code> [dm][,t][,h][,noidle]]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-iostat</code> reports I/O statistics for scsi devices (by default) or device-mapper devices (if the <code>-x dm</code> option is specified). By default <code>pcp-iostat</code> reports live data for the local host but can also report for a remote host (<code>-h</code>) or from a previously captured PCP archive (<code>-a</code>). </p>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code> and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &#8220;natural&#8221; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of these options. </p>
<p> The other options which control the source, timing and layout of the information reported by <code>pcp-iostat</code> are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> Performance metric values are retrieved from the Performance Co-Pilot (PCP) archive log files identified by the argument <i>archive</i>, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. See also <code>-u</code>.</p>
<dt><code>-G</code></p>
<dd> Specifies that statistics for device names matching the regular expression specified with the <code>-R</code> <i>regex</i> option should be aggregated according to <i>method</i>. Note this is aggregation based on matching device names (not temporal aggregation). When <code>-G</code> is used, the device name column is reported as <i>method</i>(<i>regex</i>), e.g. if <code>-G sum</code> <code>-R &#8216;sd(a|b)$&#8217;</code> is specified, the device column will be <code>sum</code>(<code>sd(a|b)$)</code> and summed statistics for <code>sda</code> and <code>sdb</code> will be reported in the remaining columns. If <code>-G</code> is specified but <code>-R</code> is not specified, then the default <i>regex</i> is <code>.*</code>, i.e. matching all device names. If <i>method</i> is <code>sum</code> then the statistics are summed. This includes the <code>%util</code> column, which may therefore exceed 100% if more than one device name matches. If <i>method</i> is <code>avg</code> then the statistics are summed and then averaged by dividing by the number of matching device names. If <i>method</i> is <code>min</code> or <code>max</code>, the minimum or maximum statistics for matching devices are reported, respectfully.</p>
<dt><code>-h</code></p>
<dd> Current performance metric values are retrieved from the nominated <i>host</i> machine.</p>
<dt><code>-s</code></p>
<dd> The argument <i>samples</i> defines the number of samples to be retrieved and reported. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pcp-iostat</code> will sample and report continuously (in real time mode) or until the end of the set of PCP archives (in archive mode).</p>
<dt><code>-t</code></p>
<dd> The default update <i>interval</i> may be set to something other than the default 1 second. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). The <code>-t</code> option is particularly useful when replaying large sets of archives (<code>-a</code> option) that span several hours or even days. In this case specifying a large <i>interval</i> (e.g. 1h for 1 hour) will reduce the volume of data reported and the i/o statistics will be averaged (interpolated) over the reporting interval (unless the <code>-u</code> option is specified, see below).</p>
<dt><code>-R</code></p>
<dd> This restricts the report to device names matching <i>regex</i>. The <i>regex</i> pattern is searched as a perl style regular expression, and will match any portion of a device name. e.g. &#8216;^sd[a-zA-Z]+&#8217; will match all device names starting with &#8216;sd&#8217; followed by one or more alphabetic characters. e.g. &#8216;^sd(a|b)$&#8217; will only match &#8216;sda&#8217; and &#8216;sdb&#8217;. e.g. &#8216;sda$&#8217; will match &#8216;sda&#8217; but not &#8216;sdab&#8217;. See also the <code>-G</code> option for aggregation options.</p>
<dt><code>-P</code></p>
<dd> This indicates the number of decimals to print. The default precision <i>N</i> may be set to something other than the default 2 decimals. Note that the <code>avgrq-sz</code> and <code>avgqu-sz</code> fields are always reported with <i>N</i>+1 decimals of precision. These fields typically have values less than 1.0.</p>
<dt><code>-u</code></p>
<dd> When replaying a set of archives, by default values are reported according to the selected sample interval (<code>-t</code> option), not according to the actual record intervals in the set of archives. To this effect PCP interpolates the values to be reported based on the records in the set of archives, and is particularly useful when the <code>-t</code> option is used to replay a set of archives with a longer sampling interval than the underlying interval the set of archives was originally recorded with. With the <code>-u</code> option, uninterpolated reporting is enabled &#8211; every value is reported according to the native recording interval in the set of archives. When the <code>-u</code> option is specified, the <code>-t</code> option makes no sense and is incompatible because the replay interval is always the same as the recording interval in the set of archive. In addition, <code>-u</code> only makes sense when replaying a set of archives, see <code>-a</code> above, and so if <code>-u</code> is specified then <code>-a</code> must also be specified.</p>
<dt><code>-Z</code></p>
<dd> By default, <code>pcp-iostat</code> reports the time of day according to the local timezone on the system where <code>pcp-iostat</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-z</code></p>
<dd> Change the reporting timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <code>-h</code> or <code>-a</code> options. When replaying a PCP archive that was captured in a foreign timezone, the <code>-z</code> option would almost always be used (the default reporting timezone is the local timezone, which may not be the same as the timezone of the PCP archive).</p>
<dt><code>-x</code></p>
<dd> Specifies a comma separated list of one or more extended reporting options as follows:<br />
 <code>dm</code> &#8211; report statistics for device-mapper logical devices instead of scsi devices,<br />
 <code>t</code> &#8211; prefix every line in the report with a timestamp in <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) format,<br />
 <code>h</code> &#8211; omit the heading, which is otherwise reported every 24 samples,<br />
 <code>noidle</code> &#8211; Do not display statistics for idle devices.</dl>
<h2>REPORT</h2>
<p> The columns in the <code>pcp-iostat</code> report have the following interpretation :</p>
<dl>
<dt><code>Timestamp</code></p>
<dd> When the <code>-x t</code> option is specified, this column is the timestamp in <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) format.</p>
<dt><code>Device</code></p>
<dd> Specifies the scsi device name, or if <code>-x dm</code> is specified, the device-mapper logical device name. When <code>-G</code> is specified, this is replaced by the aggregation method and regular expression &#8211; see the <code>-G</code> and <code>-R</code> options above.</p>
<dt><code>rrqm/s</code></p>
<dd> The number of read requests expressed as a rate per-second that were merged during the reporting interval by the I/O scheduler.</p>
<dt><code>wrqm/s</code></p>
<dd> The number of write requests expressed as a rate per-second that were merged during the reporting interval by the I/O scheduler.</p>
<dt><code>r/s</code></p>
<dd> The number of read requests completed by the device (after merges), expressed as a rate per second during the reporting interval.</p>
<dt><code>w/s</code></p>
<dd> The number of write requests completed by the device (after merges), expressed as a rate per second during the reporting interval.</p>
<dt><code>rkB/s</code></p>
<dd> The average volume of data read from the device expressed as KBytes/second during the reporting interval.</p>
<dt><code>wkB/s</code></p>
<dd> The average volume of data written to the device expressed as KBytes/second during the reporting interval.</p>
<dt><code>avgrq-sz</code></p>
<dd> The average I/O request size for both reads and writes to the device expressed as Kbytes during the reporting interval.</p>
<dt><code>avgqu-sz</code></p>
<dd> The average queue length of read and write requests to the device during the reporting interval.</p>
<dt><code>await</code></p>
<dd> The average time in milliseconds that read and write requests were queued (and serviced) to the device during the reporting interval.</p>
<dt><code>r_await</code></p>
<dd> The average time in milliseconds that read requests were queued (and serviced) to the device during the reporting interval.</p>
<dt><code>w_await</code></p>
<dd> The average time in milliseconds that write requests were queued (and serviced) to the device during the reporting interval.</p>
<dt><code>%util</code></p>
<dd> The percentage of time during the reporting interval that the device was busy processing requests. A value of 100% indicates device saturation.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-iostat2pcp/">iostat2pcp</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error and are intended to be self-explanatory. </p>
<h2>Index</h2>
