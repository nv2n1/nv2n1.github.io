---
title: "pcp-free(1)"
name: "pcp-free"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-free/"
description: "pcp-free – report on free and used memory in the system"
---

<h2>NAME</h2>
<p> <code>pcp-free</code> &#8211; report on free and used memory in the system</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>free</code> [<code>-bkmgoltV</code>] [<code>-c</code> <i>count</i>] [<code>-s</code> <i>interval</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-free</code> gives a summary display of the total amount of free and used physical memory and swap in the system, as well as the caches used by the kernel. </p>
<p> When invoked via the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, the <code>-h</code>/<code>&#8211;host</code>, <code>-a</code>/<code>&#8211;archive</code>, <code>-O</code>/<code>&#8211;origin</code>, <code>-s</code>/<code>&#8211;samples</code>, <code>-t</code>/<code>&#8211;interval</code>, <code>-Z</code>/<code>&#8211;timezone</code> and several other <i>pcp options</i> become indirectly available.</p>
<h3>Options</h3>
<p> The <code>-b</code>/<code>&#8211;bytes</code> switch displays the amount of memory in bytes; the <code>-k</code>/<code>&#8211;kilobytes</code> switch (set by default) displays it in kilobytes; the <code>-m</code>/<code>&#8211;megabytes</code> switch displays it in megabytes. </p>
<p> The <code>-t</code>/<code>&#8211;total</code> switch displays a line containing the totals. </p>
<p> The <code>-o</code> switch disables the display of a &quot;buffer adjusted&quot; line. If the <code>-o</code> option is not specified, <code>free</code> subtracts buffer memory from the used memory and adds it to the free memory reported. </p>
<p> The <code>-s</code>/<code>&#8211;interval</code> switch activates continuous polling <i>delay</i> seconds apart. You may specify any floating point number for <i>delay</i>, or indeed any valid <code><a href="/docs/linux/man/3-pmparseinterval/">pmParseInterval</a></code>(3) specification, which includes microsecond resolution delay times. This can be used in conjunction with the <code>-c</code>/<code>&#8211;samples</code> option to terminate the display after <i>count</i> iterations. </p>
<p> The <code>-l</code> switch shows detailed low and high memory statistics. </p>
<p> The current version of <code>pcp-free</code> can be queried using the <code>-V</code>/<code>&#8211;version</code> option.</p>
<h2>NOTES</h2>
<p> <code>pcp-free</code> is inspired by the <code><a href="/docs/linux/man/1-free/">free</a></code>(1) command and aims to be command line and output compatible with it. </p>
<p> The shared memory column should be ignored; it is obsolete.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-free/">free</a>(1),</code> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmparseinterval/">pmParseInterval</a></code>(3) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<h2>Index</h2>
