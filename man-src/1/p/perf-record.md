---
title: "perf-record(1)"
name: "perf-record"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-record/"
description: "perf-record – Run a command and record its profile into perf.data"
---

<h2 class="name">NAME</h2>
<p> perf-record &#8211; Run a command and record its profile into perf.data </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf record[-e&lt;EVENT&gt; | --event = EVENT][-l][-a]&lt;command&gt;
        perf record[-e&lt;EVENT&gt; | --event = EVENT][-l][-a]-- - &lt;command&gt;[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command runs a command and gathers a performance counter profile from it, into perf.data &#8211; without displaying anything. </p>
<p> This file can then be inspected later on, using <i>perf report</i>.</p>
<h2>OPTIONS</h2>
<p> &lt;command&gt;&#8230;</p>
<dl>
<dt>
<dd> Any command you can specify in a shell.</dl>
<p> -e, &#8211;event=</p>
<dl>
<dt>
<dd> Select the PMU event. Selection can be: </p>
<dl>
<dt>
<dd> &bull; a symbolic event name (use <i>perf list</i> to list all events)</dl>
<dl>
<dt>
<dd> &bull; a raw PMU event (eventsel+umask) in the form of rNNN where NNN is a hexadecimal event descriptor.</dl>
<dl>
<dt>
<dd> &bull; a hardware breakpoint event in the form of <i>\mem:addr[:access]</i> where addr is the address in memory you want to break in. Access is the memory access type (read, write, execute) it can be passed as follows: <i>\mem:addr[:[r][w][x]]</i>. If you want to profile read-write accesses in 0x1000, just set <i>mem:0x1000:rw</i>.</dl>
</dl>
<p> &#8211;filter=&lt;filter&gt;</p>
<dl>
<dt>
<dd> Event filter.</dl>
<p> -a, &#8211;all-cpus</p>
<dl>
<dt>
<dd> System-wide collection from all CPUs.</dl>
<p> -l</p>
<dl>
<dt>
<dd> Scale counter values.</dl>
<p> -p, &#8211;pid=</p>
<dl>
<dt>
<dd> Record events on existing process ID (comma separated list).</dl>
<p> -t, &#8211;tid=</p>
<dl>
<dt>
<dd> Record events on existing thread ID (comma separated list). This option also disables inheritance by default. Enable it by adding &#8211;inherit.</dl>
<p> -u, &#8211;uid=</p>
<dl>
<dt>
<dd> Record events in threads owned by uid. Name or number.</dl>
<p> -r, &#8211;realtime=</p>
<dl>
<dt>
<dd> Collect data with this RT SCHED_FIFO priority.</dl>
<p> &#8211;no-buffering</p>
<dl>
<dt>
<dd> Collect data without buffering.</dl>
<p> -c, &#8211;count=</p>
<dl>
<dt>
<dd> Event period to sample.</dl>
<p> -o, &#8211;output=</p>
<dl>
<dt>
<dd> Output file name.</dl>
<p> -i, &#8211;no-inherit</p>
<dl>
<dt>
<dd> Child tasks do not inherit counters.</dl>
<p> -F, &#8211;freq=</p>
<dl>
<dt>
<dd> Profile at this frequency.</dl>
<p> -m, &#8211;mmap-pages=</p>
<dl>
<dt>
<dd> Number of mmap data pages (must be a power of two) or size specification with appended unit character &#8211; B/K/M/G. The size is rounded up to have nearest pages power of two value.</dl>
<p> -g</p>
<dl>
<dt>
<dd> Enables call-graph (stack chain/backtrace) recording.</dl>
<p> &#8211;call-graph</p>
<dl>
<dt>
<dd> Setup and enable call-graph (stack chain/backtrace) recording, implies -g. </p>
<dl>
<dt>
<dd>
<pre>
Allows specifying &quot;fp&quot; (frame pointer) or &quot;dwarf&quot;
(DWARF's CFI - Call Frame Information) as the method to collect
the information used to show the call graphs.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
In some systems, where binaries are build with gcc
--fomit-frame-pointer, using the &quot;fp&quot; method will produce bogus
call graphs, using &quot;dwarf&quot;, if available (perf tools linked to
the libunwind library) should be used instead.
</pre>
</dl>
</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Don&#8217;t print any message, useful for scripting.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose (show counter open errors, etc).</dl>
<p> -s, &#8211;stat</p>
<dl>
<dt>
<dd> Per thread counts.</dl>
<p> -d, &#8211;data</p>
<dl>
<dt>
<dd> Sample addresses.</dl>
<p> -T, &#8211;timestamp</p>
<dl>
<dt>
<dd> Sample timestamps. Use it with <i>perf report -D</i> to see the timestamps, for instance.</dl>
<p> -n, &#8211;no-samples</p>
<dl>
<dt>
<dd> Don&#8217;t sample.</dl>
<p> -R, &#8211;raw-samples</p>
<dl>
<dt>
<dd> Collect raw sample records from all opened counters (default for tracepoint counters).</dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
<dd> Collect samples only on the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. In per-thread mode with inheritance mode on (default), samples are captured only when the thread executes on the designated CPUs. Default is to monitor all CPUs.</dl>
<p> -N, &#8211;no-buildid-cache</p>
<dl>
<dt>
<dd> Do not update the buildid cache. This saves some overhead in situations where the information in the perf.data file (which includes buildids) is sufficient.</dl>
<p> -G name,&#8230;, &#8211;cgroup name,&#8230;</p>
<dl>
<dt>
<dd> monitor only in the container (cgroup) called &quot;name&quot;. This option is available only in per-cpu mode. The cgroup filesystem must be mounted. All threads belonging to container &quot;name&quot; are monitored when they run on the monitored CPUs. Multiple cgroups can be provided. Each cgroup is applied to the corresponding event, i.e., first cgroup to first event, second cgroup to second event and so on. It is possible to provide an empty cgroup (monitor all the time) using, e.g., -G foo,,bar. Cgroups must have corresponding events, i.e., they always refer to events defined earlier on the command line.</dl>
<p> -b, &#8211;branch-any</p>
<dl>
<dt>
<dd> Enable taken branch stack sampling. Any type of taken branch may be sampled. This is a shortcut for &#8211;branch-filter any. See &#8211;branch-filter for more infos.</dl>
<p> -j, &#8211;branch-filter</p>
<dl>
<dt>
<dd> Enable taken branch stack sampling. Each sample captures a series of consecutive taken branches. The number of branches captured with each sample depends on the underlying hardware, the type of branches of interest, and the executed code. It is possible to select the types of branches captured by enabling filters. The following filters are defined: </p>
<dl>
<dt>
<dd> &bull; any: any type of branches</dl>
<dl>
<dt>
<dd> &bull; any_call: any function call or system call</dl>
<dl>
<dt>
<dd> &bull; any_ret: any function return or system call return</dl>
<dl>
<dt>
<dd> &bull; ind_call: any indirect branch</dl>
<dl>
<dt>
<dd> &bull; u: only when the branch target is at the user level</dl>
<dl>
<dt>
<dd> &bull; k: only when the branch target is in the kernel</dl>
<dl>
<dt>
<dd> &bull; hv: only when the target is at the hypervisor level</dl>
<dl>
<dt>
<dd> &bull; in_tx: only when the target is in a hardware transaction</dl>
<dl>
<dt>
<dd> &bull; no_tx: only when the target is not in a hardware transaction</dl>
<dl>
<dt>
<dd> &bull; abort_tx: only when the target is a hardware transaction abort</dl>
<dl>
<dt>
<dd> &bull; cond: conditional branches</dl>
<p> The option requires at least one branch type among any, any_call, any_ret, ind_call, cond. The privilege levels may be omitted, in which case, the privilege levels of the associated event are applied to the branch filter. Both kernel (k) and hypervisor (hv) privilege levels are subject to permissions. When sampling on multiple events, branch stack sampling is enabled for all the sampling events. The sampled branch type is the same for all events. The various filters must be specified as a comma separated list: &#8211;branch-filter any_ret,u,k Note that this feature may not be available on all processors.</dl>
<p> &#8211;weight</p>
<dl>
<dt>
<dd> Enable weightened sampling. An additional weight is recorded per sample and can be displayed with the weight and local_weight sort keys. This currently works for TSX abort events and some memory events in precise mode on modern Intel CPUs.</dl>
<p> &#8211;transaction</p>
<dl>
<dt>
<dd> Record transaction flags for transaction related events.</dl>
<p> &#8211;per-thread</p>
<dl>
<dt>
<dd> Use per-thread mmaps. By default per-cpu mmaps are created. This option overrides that and uses per-thread mmaps. A side-effect of that is that inheritance is automatically disabled. &#8211;per-thread is ignored with a warning if combined with -a or -C options.</dl>
<p> -D, &#8211;delay=</p>
<dl>
<dt>
<dd> After starting the program, wait msecs before measuring. This is useful to filter out the startup phase of the program, which is often very different.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1) </p>
<h2>Index</h2>
