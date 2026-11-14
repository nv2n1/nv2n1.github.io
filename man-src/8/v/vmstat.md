---
title: "vmstat(8)"
name: "vmstat"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vmstat/"
description: "vmstat – Report virtual memory statistics"
---

<p>vmstat &#8211; Report virtual memory statistics</p>
<h2>Synopsis</h2>
<p><code>vmstat</code> [options] [<i>delay</i> [<i>count</i>]]</p>
<h2>Description</h2>
<p><code>vmstat</code> reports information about processes, memory, paging, block IO, traps, disks and cpu activity. </p>
<p> The first report produced gives averages since the last reboot. Additional reports give information on a sampling period of length <i>delay</i>. The process and memory reports are instantaneous in either case.</p>
<h2>Options</h2>
<dl>
<dt><i>delay</i></p>
<dd>The <i>delay</i> between updates in seconds. If no <i>delay</i> is specified, only one report is printed with the average values since boot.</p>
<dt><i>count</i></p>
<dd>Number of updates. In absence of <i>count</i>, when <i>delay</i> is defined, default is infinite.</p>
<dt><code>-a</code>, <code>&#8211;active</code></p>
<dd>Display active and inactive memory, given a 2.5.41 kernel or better.</p>
<dt><code>-f</code>, <code>&#8211;forks</code></p>
<dd>The <code>-f</code> switch displays the number of forks since boot. This includes the fork, vfork, and clone system calls, and is equivalent to the total number of tasks created. Each process is represented by one or more tasks, depending on thread usage. This display does not repeat.</p>
<dt><code>-m</code>, <code>&#8211;slabs</code></p>
<dd>Displays slabinfo.</p>
<dt><code>-n</code>, <code>&#8211;one-header</code></p>
<dd>Display the header only once rather than periodically.</p>
<dt><code>-s</code>, <code>&#8211;stats</code></p>
<dd>Displays a table of various event counters and memory statistics. This display does not repeat.</p>
<dt><code>-d</code>, <code>&#8211;disk</code></p>
<dd>Report disk statistics (2.5.70 or above required).</p>
<dt><code>-D</code>, <code>&#8211;disk-sum</code></p>
<dd>Report some summary statistics about disk activity.</p>
<dt><code>-p</code>, <code>&#8211;partition</code> <i>device</i></p>
<dd>Detailed statistics about partition (2.5.70 or above required).</p>
<dt><code>-S</code>, <code>&#8211;unit</code> <i>character</i></p>
<dd>Switches outputs between 1000 (<i>k</i>), 1024 (<i>K</i>), 1000000 (<i>m</i>), or 1048576 (<i>M</i>) bytes. Note this does not change the block (bi/bo) fields, which are always measured in blocks.</p>
<dt><code>-t</code>, <code>&#8211;timestamp</code></p>
<dd>Append timestamp to each line</p>
<dt><code>-w</code>, <code>&#8211;wide</code></p>
<dd>Wide output mode (useful for systems with higher amount of memory, where the default output mode suffers from unwanted column breakage). The output is wider than 80 characters per line.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help and exit.</dl>
<h2>Field Description For Vm Mode</h2>
<h3><code>Procs</code></h3>
<pre>r: The number of runnable processes (running or waiting for run time).
b: The number of processes blocked waiting for I/O to complete.</pre>
<h3><code>Memory</code></h3>
<p>These are affected by the <code>&#8211;unit</code> option. </p>
<pre>swpd: the amount of swap memory used.
free: the amount of idle memory.
buff: the amount of memory used as buffers.
cache: the amount of memory used as cache.
inact: the amount of inactive memory. (<code>-a</code> option)
active: the amount of active memory. (<code>-a</code> option)</pre>
<h3><code>Swap</code></h3>
<p>These are affected by the <code>&#8211;unit</code> option. </p>
<pre>si: Amount of memory swapped in from disk (/s).
so: Amount of memory swapped to disk (/s).</pre>
<h3><code>IO</code></h3>
<pre>bi: Blocks received from a block device (blocks/s).
bo: Blocks sent to a block device (blocks/s).</pre>
<h3><code>System</code></h3>
<pre>in: The number of interrupts per second, including the clock.
cs: The number of context switches per second.</pre>
<h3><code>CPU</code></h3>
<p>These are percentages of total CPU time. </p>
<pre>us: Time spent running non-kernel code. (user time, including nice time)
sy: Time spent running kernel code. (system time)
id: Time spent idle. Prior to Linux 2.5.41, this includes IO-wait time.
wa: Time spent waiting for IO. Prior to Linux 2.5.41, included in idle.
st: Time stolen from a virtual machine. Prior to Linux 2.6.11, unknown.</pre>
<h2>Field Description For Disk Mode</h2>
<h3><code>Reads</code></h3>
<pre>total: Total reads completed successfully
merged: grouped reads (resulting in one I/O)
sectors: Sectors read successfully
ms: milliseconds spent reading</pre>
<h3><code>Writes</code></h3>
<pre>total: Total writes completed successfully
merged: grouped writes (resulting in one I/O)
sectors: Sectors written successfully
ms: milliseconds spent writing</pre>
<h3><code>IO</code></h3>
<pre>cur: I/O in progress
s: seconds spent for I/O</pre>
<h2>Field Description For Disk Partition Mode</h2>
<pre>reads: Total number of reads issued to this partition
read sectors: Total read sectors for partition
writes : Total number of writes issued to this partition
requested writes: Total number of write requests made for partition</pre>
<h2>Field Description For Slab Mode</h2>
<pre>cache: Cache name
num: Number of currently active objects
total: Total number of available objects
size: Size of each object
pages: Number of pages with at least one active object</pre>
<h2>Notes</h2>
<p><code>vmstat</code> does not require special permissions. </p>
<p> These reports are intended to help identify system bottlenecks. Linux <code>vmstat</code> does not count itself as a running process. </p>
<p> All linux blocks are currently 1024 bytes. Old kernels may report blocks as 512 bytes, 2048 bytes, or 4096 bytes. </p>
<p> Since procps 3.1.9, vmstat lets you choose units (k, K, m, M). Default is K (1024 bytes) in the default mode. </p>
<p> vmstat uses slabinfo 1.1</p>
<h2>Files</h2>
<pre>/proc/meminfo
/proc/stat
/proc/*/stat</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/1-mpstat/">mpstat</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1) </p>
<h2>Bugs</h2>
<p>Does not tabulate the block io per device or count the number of system calls.</p>
<h2>Authors</h2>
<p>Written by Henry Ware<br />
 Fabian Fr&eacute;d&eacute;rick (diskstat, slab, partitions&#8230;)</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
