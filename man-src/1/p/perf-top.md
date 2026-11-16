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
</dt><dd> System-wide collection. (default)</dd></dl>
<p> -c &lt;count&gt;, &#8211;count=&lt;count&gt;</p>
<dl>
<dt>
</dt><dd> Event period to sample.</dd></dl>
<p> -C &lt;cpu-list&gt;, &#8211;cpu=&lt;cpu&gt;</p>
<dl>
<dt>
</dt><dd> Monitor only on the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to monitor all CPUS.</dd></dl>
<p> -d &lt;seconds&gt;, &#8211;delay=&lt;seconds&gt;</p>
<dl>
<dt>
</dt><dd> Number of seconds to delay between refreshes.</dd></dl>
<p> -e &lt;event&gt;, &#8211;event=&lt;event&gt;</p>
<dl>
<dt>
</dt><dd> Select the PMU event. Selection can be a symbolic event name (use <i>perf list</i> to list all events) or a raw PMU event (eventsel+umask) in the form of rNNN where NNN is a hexadecimal event descriptor.</dd></dl>
<p> -E &lt;entries&gt;, &#8211;entries=&lt;entries&gt;</p>
<dl>
<dt>
</dt><dd> Display this many functions.</dd></dl>
<p> -f &lt;count&gt;, &#8211;count-filter=&lt;count&gt;</p>
<dl>
<dt>
</dt><dd> Only display functions with more events than this.</dd></dl>
<p> &#8211;group</p>
<dl>
<dt>
</dt><dd> Put the counters into a counter group.</dd></dl>
<p> -F &lt;freq&gt;, &#8211;freq=&lt;freq&gt;</p>
<dl>
<dt>
</dt><dd> Profile at this frequency.</dd></dl>
<p> -i, &#8211;inherit</p>
<dl>
<dt>
</dt><dd> Child tasks do not inherit counters.</dd></dl>
<p> -k &lt;path&gt;, &#8211;vmlinux=&lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Path to vmlinux. Required for annotation functionality.</dd></dl>
<p> -m &lt;pages&gt;, &#8211;mmap-pages=&lt;pages&gt;</p>
<dl>
<dt>
</dt><dd> Number of mmap data pages (must be a power of two) or size specification with appended unit character &#8211; B/K/M/G. The size is rounded up to have nearest pages power of two value.</dd></dl>
<p> -p &lt;pid&gt;, &#8211;pid=&lt;pid&gt;</p>
<dl>
<dt>
</dt><dd> Profile events on existing Process ID (comma separated list).</dd></dl>
<p> -t &lt;tid&gt;, &#8211;tid=&lt;tid&gt;</p>
<dl>
<dt>
</dt><dd> Profile events on existing thread ID (comma separated list).</dd></dl>
<p> -u, &#8211;uid=</p>
<dl>
<dt>
</dt><dd> Record events in threads owned by uid. Name or number.</dd></dl>
<p> -r &lt;priority&gt;, &#8211;realtime=&lt;priority&gt;</p>
<dl>
<dt>
</dt><dd> Collect data with this RT SCHED_FIFO priority.</dd></dl>
<p> &#8211;sym-annotate=&lt;symbol&gt;</p>
<dl>
<dt>
</dt><dd> Annotate this symbol.</dd></dl>
<p> -K, &#8211;hide_kernel_symbols</p>
<dl>
<dt>
</dt><dd> Hide kernel symbols.</dd></dl>
<p> -U, &#8211;hide_user_symbols</p>
<dl>
<dt>
</dt><dd> Hide user symbols.</dd></dl>
<p> &#8211;demangle-kernel</p>
<dl>
<dt>
</dt><dd> Demangle kernel symbols.</dd></dl>
<p> -D, &#8211;dump-symtab</p>
<dl>
<dt>
</dt><dd> Dump the symbol table used for profiling.</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Be more verbose (show counter open errors, etc).</dd></dl>
<p> -z, &#8211;zero</p>
<dl>
<dt>
</dt><dd> Zero history across display updates.</dd></dl>
<p> -s, &#8211;sort</p>
<dl>
<dt>
</dt><dd> Sort by key(s): pid, comm, dso, symbol, parent, srcline, weight, local_weight, abort, in_tx, transaction, overhead, sample, period. Please see description of &#8211;sort in the perf-report man page.</dd></dl>
<p> &#8211;fields=</p>
<dl>
<dt>
</dt><dd> Specify output field &#8211; multiple keys can be specified in CSV format. Following fields are available: overhead, overhead_sys, overhead_us, overhead_children, sample and period. Also it can contain any sort key(s). </dd>
<dl>
<dt>
</dt><dd>
<pre>
By default, every sort keys not specified in --field will be appended
automatically.
</pre>
</dd></dl>
</dl>
<p> -n, &#8211;show-nr-samples</p>
<dl>
<dt>
</dt><dd> Show a column with the number of samples.</dd></dl>
<p> &#8211;show-total-period</p>
<dl>
<dt>
</dt><dd> Show a column with the sum of periods.</dd></dl>
<p> &#8211;dsos</p>
<dl>
<dt>
</dt><dd> Only consider symbols in these dsos. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> &#8211;comms</p>
<dl>
<dt>
</dt><dd> Only consider symbols in these comms. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> &#8211;symbols</p>
<dl>
<dt>
</dt><dd> Only consider these symbols. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> -M, &#8211;disassembler-style=</p>
<dl>
<dt>
</dt><dd> Set disassembler style for objdump.</dd></dl>
<p> &#8211;source</p>
<dl>
<dt>
</dt><dd> Interleave source code with assembly code. Enabled by default, disable with &#8211;no-source.</dd></dl>
<p> &#8211;asm-raw</p>
<dl>
<dt>
</dt><dd> Show raw instruction encoding of assembly instructions.</dd></dl>
<p> -g</p>
<dl>
<dt>
</dt><dd> Enables call-graph (stack chain/backtrace) recording.</dd></dl>
<p> &#8211;call-graph</p>
<dl>
<dt>
</dt><dd> Setup and enable call-graph (stack chain/backtrace) recording, implies -g.</dd></dl>
<p> &#8211;children</p>
<dl>
<dt>
</dt><dd> Accumulate callchain of children to parent entry so that then can show up in the output. The output will have a new &quot;Children&quot; column and will be sorted on the data. It requires -g/&#8211;call-graph option enabled.</dd></dl>
<p> &#8211;max-stack</p>
<dl>
<dt>
</dt><dd> Set the stack depth limit when parsing the callchain, anything beyond the specified depth will be ignored. This is a trade-off between information loss and faster processing especially for workloads that can have a very long callchain stack. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default: 127
</pre>
</dd></dl>
</dl>
<p> &#8211;ignore-callees=&lt;regex&gt;</p>
<dl>
<dt>
</dt><dd> Ignore callees of the function(s) matching the given regex. This has the effect of collecting the callers of each such function into one place in the call-graph tree.</dd></dl>
<p> &#8211;percent-limit</p>
<dl>
<dt>
</dt><dd> Do not show entries which have an overhead under that percent. (Default: 0).</dd></dl>
<p> &#8211;percentage</p>
<dl>
<dt>
</dt><dd> Determine how to display the overhead percentage of filtered entries. Filters can be applied by &#8211;comms, &#8211;dsos and/or &#8211;symbols options and Zoom operations on the TUI (thread, dso, etc). </dd>
<dl>
<dt>
</dt><dd>
<pre>
&quot;relative&quot; means it's relative to filtered entries only so that the
sum of shown entries will be always 100%. &quot;absolute&quot; means it retains
the original value before and after the filter is applied.
</pre>
</dd></dl>
</dl>
<p> -w, &#8211;column-widths=&lt;width[,width&#8230;]&gt;</p>
<dl>
<dt>
</dt><dd> Force each column width to the provided list, for large terminal readability. 0 means no limit (default behavior).</dd></dl>
<h2>INTERACTIVE PROMPTING KEYS</h2>
<p> [d]</p>
<dl>
<dt>
</dt><dd> Display refresh delay.</dd></dl>
<p> [e]</p>
<dl>
<dt>
</dt><dd> Number of entries to display.</dd></dl>
<p> [E]</p>
<dl>
<dt>
</dt><dd> Event to display when multiple counters are active.</dd></dl>
<p> [f]</p>
<dl>
<dt>
</dt><dd> Profile display filter (&gt;= hit count).</dd></dl>
<p> [F]</p>
<dl>
<dt>
</dt><dd> Annotation display filter (&gt;= % of total).</dd></dl>
<p> [s]</p>
<dl>
<dt>
</dt><dd> Annotate symbol.</dd></dl>
<p> [S]</p>
<dl>
<dt>
</dt><dd> Stop annotation, return to full profile display.</dd></dl>
<p> [z]</p>
<dl>
<dt>
</dt><dd> Toggle event count zeroing across display updates.</dd></dl>
<p> [qQ]</p>
<dl>
<dt>
</dt><dd> Quit.</dd></dl>
<p> Pressing any unmapped key displays a menu, and prompts for input.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
