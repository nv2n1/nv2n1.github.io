---
title: "perf-trace(1)"
name: "perf-trace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-trace/"
description: "perf-trace – strace inspired tool"
---

<h2 class="name">NAME</h2>
<p> perf-trace &#8211; strace inspired tool </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf trace</i>
<i>perf trace record</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This command will show the events associated with the target, initially syscalls, but other system events like pagefaults, task lifetime events, scheduling events, etc. </p>
<p> This is a live mode tool in addition to working with perf.data files like the other perf tools. Files can be generated using the <i>perf record</i> command but the session needs to include the raw_syscalls events (-e <i>raw_syscalls:*</i>). Alternatively, <i>perf trace record</i> can be used as a shortcut to automatically include the raw_syscalls events when writing events to a file. </p>
<p> The following options apply to perf trace; options to perf trace record are found in the perf record man page.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all-cpus</p>
<dl>
<dt>
<dd> System-wide collection from all CPUs.</dl>
<p> -e, &#8211;expr</p>
<dl>
<dt>
<dd> List of events to show, currently only syscall names. Prefixing with ! shows all syscalls but the ones specified. You may need to escape it.</dl>
<p> -o, &#8211;output=</p>
<dl>
<dt>
<dd> Output file name.</dl>
<p> -p, &#8211;pid=</p>
<dl>
<dt>
<dd> Record events on existing process ID (comma separated list).</dl>
<p> -t, &#8211;tid=</p>
<dl>
<dt>
<dd> Record events on existing thread ID (comma separated list).</dl>
<p> -u, &#8211;uid=</p>
<dl>
<dt>
<dd> Record events in threads owned by uid. Name or number.</dl>
<p> -v, &#8211;verbose=</p>
<dl>
<dt>
<dd> Verbosity level.</dl>
<p> -i, &#8211;no-inherit</p>
<dl>
<dt>
<dd> Child tasks do not inherit counters.</dl>
<p> -m, &#8211;mmap-pages=</p>
<dl>
<dt>
<dd> Number of mmap data pages (must be a power of two) or size specification with appended unit character &#8211; B/K/M/G. The size is rounded up to have nearest pages power of two value.</dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
<dd> Collect samples only on the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. In per-thread mode with inheritance mode on (default), Events are captured only when the thread executes on the designated CPUs. Default is to monitor all CPUs.</dl>
<p> &#8211;duration: Show only events that had a duration greater than N.M ms. </p>
<p> &#8211;sched: Accrue thread runtime and provide a summary at the end of the session. </p>
<p> -i &#8211;input Process events from a given perf data file. </p>
<p> -T &#8211;time Print full timestamp rather time relative to first sample. </p>
<p> &#8211;comm</p>
<dl>
<dt>
<dd> Show process COMM right beside its ID, on by default, disable with &#8211;no-comm.</dl>
<p> -s, &#8211;summary</p>
<dl>
<dt>
<dd> Show only a summary of syscalls by thread with min, max, and average times (in msec) and relative stddev.</dl>
<p> -S, &#8211;with-summary</p>
<dl>
<dt>
<dd> Show all syscalls followed by a summary by thread with min, max, and average times (in msec) and relative stddev.</dl>
<p> &#8211;tool_stats</p>
<dl>
<dt>
<dd> Show tool stats such as number of times fd&rarr;pathname was discovered thru hooking the open syscall return + vfs_getname or via reading /proc/pid/fd, etc.</dl>
<p> -F=[all|min|maj], &#8211;pf=[all|min|maj]</p>
<dl>
<dt>
<dd> Trace pagefaults. Optionally, you can specify whether you want minor, major or all pagefaults. Default value is maj.</dl>
<p> &#8211;syscalls</p>
<dl>
<dt>
<dd> Trace system calls. This options is enabled by default.</dl>
<h2>PAGEFAULTS</h2>
<p> When tracing pagefaults, the format of the trace is as follows: </p>
<p> &lt;min|maj&gt;fault [&lt;ip.symbol&gt;+&lt;ip.offset&gt;] &rArr; &lt;m[blue]<code>addr.dso [at] addr.offset</code>m[]<font SIZE="-2">[1]</font>&gt; (&lt;map type&gt;&lt;addr level&gt;). </p>
<dl>
<dt>
<dd> &bull; min/maj indicates whether fault event is minor or major;</dl>
<dl>
<dt>
<dd> &bull; ip.symbol shows symbol for instruction pointer (the code that generated the fault); if no debug symbols available, perf trace will print raw IP;</dl>
<dl>
<dt>
<dd> &bull; addr.dso shows DSO for the faulted address;</dl>
<dl>
<dt>
<dd> &bull; map type is either <i>d</i> for non-executable maps or <i>x</i> for executable maps;</dl>
<dl>
<dt>
<dd> &bull; addr level is either <i>k</i> for kernel dso or <i>.</i> for user dso.</dl>
<p> For symbols resolution you may need to install debugging symbols. </p>
<p> Please be aware that duration is currently always 0 and doesn&#8217;t reflect actual time it took for fault to be handled! </p>
<p> When &#8211;verbose specified, perf trace tries to print all available information for both IP and fault address in the form of m[blue]<code>dso [at] symbol</code>m[]<font SIZE="-2">[2]</font>+offset.</p>
<h2>EXAMPLES</h2>
<p> Trace only major pagefaults: </p>
<dl>
<dt>
<dd>
<pre>
$ perf trace --no-syscalls -F
</pre>
</dl>
<p> Trace syscalls, major and minor pagefaults: </p>
<dl>
<dt>
<dd>
<pre>
$ perf trace -F all
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
1416.547(0.000 ms)
    : python / 20235 majfault[CRYPTO_push_info_ + 0x0] = &gt; / lib / x86_64 - linux - gnu / libcrypto.so .1.0.0 [at] 0x61be0(x.)
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
As you can see, there was major pagefault in python process, from
CRYPTO_push_info_ routine which faulted somewhere in libcrypto.so.
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-script/">perf-script</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> addr.dso [at] addr.offset</p>
<dl>
<dt>
<dd> mailto:addr.dso [at] addr.offset</dl>
<dt> 2.</p>
<dd> dso [at] symbol</p>
<dl>
<dt>
<dd> mailto:dso [at] symbol</dl>
</dl>
<h2>Index</h2>
