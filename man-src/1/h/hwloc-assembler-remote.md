---
title: "hwloc-assembler-remote(1)"
name: "hwloc-assembler-remote"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-assembler-remote/"
description: "hwloc-assembler-remote – Assemble multiple remote host topologies"
---

<h2>NAME</h2>
<p> hwloc-assembler-remote &#8211; Assemble multiple remote host topologies</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-assembler-remote</code> [<i>options</i>] output.xml host1 host2 &#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;ssh &lt;ssh&gt;</code></p>
<dd> Use the given ssh command (and options) to connect to remote hosts.</p>
<dt><code>&#8211;lstopo-path &lt;path&gt;</code></p>
<dd> Use the given path as the remote lstopo command when gathering remote topologies. By default, lstopo is taken from the PATH environment variable.</p>
<dt><code>&#8211;lstopo-opts &lt;opts&gt;</code></p>
<dd> Pass the given lstopo options when gathering remote topologies.</p>
<dt><code>&#8211;show</code></p>
<dd> Display the resulting topology before exit.</p>
<dt><code>-f &#8211;force</code></p>
<dd> Ignore failure to load a remote host topology.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-assembler-remote is a frontend to hwloc-assembler. It takes care of retrieving the remote nodes&#8217; topologies before assembling them with hwloc-assembler.</p>
<h2>EXAMPLES</h2>
<p> To assemble three nodes topologies: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-assembler-remote output.xml host1 host2 host3 </p>
<p> To assemble the topology of a multi-process MPI job defined as a machinefile: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-assembler-remote output.xml&nbsp;<wbr>`cat machinefile | sort | uniq`</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-assembler-remote returns 0. </p>
<p> hwloc-assembler-remote will return nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-assembler/">hwloc-assembler</a>(1) </p>
<h2>Index</h2>
