---
title: "perf-top(1)"
name: "perf-top"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-top/"
description: "perf-top – System profiling tool."
---

<h2 class="name">NAME</h2>
<p> perf-top &#8211; System profiling tool. </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf top[-e&lt;EVENT&gt; | --event = EVENT][&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command generates and displays a performance counter profile in real time.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all-cpus</p>
<dl>
<dt>
<dd> System-wide collection. (default)</dl>
<p> -c &lt;count&gt;, &#8211;count=&lt;count&gt;</p>
<dl>
<dt>
<dd> Event period to sample.</dl>
<p> -C &lt;cpu-list&gt;, &#8211;cpu=&lt;cpu&gt;</p>
<dl>
<dt>
<dd> Monitor only on the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to monitor all CPUS.</dl>
<p> -d &lt;seconds&gt;, &#8211;delay=&lt;seconds&gt;</p>
<dl>
<dt>
<dd> Number of seconds to delay between refreshes.</dl>
<p> -e &lt;event&gt;, &#8211;event=&lt;event&gt;</p>
<dl>
<dt>
<dd> Select the PMU event. Selection can be a symbolic event name (use <i>perf list</i> to list all events) or a raw PMU event (eventsel+umask) in the form of rNNN where NNN is a hexadecimal event descriptor.</dl>
<p> -E &lt;entries&gt;, &#8211;entries=&lt;entries&gt;</p>
<dl>
<dt>
<dd> Display this many functions.</dl>
<p> -f &lt;count&gt;, &#8211;count-filter=&lt;count&gt;</p>
<dl>
<dt>
<dd> Only display functions with more events than this.</dl>
<p> &#8211;group</p>
<dl>
<dt>
<dd> Put the counters into a counter group.</dl>
<p> -F &lt;freq&gt;, &#8211;freq=&lt;freq&gt;</p>
<dl>
<dt>
<dd> Profile at this frequency.</dl>
<p> -i, &#8211;inherit</p>
<dl>
<dt>
<dd> Child tasks do not inherit counters.</dl>
<p> -k &lt;path&gt;, &#8211;vmlinux=&lt;path&gt;</p>
<dl>
<dt>
<dd> Path to vmlinux. Required for annotation functionality.</dl>
<p> -m &lt;pages&gt;, &#8211;mmap-pages=&lt;pages&gt;</p>
<dl>
<dt>
<dd> Number of mmap data pages (must be a power of two) or size specification with appended unit character &#8211; B/K/M/G. The size is rounded up to have nearest pages power of two value.</dl>
<p> -p &lt;pid&gt;, &#8211;pid=&lt;pid&gt;</p>
<dl>
<dt>
<dd> Profile events on existing Process ID (comma separated list).</dl>
<p> -t &lt;tid&gt;, &#8211;tid=&lt;tid&gt;</p>
<dl>
<dt>
<dd> Profile events on existing thread ID (comma separated list).</dl>
<p> -u, &#8211;uid=</p>
<dl>
<dt>
<dd> Record events in threads owned by uid. Name or number.</dl>
<p> -r &lt;priority&gt;, &#8211;realtime=&lt;priority&gt;</p>
<dl>
<dt>
<dd> Collect data with this RT SCHED_FIFO priority.</dl>
<p> &#8211;sym-annotate=&lt;symbol&gt;</p>
<dl>
<dt>
<dd> Annotate this symbol.</dl>
<p> -K, &#8211;hide_kernel_symbols</p>
<dl>
<dt>
<dd> Hide kernel symbols.</dl>
<p> -U, &#8211;hide_user_symbols</p>
<dl>
<dt>
<dd> Hide user symbols.</dl>
<p> &#8211;demangle-kernel</p>
<dl>
<dt>
<dd> Demangle kernel symbols.</dl>
<p> -D, &#8211;dump-symtab</p>
<dl>
<dt>
<dd> Dump the symbol table used for profiling.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose (show counter open errors, etc).</dl>
<p> -z, &#8211;zero</p>
<dl>
<dt>
<dd> Zero history across display updates.</dl>
<p> -s, &#8211;sort</p>
<dl>
<dt>
<dd> Sort by key(s): pid, comm, dso, symbol, parent, srcline, weight, local_weight, abort, in_tx, transaction, overhead, sample, period. Please see description of &#8211;sort in the perf-report man page.</dl>
<p> &#8211;fields=</p>
<dl>
<dt>
<dd> Specify output field &#8211; multiple keys can be specified in CSV format. Following fields are available: overhead, overhead_sys, overhead_us, overhead_children, sample and period. Also it can contain any sort key(s). </p>
<dl>
<dt>
<dd>
<pre>
By default, every sort keys not specified in --field will be appended
automatically.
</pre>
</dl>
</dl>
<p> -n, &#8211;show-nr-samples</p>
<dl>
<dt>
<dd> Show a column with the number of samples.</dl>
<p> &#8211;show-total-period</p>
<dl>
<dt>
<dd> Show a column with the sum of periods.</dl>
<p> &#8211;dsos</p>
<dl>
<dt>
<dd> Only consider symbols in these dsos. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> &#8211;comms</p>
<dl>
<dt>
<dd> Only consider symbols in these comms. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> &#8211;symbols</p>
<dl>
<dt>
<dd> Only consider these symbols. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> -M, &#8211;disassembler-style=</p>
<dl>
<dt>
<dd> Set disassembler style for objdump.</dl>
<p> &#8211;source</p>
<dl>
<dt>
<dd> Interleave source code with assembly code. Enabled by default, disable with &#8211;no-source.</dl>
<p> &#8211;asm-raw</p>
<dl>
<dt>
<dd> Show raw instruction encoding of assembly instructions.</dl>
<p> -g</p>
<dl>
<dt>
<dd> Enables call-graph (stack chain/backtrace) recording.</dl>
<p> &#8211;call-graph</p>
<dl>
<dt>
<dd> Setup and enable call-graph (stack chain/backtrace) recording, implies -g.</dl>
<p> &#8211;children</p>
<dl>
<dt>
<dd> Accumulate callchain of children to parent entry so that then can show up in the output. The output will have a new &quot;Children&quot; column and will be sorted on the data. It requires -g/&#8211;call-graph option enabled.</dl>
<p> &#8211;max-stack</p>
<dl>
<dt>
<dd> Set the stack depth limit when parsing the callchain, anything beyond the specified depth will be ignored. This is a trade-off between information loss and faster processing especially for workloads that can have a very long callchain stack. </p>
<dl>
<dt>
<dd>
<pre>
Default: 127
</pre>
</dl>
</dl>
<p> &#8211;ignore-callees=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Ignore callees of the function(s) matching the given regex. This has the effect of collecting the callers of each such function into one place in the call-graph tree.</dl>
<p> &#8211;percent-limit</p>
<dl>
<dt>
<dd> Do not show entries which have an overhead under that percent. (Default: 0).</dl>
<p> &#8211;percentage</p>
<dl>
<dt>
<dd> Determine how to display the overhead percentage of filtered entries. Filters can be applied by &#8211;comms, &#8211;dsos and/or &#8211;symbols options and Zoom operations on the TUI (thread, dso, etc). </p>
<dl>
<dt>
<dd>
<pre>
&quot;relative&quot; means it's relative to filtered entries only so that the
sum of shown entries will be always 100%. &quot;absolute&quot; means it retains
the original value before and after the filter is applied.
</pre>
</dl>
</dl>
<p> -w, &#8211;column-widths=&lt;width[,width&#8230;]&gt;</p>
<dl>
<dt>
<dd> Force each column width to the provided list, for large terminal readability. 0 means no limit (default behavior).</dl>
<h2>INTERACTIVE PROMPTING KEYS</h2>
<p> [d]</p>
<dl>
<dt>
<dd> Display refresh delay.</dl>
<p> [e]</p>
<dl>
<dt>
<dd> Number of entries to display.</dl>
<p> [E]</p>
<dl>
<dt>
<dd> Event to display when multiple counters are active.</dl>
<p> [f]</p>
<dl>
<dt>
<dd> Profile display filter (&gt;= hit count).</dl>
<p> [F]</p>
<dl>
<dt>
<dd> Annotation display filter (&gt;= % of total).</dl>
<p> [s]</p>
<dl>
<dt>
<dd> Annotate symbol.</dl>
<p> [S]</p>
<dl>
<dt>
<dd> Stop annotation, return to full profile display.</dl>
<p> [z]</p>
<dl>
<dt>
<dd> Toggle event count zeroing across display updates.</dl>
<p> [qQ]</p>
<dl>
<dt>
<dd> Quit.</dl>
<p> Pressing any unmapped key displays a menu, and prompts for input.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
