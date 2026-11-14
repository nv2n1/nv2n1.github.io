---
title: "perf-report(1)"
name: "perf-report"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-report/"
description: "perf-report – Read perf.data (created by perf record) and display the profile"
---

<h2 class="name">NAME</h2>
<p> perf-report &#8211; Read perf.data (created by perf record) and display the profile </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf report</i> [-i &lt;file&gt; | --input=file]
</pre>
<h2>DESCRIPTION</h2>
<p> This command displays the performance counter profile information recorded via perf record.</p>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=</p>
<dl>
<dt>
<dd> Input file name. (default: perf.data unless stdin is a fifo)</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose. (show symbol address, etc)</dl>
<p> -n, &#8211;show-nr-samples</p>
<dl>
<dt>
<dd> Show the number of samples for each symbol</dl>
<p> &#8211;showcpuutilization</p>
<dl>
<dt>
<dd> Show sample percentage for different cpu modes.</dl>
<p> -T, &#8211;threads</p>
<dl>
<dt>
<dd> Show per-thread event counters</dl>
<p> -c, &#8211;comms=</p>
<dl>
<dt>
<dd> Only consider symbols in these comms. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> -d, &#8211;dsos=</p>
<dl>
<dt>
<dd> Only consider symbols in these dsos. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> -S, &#8211;symbols=</p>
<dl>
<dt>
<dd> Only consider these symbols. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dl>
<p> &#8211;symbol-filter=</p>
<dl>
<dt>
<dd> Only show symbols that match (partially) with this filter.</dl>
<p> -U, &#8211;hide-unresolved</p>
<dl>
<dt>
<dd> Only display entries resolved to a symbol.</dl>
<p> -s, &#8211;sort=</p>
<dl>
<dt>
<dd> Sort histogram entries by given key(s) &#8211; multiple keys can be specified in CSV format. Following sort keys are available: pid, comm, dso, symbol, parent, cpu, srcline, weight, local_weight. </p>
<dl>
<dt>
<dd>
<pre>
Each key has following meaning:
</pre>
</dl>
<dl>
<dt>
<dd> &bull; comm: command (name) of the task which can be read via /proc/&lt;pid&gt;/comm</dl>
<dl>
<dt>
<dd> &bull; pid: command and tid of the task</dl>
<dl>
<dt>
<dd> &bull; dso: name of library or module executed at the time of sample</dl>
<dl>
<dt>
<dd> &bull; symbol: name of function executed at the time of sample</dl>
<dl>
<dt>
<dd> &bull; parent: name of function matched to the parent regex filter. Unmatched entries are displayed as &quot;[other]&quot;.</dl>
<dl>
<dt>
<dd> &bull; cpu: cpu number the task ran at the time of sample</dl>
<dl>
<dt>
<dd> &bull; srcline: filename and line number executed at the time of sample. The DWARF debugging info must be provided.</dl>
<dl>
<dt>
<dd> &bull; weight: Event specific weight, e.g. memory latency or transaction abort cost. This is the global weight.</dl>
<dl>
<dt>
<dd> &bull; local_weight: Local weight version of the weight above.</dl>
<dl>
<dt>
<dd> &bull; transaction: Transaction abort flags.</dl>
<dl>
<dt>
<dd> &bull; overhead: Overhead percentage of sample</dl>
<dl>
<dt>
<dd> &bull; overhead_sys: Overhead percentage of sample running in system mode</dl>
<dl>
<dt>
<dd> &bull; overhead_us: Overhead percentage of sample running in user mode</dl>
<dl>
<dt>
<dd> &bull; overhead_guest_sys: Overhead percentage of sample running in system mode on guest machine</dl>
<dl>
<dt>
<dd> &bull; overhead_guest_us: Overhead percentage of sample running in user mode on guest machine</dl>
<dl>
<dt>
<dd> &bull; sample: Number of sample</dl>
<dl>
<dt>
<dd> &bull; period: Raw number of event count of sample </p>
<dl>
<dt>
<dd>
<pre>
By default, comm, dso and symbol keys are used.
(i.e. --sort comm,dso,symbol)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
If --branch-stack option is used, following sort keys are also
available:
dso_from, dso_to, symbol_from, symbol_to, mispredict.
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; dso_from: name of library or module branched from</dl>
<dl>
<dt>
<dd> &bull; dso_to: name of library or module branched to</dl>
<dl>
<dt>
<dd> &bull; symbol_from: name of function branched from</dl>
<dl>
<dt>
<dd> &bull; symbol_to: name of function branched to</dl>
<dl>
<dt>
<dd> &bull; mispredict: &quot;N&quot; for predicted branch, &quot;Y&quot; for mispredicted branch</dl>
<dl>
<dt>
<dd> &bull; in_tx: branch in TSX transaction</dl>
<dl>
<dt>
<dd> &bull; abort: TSX transaction abort. </p>
<dl>
<dt>
<dd>
<pre>
And default sort keys are changed to comm, dso_from, symbol_from, dso_to
and symbol_to, see '--branch-stack'.
</pre>
</dl>
</dl>
</dl>
<p> -F, &#8211;fields=</p>
<dl>
<dt>
<dd> Specify output field &#8211; multiple keys can be specified in CSV format. Following fields are available: overhead, overhead_sys, overhead_us, overhead_children, sample and period. Also it can contain any sort key(s). </p>
<dl>
<dt>
<dd>
<pre>
By default, every sort keys not specified in -F will be appended
automatically.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
If --mem-mode option is used, following sort keys are also available
(incompatible with --branch-stack):
symbol_daddr, dso_daddr, locked, tlb, mem, snoop, dcacheline.
</pre>
</dl>
<dl>
<dt>
<dd> &bull; symbol_daddr: name of data symbol being executed on at the time of sample</dl>
<dl>
<dt>
<dd> &bull; dso_daddr: name of library or module containing the data being executed on at the time of sample</dl>
<dl>
<dt>
<dd> &bull; locked: whether the bus was locked at the time of sample</dl>
<dl>
<dt>
<dd> &bull; tlb: type of tlb access for the data at the time of sample</dl>
<dl>
<dt>
<dd> &bull; mem: type of memory access for the data at the time of sample</dl>
<dl>
<dt>
<dd> &bull; snoop: type of snoop (if any) for the data at the time of sample</dl>
<dl>
<dt>
<dd> &bull; dcacheline: the cacheline the data address is on at the time of sample </p>
<dl>
<dt>
<dd>
<pre>
And default sort keys are changed to local_weight, mem, sym, dso,
symbol_daddr, dso_daddr, snoop, tlb, locked, see '--mem-mode'.
</pre>
</dl>
</dl>
</dl>
<p> -p, &#8211;parent=&lt;regex&gt;</p>
<dl>
<dt>
<dd> A regex filter to identify parent. The parent is a caller of this function and searched through the callchain, thus it requires callchain information recorded. The pattern is in the exteneded regex format and defaults to &quot;^sys_|^do_page_fault&quot;, see <i>&#8211;sort parent</i>.</dl>
<p> -x, &#8211;exclude-other</p>
<dl>
<dt>
<dd> Only display entries with parent-match.</dl>
<p> -w, &#8211;column-widths=&lt;width[,width&#8230;]&gt;</p>
<dl>
<dt>
<dd> Force each column width to the provided list, for large terminal readability. 0 means no limit (default behavior).</dl>
<p> -t, &#8211;field-separator=</p>
<dl>
<dt>
<dd> Use a special separator character and don&#8217;t pad with spaces, replacing all occurrences of this separator in symbol names (and other output) with a <i>.</i> character, that thus it&#8217;s the only non valid separator.</dl>
<p> -D, &#8211;dump-raw-trace</p>
<dl>
<dt>
<dd> Dump raw trace in ASCII.</dl>
<p> -g [type,min[,limit],order[,key]], &#8211;call-graph</p>
<dl>
<dt>
<dd> Display call chains using type, min percent threshold, optional print limit and order. type can be either: </p>
<dl>
<dt>
<dd> &bull; flat: single column, linear exposure of call chains.</dl>
<dl>
<dt>
<dd> &bull; graph: use a graph tree, displaying absolute overhead rates.</dl>
<dl>
<dt>
<dd> &bull; fractal: like graph, but displays relative rates. Each branch of the tree is considered as a new profiled object. </p>
<dl>
<dt>
<dd>
<pre>
order can be either:
- callee: callee based call graph.
- caller: inverted caller based call graph.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
key can be:
- function: compare on functions
- address: compare on individual code addresses
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Default: fractal,0.5,callee,function.
</pre>
</dl>
</dl>
</dl>
<p> &#8211;children</p>
<dl>
<dt>
<dd> Accumulate callchain of children to parent entry so that then can show up in the output. The output will have a new &quot;Children&quot; column and will be sorted on the data. It requires callchains are recorded.</dl>
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
<p> -G, &#8211;inverted</p>
<dl>
<dt>
<dd> alias for inverted caller based call graph.</dl>
<p> &#8211;ignore-callees=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Ignore callees of the function(s) matching the given regex. This has the effect of collecting the callers of each such function into one place in the call-graph tree.</dl>
<p> &#8211;pretty=&lt;key&gt;</p>
<dl>
<dt>
<dd> Pretty printing style. key: normal, raw</dl>
<p> &#8211;stdio</p>
<dl>
<dt>
<dd> Use the stdio interface.</dl>
<p> &#8211;tui</p>
<dl>
<dt>
<dd> Use the TUI interface, that is integrated with annotate and allows zooming into DSOs or threads, among other features. Use of &#8211;tui requires a tty, if one is not present, as when piping to other commands, the stdio interface is used.</dl>
<p> &#8211;gtk</p>
<dl>
<dt>
<dd> Use the GTK2 interface.</dl>
<p> -k, &#8211;vmlinux=&lt;file&gt;</p>
<dl>
<dt>
<dd> vmlinux pathname</dl>
<p> &#8211;kallsyms=&lt;file&gt;</p>
<dl>
<dt>
<dd> kallsyms pathname</dl>
<p> -m, &#8211;modules</p>
<dl>
<dt>
<dd> Load module symbols. WARNING: This should only be used with -k and a LIVE kernel.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Don&#8217;t complain, do it.</dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
<dd> Look for files with symbols relative to this directory.</dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
<dd> Only report samples for the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to report samples on all CPUs.</dl>
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
<p> &#8211;show-total-period</p>
<dl>
<dt>
<dd> Show a column with the sum of periods.</dl>
<p> -I, &#8211;show-info</p>
<dl>
<dt>
<dd> Display extended information about the perf.data file. This adds information which may be very large and thus may clutter the display. It currently includes: cpu and numa topology of the host system.</dl>
<p> -b, &#8211;branch-stack</p>
<dl>
<dt>
<dd> Use the addresses of sampled taken branches instead of the instruction address to build the histograms. To generate meaningful output, the perf.data file must have been obtained using perf record -b or perf record &#8211;branch-filter xxx where xxx is a branch filter option. perf report is able to auto-detect whether a perf.data file contains branch stacks and it will automatically switch to the branch view mode, unless &#8211;no-branch-stack is used.</dl>
<p> &#8211;objdump=&lt;path&gt;</p>
<dl>
<dt>
<dd> Path to objdump binary.</dl>
<p> &#8211;group</p>
<dl>
<dt>
<dd> Show event group information together.</dl>
<p> &#8211;demangle</p>
<dl>
<dt>
<dd> Demangle symbol names to human readable form. It&#8217;s enabled by default, disable with &#8211;no-demangle.</dl>
<p> &#8211;demangle-kernel</p>
<dl>
<dt>
<dd> Demangle kernel symbol names to human readable form (for C++ kernels).</dl>
<p> &#8211;mem-mode</p>
<dl>
<dt>
<dd> Use the data addresses of samples in addition to instruction addresses to build the histograms. To generate meaningful output, the perf.data file must have been obtained using perf record -d -W and using a special event -e cpu/mem-loads/ or -e cpu/mem-stores/. See <i>perf mem</i> for simpler access.</dl>
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
sum of shown entries will be always 100%.  &quot;absolute&quot; means it retains
the original value before and after the filter is applied.
</pre>
</dl>
</dl>
<p> &#8211;header</p>
<dl>
<dt>
<dd> Show header information in the perf.data file. This includes various information like hostname, OS and perf version, cpu/mem info, perf command line, event list and so on. Currently only &#8211;stdio output supports this feature.</dl>
<p> &#8211;header-only</p>
<dl>
<dt>
<dd> Show only perf.data header (forces &#8211;stdio).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-annotate/">perf-annotate</a></code>(1) </p>
<h2>Index</h2>
