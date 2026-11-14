---
title: "hwloc-distances(1)"
name: "hwloc-distances"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-distances/"
description: "hwloc-distances – Displays distance matrices"
---

<h2>NAME</h2>
<p> hwloc-distances &#8211; Displays distance matrices</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-distances</code> [<i>options</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> Display hwloc logical indexes (default) instead of physical/OS indexes.</p>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> Display OS/physical indexes instead of hwloc logical indexes.</p>
<dt><code>-i</code> &lt;file&gt;, <code>&#8211;input</code> &lt;file&gt;</p>
<dd> Read topology from XML file &lt;file&gt; (instead of discovering the topology on the local machine). If &lt;file&gt; is &quot;-&quot;, the standard input is used. XML support must have been compiled in to hwloc for this option to be usable.</p>
<dt><code>-i</code> &lt;directory&gt;, <code>&#8211;input</code> &lt;directory&gt;</p>
<dd> Read topology from the chroot specified by &lt;directory&gt; (instead of discovering the topology on the local machine). This option is generally only available on Linux. The chroot was usually created by gathering another machine topology with hwloc-gather-topology.</p>
<dt><code>-i</code> &lt;specification&gt;, <code>&#8211;input</code> &lt;specification&gt;</p>
<dd> Simulate a fake hierarchy (instead of discovering the topology on the local machine). If &lt;specification&gt; is &quot;node:2 pu:3&quot;, the topology will contain two NUMA nodes with 3 processing units in each of them. The &lt;specification&gt; string must end with a number of PUs.</p>
<dt><code>&#8211;if</code> &lt;format&gt;, <code>&#8211;input-format</code> &lt;format&gt;</p>
<dd> Enforce the input in the given format, among <code>xml</code>, <code>fsroot</code> and <code>synthetic</code>.</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Verbose messages.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-distances displays also distance matrices attached to the topology. The value in the i-th row and j-th column is the distance from object #i to object #j. </p>
<p> Unless defined by the user, matrices currently always contain relative latencies between NUMA nodes (which may or may not be accurate). See the definition of <i>struct hwloc_distances_s</i> in <i>include/hwloc.h</i> or the documentation for details. </p>
<p> These latencies are normalized to the latency of a local (non-NUMA) access. Hence 3.5 in row #i column #j means that the latency from cores in NUMA node #i to memory in NUMA node #j is 3.5 higher than the latency from cores to their local memory. A breadth-first traversal of the topology is performed starting from the root to find all distance matrices. </p>
<p> <code>NOTE:</code> lstopo may also display distance matrices in its verbose textual output. However lstopo only prints matrices that cover the entire topology while hwloc-distances also displays matrices that ignore part of the topology.</p>
<h2>EXAMPLES</h2>
<p> On a quad-package opteron machine: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distances<br />
&nbsp;<wbr>Latency matrix between 4 NUMANodes&nbsp;<wbr>(depth 2)&nbsp;<wbr>by logical indexes:<br />
index&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 1.000 1.600 2.200 2.200<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1 1.600 1.000 2.200 2.200<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2 2.200 2.200 1.000 1.600<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3 2.200 2.200 1.600 1.000</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-distances returns 0. </p>
<p> hwloc-distances will return nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1) </p>
<h2>Index</h2>
