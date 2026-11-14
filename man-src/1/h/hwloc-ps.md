---
title: "hwloc-ps(1)"
name: "hwloc-ps"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-ps/"
description: "hwloc-ps – List currently-running processes or threads that are bound"
---

<h2>NAME</h2>
<p> hwloc-ps &#8211; List currently-running processes or threads that are bound</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-ps</code> [<i>options</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> list all processes, even those that are not bound to any specific part of the machine.</p>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> report OS/physical indexes instead of logical indexes</p>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> report logical indexes instead of physical/OS indexes (default)</p>
<dt><code>-c</code> <code>&#8211;cpuset</code></p>
<dd> show process bindings as cpusets instead of objects.</p>
<dt><code>-t</code> <code>&#8211;threads</code></p>
<dd> show threads inside processes. If <code>-a</code> is given as well, list all threads within each process. Otherwise, show all threads inside each process where at least one thread is bound.</p>
<dt><code>-e</code> <code>&#8211;get-last-cpu-location</code></p>
<dd> Report the last processors where the process/thread ran. Note that the result may already be outdated when reported since the operating system may move the tasks to other processors at any time according to the binding.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>&#8211;pid-cmd &lt;cmd&gt;</code></p>
<dd> Append the output of the given command to each PID line. For each displayed process ID, execute the command <i>&lt;cmd&gt; &lt;pid&gt;</i> and append <code>the first line</code> of its output to the regular hwloc-ps line.</dl>
<h2>DESCRIPTION</h2>
<p> By default, hwloc-ps lists only those currently-running processes that are bound. If <code>-t</code> is given, processes that are not bound but contain at least one bound thread are also displayed, as well as all their threads. </p>
<p> hwloc-ps displays process identifier, command-line and binding. The binding may be reported as objects or cpusets. </p>
<p> By default, process bindings are restricted to the currently available topology. If some processes are bound to processors that are not available to the current process, they are ignored unless <code>&#8211;whole-system</code> is given. </p>
<p> The output is a plain list. If you wish to annotate the hierarchical topology with processes so as to see how they are actual distributed on the machine, you might want to use lstopo &#8211;ps instead (which also only shows processes that are bound). </p>
<p> The <i>-a</i> switch can be used to show <i>all</i> processes, if desired.</p>
<h2>EXAMPLES</h2>
<p> If a process is bound, it appears in the default output: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>utils/hwloc-ps<br />
&nbsp;<wbr>4759<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Core:0<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram</p>
<p> If a process is not bound but 3 of his 4 threads are bound, it only appears in the thread-aware output: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>utils/hwloc-ps </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>utils/hwloc-ps -t<br />
&nbsp;<wbr>4759<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Machine:0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram</p>
<p>&nbsp;<wbr>&nbsp;<wbr>4759<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Machine:0</p>
<p>&nbsp;<wbr>&nbsp;<wbr>4761<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PU:0</p>
<p>&nbsp;<wbr>&nbsp;<wbr>4762<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PU:2</p>
<p>&nbsp;<wbr>&nbsp;<wbr>4765<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PU:1</p>
<p> To display the binding of already running MPI processes (launched by Open MPI) and append their MPI rank (in MPI_COMM_WORLD) to each line: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>utils/hwloc-ps &#8211;pid-cmd myscript<br />
&nbsp;<wbr>29093<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>L1dCache:0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OMPI_COMM_WORLD_RANK=0</p>
<p>&nbsp;<wbr>29094<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>L1dCache:2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OMPI_COMM_WORLD_RANK=1</p>
<p>&nbsp;<wbr>29095<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>L1dCache:1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OMPI_COMM_WORLD_RANK=2</p>
<p>&nbsp;<wbr>29096<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>L1dCache:3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myprogram<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OMPI_COMM_WORLD_RANK=3</p>
<p> where <code>myscript</code> is a bash script doing: </p>
<p>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>cat&nbsp;<wbr>/proc/$1/environ 2&gt;/dev/null | xargs &#8211;null &#8211;max-args=1 echo | grep OMPI_COMM_WORLD_RANK </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-calc/">hwloc-calc</a>(1), <a href="/docs/linux/man/1-hwloc-distrib/">hwloc-distrib</a>(1) </p>
<h2>Index</h2>
