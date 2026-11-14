---
title: "hwloc_linux_parse_cpumap_file(3)"
name: "hwloc_linux_parse_cpumap_file"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_linux_parse_cpumap_file/"
description: "hwlocality_linux – Linux-specific helpers"
---

<h2 class="name">NAME</h2>
<p> hwlocality_linux &#8211; Linux-specific helpers </p>
<h3>Functions</h3>
<p> int <code>hwloc_linux_parse_cpumap_file</code> (FILE *file, <code>hwloc_cpuset_t</code> set) </p>
<p> int <code>hwloc_linux_set_tid_cpubind</code> (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_const_cpuset_t</code> set) </p>
<p> int <code>hwloc_linux_get_tid_cpubind</code> (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_cpuset_t</code> set) </p>
<p> int <code>hwloc_linux_get_tid_last_cpu_location</code> (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_bitmap_t</code> set) </p>
<h2>Detailed Description</h2>
<p> This includes helpers for manipulating Linux kernel cpumap files, and hwloc equivalents of the Linux sched_setaffinity and sched_getaffinity system calls.</p>
<h2>Function Documentation</h2>
<h3>int hwloc_linux_get_tid_cpubind (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_cpuset_t</code> set)</h3>
<p> Get the current binding of thread tid. The behavior is exactly the same as the Linux sched_getaffinity system call, but uses a hwloc cpuset. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is equivalent to calling <code>hwloc_get_proc_cpubind()</code> with <code>HWLOC_CPUBIND_THREAD</code> as flags.</dl>
<h3>int hwloc_linux_get_tid_last_cpu_location (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_bitmap_t</code> set)</h3>
<p> Get the last physical CPU where thread tid ran. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is equivalent to calling <code>hwloc_get_proc_last_cpu_location()</code> with <code>HWLOC_CPUBIND_THREAD</code> as flags.</dl>
<h3>int hwloc_linux_parse_cpumap_file (FILE * file, <code>hwloc_cpuset_t</code> set)</h3>
<p> Convert a linux kernel cpumap file file into hwloc CPU set. Might be used when reading CPU set from sysfs attributes such as topology and caches for processors, or local_cpus for devices.</p>
<h3>int hwloc_linux_set_tid_cpubind (<code>hwloc_topology_t</code> topology, pid_t tid, <code>hwloc_const_cpuset_t</code> set)</h3>
<p> Bind a thread tid on cpus given in cpuset set. The behavior is exactly the same as the Linux sched_setaffinity system call, but uses a hwloc cpuset. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is equivalent to calling <code>hwloc_set_proc_cpubind()</code> with HWLOC_CPUBIND_THREAD as flags.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
