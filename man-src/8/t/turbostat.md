---
title: "turbostat(8)"
name: "turbostat"
section: "8"
letter: "t"
url: "/docs/linux/man/8-turbostat/"
description: "turbostat – Report processor frequency and idle statistics"
---

<p>turbostat &#8211; Report processor frequency and idle statistics</p>
<h2>Synopsis</h2>
<p><code> turbostat</code> [<code>Options</code>] command<br />
 <code>turbostat</code> [<code>Options</code>] [<code>&#8211;interval seconds</code>]</p>
<h2>Description</h2>
<p><code>turbostat </code> reports processor topology, frequency, idle power-state statistics, temperature and power on X86 processors. There are two ways to invoke turbostat. The first method is to supply a <code>command</code>, which is forked and statistics are printed upon its completion. The second method is to omit the command, and turbostat displays statistics every 5 seconds. The 5-second interval can be changed using the &#8211;interval option. Some information is not available on older processors.</p>
<h3>Options</h3>
<p>Options can be specified with a single or double &#8216;-&#8216;, and only as much of the option name as necessary to disambiguate it from others is necessary. Note that options are case-sensitive. <code>&#8211;add attributes</code> add column with counter having specified &#8216;attributes&#8217;. The &#8216;location&#8217; attribute is required, all others are optional. </p>
<pre> location: {<code>msrDDD</code> | <code>msr0xXXX</code>}
 msrDDD is a decimal offset, eg. msr16
 msr0xXXX is a hex offset, eg. msr0x10
 scope: {<code>cpu</code> | <code>core</code> | <code>package</code>}
 sample and print the counter for every cpu, core, or package.
 default: cpu
 size: {<code>u32</code> | <code>u64</code> }
 MSRs are read as 64-bits, u32 truncates the displayed value to 32-bits.
 default: u64
 format: {<code>raw</code> | <code>delta</code> | <code>percent</code>}
 'raw' shows the MSR contents in hex.
 'delta' shows the difference in values during the measurement interval.
 'percent' shows the delta as a percentage of the cycles elapsed.
 default: delta</pre>
<p><code>&#8211;hide column</code> do not show the specified columns. May be invoked multiple times, or with a comma-separated list of column names. <code>&#8211;show column</code> show only the specified columns. May be invoked multiple times, or with a comma-separated list of column names. <code>&#8211;Dump</code> displays the raw counter values. <code>&#8211;debug</code> displays additional system configuration information. Invoking this parameter more than once may also enable internal turbostat debug information. <code>&#8211;interval seconds</code> overrides the default 5.0 second measurement interval. <code>&#8211;out output_file</code> turbostat output is written to the specified output_file. The file is truncated if it already exists, and it is created if it does not exist. <code>&#8211;help</code> displays usage for the most common parameters. <code>&#8211;Joules</code> displays energy in Joules, rather than dividing Joules by time to print power in Watts. <code>&#8211;Package</code> limits output to the system summary plus the 1st thread in each Package. <code>&#8211;processor</code> limits output to the system summary plus the 1st thread in each processor of each package. Ie. it skips hyper-threaded siblings. <code>&#8211;Summary</code> limits output to a 1-line System Summary for each interval. <code>&#8211;TCC temperature</code> sets the Thermal Control Circuit temperature for systems which do not export that value. This is used for making sense of the Digital Thermal Sensor outputs, as they return degrees Celsius below the TCC activation temperature. <code>&#8211;version</code> displays the version. The <code>command</code> parameter forks <code>command</code>, and upon its exit, displays the statistics gathered since it was forked. </p>
<h2>Default Field Descriptions</h2>
<pre><code>CPU</code> Linux CPU (logical processor) number. Yes, it is okay that on many systems the CPUs are not listed in numerical order -- for efficiency reasons, turbostat runs in topology order, so HT siblings appear together.
<code>AVG_MHz</code> number of cycles executed divided by time elapsed.
<code>Busy%</code> percent of the interval that the CPU retired instructions, aka. % of time in &quot;C0&quot; state.
<code>Bzy_MHz</code> average clock rate while the CPU was busy (in &quot;c0&quot; state).
<code>TSC_MHz</code> average MHz that the TSC ran during the entire interval.</pre>
<h2>Debug Field Descriptions</h2>
<pre><code>Package</code> processor package number.
<code>Core</code> processor core number.
Note that multiple CPUs per core indicate support for Intel(R) Hyper-Threading Technology (HT).
<code>CPU%c1, CPU%c3, CPU%c6, CPU%c7</code> show the percentage residency in hardware core idle states.
<code>CoreTmp</code> Degrees Celsius reported by the per-core Digital Thermal Sensor.
<code>PkgTtmp</code> Degrees Celsius reported by the per-package Package Thermal Monitor.
<code>Pkg%pc2, Pkg%pc3, Pkg%pc6, Pkg%pc7</code> percentage residency in hardware package idle states.
<code>PkgWatt</code> Watts consumed by the whole package.
<code>CorWatt</code> Watts consumed by the core part of the package.
<code>GFXWatt</code> Watts consumed by the Graphics part of the package -- available only on client processors.
<code>RAMWatt</code> Watts consumed by the DRAM DIMMS -- available only on server processors.
<code>PKG_%</code> percent of the interval that RAPL throttling was active on the Package.
<code>RAM_%</code> percent of the interval that RAPL throttling was active on DRAM.</pre>
<h2>Periodic Example</h2>
<p>Without any parameters, turbostat displays statistics ever 5 seconds. Periodic output goes to stdout, by default, unless &#8211;out is used to specify an output file. The 5-second interval can be changed with th &quot;-i sec&quot; option. Or a command may be specified as in &quot;FORK EXAMPLE&quot; below. </p>
<p> The first row of statistics is a summary for the entire system. For residency % columns, the summary is a weighted average. For Temperature columns, the summary is the column maximum. For Watts columns, the summary is a system total. Subsequent rows show per-CPU statistics. </p>
<pre>[root@ivy]# ./turbostat
 Core CPU Avg_MHz Busy% Bzy_MHz TSC_MHz SMI CPU%c1 CPU%c3 CPU%c6 CPU%c7 CoreTmp PkgTmp Pkg%pc2 Pkg%pc3 Pkg%pc6 Pkg%pc7 PkgWatt CorWatt GFXWatt 
 - - 6 0.36 1596 3492 0 0.59 0.01 99.04 0.00 23 24 23.82 0.01 72.47 0.00 6.40 1.01 0.00
 0 0 9 0.58 1596 3492 0 0.28 0.01 99.13 0.00 23 24 23.82 0.01 72.47 0.00 6.40 1.01 0.00
 0 4 1 0.07 1596 3492 0 0.79
 1 1 10 0.65 1596 3492 0 0.59 0.00 98.76 0.00 23
 1 5 5 0.28 1596 3492 0 0.95
 2 2 10 0.66 1596 3492 0 0.41 0.01 98.92 0.00 23
 2 6 2 0.10 1597 3492 0 0.97
 3 3 3 0.20 1596 3492 0 0.44 0.00 99.37 0.00 23
 3 7 5 0.31 1596 3492 0 0.33</pre>
<h2>Debug Example</h2>
<p>The &quot;&#8211;debug&quot; option prints additional system information before measurements: </p>
<pre>turbostat version 4.1 10-Feb, 2015 - Len Brown &lt;lenb [at] kernel.org&gt;
CPUID(0): GenuineIntel 13 CPUID levels; family:model:stepping 0x6:3c:3 (6:60:3)
<a href="//www.systutorials.com/docs/linux/man/6-CPUID/">CPUID</a>(6): APERF, DTS, PTM, EPB
RAPL: 3121 sec. Joule Counter Range, at 84 Watts
cpu0: MSR_NHM_PLATFORM_INFO: 0x80838f3012300
8 * 100 = 800 MHz max efficiency
35 * 100 = 3500 MHz TSC frequency
cpu0: MSR_IA32_POWER_CTL: 0x0004005d (C1E auto-promotion: DISabled)
cpu0: MSR_NHM_SNB_PKG_CST_CFG_CTL: 0x1e000400 (UNdemote-C3, UNdemote-C1, demote-C3, demote-C1, UNlocked: pkg-cstate-limit=0: pc0)
cpu0: MSR_NHM_TURBO_RATIO_LIMIT: 0x25262727
37 * 100 = 3700 MHz max turbo 4 active cores
38 * 100 = 3800 MHz max turbo 3 active cores
39 * 100 = 3900 MHz max turbo 2 active cores
39 * 100 = 3900 MHz max turbo 1 active cores
cpu0: MSR_IA32_ENERGY_PERF_BIAS: 0x00000006 (balanced)
cpu0: MSR_CORE_PERF_LIMIT_REASONS, 0x31200000 (Active: ) (Logged: Auto-HWP, Amps, MultiCoreTurbo, Transitions, )
cpu0: MSR_GFX_PERF_LIMIT_REASONS, 0x00000000 (Active: ) (Logged: )
cpu0: MSR_RING_PERF_LIMIT_REASONS, 0x0d000000 (Active: ) (Logged: Amps, PkgPwrL1, PkgPwrL2, )
cpu0: MSR_RAPL_POWER_UNIT: 0x000a0e03 (0.125000 Watts, 0.000061 Joules, 0.000977 sec.)
cpu0: MSR_PKG_POWER_INFO: 0x000002a0 (84 W TDP, RAPL 0 - 0 W, 0.000000 sec.)
cpu0: MSR_PKG_POWER_LIMIT: 0x428348001a82a0 (UNlocked)
cpu0: PKG Limit #1: ENabled (84.000000 Watts, 8.000000 sec, clamp DISabled)
cpu0: PKG Limit #2: ENabled (105.000000 Watts, 0.002441* sec, clamp DISabled)
cpu0: MSR_PP0_POLICY: 0
cpu0: MSR_PP0_POWER_LIMIT: 0x00000000 (UNlocked)
cpu0: Cores Limit: DISabled (0.000000 Watts, 0.000977 sec, clamp DISabled)
cpu0: MSR_PP1_POLICY: 0
cpu0: MSR_PP1_POWER_LIMIT: 0x00000000 (UNlocked)
cpu0: GFX Limit: DISabled (0.000000 Watts, 0.000977 sec, clamp DISabled)
cpu0: MSR_IA32_TEMPERATURE_TARGET: 0x00641400 (100 C)
cpu0: MSR_IA32_PACKAGE_THERM_STATUS: 0x88340800 (48 C)
cpu0: MSR_IA32_THERM_STATUS: 0x88340000 (48 C +/- 1)
cpu1: MSR_IA32_THERM_STATUS: 0x88440000 (32 C +/- 1)
cpu2: MSR_IA32_THERM_STATUS: 0x88450000 (31 C +/- 1)
cpu3: MSR_IA32_THERM_STATUS: 0x88490000 (27 C +/- 1)
 Core CPU Avg_MHz Busy% Bzy_MHz TSC_MHz SMI CPU%c1 CPU%c3 CPU%c6 CPU%c7 CoreTmp PkgTmp PkgWatt CorWatt GFXWatt
 - - 493 12.64 3898 3498 0 12.64 0.00 0.00 74.72 47 47 21.62 13.74 0.00
 0 0 4 0.11 3894 3498 0 99.89 0.00 0.00 0.00 47 47 21.62 13.74 0.00
 0 4 3897 99.98 3898 3498 0 0.02
 1 1 7 0.17 3887 3498 0 0.04 0.00 0.00 99.79 32
 1 5 0 0.00 3885 3498 0 0.21
 2 2 29 0.76 3895 3498 0 0.10 0.01 0.01 99.13 32
 2 6 2 0.06 3896 3498 0 0.80
 3 3 1 0.02 3832 3498 0 0.03 0.00 0.00 99.95 28
 3 7 0 0.00 3879 3498 0 0.04
^C</pre>
<p>The <code>max efficiency</code> frequency, a.k.a. Low Frequency Mode, is the frequency available at the minimum package voltage. The <code>TSC frequency</code> is the base frequency of the processor &#8212; this should match the brand string in /proc/cpuinfo. This base frequency should be sustainable on all CPUs indefinitely, given nominal power and cooling. The remaining rows show what maximum turbo frequency is possible depending on the number of idle cores. Note that not all information is available on all processors. </p>
<p> The &#8211;debug option adds additional columns to the measurement ouput, including CPU idle power-state residency processor temperature sensor readinds. See the field definitions above.</p>
<h2>Fork Example</h2>
<p>If turbostat is invoked with a command, it will fork that command and output the statistics gathered after the command exits. In this case, turbostat output goes to stderr, by default. Output can instead be saved to a file using the &#8211;out option. eg. Here a cycle soaker is run on 1 CPU (see %c0) for a few seconds until ^C while the other CPUs are mostly idle: </p>
<pre>root@ivy: turbostat cat /dev/zero &gt; /dev/null
^C
 Core CPU Avg_MHz Busy% Bzy_MHz TSC_MHz SMI CPU%c1 CPU%c3 CPU%c6 CPU%c7 CoreTmp PkgTmp Pkg%pc2 Pkg%pc3 Pkg%pc6 Pkg%pc7 PkgWatt CorWatt GFXWatt 
 - - 496 12.75 3886 3492 0 13.16 0.04 74.04 0.00 36 36 0.00 0.00 0.00 0.00 23.15 17.65 0.00
 0 0 22 0.57 3830 3492 0 0.83 0.02 98.59 0.00 27 36 0.00 0.00 0.00 0.00 23.15 17.65 0.00
 0 4 9 0.24 3829 3492 0 1.15
 1 1 4 0.09 3783 3492 0 99.91 0.00 0.00 0.00 36
 1 5 3880 99.82 3888 3492 0 0.18
 2 2 17 0.44 3813 3492 0 0.77 0.04 98.75 0.00 28
 2 6 12 0.32 3823 3492 0 0.89
 3 3 16 0.43 3844 3492 0 0.63 0.11 98.84 0.00 30
 3 7 4 0.11 3827 3492 0 0.94
30.372243 sec</pre>
<p>Above the cycle soaker drives cpu5 up its 3.8 GHz turbo limit while the other processors are generally in various states of idle. </p>
<p> Note that cpu1 and cpu5 are HT siblings within core1. As cpu5 is very busy, it prevents its sibling, cpu1, from entering a c-state deeper than c1. </p>
<p> Note that the Avg_MHz column reflects the total number of cycles executed divided by the measurement interval. If the Busy% column is 100%, then the processor was running at that speed the entire interval. The Avg_MHz multiplied by the Busy% results in the Bzy_MHz &#8212; which is the average frequency while the processor was executing &#8212; not including any non-busy idle time.</p>
<h2>Notes</h2>
<p><code>turbostat </code> must be run as root. Alternatively, non-root users can be enabled to run turbostat this way: # setcap cap_sys_rawio=ep ./turbostat # chmod +r /dev/cpu/*/msr <code>turbostat </code> reads hardware counters, but doesn&#8217;t write them. So it will not interfere with the OS or other programs, including multiple invocations of itself. <code>turbostat </code> may work poorly on Linux-2.6.20 through 2.6.29, as <code>acpi-cpufreq </code>periodically cleared the APERF and MPERF MSRs in those kernels. AVG_MHz = APERF_delta/measurement_interval. This is the actual number of elapsed cycles divided by the entire sample interval &#8212; including idle time. Note that this calculation is resilient to systems lacking a non-stop TSC. TSC_MHz = TSC_delta/measurement_interval. On a system with an invariant TSC, this value will be constant and will closely match the base frequency value shown in the brand string in /proc/cpuinfo. On a system where the TSC stops in idle, TSC_MHz will drop below the processor&#8217;s base frequency. Busy% = MPERF_delta/TSC_delta Bzy_MHz = TSC_delta/APERF_delta/MPERF_delta/measurement_interval Note that these calculations depend on TSC_delta, so they are not reliable during intervals when TSC_MHz is not running at the base frequency. Turbostat data collection is not atomic. Extremely short measurement intervals (much less than 1 second), or system activity that prevents turbostat from being able to run on all CPUS to quickly collect data, will result in inconsistent results. The APERF, MPERF MSRs are defined to count non-halted cycles. Although it is not guaranteed by the architecture, turbostat assumes that they count at TSC rate, which is true on all processors tested to date. </p>
<h2>References</h2>
<p>Volume 3B: System Programming Guide&quot; <a rel="nofollow" href="http://www.intel.com/products/processor/manuals/">http://www.intel.com/products/processor/manuals/</a></p>
<h2>Files</h2>
<pre>/dev/cpu/*/msr</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/4-msr/">msr</a>(4), <a href="/docs/linux/man/8-vmstat/">vmstat</a>(8) </p>
<h2>Author</h2>
<pre>Written by Len Brown &lt;len.brown [at] intel.com&gt;</pre>
