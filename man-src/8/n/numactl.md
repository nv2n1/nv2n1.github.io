---
title: "numactl(8)"
name: "numactl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-numactl/"
description: "numactl – Control NUMA policy for processes or shared memory"
---

<p>numactl &#8211; Control NUMA policy for processes or shared memory</p>
<h2>Synopsis</h2>
<p><code>numactl</code> [ <code>&#8211;all</code> ] [ <code>&#8211;interleave nodes</code> ] [ <code>&#8211;preferred node </code> ] [ <code>&#8211;membind nodes</code> ] [ <code>&#8211;cpunodebind nodes</code> ] [ <code>&#8211;physcpubind cpus</code> ] [ <code>&#8211;localalloc</code> ] [&#8211;] command {arguments &#8230;}<br />
 <code>numactl &#8211;show</code><br />
 <code>numactl &#8211;hardware</code><br />
 <code>numactl </code> [ <code>&#8211;huge</code> ] [ <code>&#8211;offset offset</code> ] [ <code>&#8211;shmmode shmmode</code> ] [ <code>&#8211;length length</code> ] [ <code>&#8211;strict</code> ]<br />
 [ <code>&#8211;shmid id</code> ] <code>&#8211;shm shmkeyfile</code> | <code>&#8211;file tmpfsfile</code><br />
 [ <code>&#8211;touch</code> ] [ <code>&#8211;dump</code> ] [ <code>&#8211;dump-nodes</code> ] memory policy</p>
<h2>Description</h2>
<p><code>numactl</code> runs processes with a specific NUMA scheduling or memory placement policy. The policy is set for command and inherited by all of its children. In addition it can set persistent policy for shared memory segments or files. </p>
<p> Use &#8212; before command if using command options that could be confused with numactl options. </p>
<p> <i>nodes</i> may be specified as N,N,N or N-N or N,N-N or N-N,N-N and so forth. Relative <i>nodes</i> may be specifed as +N,N,N or +N-N or +N,N-N and so forth. The + indicates that the node numbers are relative to the process&#8217; set of allowed nodes in its current cpuset. A !N-N notation indicates the inverse of N-N, in other words all nodes except N-N. If used with + notation, specify !+N-N. When <i>same</i> is specified the previous nodemask specified on the command line is used. all means all nodes in the current cpuset. </p>
<p> Instead of a number a node can also be: </p>
<table>
<tr VALIGN=top>
<td>netdev:DEV</td>
<td>The node connected to network device DEV.
</td>
</tr>
<tr VALIGN=top>
<td>file:PATH </td>
<td>The node the block device of PATH.
</td>
</tr>
<tr VALIGN=top>
<td>ip:HOST </td>
<td>The node of the network device of HOST
</td>
</tr>
<tr VALIGN=top>
<td>block:PATH</td>
<td>The node of block device PATH
</td>
</tr>
<tr VALIGN=top>
<td>pci:[seg:]bus:dev[:func]</td>
<td>The node of a PCI device.
</td>
</tr>
</table>
<p> Note that block resolves the kernel block device names only for udev names in /dev use <i>file:</i></p>
<dl>
<dt>Policy settings are:</p>
<dd>
<dt><code>&#8211;all, -a</code></p>
<dd>Unset default cpuset awareness, so user can use all possible CPUs/nodes for following policy settings.</p>
<dt><code>&#8211;interleave=nodes, -i nodes</code></p>
<dd>Set a memory interleave policy. Memory will be allocated using round robin on <i>nodes.</i> When memory cannot be allocated on the current interleave target fall back to other nodes. Multiple nodes may be specified on &#8211;interleave, &#8211;membind and &#8211;cpunodebind.</p>
<dt><code>&#8211;membind=nodes, -m nodes</code></p>
<dd>Only allocate memory from nodes. Allocation will fail when there is not enough memory available on these nodes. <i>nodes</i> may be specified as noted above.</p>
<dt><code>&#8211;cpunodebind=nodes, -N nodes</code></p>
<dd>Only execute <i>command</i> on the CPUs of <i>nodes. </i> Note that nodes may consist of multiple CPUs. <i>nodes</i> may be specified as noted above.</p>
<dt><code>&#8211;physcpubind=cpus, -C cpus</code></p>
<dd>Only execute <i>process</i> on <i>cpus.</i> This accepts cpu numbers as shown in the <i>processor</i> fields of <i>/proc/cpuinfo,</i> or relative cpus as in relative to the current cpuset. You may specify &quot;all&quot;, which means all cpus in the current cpuset. Physical <i>cpus</i> may be specified as N,N,N or N-N or N,N-N or N-N,N-N and so forth. Relative <i>cpus</i> may be specifed as +N,N,N or +N-N or +N,N-N and so forth. The + indicates that the cpu numbers are relative to the process&#8217; set of allowed cpus in its current cpuset. A !N-N notation indicates the inverse of N-N, in other words all cpus except N-N. If used with + notation, specify !+N-N.</p>
<dt><code>&#8211;localalloc, -l </code></p>
<dd>Falls back to the system default which is local allocation by using <i>MPOL_DEFAULT</i> policy. See <i><a href="/docs/linux/man/2-mbind/">mbind</a>(2)</i> for details.</p>
<dt><code>&#8211;preferred=node</code></p>
<dd>Preferably allocate memory on <i>node,</i> but if memory cannot be allocated there fall back to other nodes. This option takes only a single node number. Relative notation may be used.</p>
<dt><code>&#8211;show, -s</code></p>
<dd>Show NUMA policy settings of the current process.</p>
<dt><code>&#8211;hardware, -H</code></p>
<dd>Show inventory of available nodes on the system.</p>
<dt>Numactl can set up policy for a SYSV shared memory segment or a file in shmfs/hugetlbfs.</p>
<dd>&nbsp;<wbr> This policy is persistent and will be used by all mappings from that shared memory. The order of options matters here. The specification must at least include either of <i>&#8211;shm, </i> <i>&#8211;shmid, </i> <i>&#8211;file</i> to specify the shared memory segment or file and a memory policy like described above ( <i>&#8211;interleave, </i> <i>&#8211;localalloc, </i> <i>&#8211;preferred,</i> <i>&#8211;membind</i> ).</p>
<dt><code>&#8211;huge</code></p>
<dd>When creating a SYSV shared memory segment use huge pages. Only valid before &#8211;shmid or &#8211;shm</p>
<dt><code>&#8211;offset</code></p>
<dd>Specify offset into the shared memory segment. Default 0. Valid units are <i>m</i> (for MB), <i>g </i> (for GB), <i>k </i> (for KB), otherwise it specifies bytes.</p>
<dt><code>&#8211;strict</code></p>
<dd>Give an error when a page in the policied area in the shared memory segment already was faulted in with a conflicting policy. Default is to silently ignore this.</p>
<dt><code>&#8211;shmmode shmmode</code></p>
<dd>Only valid before &#8211;shmid or &#8211;shm When creating a shared memory segment set it to numeric mode <i>shmmode.</i></p>
<dt><code>&#8211;length length</code></p>
<dd>Apply policy to <i>length </i> range in the shared memory segment or make the segment length long Default is to use the remaining length Required when a shared memory segment is created and specifies the length of the new segment then. Valid units are <i>m</i> (for MB), <i>g </i> (for GB), <i>k </i> (for KB), otherwise it specifies bytes.</p>
<dt><code>&#8211;shmid id</code></p>
<dd>Create or use an shared memory segment with numeric ID <i>id</i></p>
<dt><code>&#8211;shm shmkeyfile</code></p>
<dd>Create or use an shared memory segment, with the ID generated using <i><a href="/docs/linux/man/3-ftok/">ftok</a>(3) </i> from shmkeyfile</p>
<dt><code>&#8211;file tmpfsfile</code></p>
<dd>Set policy for a file in tmpfs or hugetlbfs</p>
<dt><code>&#8211;touch</code></p>
<dd>Touch pages to enforce policy early. Default is to not touch them, the policy is applied when an applications maps and accesses a page.</p>
<dt><code>&#8211;dump</code></p>
<dd>Dump policy in the specified range.</p>
<dt><code>&#8211;dump-nodes</code></p>
<dd>Dump all nodes of the specific range (very verbose!)</p>
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
<h2>Examples</h2>
<p>numactl &#8211;physcpubind=+0-4,8-12 myapplic arguments Run myapplic on cpus 0-4 and 8-12 of the current cpuset. </p>
<p> numactl &#8211;interleave=all bigdatabase arguments Run big database with its memory interleaved on all CPUs. </p>
<p> numactl &#8211;cpunodebind=0 &#8211;membind=0,1 process Run process on node 0 with memory allocated on node 0 and 1. </p>
<p> numactl &#8211;cpunodebind=0 &#8211;membind=0,1 &#8212; process -l Run process as above, but with an option (-l) that would be confused with a numactl option. </p>
<p> numactl &#8211;cpunodebind=netdev:eth0 &#8211;membind=netdev:eth0 network-server Run network-server on the node of network device eth0 with its memory also in the same node. </p>
<p> numactl &#8211;preferred=1 numactl &#8211;show Set preferred node 1 and show the resulting state. </p>
<p> numactl &#8211;interleave=all &#8211;shm /tmp/shmkey Interleave all of the sysv shared memory region specified by /tmp/shmkey over all nodes. </p>
<p> Place a tmpfs file on 2 nodes:<br />
&nbsp;<wbr>&nbsp;<wbr>numactl &#8211;membind=2 dd if=/dev/zero of=/dev/shm/A bs=1M count=1024<br />
&nbsp;<wbr>&nbsp;<wbr>numactl &#8211;membind=3 dd if=/dev/zero of=/dev/shm/A seek=1024 bs=1M count=1024 </p>
<p> numactl &#8211;localalloc /dev/shm/file Reset the policy for the shared memory file <i>file</i> to the default localalloc policy.</p>
<h2>Notes</h2>
<p>Requires an NUMA policy aware kernel. Command is not executed using a shell. If you want to use shell metacharacters in the child use sh -c as wrapper. Setting policy for a hugetlbfs file does currently not work because it cannot be extended by truncate. Shared memory segments larger than numactl&#8217;s address space cannot be completely policied. This could be a problem on 32bit architectures. Changing it piece by piece may work. The old <i>&#8211;cpubind</i> which accepts node numbers, not cpu numbers, is deprecated and replaced with the new <i>&#8211;cpunodebind</i> and <i>&#8211;physcpubind</i> options. </p>
<h2>Files</h2>
<p><i>/proc/cpuinfo</i> for the listing of active CPUs. See <i><a href="/docs/linux/man/5-proc/">proc</a>(5)</i> for details. </p>
<p> <i>/sys/devices/system/node/node*/numastat</i> for NUMA memory hit statistics.</p>
<h2>Copyright</h2>
<p>Copyright 2002,2004 Andi Kleen, SuSE Labs. numactl and the demo programs are under the GNU General Public License, v.2</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a>(2)</i> , <i><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a>(2)</i> , <i><a href="/docs/linux/man/2-mbind/">mbind</a>(2)</i> , <i><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a>(2)</i> , <i><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a>(2)</i> , <i><a href="/docs/linux/man/5-proc/">proc</a>(5)</i> , <i><a href="/docs/linux/man/3-ftok/">ftok</a>(3)</i> , <i><a href="/docs/linux/man/2-shmat/">shmat</a>(2)</i> , <i><a href="/docs/linux/man/8-migratepages/">migratepages</a>(8)</i> </p>
