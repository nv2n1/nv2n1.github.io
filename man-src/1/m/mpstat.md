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
<dt><code>-A</code></p>
<dd> This option is equivalent to specifying <code>-n -u -I ALL</code>. This option also implies specifying <code>-N ALL -P ALL</code> unless these options are explicitly set on the command line.</p>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></p>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</p>
<dt><code>-I { </code><i>keyword</i><code>[,&#8230;] | ALL }</code></p>
<dd> Report interrupts statistics. Possible <i>keywords </i>are <code>CPU</code>, <code>SCPU</code>, and <code>SUM</code>.</dl>
<dl>
<dt>
<dd> With the <code>CPU</code> keyword, the number of each individual interrupt received per second by the CPU or CPUs is displayed. Interrupts are those listed in <i>/proc/interrupts </i>file. </p>
<p> With the <code>SCPU</code> keyword, the number of each individual software interrupt received per second by the CPU or CPUs is displayed. This option works only with kernels 2.6.31 and later. Software interrupts are those listed in <i>/proc/softirqs </i>file. </p>
<p> With the <code>SUM </code>keyword, the <code>mpstat</code> command reports the total number of interrupts per processor. The following values are displayed: </p>
<dl>
<dt>CPU</p>
<dd> Processor number. The keyword <code>all</code> indicates that statistics are calculated as averages among all processors. </p>
<dt>intr/s</p>
<dd> Show the total number of interrupts received per second by the CPU or CPUs.</dl>
</dl>
<dl>
<dt>
<dd> The <code>ALL</code> keyword is equivalent to specifying all the keywords above and therefore all the interrupts statistics are displayed.</p>
<dt><code>-N { </code><i>node_list </i><code>| ALL }</code></p>
<dd> Indicate the NUMA nodes for which statistics are to be reported. <i>node_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that node <code>all</code> is the global average among all nodes. The <code>ALL</code> keyword indicates that statistics are to be reported for all nodes.</p>
<dt><code>-n</code></p>
<dd> Report summary CPU statistics based on NUMA node placement. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>NODE</p>
<dd> Logical NUMA node number. The keyword <code>all</code> indicates that statistics are calculated as averages among all nodes.</dl>
</dl>
<dt>
<dd> All the other fields are the same as those displayed with option <code>-u </code>(see below).</p>
<dt><code>-o JSON</code></p>
<dd> Display the statistics in JSON (Javascript Object Notation) format. JSON output field order is undefined, and new fields may be added in the future.</p>
<dt><code>-P { </code><i>cpu_list </i><code>| ALL }</code></p>
<dd> Indicate the processors for which statistics are to be reported. <i>cpu_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that processor 0 is the first processor, and processor <code>all</code> is the global average among all processors. The <code>ALL</code> keyword indicates that statistics are to be reported for all processors. Offline processors are not displayed.</p>
<dt><code>-T</code></p>
<dd> Display topology elements in the CPU report (see option <code>-u</code> below). The following elements are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CORE</p>
<dd> Logical core number.</p>
<dt>SOCK</p>
<dd> Logical socket number.</p>
<dt>NODE</p>
<dd> Logical NUMA node number.</dl>
</dl>
<dt><code>-u</code></p>
<dd> Report CPU utilization. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CPU</p>
<dd> Processor number. The keyword <i>all</i> indicates that statistics are calculated as averages among all processors.</p>
<dt>%usr</p>
<dd> Show the percentage of CPU utilization that occurred while executing at the user level (application).</p>
<dt>%nice</p>
<dd> Show the percentage of CPU utilization that occurred while executing at the user level with nice priority.</p>
<dt>%sys</p>
<dd> Show the percentage of CPU utilization that occurred while executing at the system level (kernel). Note that this does not include time spent servicing hardware and software interrupts.</p>
<dt>%iowait</p>
<dd> Show the percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.</p>
<dt>%irq</p>
<dd> Show the percentage of time spent by the CPU or CPUs to service hardware interrupts.</p>
<dt>%soft</p>
<dd> Show the percentage of time spent by the CPU or CPUs to service software interrupts.</p>
<dt>%steal</p>
<dd> Show the percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.</p>
<dt>%guest</p>
<dd> Show the percentage of time spent by the CPU or CPUs to run a virtual processor.</p>
<dt>%gnice</p>
<dd> Show the percentage of time spent by the CPU or CPUs to run a niced guest.</p>
<dt>%idle</p>
<dd> Show the percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.</dl>
</dl>
<dt><code>-V</code></p>
<dd> Print version number then exit. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>mpstat</code> command takes into account the following environment variable:</p>
<dl>
<dt><code>S_COLORS</code></p>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <i>never</i>, <i>always </i>or <i>auto</i> (the latter is equivalent to the default settings).<br />
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</p>
<dt><code>S_COLORS_SGR</code></p>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>H=31;1:I=32;22:M=35;1:N=34;1:Z=34;22</code>. Supported capabilities are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>H=</code></p>
<dd> SGR (Select Graphic Rendition) substring for percentage values greater than or equal to 75%.</p>
<dt><code>I=</code></p>
<dd> SGR substring for CPU number.</p>
<dt><code>M=</code></p>
<dd> SGR substring for percentage values in the range from 50% to 75%.</p>
<dt><code>N=</code></p>
<dd> SGR substring for non-zero statistics values.</p>
<dt><code>Z=</code></p>
<dd> SGR substring for zero values.</dl>
</dl>
<dt><code>S_TIME_FORMAT</code></p>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>mpstat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp will also be compliant with ISO 8601 format. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>mpstat 2 5</code></p>
<dd> Display five reports of global statistics among all processors at two second intervals.</p>
<dt><code>mpstat -P ALL 2 5</code></p>
<dd> Display five reports of statistics for all processors at two second intervals. </p>
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
