---
title: "hwloc-bind(1)"
name: "hwloc-bind"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-bind/"
description: "hwloc-bind – Launch a command that is bound to specific processors and/or memory, or consult the binding of an existing program"
---

<h2>NAME</h2>
<p> hwloc-bind &#8211; Launch a command that is bound to specific processors and/or memory, or consult the binding of an existing program</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-bind</code> [<i>options</i>] <i>&lt;location1&gt; [&lt;location2&gt; [&#8230;] ] [&#8211;] &lt;command&gt; </i>&#8230; </p>
<p> Note that <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) provides a detailed explanation of the hwloc system and of valid &lt;location&gt; formats; it should be read before reading this man page.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cpubind</code></p>
<dd> Use following arguments for CPU binding (default).</p>
<dt><code>&#8211;membind</code></p>
<dd> Use following arguments for memory binding. If <code>&#8211;mempolicy</code> is not also given, the default policy is bind.</p>
<dt><code>&#8211;mempolicy</code> &lt;policy&gt;</p>
<dd> Change the memory binding policy. The available policies are default, firsttouch, bind, interleave replicate and nexttouch. This option is only meaningful when an actual binding is also given with <code>&#8211;membind</code>. If <code>&#8211;membind</code> is given without <code>&#8211;mempolicy</code>, the default policy is bind. </p>
<dt><code>&#8211;get</code></p>
<dd> Report the current bindings.</p>
<dt>&nbsp;<wbr></p>
<dd> When a command is given, the binding is displayed before executing the command. When no command is given, the program exits after displaying the current binding.</p>
<dt>&nbsp;<wbr></p>
<dd> When combined with <code>&#8211;membind</code>, report the memory binding instead of CPU binding.</p>
<dt>&nbsp;<wbr></p>
<dd> No location may be given since no binding is performed. </p>
<dt><code>-e</code> <code>&#8211;get-last-cpu-location</code></p>
<dd> Report the last processors where the process ran. Note that the result may already be outdated when reported since the operating system may move the process to other processors at any time according to the binding.</p>
<dt>&nbsp;<wbr></p>
<dd> When a command is given, the last processors is displayed before executing the command. When no command is given, the program exits after displaying the last processors.</p>
<dt>&nbsp;<wbr></p>
<dd> This option cannot be combined with <code>&#8211;membind</code>.</p>
<dt>&nbsp;<wbr></p>
<dd> No location may be given since no binding is performed. </p>
<dt><code>&#8211;single</code></p>
<dd> Bind on a single CPU to prevent migration.</p>
<dt><code>&#8211;strict</code></p>
<dd> Require strict binding.</p>
<dt><code>&#8211;pid</code> &lt;pid&gt;</p>
<dd> Operate on pid &lt;pid&gt;</p>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> take OS/physical indexes instead of logical indexes</p>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> take logical indexes instead of physical/OS indexes (default)</p>
<dt><code>&#8211;taskset</code></p>
<dd> Display CPU set strings in the format recognized by the taskset command-line program instead of hwloc-specific CPU set string format. This option has no impact on the format of input CPU set strings, both formats are always accepted.</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>-f</code> <code>&#8211;force</code></p>
<dd> Launch the executable even if binding failed.</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Hide non-fatal error messages. It includes locations pointing to non-existing objects, as well as failure to bind. This is usually useful in addition to <code>&#8211;force</code>.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Verbose output.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-bind execs an executable (with optional command line arguments) that is bound to the specified location (or list of locations). Upon successful execution, hwloc-bind simply sets bindings and then execs the executable over itself. </p>
<p> If binding fails, or if the binding set is empty, and <code>&#8211;force</code> was not given, hwloc-bind returns with an error instead of launching the executable. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-bind utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-bind&#8217;s operation is best described through several examples. More details about how locations are specified on the hwloc-bind command line are described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7). </p>
<p> To run the echo command on the first logical processor of the second package: </p>
<p>&nbsp;<wbr>hwloc-bind package:1.pu:0 &#8212; echo hello </p>
<p> which is exactly equivalent to </p>
<p>&nbsp;<wbr>hwloc-bind package:1.pu:0 echo hello </p>
<p> To bind the &quot;echo&quot; command to the first core of the second package and the second core of the first package: </p>
<p>&nbsp;<wbr>hwloc-bind package:1.core:0 package:0.core:1 echo hello </p>
<p> Note that binding the &quot;echo&quot; command to multiple processors is probably meaningless (because &quot;echo&quot; is likely implemented as a single-threaded application); these examples just serve to show what hwloc-bind can do. </p>
<p> To run on the first three packages on the second and third nodes: </p>
<p>&nbsp;<wbr>hwloc-bind node:1-2.package:0:3 echo hello </p>
<p> which is also equivalent to: </p>
<p>&nbsp;<wbr>hwloc-bind node:1-2.package:0-2 echo hello </p>
<p> Note that if you attempt to bind to objects that do not exist, hwloc-bind will not warn unless <i>-v</i> was specified. </p>
<p> To run on processor with physical index 2 in package with physical index 1: </p>
<p>&nbsp;<wbr>hwloc-bind &#8211;physical package:1.core:2 echo hello </p>
<p> To run on odd cores within even packages: </p>
<p>&nbsp;<wbr>hwloc-bind package:even.core:odd echo hello </p>
<p> To run on the first package, except on its second and fifth cores: </p>
<p>&nbsp;<wbr>hwloc-bind package:0&nbsp;<wbr>~package:0.core:1&nbsp;<wbr>~package:0.core:4 echo hello </p>
<p> To run anywhere except on the first package: </p>
<p>&nbsp;<wbr>hwloc-bind all&nbsp;<wbr>~package:0 echo hello </p>
<p> To run on a core near the network interface named eth0: </p>
<p>&nbsp;<wbr>hwloc-bind os=eth0 echo hello </p>
<p> To run on a core near the PCI device whose bus ID is 0000:01:02.0: </p>
<p>&nbsp;<wbr>hwloc-bind pci=0000:01:02.0 echo hello </p>
<p> To bind memory on second memory node and run on first node (when supported by the OS): </p>
<p>&nbsp;<wbr>hwloc-bind &#8211;cpubind node:1 &#8211;membind node:0 echo hello </p>
<p> The &#8211;get option can report current bindings. This example shows nesting hwloc-bind invocations to set a binding and then report it: </p>
<p>&nbsp;<wbr>hwloc-bind node:1.package:2 hwloc-bind &#8211;get </p>
<p> On one of the hwloc developer&#8217;s machines, this example reports &quot;0x00004444,0x44000000&quot;. The mask reported on your machine may be different. </p>
<p> Locations may also be specified as a hex bit mask (typically generated by hwloc-calc). For example: </p>
<p>&nbsp;<wbr>hwloc-bind 0x00004444,0x44000000 echo hello<br />
&nbsp;<wbr>hwloc-bind&nbsp;<wbr>`hwloc-calc node:1.package:2`&nbsp;<wbr>echo hello </p>
<p> Memory binding may also be reported: </p>
<p>&nbsp;<wbr>hwloc-bind &#8211;membind node:1 &#8211;mempolicy interleave &#8212; hwloc-bind &#8211;get &#8211;membind </p>
<p> This returns a string describing the memory binding, such as &quot;0x000000f0 (interleave)&quot;. Note that if the system does not contain any NUMA nodes, the reported string will indicate that the process is bound to the entire system memory (e.g., &quot;0xf&#8230;f&quot;).</p>
<h2>HINT</h2>
<p> If the graphics-enabled lstopo is available, use for instance </p>
<p>&nbsp;<wbr>hwloc-bind core:2 &#8212; lstopo &#8211;pid 0 </p>
<p> to check what the result of your binding command actually is. lstopo will graphically show where it is bound to by hwloc-bind.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-bind execs the command over itself. The return value is therefore whatever the return value of the command is. </p>
<p> hwloc-bind will return nonzero if any kind of error occurs, such as (but not limited to): failure to parse the command line, failure to retrieve process bindings, or lack of a command to execute.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-calc/">hwloc-calc</a>(1), <a href="/docs/linux/man/1-hwloc-distrib/">hwloc-distrib</a>(1) </p>
<h2>Index</h2>
