---
title: "numa_maps(5)"
name: "numa_maps"
section: "5"
letter: "n"
url: "/docs/linux/man/5-numa_maps/"
description: "numa – overview of Non-Uniform Memory Architecture"
---

<p>numa &#8211; overview of Non-Uniform Memory Architecture</p>
<h2>Description</h2>
<p>Non-Uniform Memory Access (NUMA) refers to multiprocessor systems whose memory is divided into multiple memory nodes. The access time of a memory node depends on the relative locations of the accessing CPU and the accessed node. (This contrasts with a symmetric multiprocessor system, where the access time for all of the memory is the same for all CPUs.) Normally, each CPU on a NUMA system has a local memory node whose contents can be accessed faster than the memory in the node local to another CPU or the memory on a bus shared by all CPUs.</p>
<h3>NUMA system calls</h3>
<p>The Linux kernel implements the following NUMA-related system calls: <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-migrate_pages/">migrate_pages</a></code>(2), <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2), and <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). However, applications should normally use the interface provided by <i>libnuma</i>; see &quot;Library Support&quot; below.</p>
<h3>/proc/[number]/numa_maps (since Linux 2.6.14)</h3>
<p>This file displays information about a process&#8217;s NUMA memory policy and allocation. </p>
<p> Each line contains information about a memory range used by the process, displaying&#8212;among other information&#8212;the effective memory policy for that memory range and on which nodes the pages have been allocated. </p>
<p> <i>numa_maps</i> is a read-only file. When <i>/proc/&lt;pid&gt;/numa_maps</i> is read, the kernel will scan the virtual address space of the process and report how memory is used. One line is displayed for each unique memory range of the process. </p>
<p> The first field of each line shows the starting address of the memory range. This field allows a correlation with the contents of the <i>/proc/&lt;pid&gt;/maps</i> file, which contains the end address of the range and other information, such as the access permissions and sharing. </p>
<p> The second field shows the memory policy currently in effect for the memory range. Note that the effective policy is not necessarily the policy installed by the process for that memory range. Specifically, if the process installed a &quot;default&quot; policy for that range, the effective policy for that range will be the process policy, which may or may not be &quot;default&quot;. </p>
<p> The rest of the line contains information about the pages allocated in the memory range, as follows:</p>
<dl>
<dt><i>N&lt;node&gt;=&lt;nr_pages&gt;</i></p>
<dd>The number of pages allocated on <i>&lt;node&gt;</i>. <i>&lt;nr_pages&gt;</i> includes only pages currently mapped by the process. Page migration and memory reclaim may have temporarily unmapped pages associated with this memory range. These pages may show up again only after the process has attempted to reference them. If the memory range represents a shared memory area or file mapping, other processes may currently have additional pages mapped in a corresponding memory range.</p>
<dt><i>file=&lt;filename&gt;</i></p>
<dd>The file backing the memory range. If the file is mapped as private, write accesses may have generated COW (Copy-On-Write) pages in this memory range. These pages are displayed as anonymous pages.</p>
<dt><i>heap</i></p>
<dd>Memory range is used for the heap.</p>
<dt><i>stack</i></p>
<dd>Memory range is used for the stack.</p>
<dt><i>huge</i></p>
<dd>Huge memory range. The page counts shown are huge pages and not regular sized pages.</p>
<dt><i>anon=&lt;pages&gt;</i></p>
<dd>The number of anonymous page in the range.</p>
<dt><i>dirty=&lt;pages&gt;</i></p>
<dd>Number of dirty pages.</p>
<dt><i>mapped=&lt;pages&gt;</i></p>
<dd>Total number of mapped pages, if different from <i>dirty</i> and <i>anon</i> pages.</p>
<dt><i>mapmax=&lt;count&gt;</i></p>
<dd>Maximum mapcount (number of processes mapping a single page) encountered during the scan. This may be used as an indicator of the degree of sharing occurring in a given memory range.</p>
<dt><i>swapcache=&lt;count&gt;</i></p>
<dd>Number of pages that have an associated entry on a swap device.</p>
<dt><i>active=&lt;pages&gt;</i></p>
<dd>The number of pages on the active list. This field is shown only if different from the number of pages in this range. This means that some inactive pages exist in the memory range that may be removed from memory by the swapper soon.</p>
<dt><i>writeback=&lt;pages&gt;</i></p>
<dd>Number of pages that are currently being written out to disk.</dl>
<h2>Conforming To</h2>
<p>No standards govern NUMA interfaces.</p>
<h2>Notes</h2>
<p>The Linux NUMA system calls and <i>/proc</i> interface are available only if the kernel was configured and built with the <code>CONFIG_NUMA</code> option.</p>
<h3>Library support</h3>
<p>Link with <i>-lnuma</i> to get the system call definitions. <i>libnuma</i> and the required <i>&lt;numaif.h&gt;</i> header are available in the <i>numactl</i> package. </p>
<p> However, applications should not use these system calls directly. Instead, the higher level interface provided by the <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) functions in the <i>numactl</i> package is recommended. The <i>numactl</i> package is available at The package is also included in some Linux distributions. Some distributions include the development library and header in the separate <i>numactl-devel</i> package.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.05 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
