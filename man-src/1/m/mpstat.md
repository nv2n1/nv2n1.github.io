---
title: "mpstat(1)"
name: "mpstat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpstat/"
description: "mpstat – Report processors related statistics."
---

<h2 class="name">NAME</h2>
<p> mpstat &#8211; Report processors related statistics.</p>
<h2>SYNOPSIS</h2>
<p> <code>mpstat [ -A ] [ &#8211;dec={ 0 | 1 | 2 } ] [ -n ] [ -u ] [ -T ] [ -V ] [ -I {</code> <i>keyword</i><code>[,&#8230;] | ALL } ] [ -N { </code><i>node_list </i><code>| ALL } ] [ -o JSON ] [ -P {</code> <i>cpu_list </i><code>| ALL } ] [ </code><i>interval </i><code>[ </code><i>count </i><code>] ]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>mpstat</code> command writes to standard output activities for each available processor, processor 0 being the first one. Global average activities among all processors are also reported. The <code>mpstat</code> command can be used on both SMP and UP machines, but in the latter, only global average activities will be printed. If no activity has been selected, then the default report is the CPU utilization report. </p>
<p> The <i>interval</i> parameter specifies the amount of time in seconds between each report. A value of 0 (or no parameters at all) indicates that processors statistics are to be reported for the time since system startup (boot). The <i>count </i>parameter can be specified in conjunction with the <i>interval</i> parameter if this one is not set to zero. The value of <i>count</i> determines the number of reports generated at <i>interval </i>seconds apart. If the <i>interval</i> parameter is specified without the <i>count </i>parameter, the <code>mpstat</code> command generates reports continuously. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></dt>
<dd> This option is equivalent to specifying <code>-n -u -I ALL</code>. This option also implies specifying <code>-N ALL -P ALL</code> unless these options are explicitly set on the command line.</dd>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></dt>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</dd>
<dt><code>-I { </code><i>keyword</i><code>[,&#8230;] | ALL }</code></dt>
<dd> Report interrupts statistics. Possible <i>keywords </i>are <code>CPU</code>, <code>SCPU</code>, and <code>SUM</code>.</dd></dl>
<dl>
<dt>
</dt><dd> With the <code>CPU</code> keyword, the number of each individual interrupt received per second by the CPU or CPUs is displayed. Interrupts are those listed in <i>/proc/interrupts </i>file. </dd>
<p> With the <code>SCPU</code> keyword, the number of each individual software interrupt received per second by the CPU or CPUs is displayed. This option works only with kernels 2.6.31 and later. Software interrupts are those listed in <i>/proc/softirqs </i>file. </p>
<p> With the <code>SUM </code>keyword, the <code>mpstat</code> command reports the total number of interrupts per processor. The following values are displayed: </p>
<dl>
<dt>CPU</dt>
<dd> Processor number. The keyword <code>all</code> indicates that statistics are calculated as averages among all processors. </dd>
<dt>intr/s</dt>
<dd> Show the total number of interrupts received per second by the CPU or CPUs.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> The <code>ALL</code> keyword is equivalent to specifying all the keywords above and therefore all the interrupts statistics are displayed.</dd>
<dt><code>-N { </code><i>node_list </i><code>| ALL }</code></dt>
<dd> Indicate the NUMA nodes for which statistics are to be reported. <i>node_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that node <code>all</code> is the global average among all nodes. The <code>ALL</code> keyword indicates that statistics are to be reported for all nodes.</dd>
<dt><code>-n</code></dt>
<dd> Report summary CPU statistics based on NUMA node placement. The following values are displayed:</dd>
<dl>
<dl>
<dt>NODE</dt>
<dd> Logical NUMA node number. The keyword <code>all</code> indicates that statistics are calculated as averages among all nodes.</dd></dl>
</dl>
<dt>
</dt><dd> All the other fields are the same as those displayed with option <code>-u </code>(see below).</dd>
<dt><code>-o JSON</code></dt>
<dd> Display the statistics in JSON (Javascript Object Notation) format. JSON output field order is undefined, and new fields may be added in the future.</dd>
<dt><code>-P { </code><i>cpu_list </i><code>| ALL }</code></dt>
<dd> Indicate the processors for which statistics are to be reported. <i>cpu_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that processor 0 is the first processor, and processor <code>all</code> is the global average among all processors. The <code>ALL</code> keyword indicates that statistics are to be reported for all processors. Offline processors are not displayed.</dd>
<dt><code>-T</code></dt>
<dd> Display topology elements in the CPU report (see option <code>-u</code> below). The following elements are displayed:</dd>
<dl>
<dl>
<dt>CORE</dt>
<dd> Logical core number.</dd>
<dt>SOCK</dt>
<dd> Logical socket number.</dd>
<dt>NODE</dt>
<dd> Logical NUMA node number.</dd></dl>
</dl>
<dt><code>-u</code></dt>
<dd> Report CPU utilization. The following values are displayed:</dd>
<dl>
<dl>
<dt>CPU</dt>
<dd> Processor number. The keyword <i>all</i> indicates that statistics are calculated as averages among all processors.</dd>
<dt>%usr</dt>
<dd> Show the percentage of CPU utilization that occurred while executing at the user level (application).</dd>
<dt>%nice</dt>
<dd> Show the percentage of CPU utilization that occurred while executing at the user level with nice priority.</dd>
<dt>%sys</dt>
<dd> Show the percentage of CPU utilization that occurred while executing at the system level (kernel). Note that this does not include time spent servicing hardware and software interrupts.</dd>
<dt>%iowait</dt>
<dd> Show the percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.</dd>
<dt>%irq</dt>
<dd> Show the percentage of time spent by the CPU or CPUs to service hardware interrupts.</dd>
<dt>%soft</dt>
<dd> Show the percentage of time spent by the CPU or CPUs to service software interrupts.</dd>
<dt>%steal</dt>
<dd> Show the percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.</dd>
<dt>%guest</dt>
<dd> Show the percentage of time spent by the CPU or CPUs to run a virtual processor.</dd>
<dt>%gnice</dt>
<dd> Show the percentage of time spent by the CPU or CPUs to run a niced guest.</dd>
<dt>%idle</dt>
<dd> Show the percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.</dd></dl>
</dl>
<dt><code>-V</code></dt>
<dd> Print version number then exit. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>mpstat</code> command takes into account the following environment variable:</p>
<dl>
<dt><code>S_COLORS</code></dt>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <i>never</i>, <i>always </i>or <i>auto</i> (the latter is equivalent to the default settings).<br />
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</dd>
<dt><code>S_COLORS_SGR</code></dt>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>H=31;1:I=32;22:M=35;1:N=34;1:Z=34;22</code>. Supported capabilities are:</dd>
<dl>
<dl>
<dt><code>H=</code></dt>
<dd> SGR (Select Graphic Rendition) substring for percentage values greater than or equal to 75%.</dd>
<dt><code>I=</code></dt>
<dd> SGR substring for CPU number.</dd>
<dt><code>M=</code></dt>
<dd> SGR substring for percentage values in the range from 50% to 75%.</dd>
<dt><code>N=</code></dt>
<dd> SGR substring for non-zero statistics values.</dd>
<dt><code>Z=</code></dt>
<dd> SGR substring for zero values.</dd></dl>
</dl>
<dt><code>S_TIME_FORMAT</code></dt>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>mpstat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp will also be compliant with ISO 8601 format. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>mpstat 2 5</code></dt>
<dd> Display five reports of global statistics among all processors at two second intervals.</dd>
<dt><code>mpstat -P ALL 2 5</code></dt>
<dd> Display five reports of statistics for all processors at two second intervals. </dd>
</dl>
<h2>BUGS</h2>
<p> <i>/proc </i>filesystem must be mounted for the <code>mpstat </code>command to work. </p>
<h2>FILES</h2>
<p> <i>/proc </i>contains various files with system statistics. </p>
<h2>AUTHOR</h2>
<p> Sebastien Godard (sysstat &lt;at&gt; orange.fr) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/1-pidstat/">pidstat</a></code>(1), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8) </p>
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
