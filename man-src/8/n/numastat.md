---
title: "numastat(8)"
name: "numastat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-numastat/"
---

<h2>numastat</h2>
<p><code>numastat</code> &#8211; Show per-NUMA-node memory statistics for processes and the operating system</p>
<h2>Syntax</h2>
<p><code>numastat</code> </p>
<p> <code>numastat</code> [<i>-V</i>] </p>
<p> <code>numastat</code> [<i>&lt;PID&gt;|&lt;pattern&gt;&#8230;</i>] </p>
<p> <code>numastat</code> [<i>-c</i>] [<i>-m</i>] [<i>-n</i>] [<i>-p &lt;PID&gt;|&lt;pattern&gt;</i>] [<i>-s[&lt;node&gt;]</i>] [<i>-v</i>] [<i>-z</i>] [<i>&lt;PID&gt;|&lt;pattern&gt;&#8230;</i>]</p>
<h2>Description</h2>
<p><code>numastat </code> with no command options or arguments at all, displays per-node NUMA hit and miss system statistics from the kernel memory allocator. This default <code>numastat</code> behavior is strictly compatible with the previous long-standing <code>numastat</code> perl script, written by Andi Kleen. The default <code>numastat</code> statistics shows per-node numbers (in units of pages of memory) in these categories: </p>
<p> <code>numa_hit </code> is memory successfully allocated on this node as intended. </p>
<p> <code>numa_miss</code> is memory allocated on this node despite the process preferring some different node. Each <i>numa_miss</i> has a <i>numa_foreign</i> on another node. </p>
<p> <code>numa_foreign</code> is memory intended for this node, but actually allocated on some different node. Each <i>numa_foreign</i> has a <i>numa_miss</i> on another node. </p>
<p> <code>interleave_hit</code> is interleaved memory successfully allocated on this node as intended. </p>
<p> <code>local_node</code> is memory allocated on this node while a process was running on it. </p>
<p> <code>other_node</code> is memory allocated on this node while a process was running on some other node. </p>
<p> Any supplied options or arguments with the <code>numastat</code> command will significantly change both the content and the format of the display. Specified options will cause display units to change to megabytes of memory, and will change other specific behaviors of <code>numastat</code> as described below.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Minimize table display width by dynamically shrinking column widths based on data contents. With this option, amounts of memory will be rounded to the nearest megabyte (rather than the usual display with two decimal places). Column width and inter-column spacing will be somewhat unpredictable with this option, but the more dense display will be very useful on systems with many NUMA nodes.</p>
<dt><code>-m</code></p>
<dd>Show the meminfo-like system-wide memory usage information. This option produces a per-node breakdown of memory usage information similar to that found in /proc/meminfo.</p>
<dt><code>-n</code></p>
<dd>Show the original <code>numastat</code> statistics info. This will show the same information as the default <code>numastat</code> behavior but the units will be megabytes of memory, and there will be other formatting and layout changes versus the original <code>numastat</code> behavior.</p>
<dt><code>-p</code> &lt;<code>PID</code>&gt; or &lt;<code>pattern</code>&gt;</p>
<dd>Show per-node memory allocation information for the specified PID or pattern. If the -p argument is only digits, it is assumed to be a numerical PID. If the argument characters are not only digits, it is assumed to be a text fragment pattern to search for in process command lines. For example, <code>numastat -p qemu</code> will attempt to find and show information for processes with &quot;qemu&quot; in the command line. Any command line arguments remaining after <code>numastat</code> option flag processing is completed, are assumed to be additional &lt;<code>PID</code>&gt; or &lt;<code>pattern</code>&gt; process specifiers. In this sense, the <code>-p</code> option flag is optional: <code>numastat qemu</code> is equivalent to <code>numastat -p qemu</code></p>
<dt><code>-s[&lt;node&gt;]</code></p>
<dd>Sort the table data in descending order before displaying it, so the biggest memory consumers are listed first. With no specified &lt;node&gt;, the table will be sorted by the total column. If the optional &lt;node&gt; argument is supplied, the data will be sorted by the &lt;node&gt; column. Note that &lt;node&gt; must follow the <code>-s</code> immediately with no intermediate white space (e.g., <code>numastat -s2</code>). Because <code>-s</code> can allow an optional argument, it must always be the last option character in a compound option character string. For example, instead of <code>numastat -msc</code> (which probably will not work as you expect), use <code>numastat -mcs</code></p>
<dt><code>-v</code></p>
<dd>Make some reports more verbose. In particular, process information for multiple processes will display detailed information for each process. Normally when per-node information for multiple processes is displayed, only the total lines are shown.</p>
<dt><code>-V</code></p>
<dd>Display <code>numastat</code> version information and exit.</p>
<dt><code>-z</code></p>
<dd>Skip display of table rows and columns of only zero valuess. This can be used to greatly reduce the amount of uninteresting zero data on systems with many NUMA nodes. Note that when rows or columns of zeros are still displayed with this option, that probably means there is at least one value in the row or column that is actually non-zero, but rounded to zero for display.</dl>
<h2>Notes</h2>
<p><code>numastat</code> attempts to fold each table display so it will be conveniently readable on the output terminal. Normally a terminal width of 80 characters is assumed. When the <code>resize</code> command is available, <code>numastat</code> attempts to dynamically determine and fine tune the output tty width from <code>resize</code> output. If <code>numastat</code> output is not to a tty, very long output lines can be produced, depending on how many NUMA nodes are present. In all cases, output width can be explicitly specified via the <code>NUMASTAT_WIDTH</code> environment variable. For example, <code>NUMASTAT_WIDTH=100 numastat</code>. On systems with many NUMA nodes, <code>numastat -c -z &#8230;.</code> can be very helpful to selectively reduce the amount of displayed information.</p>
<h2>Environment Variables</h2>
<dl>
<dt>NUMASTAT_WIDTH</p>
<dd></dl>
<h2>Files</h2>
<p><i>/proc/*/numa_maps</i><br />
 <i>/sys/devices/system/node/node*/meminfo</i><br />
 <i>/sys/devices/system/node/node*/numastat</i></p>
<h2>Examples</h2>
<p><i>numastat -c -z -m -n</i><br />
 <i>numastat -czs libvirt kvm qemu</i><br />
 <i>watch -n1 numastat</i><br />
 <i>watch -n1 &#8211;differences=cumulative numastat</i></p>
<h2>Authors</h2>
<p>The original <code>numastat</code> perl script was written circa 2003 by Andi Kleen &lt;andi.kleen [at] intel.com&gt;. The current <code>numastat</code> program was written in 2012 by Bill Gray &lt;bgray [at] redhat.com&gt; to be compatible by default with the original, and to add options to display per-node system memory usage and per-node process memory allocation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8), <code>set_mempolicy(</code>2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) </p>
