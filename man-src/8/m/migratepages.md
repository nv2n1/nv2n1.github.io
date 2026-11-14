---
title: "migratepages(8)"
name: "migratepages"
section: "8"
letter: "m"
url: "/docs/linux/man/8-migratepages/"
description: "migratepages – Migrate the physical location a processes pages"
---

<p>migratepages &#8211; Migrate the physical location a processes pages</p>
<h2>Synopsis</h2>
<p><code>migratepages</code> pid from-nodes to-nodes</p>
<h2>Description</h2>
<p><code>migratepages</code> moves the physical location of a processes pages without any changes of the virtual address space of the process. Moving the pages allows one to change the distances of a process to its memory. Performance may be optimized by moving a processes pages to the node where it is executing. </p>
<p> If multiple nodes are specified for from-nodes or to-nodes then an attempt is made to preserve the relative location of each page in each nodeset. </p>
<p> For example if we move from nodes 2-5 to 7,9,12-13 then the preferred mode of operation is to move pages from 2-&gt;7, 3-&gt;9, 4-&gt;12 and 5-&gt;13. However, this is only posssible if enough memory is available.</p>
<dl>
<dt>Valid node specifiers</p>
<dd>
<table>
<tr VALIGN=top>
<td>all</td>
<td>All nodes
</td>
</tr>
<tr VALIGN=top>
<td>number</td>
<td>Node number
</td>
</tr>
<tr VALIGN=top>
<td>number1{,number2}</td>
<td>Node number1 and Node number2
</td>
</tr>
<tr VALIGN=top>
<td>number1-number2</td>
<td>Nodes from number1 to number2
</td>
</tr>
<tr VALIGN=top>
<td>! nodes</td>
<td>Invert selection of the following specification.
</td>
</tr>
</table>
</dl>
<h2>Notes</h2>
<p>Requires an NUMA policy aware kernel with support for page migration (linux 2.6.16 and later). migratepages will only move pages that are not shared with other processes if called by a user without administrative priviledges (but with the right to modify the process). migratepages will move all pages if invoked from root (or a user with administrative priviledges). </p>
<h2>Files</h2>
<p><i>/proc/&lt;pid&gt;/numa_maps</i> for information about the NUMA memory use of a process.</p>
<h2>Copyright</h2>
<p>Copyright 2005-2006 Christoph Lameter, Silicon Graphics, Inc. migratepages is under the GNU General Public License, v.2</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-numactl/">numactl</a>(8)</i> , <i><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a>(2)</i> , <i><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a>(2)</i> , <i><a href="/docs/linux/man/2-mbind/">mbind</a>(2)</i> , <i><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a>(2)</i> , <i><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a>(2)</i> , <i><a href="/docs/linux/man/5-proc/">proc</a>(5)</i> , <i><a href="/docs/linux/man/3-ftok/">ftok</a>(3)</i> , <i><a href="/docs/linux/man/2-shmat/">shmat</a>(2)</i> , <i><a href="/docs/linux/man/1-taskset/">taskset</a>(1)</i> </p>
