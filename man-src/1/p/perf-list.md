---
title: "perf-list(1)"
name: "perf-list"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-list/"
description: "perf-list – List all symbolic event types"
---

<h2 class="name">NAME</h2>
<p> perf-list &#8211; List all symbolic event types </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf list</i> [hw|sw|cache|tracepoint|pmu|event_glob]
</pre>
<h2>DESCRIPTION</h2>
<p> This command displays the symbolic event types which can be selected in the various perf commands with the -e option.</p>
<h2>EVENT MODIFIERS</h2>
<p> Events can optionally have a modifier by appending a colon and one or more modifiers. Modifiers allow the user to restrict the events to be counted. The following modifiers exist: </p>
<dl>
<dt>
<dd>
<pre>
u - user-space counting
k - kernel counting
h - hypervisor counting
G - guest counting (in KVM guests)
H - host counting (not in KVM guests)
p - precise level
S - read sample value (PERF_SAMPLE_READ)
D - pin the event to the PMU
</pre>
</dl>
<p> The <i>p</i> modifier can be used for specifying how precise the instruction address should be. The <i>p</i> modifier can be specified multiple times: </p>
<dl>
<dt>
<dd>
<pre>
0 - SAMPLE_IP can have arbitrary skid
1 - SAMPLE_IP must have constant skid
2 - SAMPLE_IP requested to have 0 skid
3 - SAMPLE_IP must have 0 skid
</pre>
</dl>
<p> For Intel systems precise event sampling is implemented with PEBS which supports up to precise-level 2. </p>
<p> On AMD systems it is implemented using IBS (up to precise-level 2). The precise modifier works with event types 0x76 (cpu-cycles, CPU clocks not halted) and 0xC1 (micro-ops retired). Both events map to IBS execution sampling (IBS op) with the IBS Op Counter Control bit (IbsOpCntCtl) set respectively (see AMD64 Architecture Programmer&#8217;s Manual Volume 2: System Programming, 13.3 Instruction-Based Sampling). Examples to use IBS: </p>
<dl>
<dt>
<dd>
<pre>
perf record -a -e cpu-cycles:p ...    # use ibs op counting cycles
perf record -a -e r076:p ...          # same as -e cpu-cycles:p
perf record -a -e r0C1:p ...          # use ibs op counting micro-ops
</pre>
</dl>
<h2>RAW HARDWARE EVENT DESCRIPTOR</h2>
<p> Even when an event is not available in a symbolic form within perf right now, it can be encoded in a per processor specific way. </p>
<p> For instance For x86 CPUs NNN represents the raw register encoding with the layout of IA32_PERFEVTSELx MSRs (see [Intel&#174; 64 and IA-32 Architectures Software Developer&#8217;s Manual Volume 3B: System Programming Guide] Figure 30-1 Layout of IA32_PERFEVTSELx MSRs) or AMD&#8217;s PerfEvtSeln (see [AMD64 Architecture Programmer&#8217;s Manual Volume 2: System Programming], Page 344, Figure 13-7 Performance Event-Select Register (PerfEvtSeln)). </p>
<p> Note: Only the following bit fields can be set in x86 counter registers: event, umask, edge, inv, cmask. Esp. guest/host only and OS/user mode flags must be setup using EVENT MODIFIERS. </p>
<p> Example: </p>
<p> If the Intel docs for a QM720 Core i7 describe an event as: </p>
<dl>
<dt>
<dd>
<pre>
Event  Umask  Event Mask
Num.   Value  Mnemonic    Description                        Comment
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
A8H      01H  LSD.UOPS    Counts the number of micro-ops     Use cmask=1 and
                          delivered by loop stream detector  invert to count
                                                             cycles
</pre>
</dl>
<p> raw encoding of 0x1A8 can be used: </p>
<dl>
<dt>
<dd>
<pre>
perf stat -e r1a8 -a sleep 1
perf record -e r1a8 ...
</pre>
</dl>
<p> You should refer to the processor specific documentation for getting these details. Some of them are referenced in the SEE ALSO section below.</p>
<h2>OPTIONS</h2>
<p> Without options all known events will be listed. </p>
<p> To limit the list use: </p>
<dl>
<dt>
<dd> 1. <i>hw</i> or <i>hardware</i> to list hardware events such as cache-misses, etc.</dl>
<dl>
<dt>
<dd> 2. <i>sw</i> or <i>software</i> to list software events such as context switches, etc.</dl>
<dl>
<dt>
<dd> 3. <i>cache</i> or <i>hwcache</i> to list hardware cache events such as L1-dcache-loads, etc.</dl>
<dl>
<dt>
<dd> 4. <i>tracepoint</i> to list all tracepoint events, alternatively use <i>subsys_glob:event_glob</i> to filter by tracepoint subsystems such as sched, block, etc.</dl>
<dl>
<dt>
<dd> 5. <i>pmu</i> to print the kernel supplied PMU events.</dl>
<dl>
<dt>
<dd> 6. If none of the above is matched, it will apply the supplied glob to all events, printing the ones that match.</dl>
<p> One or more types can be used at the same time, listing the events for the types specified.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-top/">perf-top</a></code>(1), <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), m[blue]<code>Intel&#174; 64 and IA-32 Architectures Software Developer&#8217;s Manual Volume 3B: System Programming Guide</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>AMD64 Architecture Programmer&#8217;s Manual Volume 2: System Programming</code>m[]<font SIZE="-2">[2]</font></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Intel&#174; 64 and IA-32 Architectures Software Developer&#8217;s Manual Volume 3B: System Programming Guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.intel.com/Assets/PDF/manual/253669.pdf">http://www.intel.com/Assets/PDF/manual/253669.pdf</a></dl>
<dt> 2.</p>
<dd> AMD64 Architecture Programmer&#8217;s Manual Volume 2: System Programming</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://support.amd.com/us/Processor_TechDocs/24593_APM_v2.pdf">http://support.amd.com/us/Processor_TechDocs/24593_APM_v2.pdf</a></dl>
</dl>
<h2>Index</h2>
