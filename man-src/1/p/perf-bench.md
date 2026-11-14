---
title: "perf-bench(1)"
name: "perf-bench"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-bench/"
description: "perf-bench – General framework for benchmark suites"
---

<h2 class="name">NAME</h2>
<p> perf-bench &#8211; General framework for benchmark suites </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf bench[&lt;common options&gt;]&lt;subsystem&gt;&lt;suite&gt;[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This <i>perf bench</i> command is a general framework for benchmark suites.</p>
<h2>COMMON OPTIONS</h2>
<p> -r, &#8211;repeat=</p>
<dl>
<dt>
<dd> Specify amount of times to repeat the run (default 10).</dl>
<p> -f, &#8211;format=</p>
<dl>
<dt>
<dd> Specify format style. Current available format styles are:</dl>
<p> <i>default</i></p>
<dl>
<dt>
<dd> Default style. This is mainly for human reading.</dl>
<dl>
<dt>
<dd>
<pre>
.ft C
% perf bench sched pipe                      # with no style specified
(executing 1000000 pipe operations between two tasks)
        Total time:5.855 sec
                5.855061 usecs/op
                170792 ops/sec
.ft
</pre>
</dl>
<p> <i>simple</i></p>
<dl>
<dt>
<dd> This simple style is friendly for automated processing by scripts.</dl>
<dl>
<dt>
<dd>
<pre>
.ft C
% perf bench --format=simple sched pipe      # specified simple
5.988
.ft
</pre>
</dl>
<h2>SUBSYSTEM</h2>
<p> <i>sched</i></p>
<dl>
<dt>
<dd> Scheduler and IPC mechanisms.</dl>
<p> <i>mem</i></p>
<dl>
<dt>
<dd> Memory access performance.</dl>
<p> <i>numa</i></p>
<dl>
<dt>
<dd> NUMA scheduling and MM benchmarks.</dl>
<p> <i>futex</i></p>
<dl>
<dt>
<dd> Futex stressing benchmarks.</dl>
<p> <i>all</i></p>
<dl>
<dt>
<dd> All benchmark subsystems.</dl>
<h3>SUITES FOR <i>sched</i></h3>
<p> <code>messaging</code></p>
<dl>
<dt>
<dd> Suite for evaluating performance of scheduler and IPC mechanisms. Based on hackbench by Rusty Russell.</dl>
<p> <font SIZE="+1"> <code>Options of messaging</code></p>
<dl>
<dt>
<dd>
<p> -p, &#8211;pipe</p>
<dl>
<dt>
<dd> Use pipe() instead of socketpair()</dl>
<p> -t, &#8211;thread</p>
<dl>
<dt>
<dd> Be multi thread instead of multi process</dl>
<p> -g, &#8211;group=</p>
<dl>
<dt>
<dd> Specify number of groups</dl>
<p> -l, &#8211;loop=</p>
<dl>
<dt>
<dd> Specify number of loops</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Example of messaging</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
.ft C
% perf bench sched messaging                 # run with default
options (20 sender and receiver processes per group)
(10 groups == 400 processes run)
      Total time:0.308 sec
% perf bench sched messaging -t -g 20        # be multi-thread, with 20 groups
(20 sender and receiver threads per group)
(20 groups == 800 threads run)
      Total time:0.582 sec
.ft
</pre>
</dl>
<p> <code>pipe</code></p>
<dl>
<dt>
<dd> Suite for pipe() system call. Based on pipe-test-1m.c by Ingo Molnar.</dl>
</dl>
<p> <font SIZE="+1"> <code>Options of pipe</code></p>
<dl>
<dt>
<dd>
<p> -l, &#8211;loop=</p>
<dl>
<dt>
<dd> Specify number of loops.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Example of pipe</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
.ft C
% perf bench sched pipe
(executing 1000000 pipe operations between two tasks)
        Total time:8.091 sec
                8.091833 usecs/op
                123581 ops/sec
% perf bench sched pipe -l 1000              # loop 1000
(executing 1000 pipe operations between two tasks)
        Total time:0.016 sec
                16.948000 usecs/op
                59004 ops/sec
.ft
</pre>
</dl>
</dl>
<h3>SUITES FOR <i>mem</i></h3>
<p> <code>memcpy</code></p>
<dl>
<dt>
<dd> Suite for evaluating performance of simple memory copy in various ways.</dl>
<p> <font SIZE="+1"> <code>Options of memcpy</code></p>
<dl>
<dt>
<dd>
<p> -l, &#8211;length</p>
<dl>
<dt>
<dd> Specify length of memory to copy (default: 1MB). Available units are B, KB, MB, GB and TB (case insensitive).</dl>
<p> -r, &#8211;routine</p>
<dl>
<dt>
<dd> Specify routine to copy (default: default). Available routines are depend on the architecture. On x86-64, x86-64-unrolled, x86-64-movsq and x86-64-movsb are supported.</dl>
<p> -i, &#8211;iterations</p>
<dl>
<dt>
<dd> Repeat memcpy invocation this number of times.</dl>
<p> -c, &#8211;cycle</p>
<dl>
<dt>
<dd> Use perf&#8217;s cpu-cycles event instead of gettimeofday syscall.</dl>
<p> -o, &#8211;only-prefault</p>
<dl>
<dt>
<dd> Show only the result with page faults before memcpy.</dl>
<p> -n, &#8211;no-prefault</p>
<dl>
<dt>
<dd> Show only the result without page faults before memcpy.</dl>
<p> <code>memset</code></p>
<dl>
<dt>
<dd> Suite for evaluating performance of simple memory set in various ways.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Options of memset</code></p>
<dl>
<dt>
<dd>
<p> -l, &#8211;length</p>
<dl>
<dt>
<dd> Specify length of memory to set (default: 1MB). Available units are B, KB, MB, GB and TB (case insensitive).</dl>
<p> -r, &#8211;routine</p>
<dl>
<dt>
<dd> Specify routine to set (default: default). Available routines are depend on the architecture. On x86-64, x86-64-unrolled, x86-64-stosq and x86-64-stosb are supported.</dl>
<p> -i, &#8211;iterations</p>
<dl>
<dt>
<dd> Repeat memset invocation this number of times.</dl>
<p> -c, &#8211;cycle</p>
<dl>
<dt>
<dd> Use perf&#8217;s cpu-cycles event instead of gettimeofday syscall.</dl>
<p> -o, &#8211;only-prefault</p>
<dl>
<dt>
<dd> Show only the result with page faults before memset.</dl>
<p> -n, &#8211;no-prefault</p>
<dl>
<dt>
<dd> Show only the result without page faults before memset.</dl>
</dl>
<p> </font></p>
<h3>SUITES FOR <i>numa</i></h3>
<p> <code>mem</code></p>
<dl>
<dt>
<dd> Suite for evaluating NUMA workloads.</dl>
<h3>SUITES FOR <i>futex</i></h3>
<p> <code>hash</code></p>
<dl>
<dt>
<dd> Suite for evaluating hash tables.</dl>
<p> <code>wake</code></p>
<dl>
<dt>
<dd> Suite for evaluating wake calls.</dl>
<p> <code>requeue</code></p>
<dl>
<dt>
<dd> Suite for evaluating requeue calls.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf/">perf</a></code>(1) </p>
<h2>Index</h2>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd></dl>
