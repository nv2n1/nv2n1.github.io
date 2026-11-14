---
title: "perf-stat(1)"
name: "perf-stat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-stat/"
description: "perf-stat – Run a command and gather performance counter statistics"
---

<h2 class="name">NAME</h2>
<p> perf-stat &#8211; Run a command and gather performance counter statistics </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf stat[-e&lt;EVENT&gt; | --event = EVENT][-a]&lt;command&gt;
        perf stat[-e&lt;EVENT&gt; | --event = EVENT][-a]-- - &lt;command&gt;[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command runs a command and gathers performance counter statistics from it.</p>
<h2>OPTIONS</h2>
<p> &lt;command&gt;&#8230;</p>
<dl>
<dt>
<dd> Any command you can specify in a shell.</dl>
<p> -e, &#8211;event=</p>
<dl>
<dt>
<dd> Select the PMU event. Selection can be a symbolic event name (use <i>perf list</i> to list all events) or a raw PMU event (eventsel+umask) in the form of rNNN where NNN is a hexadecimal event descriptor.</dl>
<p> -i, &#8211;no-inherit</p>
<dl>
<dt>
<dd> child tasks do not inherit counters</dl>
<p> -p, &#8211;pid=&lt;pid&gt;</p>
<dl>
<dt>
<dd> stat events on existing process id (comma separated list)</dl>
<p> -t, &#8211;tid=&lt;tid&gt;</p>
<dl>
<dt>
<dd> stat events on existing thread id (comma separated list)</dl>
<p> -a, &#8211;all-cpus</p>
<dl>
<dt>
<dd> system-wide collection from all CPUs</dl>
<p> -c, &#8211;scale</p>
<dl>
<dt>
<dd> scale/normalize counter values</dl>
<p> -d, &#8211;detailed</p>
<dl>
<dt>
<dd> print more detailed statistics, can be specified up to 3 times </p>
<dl>
<dt>
<dd>
<pre>
      -d:          detailed events, L1 and LLC data cache
   -d -d:     more detailed events, dTLB and iTLB events
-d -d -d:     very detailed events, adding prefetch events
</pre>
</dl>
</dl>
<p> -r, &#8211;repeat=&lt;n&gt;</p>
<dl>
<dt>
<dd> repeat command and print average + stddev (max: 100). 0 means forever.</dl>
<p> -B, &#8211;big-num</p>
<dl>
<dt>
<dd> print large numbers with thousands&#8217; separators according to locale</dl>
<p> -C, &#8211;cpu=</p>
<dl>
<dt>
<dd> Count only on the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. In per-thread mode, this option is ignored. The -a option is still necessary to activate system-wide monitoring. Default is to count on all CPUs.</dl>
<p> -A, &#8211;no-aggr</p>
<dl>
<dt>
<dd> Do not aggregate counts across all monitored CPUs in system-wide mode (-a). This option is only valid in system-wide mode.</dl>
<p> -n, &#8211;null</p>
<dl>
<dt>
<dd> null run &#8211; don&#8217;t start any counters</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> be more verbose (show counter open errors, etc)</dl>
<p> -x SEP, &#8211;field-separator SEP</p>
<dl>
<dt>
<dd> print counts using a CSV-style output to make it easy to import directly into spreadsheets. Columns are separated by the string specified in SEP.</dl>
<p> -G name, &#8211;cgroup name</p>
<dl>
<dt>
<dd> monitor only in the container (cgroup) called &quot;name&quot;. This option is available only in per-cpu mode. The cgroup filesystem must be mounted. All threads belonging to container &quot;name&quot; are monitored when they run on the monitored CPUs. Multiple cgroups can be provided. Each cgroup is applied to the corresponding event, i.e., first cgroup to first event, second cgroup to second event and so on. It is possible to provide an empty cgroup (monitor all the time) using, e.g., -G foo,,bar. Cgroups must have corresponding events, i.e., they always refer to events defined earlier on the command line.</dl>
<p> -o file, &#8211;output file</p>
<dl>
<dt>
<dd> Print the output into the designated file.</dl>
<p> &#8211;append</p>
<dl>
<dt>
<dd> Append to the output file designated with the -o option. Ignored if -o is not specified.</dl>
<p> &#8211;log-fd</p>
<dl>
<dt>
<dd> Log output to fd, instead of stderr. Complementary to &#8211;output, and mutually exclusive with it. &#8211;append may be used here. Examples: 3&gt;results perf stat &#8211;log-fd 3 &#8212; $cmd 3&gt;&gt;results perf stat &#8211;log-fd 3 &#8211;append &#8212; $cmd</dl>
<p> &#8211;pre, &#8211;post</p>
<dl>
<dt>
<dd> Pre and post measurement hooks, e.g.:</dl>
<p> perf stat &#8211;repeat 10 &#8211;null &#8211;sync &#8211;pre <i>make -s O=defconfig-build/clean</i> &#8212; make -s -j64 O=defconfig-build/ bzImage </p>
<p> -I msecs, &#8211;interval-print msecs</p>
<dl>
<dt>
<dd> Print count deltas every N milliseconds (minimum: 100ms) example: perf stat -I 1000 -e cycles -a sleep 5</dl>
<p> &#8211;per-socket</p>
<dl>
<dt>
<dd> Aggregate counts per processor socket for system-wide mode measurements. This is a useful mode to detect imbalance between sockets. To enable this mode, use &#8211;per-socket in addition to -a. (system-wide). The output includes the socket number and the number of online processors on that socket. This is useful to gauge the amount of aggregation.</dl>
<p> &#8211;per-core</p>
<dl>
<dt>
<dd> Aggregate counts per physical processor for system-wide mode measurements. This is a useful mode to detect imbalance between physical cores. To enable this mode, use &#8211;per-core in addition to -a. (system-wide). The output includes the core number and the number of online logical processors on that physical processor.</dl>
<p> -D msecs, &#8211;delay msecs</p>
<dl>
<dt>
<dd> After starting the program, wait msecs before measuring. This is useful to filter out the startup phase of the program, which is often very different.</dl>
<p> -T, &#8211;transaction</p>
<dl>
<dt>
<dd> Print statistics of transactional execution if supported.</dl>
<h2>EXAMPLES</h2>
<p> $ perf stat &#8212; make -j </p>
<dl>
<dt>
<dd>
<pre>
Performance counter stats for 'make -j':
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
8117.370256  task clock ticks     #      11.281 CPU utilization factor
        678  context switches     #       0.000 M/sec
        133  CPU migrations       #       0.000 M/sec
     235724  pagefaults           #       0.029 M/sec
24821162526  CPU cycles           #    3057.784 M/sec
18687303457  instructions         #    2302.138 M/sec
  172158895  cache references     #      21.209 M/sec
   27075259  cache misses         #       3.335 M/sec
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Wall-clock time elapsed:   719.554352 msecs
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-top/">perf-top</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1) </p>
<h2>Index</h2>
