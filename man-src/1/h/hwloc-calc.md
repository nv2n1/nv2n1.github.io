---
title: "hwloc-calc(1)"
name: "hwloc-calc"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-calc/"
description: "hwloc-calc – Operate on cpu mask strings and objects"
---

<h2>NAME</h2>
<p> hwloc-calc &#8211; Operate on cpu mask strings and objects</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-calc</code> [<i>options</i>] <i>&lt;location1&gt; [&lt;location2&gt; [&#8230;] ] </p>
<p> Note that <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) provides a detailed explanation of the hwloc system and of valid &lt;location&gt; formats; it should be read before reading this man page. </i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> Use OS/physical indexes instead of logical indexes for both input and output.</p>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> Use logical indexes instead of physical/OS indexes for both input and output (default).</p>
<dt><code>&#8211;pi</code> <code>&#8211;physical-input</code></p>
<dd> Use OS/physical indexes instead of logical indexes for input.</p>
<dt><code>&#8211;li</code> <code>&#8211;logical-input</code></p>
<dd> Use logical indexes instead of physical/OS indexes for input (default).</p>
<dt><code>&#8211;po</code> <code>&#8211;physical-output</code></p>
<dd> Use OS/physical indexes instead of logical indexes for output.</p>
<dt><code>&#8211;lo</code> <code>&#8211;logical-output</code></p>
<dd> Use logical indexes instead of physical/OS indexes for output (default, except for cpusets which are always physical).</p>
<dt><code>-N &#8211;number-of &lt;type|depth&gt;</code></p>
<dd> Report the number of objects of the given type or depth that intersect the CPU set. This is convenient for finding how many cores, NUMA nodes or PUs are available in a machine.</p>
<dt><code>-I &#8211;intersect &lt;type|depth&gt;</code></p>
<dd> Find the list of objects of the given type or depth that intersect the CPU set and report the comma-separated list of their indexes instead of the cpu mask string. This may be used for determining the list of objects above or below the input objects. When combined with <code>&#8211;physical</code>, the list is convenient to pass to external tools such as taskset or numactl <code>&#8211;physcpubind</code> or <code>&#8211;membind</code>. This is different from &#8211;largest since the latter requires that all reported objects are strictly included inside the input objects.</p>
<dt><code>-H &#8211;hierarchical &lt;type1&gt;.&lt;type2&gt;&#8230;</code></p>
<dd> Find the list of objects of type &lt;type2&gt; that intersect the CPU set and report the space-separated list of their hierarchical indexes with respect to &lt;type1&gt;, &lt;type2&gt;, etc. For instance, if <i>package.core</i> is given, the output would be <i>Package:1.Core:2 Package:2.Core:3</i> if the input contains the third core of the second package and the fourth core of the third package.</p>
<dt><code>&#8211;largest</code></p>
<dd> Report (in a human readable format) the list of largest objects which exactly include all input objects. None of these output objects intersect each other, and the sum of them is exactly equivalent to the input. No largest object is included in the input This is different from &#8211;intersect where reported objects may not be strictly included in the input.</p>
<dt><code>&#8211;sep &lt;sep&gt;</code></p>
<dd> Change the field separator in the output. By default, a space is used to separate output objects (for instance when <code>&#8211;hierarchical</code> or <code>&#8211;largest</code> is given) while a comma is used to separate indexes (for instance when <code>&#8211;intersect</code> is given).</p>
<dt><code>&#8211;single</code></p>
<dd> Singlify the output to a single CPU.</p>
<dt><code>&#8211;taskset</code></p>
<dd> Display CPU set strings in the format recognized by the taskset command-line program instead of hwloc-specific CPU set string format. This option has no impact on the format of input CPU set strings, both formats are always accepted.</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>-i</code> &lt;file&gt;, <code>&#8211;input</code> &lt;file&gt;</p>
<dd> Read topology from XML file &lt;file&gt; (instead of discovering the topology on the local machine). If &lt;file&gt; is &quot;-&quot;, the standard input is used. XML support must have been compiled in to hwloc for this option to be usable.</p>
<dt><code>-i</code> &lt;directory&gt;, <code>&#8211;input</code> &lt;directory&gt;</p>
<dd> Read topology from the chroot specified by &lt;directory&gt; (instead of discovering the topology on the local machine). This option is generally only available on Linux. The chroot was usually created by gathering another machine topology with hwloc-gather-topology.</p>
<dt><code>-i</code> &lt;specification&gt;, <code>&#8211;input</code> &lt;specification&gt;</p>
<dd> Simulate a fake hierarchy (instead of discovering the topology on the local machine). If &lt;specification&gt; is &quot;node:2 pu:3&quot;, the topology will contain two NUMA nodes with 3 processing units in each of them. The &lt;specification&gt; string must end with a number of PUs.</p>
<dt><code>&#8211;if</code> &lt;format&gt;, <code>&#8211;input-format</code> &lt;format&gt;</p>
<dd> Enforce the input in the given format, among <code>xml</code>, <code>fsroot</code> and <code>synthetic</code>.</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Hide non-fatal error messages. It mostly includes locations pointing to non-existing objects.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Verbose output.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-calc generates and manipulates CPU mask strings or objects. Both input and output may be either objects (with physical or logical indexes), CPU lists (with physical or logical indexes), or CPU mask strings (always physically indexed). </p>
<p> If objects or CPU mask strings are given on the command-line, they are combined and a single output is printed. If no object or CPU mask strings are given on the command-line, the program will read the standard input. It will combine multiple objects or CPU mask strings that are given on the same line of the standard input line with spaces as separators. Different input lines will be processed separately. </p>
<p> Command-line arguments and options are processed in order. For instance, it means that changing the type of input indexes with <code>&#8211;li</code> or changing the input topology with <code>-i</code> only affects the processing the following arguments. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-calc utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-calc&#8217;s operation is best described through several examples. </p>
<p> To display the (physical) CPU mask corresponding to the second package: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc package:1<br />
&nbsp;<wbr>0x000000f0 </p>
<p> To display the (physical) CPU mask corresponding to the third pacakge, excluding its even numbered logical processors: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc package:2&nbsp;<wbr>~PU:even<br />
&nbsp;<wbr>0x00000c00 </p>
<p> To combine two (physical) CPU masks: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc 0x0000ffff 0xff000000<br />
&nbsp;<wbr>0xff00ffff </p>
<p> To display the list of logical numbers of processors included in the second package: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc &#8211;intersect PU package:1<br />
&nbsp;<wbr>4,5,6,7 </p>
<p> To bind GNU OpenMP threads logically over the whole machine, we need to use physical number output instead: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>export GOMP_CPU_AFFINITY=`hwloc-calc &#8211;physical-output &#8211;intersect PU machine:0`<br />
&nbsp;<wbr>$&nbsp;<wbr>echo&nbsp;<wbr>$GOMP_CPU_AFFINITY<br />
&nbsp;<wbr>0,4,1,5,2,6,3,7 </p>
<p> To display the list of NUMA nodes, by physical indexes, that intersect a given (physical) CPU mask: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc &#8211;physical &#8211;intersect NUMAnode 0xf0f0f0f0<br />
&nbsp;<wbr>0,2 </p>
<p> To display the physical index of a processor given by its logical index: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc PU:2 &#8211;physical-output &#8211;intersect PU<br />
&nbsp;<wbr>3 </p>
<p> To display the set of CPUs near network interface eth0: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc os=eth0<br />
&nbsp;<wbr>0x00005555 </p>
<p> To display the indexes of packages near PCI device whose bus ID is 0000:01:02.0: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc pci=0000:01:02.0 &#8211;intersect Package<br />
&nbsp;<wbr>1 </p>
<p> To display the list of per-package cores that intersect the input: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc 0x00003c00 &#8211;hierarchical package.core<br />
&nbsp;<wbr>Package:2.Core:1 Package:3.Core:0 </p>
<p> To display the (physical) CPU mask of the entire topology except the third package: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc all&nbsp;<wbr>~package:3<br />
&nbsp;<wbr>0x0000f0ff </p>
<p> To combine both physical and logical indexes as input: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc PU:2 &#8211;physical-input PU:3<br />
&nbsp;<wbr>0x0000000c </p>
<p> To synthetize a set of cores into largest objects on a 2-node 2-package 2-core machine: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc core:0 &#8211;largest<br />
&nbsp;<wbr>Core:0<br />
&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc core:0-1 &#8211;largest<br />
&nbsp;<wbr>Package:0<br />
&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc core:4-7 &#8211;largest<br />
&nbsp;<wbr>NUMANode:1<br />
&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc core:2-6 &#8211;largest<br />
&nbsp;<wbr>Package:1 Package:2 Core:6<br />
&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc pack:2 &#8211;largest<br />
&nbsp;<wbr>Package:2<br />
&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc package:2-3 &#8211;largest<br />
&nbsp;<wbr>NUMANode:1 </p>
<p> To get the set of first threads of all cores: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-calc core:all.pu:0 </p>
<p> This can also be very useful in order to make GNU OpenMP use exactly one thread per core, and in logical core order: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>export OMP_NUM_THREADS=`hwloc-calc &#8211;number-of core machine:0`<br />
&nbsp;<wbr>$&nbsp;<wbr>echo&nbsp;<wbr>$OMP_NUM_THREADS<br />
&nbsp;<wbr>4<br />
&nbsp;<wbr>$&nbsp;<wbr>export GOMP_CPU_AFFINITY=`hwloc-calc &#8211;physical-output &#8211;intersect PU core:all.pu:0`<br />
&nbsp;<wbr>$&nbsp;<wbr>echo&nbsp;<wbr>$GOMP_CPU_AFFINITY<br />
&nbsp;<wbr>0,2,1,3 </p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-calc displays the (physical) CPU mask string, (physical or logical) object list, or (physical or logical) object number list. The return value is 0. </p>
<p> hwloc-calc will return nonzero if any kind of error occurs, such as (but not limited to): failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-info/">hwloc-info</a>(1), <a href="/docs/linux/man/1-hwloc-gather-topology/">hwloc-gather-topology</a>(1) </p>
<h2>Index</h2>
