---
title: "cpupower-monitor(1)"
name: "cpupower-monitor"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower-monitor/"
description: "cpupower-monitor – Report processor frequency and idle statistics"
---

<h2>NAME</h2>
<p> cpupower-monitor &#8211; Report processor frequency and idle statistics</p>
<h2>SYNOPSIS</h2>
<p> <code> cpupower monitor</code> -l </p>
<p> <code>cpupower monitor</code> [<code>-c</code>]<code>[</code>-m &lt;mon1&gt;,<code>[</code>&lt;mon2&gt;,&#8230;<code>]</code>] [<code>-i seconds</code>]<br />
 <code>cpupower monitor</code> [<code>-c</code>][<code>-m &lt;mon1&gt;,</code>[<code>&lt;mon2&gt;,&#8230;</code>]<code>]</code> command </p>
<h2>DESCRIPTION</h2>
<p> <code>cpupower-monitor </code> reports processor topology, frequency and idle power state statistics. Either <code>command</code> is forked and statistics are printed upon its completion, or statistics are printed periodically. </p>
<p> <code>cpupower-monitor </code> implements independent processor sleep state and frequency counters. Some are retrieved from kernel statistics, some are directly reading out hardware registers. Use -l to get an overview which are supported on your system. </p>
<h2>Options</h2>
<p> -l</p>
<dl>
<dt>
<dd> List available monitors on your system. Additional details about each monitor are shown:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The name in quotation marks which can be passed to the -m parameter.</p>
<dt>&bull;</p>
<dd> The number of different counters the monitor supports in brackets.</p>
<dt>&bull;</p>
<dd> The amount of time in seconds the counters might overflow, due to implementation constraints.</p>
<dt>&bull;</p>
<dd> The name and a description of each counter and its processor hierarchy level coverage in square brackets:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> [T] -&gt; Thread</p>
<dt>&bull;</p>
<dd> [C] -&gt; Core</p>
<dt>&bull;</p>
<dd> [P] -&gt; Processor Package (Socket)</p>
<dt>&bull;</p>
<dd> [M] -&gt; Machine/Platform wide counter</dl>
</dl>
</dl>
</dl>
</dl>
<p> -m &lt;mon1&gt;,&lt;mon2&gt;,&#8230;</p>
<dl>
<dt>
<dd> Only display specific monitors. Use the monitor string(s) provided by -l option.</dl>
<p> -i seconds</p>
<dl>
<dt>
<dd> Measure intervall.</dl>
<p> -c</p>
<dl>
<dt>
<dd> Schedule the process on every core before starting and ending measuring. This could be needed for the Idle_Stats monitor when no other MSR based monitor (has to be run on the core that is measured) is run in parallel. This is to wake up the processors from deeper sleep states and let the kernel re -account its cpuidle (C-state) information before reading the cpuidle timings from sysfs.</dl>
<p> command</p>
<dl>
<dt>
<dd> Measure idle and frequency characteristics of an arbitrary command/workload. The executable <code>command</code> is forked and upon its exit, statistics gathered since it was forked are displayed.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Increase verbosity if the binary was compiled with the DEBUG option set.</dl>
<h2>MONITOR DESCRIPTIONS</h2>
<h3>Idle_Stats</h3>
<p> Shows statistics of the cpuidle kernel subsystem. Values are retrieved from /sys/devices/system/cpu/cpu*/cpuidle/state*/. The kernel updates these values every time an idle state is entered or left. Therefore there can be some inaccuracy when cores are in an idle state for some time when the measure starts or ends. In worst case it can happen that one core stayed in an idle state for the whole measure time and the idle state usage time as exported by the kernel did not get updated. In this case a state residency of 0 percent is shown while it was 100. </p>
<h3>Mperf</h3>
<p> The name comes from the aperf/mperf (average and maximum) MSR registers used which are available on recent X86 processors. It shows the average frequency (including boost frequencies). The fact that on all recent hardware the mperf timer stops ticking in any idle state it is also used to show C0 (processor is active) and Cx (processor is in any sleep state) times. These counters do not have the inaccuracy restrictions the &quot;Idle_Stats&quot; counters may show. May work poorly on Linux-2.6.20 through 2.6.29, as the <code>acpi-cpufreq </code> kernel frequency driver periodically cleared aperf/mperf registers in those kernels. </p>
<h3>Nehalem SandyBridge HaswellExtended</h3>
<p> Intel Core and Package sleep state counters. Threads (hyperthreaded cores) may not be able to enter deeper core states if its sibling is utilized. Deepest package sleep states may in reality show up as machine/platform wide sleep states and can only be entered if all cores are idle. Look up Intel manuals (some are provided in the References section) for further details. The monitors are named after the CPU family where the sleep state capabilities got introduced and may not match exactly the CPU name of the platform. For example an IvyBridge processor has sleep state capabilities which got introduced in Nehalem and SandyBridge processor families. Thus on an IvyBridge processor one will get Nehalem and SandyBridge sleep state monitors. HaswellExtended extra package sleep state capabilities are available only in a specific Haswell (family 0x45) and probably also other future processors. </p>
<h3>Fam_12h Fam_14h</h3>
<p> AMD laptop and desktop processor (family 12h and 14h) sleep state counters. The registers are accessed via PCI and therefore can still be read out while cores have been offlined. </p>
<p> There is one special counter: NBP1 (North Bridge P1). This one always returns 0 or 1, depending on whether the North Bridge P1 power state got entered at least once during measure time. Being able to enter NBP1 state also depends on graphics power management. Therefore this counter can be used to verify whether the graphics&#8217; driver power management is working as expected. </p>
<h2>EXAMPLES</h2>
<p> cpupower monitor -l&quot; may show:</p>
<dl>
<dt>
<dd> Monitor &quot;Mperf&quot; (3 states) &#8211; Might overflow after 922000000 s </p>
<p>&#8230; </p>
<p> Monitor &quot;Idle_Stats&quot; (3 states) &#8211; Might overflow after 4294967295 s </p>
<p>&#8230; </p>
</dl>
<p> cpupower monitor -m &quot;Idle_Stats,Mperf&quot; scp /tmp/test /nfs/tmp </p>
<p> Monitor the scp command, show both Mperf and Idle_Stats states counter statistics, but in exchanged order. </p>
<p> Be careful that the typical command to fully utilize one CPU by doing: </p>
<p> cpupower monitor cat /dev/zero &gt;/dev/null </p>
<p> Does not work as expected, because the measured output is redirected to /dev/null. This could get workarounded by putting the line into an own, tiny shell script. Hit CTRL-c to terminate the command and get the measure output displayed. </p>
<h2>REFERENCES</h2>
<p> &quot;BIOS and Kernel Developer’s Guide (BKDG) for AMD Family 14h Processors&quot; <a rel="nofollow" href="http://support.amd.com/us/Processor_TechDocs/43170.pdf">http://support.amd.com/us/Processor_TechDocs/43170.pdf</a> </p>
<p> &quot;Intel® Turbo Boost Technology in Intel® Core&#x2122; Microarchitecture (Nehalem) Based Processors&quot; <a rel="nofollow" href="http://download.intel.com/design/processor/applnots/320354.pdf">http://download.intel.com/design/processor/applnots/320354.pdf</a> </p>
<p> &quot;Intel® 64 and IA-32 Architectures Software Developer&#8217;s Manual Volume 3B: System Programming Guide&quot; <a rel="nofollow" href="http://www.intel.com/products/processor/manuals">http://www.intel.com/products/processor/manuals</a> </p>
<h2>FILES</h2>
<pre>
/dev/cpu/*/msr
/sys/devices/system/cpu/cpu*/cpuidle/state*/.
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-powertop/">powertop</a>(8), <a href="/docs/linux/man/4-msr/">msr</a>(4), <a href="/docs/linux/man/8-vmstat/">vmstat</a>(8) </p>
<h2>AUTHORS</h2>
<pre><code>
Written by Thomas Renninger&lt;trenn[at] suse.de&gt;
    Nehalem, SandyBridge monitors and command passing
                 based on turbostat .8 from Len Brown&lt;len.brown[at] intel.com&gt;
</code></pre>
<h2>Index</h2>
