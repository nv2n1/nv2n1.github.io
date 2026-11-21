---

title: "perf-report(1)"
name: "perf-report"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-report/"
description: "perf-report – Read perf.data (created by perf record) and display the profile"
---

<pre>
<i>perf report</i> [-i &lt;file&gt; | --input=file]
</pre>
<p> This command displays the performance counter profile information recorded via perf record.</p>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=</p>
<dl>
<dt>
</dt><dd> Input file name. (default: perf.data unless stdin is a fifo)</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Be more verbose. (show symbol address, etc)</dd></dl>
<p> -n, &#8211;show-nr-samples</p>
<dl>
<dt>
</dt><dd> Show the number of samples for each symbol</dd></dl>
<p> &#8211;showcpuutilization</p>
<dl>
<dt>
</dt><dd> Show sample percentage for different cpu modes.</dd></dl>
<p> -T, &#8211;threads</p>
<dl>
<dt>
</dt><dd> Show per-thread event counters</dd></dl>
<p> -c, &#8211;comms=</p>
<dl>
<dt>
</dt><dd> Only consider symbols in these comms. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> -d, &#8211;dsos=</p>
<dl>
<dt>
</dt><dd> Only consider symbols in these dsos. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> -S, &#8211;symbols=</p>
<dl>
<dt>
</dt><dd> Only consider these symbols. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the overhead column. See &#8211;percentage for more info.</dd></dl>
<p> &#8211;symbol-filter=</p>
<dl>
<dt>
</dt><dd> Only show symbols that match (partially) with this filter.</dd></dl>
<p> -U, &#8211;hide-unresolved</p>
<dl>
<dt>
</dt><dd> Only display entries resolved to a symbol.</dd></dl>
<p> -s, &#8211;sort=</p>
<dl>
<dt>
</dt><dd> Sort histogram entries by given key(s) &#8211; multiple keys can be specified in CSV format. Following sort keys are available: pid, comm, dso, symbol, parent, cpu, srcline, weight, local_weight. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Each key has following meaning:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd> &bull; comm: command (name) of the task which can be read via /proc/&lt;pid&gt;/comm</dd></dl>
<dl>
<dt>
</dt><dd> &bull; pid: command and tid of the task</dd></dl>
<dl>
<dt>
</dt><dd> &bull; dso: name of library or module executed at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; symbol: name of function executed at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; parent: name of function matched to the parent regex filter. Unmatched entries are displayed as &quot;[other]&quot;.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; cpu: cpu number the task ran at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; srcline: filename and line number executed at the time of sample. The DWARF debugging info must be provided.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; weight: Event specific weight, e.g. memory latency or transaction abort cost. This is the global weight.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; local_weight: Local weight version of the weight above.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; transaction: Transaction abort flags.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; overhead: Overhead percentage of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; overhead_sys: Overhead percentage of sample running in system mode</dd></dl>
<dl>
<dt>
</dt><dd> &bull; overhead_us: Overhead percentage of sample running in user mode</dd></dl>
<dl>
<dt>
</dt><dd> &bull; overhead_guest_sys: Overhead percentage of sample running in system mode on guest machine</dd></dl>
<dl>
<dt>
</dt><dd> &bull; overhead_guest_us: Overhead percentage of sample running in user mode on guest machine</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sample: Number of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; period: Raw number of event count of sample </dd>
<dl>
<dt>
</dt><dd>
<pre>
By default, comm, dso and symbol keys are used.
(i.e. --sort comm,dso,symbol)
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
If --branch-stack option is used, following sort keys are also
available:
dso_from, dso_to, symbol_from, symbol_to, mispredict.
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; dso_from: name of library or module branched from</dd></dl>
<dl>
<dt>
</dt><dd> &bull; dso_to: name of library or module branched to</dd></dl>
<dl>
<dt>
</dt><dd> &bull; symbol_from: name of function branched from</dd></dl>
<dl>
<dt>
</dt><dd> &bull; symbol_to: name of function branched to</dd></dl>
<dl>
<dt>
</dt><dd> &bull; mispredict: &quot;N&quot; for predicted branch, &quot;Y&quot; for mispredicted branch</dd></dl>
<dl>
<dt>
</dt><dd> &bull; in_tx: branch in TSX transaction</dd></dl>
<dl>
<dt>
</dt><dd> &bull; abort: TSX transaction abort. </dd>
<dl>
<dt>
</dt><dd>
<pre>
And default sort keys are changed to comm, dso_from, symbol_from, dso_to
and symbol_to, see '--branch-stack'.
</pre>
</dd></dl>
</dl>
</dl>
<p> -F, &#8211;fields=</p>
<dl>
<dt>
</dt><dd> Specify output field &#8211; multiple keys can be specified in CSV format. Following fields are available: overhead, overhead_sys, overhead_us, overhead_children, sample and period. Also it can contain any sort key(s). </dd>
<dl>
<dt>
</dt><dd>
<pre>
By default, every sort keys not specified in -F will be appended
automatically.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
If --mem-mode option is used, following sort keys are also available
(incompatible with --branch-stack):
symbol_daddr, dso_daddr, locked, tlb, mem, snoop, dcacheline.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd> &bull; symbol_daddr: name of data symbol being executed on at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; dso_daddr: name of library or module containing the data being executed on at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; locked: whether the bus was locked at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; tlb: type of tlb access for the data at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; mem: type of memory access for the data at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; snoop: type of snoop (if any) for the data at the time of sample</dd></dl>
<dl>
<dt>
</dt><dd> &bull; dcacheline: the cacheline the data address is on at the time of sample </dd>
<dl>
<dt>
</dt><dd>
<pre>
And default sort keys are changed to local_weight, mem, sym, dso,
symbol_daddr, dso_daddr, snoop, tlb, locked, see '--mem-mode'.
</pre>
</dd></dl>
</dl>
</dl>
<p> -p, &#8211;parent=&lt;regex&gt;</p>
<dl>
<dt>
</dt><dd> A regex filter to identify parent. The parent is a caller of this function and searched through the callchain, thus it requires callchain information recorded. The pattern is in the exteneded regex format and defaults to &quot;^sys_|^do_page_fault&quot;, see <i>&#8211;sort parent</i>.</dd></dl>
<p> -x, &#8211;exclude-other</p>
<dl>
<dt>
</dt><dd> Only display entries with parent-match.</dd></dl>
<p> -w, &#8211;column-widths=&lt;width[,width&#8230;]&gt;</p>
<dl>
<dt>
</dt><dd> Force each column width to the provided list, for large terminal readability. 0 means no limit (default behavior).</dd></dl>
<p> -t, &#8211;field-separator=</p>
<dl>
<dt>
</dt><dd> Use a special separator character and don&#8217;t pad with spaces, replacing all occurrences of this separator in symbol names (and other output) with a <i>.</i> character, that thus it&#8217;s the only non valid separator.</dd></dl>
<p> -D, &#8211;dump-raw-trace</p>
<dl>
<dt>
</dt><dd> Dump raw trace in ASCII.</dd></dl>
<p> -g [type,min[,limit],order[,key]], &#8211;call-graph</p>
<dl>
<dt>
</dt><dd> Display call chains using type, min percent threshold, optional print limit and order. type can be either: </dd>
<dl>
<dt>
</dt><dd> &bull; flat: single column, linear exposure of call chains.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; graph: use a graph tree, displaying absolute overhead rates.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fractal: like graph, but displays relative rates. Each branch of the tree is considered as a new profiled object. </dd>
<dl>
<dt>
</dt><dd>
<pre>
order can be either:
- callee: callee based call graph.
- caller: inverted caller based call graph.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
key can be:
- function: compare on functions
- address: compare on individual code addresses
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
Default: fractal,0.5,callee,function.
</pre>
</dd></dl>
</dl>
</dl>
<p> &#8211;children</p>
<dl>
<dt>
</dt><dd> Accumulate callchain of children to parent entry so that then can show up in the output. The output will have a new &quot;Children&quot; column and will be sorted on the data. It requires callchains are recorded.</dd></dl>
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
<p> -G, &#8211;inverted</p>
<dl>
<dt>
</dt><dd> alias for inverted caller based call graph.</dd></dl>
<p> &#8211;ignore-callees=&lt;regex&gt;</p>
<dl>
<dt>
</dt><dd> Ignore callees of the function(s) matching the given regex. This has the effect of collecting the callers of each such function into one place in the call-graph tree.</dd></dl>
<p> &#8211;pretty=&lt;key&gt;</p>
<dl>
<dt>
</dt><dd> Pretty printing style. key: normal, raw</dd></dl>
<p> &#8211;stdio</p>
<dl>
<dt>
</dt><dd> Use the stdio interface.</dd></dl>
<p> &#8211;tui</p>
<dl>
<dt>
</dt><dd> Use the TUI interface, that is integrated with annotate and allows zooming into DSOs or threads, among other features. Use of &#8211;tui requires a tty, if one is not present, as when piping to other commands, the stdio interface is used.</dd></dl>
<p> &#8211;gtk</p>
<dl>
<dt>
</dt><dd> Use the GTK2 interface.</dd></dl>
<p> -k, &#8211;vmlinux=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> vmlinux pathname</dd></dl>
<p> &#8211;kallsyms=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> kallsyms pathname</dd></dl>
<p> -m, &#8211;modules</p>
<dl>
<dt>
</dt><dd> Load module symbols. WARNING: This should only be used with -k and a LIVE kernel.</dd></dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
</dt><dd> Don&#8217;t complain, do it.</dd></dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
</dt><dd> Look for files with symbols relative to this directory.</dd></dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
</dt><dd> Only report samples for the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to report samples on all CPUs.</dd></dl>
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
<p> &#8211;show-total-period</p>
<dl>
<dt>
</dt><dd> Show a column with the sum of periods.</dd></dl>
<p> -I, &#8211;show-info</p>
<dl>
<dt>
</dt><dd> Display extended information about the perf.data file. This adds information which may be very large and thus may clutter the display. It currently includes: cpu and numa topology of the host system.</dd></dl>
<p> -b, &#8211;branch-stack</p>
<dl>
<dt>
</dt><dd> Use the addresses of sampled taken branches instead of the instruction address to build the histograms. To generate meaningful output, the perf.data file must have been obtained using perf record -b or perf record &#8211;branch-filter xxx where xxx is a branch filter option. perf report is able to auto-detect whether a perf.data file contains branch stacks and it will automatically switch to the branch view mode, unless &#8211;no-branch-stack is used.</dd></dl>
<p> &#8211;objdump=&lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Path to objdump binary.</dd></dl>
<p> &#8211;group</p>
<dl>
<dt>
</dt><dd> Show event group information together.</dd></dl>
<p> &#8211;demangle</p>
<dl>
<dt>
</dt><dd> Demangle symbol names to human readable form. It&#8217;s enabled by default, disable with &#8211;no-demangle.</dd></dl>
<p> &#8211;demangle-kernel</p>
<dl>
<dt>
</dt><dd> Demangle kernel symbol names to human readable form (for C++ kernels).</dd></dl>
<p> &#8211;mem-mode</p>
<dl>
<dt>
</dt><dd> Use the data addresses of samples in addition to instruction addresses to build the histograms. To generate meaningful output, the perf.data file must have been obtained using perf record -d -W and using a special event -e cpu/mem-loads/ or -e cpu/mem-stores/. See <i>perf mem</i> for simpler access.</dd></dl>
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
sum of shown entries will be always 100%.  &quot;absolute&quot; means it retains
the original value before and after the filter is applied.
</pre>
</dd></dl>
</dl>
<p> &#8211;header</p>
<dl>
<dt>
</dt><dd> Show header information in the perf.data file. This includes various information like hostname, OS and perf version, cpu/mem info, perf command line, event list and so on. Currently only &#8211;stdio output supports this feature.</dd></dl>
<p> &#8211;header-only</p>
<dl>
<dt>
</dt><dd> Show only perf.data header (forces &#8211;stdio).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-annotate/">perf-annotate</a></code>(1) </p>
