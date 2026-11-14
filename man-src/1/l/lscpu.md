---
title: "lscpu(1)"
name: "lscpu"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lscpu/"
description: "lscpu – display information about the CPU architecture"
---

<h2 class="name">NAME</h2>
<p> lscpu &#8211; display information about the CPU architecture </p>
<h2>SYNOPSIS</h2>
<p> <code>lscpu</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>lscpu</code> gathers CPU architecture information from <i>sysfs</i>, <i>/proc/cpuinfo</i> and any applicable architecture-specific libraries (e.g. <code>librtas</code> on Powerpc). The command output can be optimized for parsing or for easy readability by humans. The information includes, for example, the number of CPUs, threads, cores, sockets, and Non-Uniform Memory Access (NUMA) nodes. There is also information about the CPU caches and cache sharing, family, model, bogoMIPS, byte order, and stepping. </p>
<p> The default output formatting on terminal is subject to change and maybe optimized for better readability. The output for non-terminals (e.g., pipes) is never affected by this optimization and it is always in &quot;Field: data
&quot; format. Use for example &quot;<code>lscpu | less</code>&quot; to see the default output without optimizations. </p>
<p> In virtualized environments, the CPU architecture information displayed reflects the configuration of the guest operating system which is typically different from the physical (host) system. On architectures that support retrieving physical topology information, <code>lscpu</code> also displays the number of physical sockets, chips, cores in the host system. </p>
<p> Options that result in an output table have a <i>list</i> argument. Use this argument to customize the command output. Specify a comma-separated list of column labels to limit the output table to only the specified columns, arranged in the specified order. See <code>COLUMNS</code> for a list of valid column labels. The column labels are not case sensitive. </p>
<p> Not all columns are supported on all architectures. If an unsupported column is specified, <code>lscpu</code> prints the column but does not provide any data for it. </p>
<p> The cache sizes are reported as summary from all CPUs. The versions before v2.34 reported per-core sizes, but this output was confusing due to complicated CPUs topology and the way how caches are shared between CPUs. For more details about caches see <code>&#8211;cache</code>. Since version v2.37 <code>lscpu</code> follows cache IDs as provided by Linux kernel and it does not always start from zero.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Include lines for online and offline CPUs in the output (default for <code>-e</code>). This option may only be specified together with option <code>-e</code> or <code>-p</code>.</dl>
<p> <code>-B</code>, <code>&#8211;bytes</code></p>
<dl>
<dt>
<dd> Print the sizes in bytes rather than in a human-readable format.</dl>
<p> <code>-b</code>, <code>&#8211;online</code></p>
<dl>
<dt>
<dd> Limit the output to online CPUs (default for <code>-p</code>). This option may only be specified together with option <code>-e</code> or <code>-p</code>.</dl>
<p> <code>-C</code>, <code>&#8211;caches</code>[=<i>list</i>]</p>
<dl>
<dt>
<dd> Display details about CPU caches. For details about available information see <code>&#8211;help</code> output. </p>
<p> If the <i>list</i> argument is omitted, all columns for which data is available are included in the command output. </p>
<p> When specifying the <i>list</i> argument, the string of option, equal sign (=), and <i>list</i> must not contain any blanks or other whitespace. Examples: &#8216;<code>-C=NAME,ONE-SIZE</code>&#8216; or &#8216;<code>&#8211;caches=NAME,ONE-SIZE</code>&#8216;. </p>
<p> The default list of columns may be extended if list is specified in the format +list (e.g., lscpu -C=+ALLOC-POLICY).</dl>
<p> <code>-c</code>, <code>&#8211;offline</code></p>
<dl>
<dt>
<dd> Limit the output to offline CPUs. This option may only be specified together with option <code>-e</code> or <code>-p</code>.</dl>
<p> <code>-e</code>, <code>&#8211;extended</code>[=<i>list</i>]</p>
<dl>
<dt>
<dd> Display the CPU information in human-readable format. </p>
<p> If the <i>list</i> argument is omitted, the default columns are included in the command output. The default output is subject to change. </p>
<p> When specifying the <i>list</i> argument, the string of option, equal sign (=), and <i>list</i> must not contain any blanks or other whitespace. Examples: &#8216;<code>-e=cpu,node</code>&#8216; or &#8216;<code>&#8211;extended=cpu,node</code>&#8216;. </p>
<p> The default list of columns may be extended if list is specified in the format +list (e.g., lscpu -e=+MHZ).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dt>
<dd> Use JSON output format for the default summary or extended output (see <code>&#8211;extended</code>).</dl>
<p> <code>-p</code>, <code>&#8211;parse</code>[=<i>list</i>]</p>
<dl>
<dt>
<dd> Optimize the command output for easy parsing. </p>
<p> If the <i>list</i> argument is omitted, the command output is compatible with earlier versions of <code>lscpu</code>. In this compatible format, two commas are used to separate CPU cache columns. If no CPU caches are identified the cache column is omitted. If the <i>list</i> argument is used, cache columns are separated with a colon (:). </p>
<p> When specifying the <i>list</i> argument, the string of option, equal sign (=), and <i>list</i> must not contain any blanks or other whitespace. Examples: &#8216;<code>-p=cpu,node</code>&#8216; or &#8216;<code>&#8211;parse=cpu,node</code>&#8216;. </p>
<p> The default list of columns may be extended if list is specified in the format +list (e.g., lscpu -p=+MHZ).</dl>
<p> <code>-s</code>, <code>&#8211;sysroot</code> <i>directory</i></p>
<dl>
<dt>
<dd> Gather CPU data for a Linux instance other than the instance from which the <code>lscpu</code> command is issued. The specified <i>directory</i> is the system root of the Linux instance to be inspected.</dl>
<p> <code>-x</code>, <code>&#8211;hex</code></p>
<dl>
<dt>
<dd> Use hexadecimal masks for CPU sets (for example &quot;ff&quot;). The default is to print the sets in list format (for example 0,1). Note that before version 2.30 the mask has been printed with 0x prefix.</dl>
<p> <code>-y</code>, <code>&#8211;physical</code></p>
<dl>
<dt>
<dd> Display physical IDs for all columns with topology elements (core, socket, etc.). Other than logical IDs, which are assigned by <code>lscpu</code>, physical IDs are platform-specific values that are provided by the kernel. Physical IDs are not necessarily unique and they might not be arranged sequentially. If the kernel could not retrieve a physical ID for an element <code>lscpu</code> prints the dash (-) character. </p>
<p> The CPU logical numbers are not affected by this option.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dt>
<dd> Output all available columns. This option must be combined with either <code>&#8211;extended</code>, <code>&#8211;parse</code> or <code>&#8211;caches</code>.</dl>
<h2>BUGS</h2>
<p> The basic overview of CPU family, model, etc. is always based on the first CPU only. </p>
<p> Sometimes in Xen Dom0 the kernel reports wrong data. </p>
<p> On virtual hardware the number of cores per socket, etc. can be wrong.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-chcpu/">chcpu</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>lscpu</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
