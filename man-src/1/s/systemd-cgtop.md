---
title: "systemd-cgtop(1)"
name: "systemd-cgtop"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-cgtop/"
description: "systemd-cgtop – Show top control groups by their resource usage"
---

<h2 class="name">NAME</h2>
<p> systemd-cgtop &#8211; Show top control groups by their resource usage </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-cgtop</code> [OPTIONS&#8230;] [GROUP]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-cgtop</code></p>
<dd>shows the top control groups of the local Linux control group hierarchy, ordered by their CPU, memory, or disk I/O load. The display is refreshed in regular intervals (by default every 1s), similar in style to <code><a href="/docs/linux/man/1-top/">top</a></code>(1). If a control group path is specified, shows only the services of the specified control group. </p>
<p> If <code>systemd-cgtop</code> is not connected to a tty, no column headers are printed and the default is to only run one iteration. The <code>&#8211;iterations=</code> argument, if given, is honored. This mode is suitable for scripting. </p>
<p> Resource usage is only accounted for control groups in the relevant hierarchy, i.e. CPU usage is only accounted for control groups in the &quot;cpuacct&quot; hierarchy, memory usage only for those in &quot;memory&quot; and disk I/O usage for those in &quot;blkio&quot;. If resource monitoring for these resources is required, it is recommended to add the <i>CPUAccounting=1</i>, <i>MemoryAccounting=1</i> and <i>BlockIOAccounting=1</i> settings in the unit files in question. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for details. </p>
<p> The CPU load value can be between 0 and 100 times the number of processors the system has. For example, if the system has 8 processors, the CPU load value is going to be between 0% and 800%. The number of processors can be found in &quot;/proc/cpuinfo&quot;. </p>
<p> To emphasize this: unless &quot;CPUAccounting=1&quot;, &quot;MemoryAccounting=1&quot; and &quot;BlockIOAccounting=1&quot; are enabled for the services in question, no resource accounting will be available for system services and the data shown by <code>systemd-cgtop</code> will be incomplete.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-p</code>, <code>&#8211;order=path</code></p>
<dl>
<dt>
<dd> Order by control group path name.</dl>
<p> <code>-t</code>, <code>&#8211;order=tasks</code></p>
<dl>
<dt>
<dd> Order by number of tasks/processes in the control group.</dl>
<p> <code>-c</code>, <code>&#8211;order=cpu</code></p>
<dl>
<dt>
<dd> Order by CPU load.</dl>
<p> <code>-m</code>, <code>&#8211;order=memory</code></p>
<dl>
<dt>
<dd> Order by memory usage.</dl>
<p> <code>-i</code>, <code>&#8211;order=io</code></p>
<dl>
<dt>
<dd> Order by disk I/O load.</dl>
<p> <code>-b</code>, <code>&#8211;batch</code></p>
<dl>
<dt>
<dd> Run in &quot;batch&quot; mode: do not accept input and run until the iteration limit set with <code>&#8211;iterations=</code> is exhausted or until killed. This mode could be useful for sending output from <code>systemd-cgtop</code> to other programs or to a file.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Format byte counts (as in memory usage and I/O metrics) and CPU time with raw numeric values rather than human-readable numbers.</dl>
<p> <code>&#8211;cpu=percentage</code>, <code>&#8211;cpu=time</code></p>
<dl>
<dt>
<dd> Controls whether the CPU usage is shown as percentage or time. By default, the CPU usage is shown as percentage. This setting may also be toggled at runtime by pressing the % key.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> Count only userspace processes instead of all tasks. By default, all tasks are counted: each kernel thread and each userspace thread individually. With this setting, kernel threads are excluded from the counting and each userspace process only counts as one, regardless how many threads it consists of. This setting may also be toggled at runtime by pressing the P key. This option may not be combined with <code>-k</code>.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Count only userspace processes and kernel threads instead of all tasks. By default, all tasks are counted: each kernel thread and each userspace thread individually. With this setting, kernel threads are included in the counting and each userspace process only counts as on one, regardless how many threads it consists of. This setting may also be toggled at runtime by pressing the k key. This option may not be combined with <code>-P</code>.</dl>
<p> <code>&#8211;recursive=</code></p>
<dl>
<dt>
<dd> Controls whether the number of processes shown for a control group shall include all processes that are contained in any of the child control groups as well. Takes a boolean argument, which defaults to &quot;yes&quot;. If enabled, the processes in child control groups are included, if disabled, only the processes in the control group itself are counted. This setting may also be toggled at runtime by pressing the r key. Note that this setting only applies to process counting, i.e. when the <code>-P</code> or <code>-k</code> options are used. It has not effect if all tasks are counted, in which case the counting is always recursive.</dl>
<p> <code>-n</code>, <code>&#8211;iterations=</code></p>
<dl>
<dt>
<dd> Perform only this many iterations. A value of 0 indicates that the program should run indefinitely.</dl>
<p> <code>-1</code></p>
<dl>
<dt>
<dd> A shortcut for <code>&#8211;iterations=1</code>.</dl>
<p> <code>-d</code>, <code>&#8211;delay=</code></p>
<dl>
<dt>
<dd> Specify refresh delay in seconds (or if one of &quot;ms&quot;, &quot;us&quot;, &quot;min&quot; is specified as unit in this time unit). This setting may also be increased and decreased at runtime by pressing the + and &#8211; keys.</dl>
<p> <code>&#8211;depth=</code></p>
<dl>
<dt>
<dd> Maximum control group tree traversal depth. Specifies how deep <code>systemd-cgtop</code> shall traverse the control group hierarchies. If 0 is specified, only the root group is monitored. For 1, only the first level of control groups is monitored, and so on. Defaults to 3.</dl>
<p> <code>-M </code><i>MACHINE</i>, <code>&#8211;machine=</code><i>MACHINE</i></p>
<dl>
<dt>
<dd> Limit control groups shown to the part corresponding to the container <i>MACHINE</i>. This option may not be used when a control group path is specified.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>KEYS</h2>
<p> <code>systemd-cgtop</code> is an interactive tool and may be controlled via user input using the following keys: </p>
<p> h</p>
<dl>
<dt>
<dd> Shows a short help text.</dl>
<p> Space</p>
<dl>
<dt>
<dd> Immediately refresh output.</dl>
<p> q</p>
<dl>
<dt>
<dd> Terminate the program.</dl>
<p> p, t, c, m, i</p>
<dl>
<dt>
<dd> Sort the control groups by path, number of tasks, CPU load, memory usage, or I/O load, respectively. This setting may also be controlled using the <code>&#8211;order=</code> command line switch.</dl>
<p> %</p>
<dl>
<dt>
<dd> Toggle between showing CPU time as time or percentage. This setting may also be controlled using the <code>&#8211;cpu=</code> command line switch.</dl>
<p> +, &#8211;</p>
<dl>
<dt>
<dd> Increase or decrease refresh delay, respectively. This setting may also be controlled using the <code>&#8211;delay=</code> command line switch.</dl>
<p> P</p>
<dl>
<dt>
<dd> Toggle between counting all tasks, or only userspace processes. This setting may also be controlled using the <code>-P</code> command line switch (see above).</dl>
<p> k</p>
<dl>
<dt>
<dd> Toggle between counting all tasks, or only userspace processes and kernel threads. This setting may also be controlled using the <code>-k</code> command line switch (see above).</dl>
<p> r</p>
<dl>
<dt>
<dd> Toggle between recursively including or excluding processes in child control groups in control group process counts. This setting may also be controlled using the <code>&#8211;recursive=</code> command line switch. This key is not available if all tasks are counted, it is only available if processes are counted, as enabled with the P or k keys.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-systemd-cgls/">systemd-cgls</a></code>(1), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/1-top/">top</a></code>(1) </p>
<h2>Index</h2>
