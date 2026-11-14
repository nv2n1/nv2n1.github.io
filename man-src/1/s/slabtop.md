---
title: "slabtop(1)"
name: "slabtop"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slabtop/"
description: "slabtop – display kernel slab cache information in real time"
---

<h2 class="name">NAME</h2>
<p> slabtop &#8211; display kernel slab cache information in real time </p>
<h2>SYNOPSIS</h2>
<p> <code>slabtop</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>slabtop</code> displays detailed kernel slab cache information in real time. It displays a listing of the top caches sorted by one of the listed sort criteria. It also displays a statistics header filled with slab layer information.</p>
<h2>OPTIONS</h2>
<p> Normal invocation of <code>slabtop</code> does not require any options. The behavior, however, can be fine-tuned by specifying one or more of the following flags:</p>
<dl>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>N</i></p>
<dd> Refresh the display every <i>n</i> in seconds. By default, <code>slabtop</code> refreshes the display every three seconds. To exit the program, hit <code>q.</code></p>
<dt><code>-s</code>, <code>&#8211;sort</code>=<i>S</i></p>
<dd> Sort by <i>S</i>, where <i>S</i> is one of the sort criteria.</p>
<dt><code>-o</code>, <code>&#8211;once</code></p>
<dd> Display the output once and then exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</dl>
<h2>SORT CRITERIA</h2>
<p> The following are valid sort criteria used to sort the individual slab caches and thereby determine what are the &quot;top&quot; slab caches to display. The default sort criteria is to sort by the number of objects (&quot;o&quot;). </p>
<p> The sort criteria can also be changed while <code>slabtop</code> is running by pressing the associated character. </p>
<table>
<tr VALIGN=top>
<td><code>character</code></td>
<td>description</td>
<td>header
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>number of active objects</td>
<td>ACTIVE
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td>objects per slab</td>
<td>OBJ/SLAB
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td>cache size</td>
<td>CACHE SIZE
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>number of slabs</td>
<td>SLABS
</td>
</tr>
<tr VALIGN=top>
<td>v</td>
<td>number of active slabs</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>name</td>
<td>NAME
</td>
</tr>
<tr VALIGN=top>
<td>o</td>
<td>number of objects</td>
<td>OBJS
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>pages per slab</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>object size</td>
<td>OBJ SIZE
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>cache utilization</td>
<td>USE
</td>
</tr>
</table>
<h2>COMMANDS</h2>
<p> <code>slabtop</code> accepts keyboard commands from the user during use. The following are supported. In the case of letters, both cases are accepted. </p>
<p> Each of the valid sort characters are also accepted, to change the sort routine. See the section <code>SORT CRITERIA</code>.</p>
<dl>
<dt><code>&lt;SPACEBAR&gt;</code></p>
<dd> Refresh the screen.</p>
<dt><code>Q</code></p>
<dd> Quit the program.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/proc/slabinfo</i></p>
<dd> slab information</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8)</p>
<h2>NOTES</h2>
<p> Currently, <code>slabtop</code> requires a 2.4 or later kernel (specifically, a version 1.1 or later <i>/proc/slabinfo</i>). Kernel 2.2 should be supported in the future. </p>
<p> The <code>slabtop</code> statistic header is tracking how many bytes of slabs are being used and is not a measure of physical memory. The &#8216;Slab&#8217; field in the /proc/meminfo file is tracking information about used slab physical memory.</p>
<h2>AUTHORS</h2>
<p> Written by Chris Rivera and Robert Love. </p>
<p> <code>slabtop</code> was inspired by Martin Bligh&#8217;s perl script, <code>vmtop</code>.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
