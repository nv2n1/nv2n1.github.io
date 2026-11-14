---
title: "hwloc(7)"
name: "hwloc"
section: "7"
letter: "h"
url: "/docs/linux/man/7-hwloc/"
description: "hwloc – General information about hwloc (\"hardware locality\")."
---

<p>hwloc &#8211; General information about hwloc (&quot;hardware locality&quot;).</p>
<h2>Description</h2>
<p>hwloc provides command line tools and a C API to obtain the hierarchical map of key computing elements, such as: NUMA memory nodes, shared caches, processor packages, processor cores, and processor &quot;threads&quot;. hwloc also gathers various attributes such as cache and memory information, and is portable across a variety of different operating systems and platforms.</p>
<h3>Definitions</h3>
<p>Hwloc has some specific definitions for terms that are used in this man page and other hwloc documentation.</p>
<dl>
<dt><code>Hwloc CPU set:</code></p>
<dd>A set of processors included in an hwloc object, expressed as a bitmask indexed by the physical numbers of the CPUs (as announced by the OS). The hwloc definition of &quot;CPU set&quot; does not carry any the same connotations as Linux&#8217;s &quot;CPU set&quot; (e.g., process affinity, etc.).</p>
<dt><code>Linux CPU set:</code></p>
<dd>See <a rel="nofollow" href="http://www.mjmwired.net/kernel/Documentation/cpusets.txt">http://www.mjmwired.net/kernel/Documentation/cpusets.txt</a> for a discussion of Linux CPU sets. A super-short-ignoring-many-details description (taken from that page) is:</p>
<dd>&nbsp;<wbr>&quot;Cpusets provide a mechanism for assigning a set of CPUs and Memory Nodes to a set of tasks.&quot;</p>
<dt><code>Linux Cgroup:</code></p>
<dd>See <a rel="nofollow" href="http://www.mjmwired.net/kernel/Documentation/cgroups.txt">http://www.mjmwired.net/kernel/Documentation/cgroups.txt</a> for a discussion of Linux control groups. A super-short-ignoring-many-details description (taken from that page) is:</p>
<dt>
&nbsp;<wbr>&quot;Control Groups provide a mechanism for aggregating/partitioning sets</p>
<dd>of tasks, and all their future children, into hierarchical groups with specialized behaviour.&quot;</dl>
<p> To be clear, hwloc supports all of the above concepts. It is simply worth noting that they are 3 different things.</p>
<h3>Location Specification</h3>
<p>Locations refer to specific regions within a topology. Before reading the rest of this man page, it may be useful to read <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1) and/or run lstopo on your machine to see the reported topology tree. Seeing and understanding a topology tree will definitely help in understanding the concepts that are discussed below. </p>
<p> Locations can be specified in multiple ways:</p>
<dl>
<dt><code>Tuples:</code></p>
<dd>Tuples of hwloc &quot;objects&quot; and associated indexes can be specified in the form <i>object:index</i>. Hwloc objects represent types of mapped items (e.g., packages, cores, etc.) in a topology tree; indexes are non-negative integers that specify a unique physical object in a topology tree. Both concepts are described in detail, below.</p>
<dt>Chaining multiple tuples together in the more general form</p>
<dd><i>object1:index[.object2:index2[&#8230;]]</i> is permissable. While the first tuple&#8217;s object may appear anywhere in the topology, the Nth tuple&#8217;s object must have a shallower topology depth than the (N+1)th tuple&#8217;s object. Put simply: as you move right in a tuple chain, objects must go deeper in the topology tree. When using logical indexes (which is the default), indexes specified in chained tuples are relative to the scope of the parent object. For example, &quot;package:0.core:1&quot; refers to the second core in the first package. When using OS/physical indexes, the first object matching the given index is used.</p>
<dt><code>Hex:</code></p>
<dd>Locations can also be specified as hexidecimal bitmasks prefixed with &quot;0x&quot;. Commas must be used to separate the hex digits into blocks of 8, such as &quot;0xffc0140,0x00020110&quot;. Leading zeros in each block do not need to be specified. For example, &quot;0xffc0140,0x20110&quot; is equivalent to the prior example, and &quot;0x0000000f&quot; is exactly equivalent to &quot;0xf&quot;. Intermediate blocks of 8 digits that are all zeoro can be left empty; &quot;0xff0,,0x13&quot; is equivalent to &quot;0xff0,0x00000000,0x13&quot;. If the location is prefixed with the special string &quot;0xf&#8230;f&quot;, then all unspecified bits are set (as if the set were infinite). For example, &quot;0xf&#8230;f,0x1&quot; sets both the first bit and all bits starting with the 33rd. The string &quot;0xf&#8230;f&quot; &#8212; with no other specified values &#8212; sets all bits.</p>
<dt><code>I/O devices:</code></p>
<dd>Locations may also be a PCI or OS object. The corresponding value is the set of CPUs that are close to the physical device. For example, &quot;<code>pci=02:03.1</code>&quot; is equivalent to the set of processors that are close to the hostbridge above PCI device with bus ID &quot;02:03.1&quot;. &quot;<code>os=eth0</code>&quot; is equivalent to all processors close to the network interface whose software name is &quot;eth0&quot;.</dl>
<p> Multiple locations can be specified on the command lines (delimited by whitespace); the first token of the execution command is assumed to either follow &quot;&#8211;&quot; (if specified) or the first token that is unrecognized as a location. </p>
<p> By default, if multiple locations are specified, they are added, meaning that the binding will be wider in the sense that the process may run on more objects. </p>
<p> If prefixed with &quot;~&quot;, the given location will be cleared instead of added to the current list of locations. If prefixed with &quot;x&quot;, the given location will be and&#8217;ed instead of added to the current list. If prefixed with &quot;^&quot;, the given location will be xor&#8217;ed. </p>
<p> &quot;all&quot; and &quot;root&quot; are special locations consisting in the root object in tree. It contains the entire current topology. More complex operations may be performed by using <i>hwloc-calc</i> to compute intermediate values.</p>
<h3>Hwloc Objects</h3>
<p>Objects in tuples can be any of the following strings (listed from &quot;biggest&quot; to &quot;smallest&quot;):</p>
<dl>
<dt><code>machine</code></p>
<dd>A set of processors and memory.</p>
<dt><code>node</code></p>
<dd>A NUMA node; a set of processors around memory which the processors can directly access.</p>
<dt><code>package</code></p>
<dd>Typically a physical package or chip, that goes into a package, it is a grouping of one or more processors.</p>
<dt><code>cache</code></p>
<dd>A cache memory. If several kinds of caches exist in the system, a specific one may be identified by its level (e.g. <code>l1cache</code>) and optionally by its type (e.g. <code>l1icache</code>).</p>
<dt><code>core</code></p>
<dd>A single, physical processing unit which may still contain multiple logical processors, such as hardware threads.</p>
<dt><code>pu</code></p>
<dd>Short for <i>processor unit</i> (not <i>process</i>!). The smallest physical execution unit that hwloc recognizes. For example, there may be multiple PUs on a core (e.g., hardware threads).</dl>
<p> The additional <code>system</code> type can be used when several machines form an overall single system image (SSI), such as Kerrighed. </p>
<p> I/O devices are not listed here since they are not identified using tuples as explained in <code>Location Specification</code>. </p>
<p> Finally, note that an object can be denoted by its numeric &quot;depth&quot; in the topology graph.</p>
<h3>Hwloc Indexes</h3>
<p>Indexes are integer values that uniquely specify a given object of a specific type. Indexes can be expressed either as <i>logical</i> values or <i>physical</i> values. Most hwloc utilities accept logical indexes by default. Passing <code>&#8211;physical</code> switches to physical/OS indexes. Both logical and physical indexes are described on this man page. </p>
<p> <i>Logical</i> indexes are relative to the object order in the output from the lstopo command. They always start with 0 and increment by 1 for each successive object. </p>
<p> <i>Physical</i> indexes are how the operating system refers to objects. Note that while physical indexes are non-negative integer values, the hardware and/or operating system may choose arbitrary values &#8212; they may not start with 0, and successive objects may not have consecutive values. </p>
<p> For example, if the first few lines of lstopo -p output are the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Machine&nbsp;<wbr>(47GB)<br />
&nbsp;<wbr>NUMANode P#0&nbsp;<wbr>(24GB)&nbsp;<wbr>+&nbsp;<wbr>Package P#0&nbsp;<wbr>+&nbsp;<wbr>L3&nbsp;<wbr>(12MB)<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#0&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#1&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#2&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#8&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#9&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#10&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
&nbsp;<wbr>NUMANode P#1&nbsp;<wbr>(24GB)&nbsp;<wbr>+&nbsp;<wbr>Package P#1&nbsp;<wbr>+&nbsp;<wbr>L3&nbsp;<wbr>(12MB)<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#0&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#1&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#2&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#8&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#9&nbsp;<wbr>+&nbsp;<wbr>PU P#0<br />
L2&nbsp;<wbr>(256KB)&nbsp;<wbr>+&nbsp;<wbr>L1&nbsp;<wbr>(32KB)&nbsp;<wbr>+&nbsp;<wbr>Core P#10&nbsp;<wbr>+&nbsp;<wbr>PU P#0 </p>
<p> In this example, the first core on the second package is logically number 6 (i.e., logically the 7th core, starting from 0). Its physical index is 0, but note that another core <i>also</i> has a physical index of 0. Hence, physical indexes may only be relevant within the scope of their parent (or set of ancestors). In this example, to uniquely identify logical core 6 with physical indexes, you must specify (at a minimum) both a package and a core: package 1, core 0. </p>
<p> Index values, regardless of whether they are logical or physical, can be expressed in several different forms (where X, Y, and N are positive integers):</p>
<dl>
<dt><code>X</code></p>
<dd>The object with index value X.</p>
<dt><code>X-Y</code></p>
<dd>All the objects with index values &gt;= X and &lt;= Y.</p>
<dt><code>X-</code></p>
<dd>All the objects with index values &gt;= X.</p>
<dt><code>X:N</code></p>
<dd>N objects starting with index X, possibly wrapping around the end of the level.</p>
<dt><code>all</code></p>
<dd>A special index value indicating all valid index values.</p>
<dt><code>odd</code></p>
<dd>A special index value indicating all valid odd index values.</p>
<dt><code>even</code></p>
<dd>A special index value indicating all valid even index values.</dl>
<p> <i>REMEMBER</i>: hwloc&#8217;s command line tools accept <i>logical</i> indexes for location values by default. Use <code>&#8211;physical</code> and <code>&#8211;logical</code> to switch from one mode to another.</p>
<h2>See Also</h2>
<p>Hwloc&#8217;s command line tool documentation: <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-bind/">hwloc-bind</a>(1), <a href="/docs/linux/man/1-hwloc-calc/">hwloc-calc</a>(1), <a href="/docs/linux/man/1-hwloc-distrib/">hwloc-distrib</a>(1), <a href="/docs/linux/man/1-hwloc-ps/">hwloc-ps</a>(1). Hwloc has many C API functions, each of which have their own man page. Some top-level man pages are also provided, grouping similar functions together. A few good places to start might include: <a href="/docs/linux/man/3-hwlocality_objects/">hwlocality_objects</a>(3), <a href="/docs/linux/man/3-hwlocality_types/">hwlocality_types</a>(3), <a href="/docs/linux/man/3-hwlocality_creation/">hwlocality_creation</a>(3), <a href="/docs/linux/man/3-hwlocality_cpuset/">hwlocality_cpuset</a>(3), <a href="/docs/linux/man/3-hwlocality_information/">hwlocality_information</a>(3), and <a href="/docs/linux/man/3-hwlocality_binding/">hwlocality_binding</a>(3). For a listing of all available hwloc man pages, look at all &quot;hwloc*&quot; files in the man1 and man3 directories. </p>
