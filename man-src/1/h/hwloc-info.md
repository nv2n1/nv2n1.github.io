---
title: "hwloc-info(1)"
name: "hwloc-info"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-info/"
description: "hwloc-info – Show some information about some objects or about a topology"
---

<h2>NAME</h2>
<p> hwloc-info &#8211; Show some information about some objects or about a topology</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-info</code> [ <i>options </i>]&#8230; <i>&lt;object&gt;</i>&#8230; </p>
<p> <code>hwloc-info</code> [ <i>options </i>]&#8230; </p>
<p> Note that <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) provides a detailed explanation of the hwloc system and of valid &lt;object&gt; formats; it should be read before reading this man page.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;file&gt;, <code>&#8211;input</code> &lt;file&gt;</p>
<dd> Read topology from XML file &lt;file&gt; (instead of discovering the topology on the local machine). If &lt;file&gt; is &quot;-&quot;, the standard input is used. XML support must have been compiled in to hwloc for this option to be usable.</p>
<dt><code>-i</code> &lt;directory&gt;, <code>&#8211;input</code> &lt;directory&gt;</p>
<dd> Read topology from the chroot specified by &lt;directory&gt; (instead of discovering the topology on the local machine). This option is generally only available on Linux. The chroot was usually created by gathering another machine topology with hwloc-gather-topology.</p>
<dt><code>-i</code> &lt;specification&gt;, <code>&#8211;input</code> &lt;specification&gt;</p>
<dd> Simulate a fake hierarchy (instead of discovering the topology on the local machine). If &lt;specification&gt; is &quot;node:2 pu:3&quot;, the topology will contain two NUMA nodes with 3 processing units in each of them. The &lt;specification&gt; string must end with a number of PUs.</p>
<dt><code>&#8211;if</code> &lt;format&gt;, <code>&#8211;input-format</code> &lt;format&gt;</p>
<dd> Enforce the input in the given format, among <code>xml</code>, <code>fsroot</code> and <code>synthetic</code>.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Include additional detail.</p>
<dt><code>-s</code> <code>&#8211;silent</code></p>
<dd> Reduce the amount of details to show. A single summary line per object is displayed.</p>
<dt><code>&#8211;ancestors</code></p>
<dd> Display information about the object as well as about all its ancestors up to the root of the topology.</p>
<dt><code>&#8211;ancestor</code> &lt;type&gt;</p>
<dd> Only display the object ancestors that match the given type.</p>
<dt><code>-n</code></p>
<dd> When outputting object information, prefix each line with the index of the considered object within the input. For instance, if three cores were given in input, the output lines will be prefixed with &quot;0: &quot;, &quot;1: &quot; or &quot;2: &quot;. If <code>&#8211;ancestor</code> is also used, the prefix will be &quot;X.Y: &quot; where X is the index of the considered object within the input, and Y is the parent index (0 for the object itself, increasing towards the root of the topology).</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;restrict</code> binding</p>
<dd> Restrict the topology to the current process binding. This option requires the use of the actual current machine topology (or any other topology with <code>&#8211;thissystem</code> or with HWLOC_THISSYSTEM set to 1 in the environment).</p>
<dt><code>&#8211;no-icaches</code></p>
<dd> Do not show Instruction caches, only Data and Unified caches are considered.</p>
<dt><code>&#8211;no-io</p>
<dd> Do not show any I/O device or bridge. By default, common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;no-bridges</p>
<dd> Do not show any I/O bridge except hostbridges. By default, common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;whole-io</p>
<dd> Show all I/O devices and bridges. By default, only common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;thissystem</code></p>
<dd> Assume that the selected backend provides the topology for the system on which we are running. This is useful when using <code>&#8211;restrict</code> binding and loading a custom topology such as an XML file.</p>
<dt><code>&#8211;pid</code> &lt;pid&gt;</p>
<dd> Detect topology as seen by process &lt;pid&gt;, i.e. as if process &lt;pid&gt; did the discovery itself. Note that this can for instance change the set of allowed processors. Also show this process current CPU binding by marking the corresponding PUs (in Green in the graphical output, see the COLORS section below, or by appending <i>(binding)</i> to the verbose text output). If 0 is given as pid, the current binding for the lstopo process will be shown.</p>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> Use OS/physical indexes instead of logical indexes for input.</p>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> Use logical indexes instead of physical/OS indexes for input (default).</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-info displays information about the specified object. It is intended to be used with tools such as grep for filtering certain attribute lines. When no object is specified, hwloc-info prints a summary of the topology. </p>
<p> Objects may be specified as location tuples, as explained in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7). However hexadecimal bitmasks are not accepted since they may correspond to multiple objects. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-calc utility.</p>
<h2>EXAMPLES</h2>
<p> To display information about each package: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-info package:all<br />
&nbsp;<wbr>Package L#0<br />
&nbsp;<wbr>&nbsp;<wbr>logical index&nbsp;<wbr>=&nbsp;<wbr>0<br />
&nbsp;<wbr>&#8230; </p>
<p> To display information about the core whose physical index is 2: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>utils/hwloc-info -p core:2<br />
&nbsp;<wbr>Core L#1<br />
&nbsp;<wbr>&nbsp;<wbr>logical index&nbsp;<wbr>=&nbsp;<wbr>1<br />
&nbsp;<wbr>&nbsp;<wbr>os index&nbsp;<wbr>=&nbsp;<wbr>2<br />
&#8230;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-calc/">hwloc-calc</a>(1), <a href="/docs/linux/man/1-hwloc-bind/">hwloc-bind</a>(1), <a href="/docs/linux/man/1-hwloc-ps/">hwloc-ps</a>(1), <a href="/docs/linux/man/1-hwloc-gather-topology/">hwloc-gather-topology</a>(1) </p>
<h2>Index</h2>
