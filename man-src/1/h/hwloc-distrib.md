---
title: "hwloc-distrib(1)"
name: "hwloc-distrib"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-distrib/"
description: "hwloc-distrib – Build a number of cpu masks distributed on the system"
---

<h2>NAME</h2>
<p> hwloc-distrib &#8211; Build a number of cpu masks distributed on the system</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-distrib</code> [<i>options</i>] <i>&lt;integer&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;single</code></p>
<dd> Singlify each output to a single CPU.</p>
<dt><code>&#8211;taskset</code></p>
<dd> Show CPU set strings in the format recognized by the taskset command-line program instead of hwloc-specific CPU set string format.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Verbose messages.</p>
<dt><code>-i</code> &lt;file&gt;, <code>&#8211;input</code> &lt;file&gt;</p>
<dd> Read topology from XML file &lt;file&gt; (instead of discovering the topology on the local machine). If &lt;file&gt; is &quot;-&quot;, the standard input is used. XML support must have been compiled in to hwloc for this option to be usable.</p>
<dt><code>-i</code> &lt;directory&gt;, <code>&#8211;input</code> &lt;directory&gt;</p>
<dd> Read topology from the chroot specified by &lt;directory&gt; (instead of discovering the topology on the local machine). This option is generally only available on Linux. The chroot was usually created by gathering another machine topology with hwloc-gather-topology.</p>
<dt><code>-i</code> &lt;specification&gt;, <code>&#8211;input</code> &lt;specification&gt;</p>
<dd> Simulate a fake hierarchy (instead of discovering the topology on the local machine). If &lt;specification&gt; is &quot;node:2 pu:3&quot;, the topology will contain two NUMA nodes with 3 processing units in each of them. The &lt;specification&gt; string must end with a number of PUs.</p>
<dt><code>&#8211;if</code> &lt;format&gt;, <code>&#8211;input-format</code> &lt;format&gt;</p>
<dd> Enforce the input in the given format, among <code>xml</code>, <code>fsroot</code> and <code>synthetic</code>.</p>
<dt><code>&#8211;ignore</code> &lt;type&gt;</p>
<dd> Ignore all objects of type &lt;type&gt; in the topology.</p>
<dt><code>&#8211;from</code> &lt;type&gt;</p>
<dd> Distribute starting from objects of the given type instead of from the top of the topology hierarchy, i.e. ignoring the structure given by objects above.</p>
<dt><code>&#8211;to</code> &lt;type&gt;</p>
<dd> Distribute down to objects of the given type instead of down to the bottom of the topology hierarchy, i.e. ignoring the structure given by objects below. This may be useful if some latitude is desired for the binding, e.g. just bind several processes to each package without specifying a single core for each of them.</p>
<dt><code>&#8211;at</code> &lt;type&gt;</p>
<dd> Distribute among objects of the given type. This is equivalent to specifying both <code>&#8211;from</code> and <code>&#8211;to</code> at the same time.</p>
<dt><code>&#8211;reverse</code></p>
<dd> Distribute by starting with the last objects first, and singlify CPU sets by keeping the last bit (instead of the first bit).</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-distrib generates a series of CPU masks corresponding to a distribution of a given number of elements over the topology of the machine. The distribution is done recursively from the top of the hierarchy (or from the level specified by option <code>&#8211;from</code>) down to the bottom of the hierarchy (or down to the level specified by option <code>&#8211;to</code>, or until only one element remains), splitting the number of elements at each encountered hierarchy level not ignored by options <code>&#8211;ignore</code>. </p>
<p> This can e.g. be used to distribute a set of processes hierarchically according to the topology of a machine. These masks can be used with <a href="/docs/linux/man/1-hwloc-bind/">hwloc-bind</a>(1). </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-bind utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-distrib&#8217;s operation is best described through several examples. </p>
<p> If 4 processes have to be distributed across a machine, their CPU masks may be obtained with: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distrib 4<br />
&nbsp;<wbr>0x0000000f<br />
&nbsp;<wbr>0x00000f00<br />
&nbsp;<wbr>0x000000f0<br />
&nbsp;<wbr>0x0000f000 </p>
<p> To distribute only among the second package, the topology should be restricted: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distrib &#8211;restrict&nbsp;<wbr>$(hwloc-calc package:1)&nbsp;<wbr>4<br />
&nbsp;<wbr>0x00000010<br />
&nbsp;<wbr>0x00000020<br />
&nbsp;<wbr>0x00000040<br />
&nbsp;<wbr>0x00000080 </p>
<p> To get a single processor of each CPU masks (prevent migration in case of binding) </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distrib 4 &#8211;single<br />
&nbsp;<wbr>0x00000001<br />
&nbsp;<wbr>0x00000100<br />
&nbsp;<wbr>0x00000010<br />
&nbsp;<wbr>0x00001000 </p>
<p> Each output line may be converted independently with hwloc-calc: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distrib 4 &#8211;single | hwloc-calc &#8211;taskset<br />
&nbsp;<wbr>0x1<br />
&nbsp;<wbr>0x100<br />
&nbsp;<wbr>0x10<br />
&nbsp;<wbr>0x1000 </p>
<p> To convert the output into a list of processors that may be passed to dplace -c inside a mpirun command line: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-distrib 4 &#8211;single | xargs hwloc-calc &#8211;pulist<br />
&nbsp;<wbr>0,8,4,16</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-distrib displays one or more CPU mask strings. The return value is 0. </p>
<p> hwloc-distrib will return nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-hwloc-gather-topology/">hwloc-gather-topology</a>(1) </p>
<h2>Index</h2>
