---
title: "perfevent-conf(5)"
name: "perfevent-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-perfevent-conf/"
description: "perfevent.conf – the Performance Co-Pilot perfevent PMDA configuration file"
---

<p><code>perfevent.conf</code> &#8211; the Performance Co-Pilot perfevent PMDA configuration file</p>
<h2>Synopsis</h2>
<p><i>$PCP_PMDAS_DIRS/perfevent/perfevent.conf</i></p>
<h2>Description</h2>
<p>The perfevent.conf configuration file defines which hardware performance counters are enabled by the perfevent PMDA. </p>
<p> The configuration file contains a list of events that should be enabled for each PMU. The perfevent PMDA detects which PMUs present and programs the configured events. If multiple PMUs are available, the perfevent PMDA uses the order of the entries in the configuration file to determine which PMU settings to use. The entries at the top of the configuration file have higher precedence. Only one PMU configuration setting is used. The configuration file may also contain perf derived events. A derived event has a list of events which must be listed as base events. The values for the counters in the derived events are aggregated and displayed.</p>
<h2>File Format</h2>
<p>The file consists of one or more groups of PMUs and the events that go with them. </p>
<p> The PMU identification string is enclosed in brackets and one or more events are listed below, one per line. </p>
<dl>
<dd><code>[PMU identification string]</code></dl>
<dl>
<dd><code>EVENT_NAME [CPU OPTION]</code></dl>
<dl>
<dd><code>&#8230;</code></dl>
<p> For derived events, one or more groups of events can be specified where, counters in one group can be specific to one architecture and the counters in other group can be specific to some other architecture. Else, only one group can be specified. EVENT_NAME_1, EVENT_NAME_2 etc. belong to group 1 and EVENT_NAME_3, EVENT_NAME_4 belong to group 2 and so on. If any of the event in the first group is not available, entire group will be discarded. And, the next group will be checked. The first group with all the events available will be activated and monitored. The derived perf event is enclosed in brackets along with :derived as a suffix. Note that the EVENT_NAME listed under derived event must be present as a base event in the configuration file. And, all the events under a particular derived perf event group must have the same CPU_OPTION. || acts as a separator for different groups inside a single derived event. The syntax is : </p>
<dl>
<dd><code>[event:derived]</code></dl>
<dl>
<dd><code>EVENT_NAME_1 [CPU_OPTION] [scale]</code></dl>
<dl>
<dd><code>EVENT_NAME_2 [CPU_OPTION] [scale]</code></dl>
<dl>
<dd><code>&#8230;</code></dl>
<dl>
<dd><code>||</code></dl>
<dl>
<dd><code>EVENT_NAME_3 [CPU_OPTION] [scale]</code></dl>
<dl>
<dd><code>EVENT_NAME_4 [CPU_OPTION] [scale]</code></dl>
<dl>
<dd><code>&#8230;</code></dl>
<dl>
<dd>The available event cpu options are as follows:</p>
<dl>
<dt><code>cpu </code></p>
<dd>to add the counter to all cpus in the system</p>
<dt><code>cpu_rr </code></p>
<dd>to add to one of the cpus in a round-robin allocation strategy</p>
<dt><code>node</code></p>
<dd>to add the counter to the first cpu in each numa node</p>
<dt><code>node_rr</code></p>
<dd>to add the counter to the cpus in each numa node in a round-robin allocation strategy</p>
<dt><code>[N] </code></p>
<dd>where N is the numerical digit of the CPU index</dl>
<p> if the CPU option is absent then the event is programmed on all cpus. </p>
<p> <code>scale</code> is applicable for the counters in derived events. If scale is given, the counters will be scaled to their respective values. The options are as follows :</p>
<dl>
<dt><code>a float value</code></p>
<dd>Can be a simple float value, or a value in scientific notation.</p>
<dt><code>perf_scale</code></p>
<dd>The scale will be taken from the kernel sysfs scale file entry for that event. Its generally specified in <code>/sys/bus/event_source/device/events/&lt;event_name&gt;.scale</code></dl>
<p> If no scale is given, the default scale will be taken as 1.0. </p>
<p> Blank lines are ignored. Lines that begin with the # sign are ignored. </p>
<p> Multiple, comma separated, PMUs may be specified in the PMU definition.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmdaperfevent/">pmdaperfevent</a></code>(1). </p>
