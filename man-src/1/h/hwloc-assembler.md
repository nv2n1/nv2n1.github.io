---
title: "hwloc-assembler(1)"
name: "hwloc-assembler"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-assembler/"
description: "hwloc-assembler – Assemble multiple XML topologies"
---

<h2>NAME</h2>
<p> hwloc-assembler &#8211; Assemble multiple XML topologies</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-assembler</code> [<i>options</i>] output.xml [&#8211;name &lt;name1&gt;] input1.xml [&#8211;name &lt;name2&gt;] input2.xml &#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n &#8211;name &lt;name&gt;</code></p>
<dd> Set &lt;name&gt; in the <i>AssemblerName</i> info attribute of the next input topology root to ease identification within the final global topology.</p>
<dt><code>-f &#8211;force</code></p>
<dd> Ignore errors while reading input files.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Verbose messages.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-assembler combines the input XML topologies and exports the resulting global topologies to a new XML file. All inputs are inserting as children of the global root object. </p>
<p> Each input topology root is annotated with info attributes before insertion. <i>AssemblerIndex</i> is set to the index within the list of inputs. <i>AssemblerName</i> is set to the name given with <code>&#8211;name</code> if any. </p>
<p> hwloc-assembler-remote offers a frontend for assembling remote nodes topologies without having to manually gather and transfer each of them.</p>
<h2>EXAMPLES</h2>
<p> To assemble two nodes topologies: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-assembler output.xml &#8211;name host1 host1.xml &#8211;name host2 host2.xml</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-assembler returns 0. </p>
<p> hwloc-assembler will return nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-assembler-remote/">hwloc-assembler-remote</a>(1) </p>
<h2>Index</h2>
