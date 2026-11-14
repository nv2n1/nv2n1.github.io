---
title: "pcp-numastat(1)"
name: "pcp-numastat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-numastat/"
description: "pcp-numastat – report on NUMA memory allocation"
---

<h2>NAME</h2>
<p> <code>pcp-numastat</code> &#8211; report on NUMA memory allocation</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>numastat</code> [<code>-V</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-numastat</code> displays NUMA allocation statistics from the kernel memory allocator. Each process has NUMA policies that specify on which node pages are allocated. The performance counters in the kernel track on which nodes memory is allocated and these values are sampled and reported by <code>pcp-numastat</code>. </p>
<p> Counters are maintained individually for each NUMA node. Details of the semantics of each reported metric can be retrieved using the following command: </p>
<pre>
# pminfo -dt mem.numa.alloc
</pre>
<p> When invoked via the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, the <code>-h</code>/<code>&#8211;host</code>, <code>-a</code>/<code>&#8211;archive</code>, <code>-O</code>/<code>&#8211;origin</code>, <code>-Z</code>/<code>&#8211;timezone</code> and several other <i>pcp options</i> become indirectly available. </p>
<p> The current version of <code>pcp-numastat</code> can be queried using the <code>-V</code>/<code>&#8211;version</code> option.</p>
<h2>NOTES</h2>
<p> <code>pcp-numastat</code> is inspired by the <code><a href="/docs/linux/man/1-numastat/">numastat</a></code>(1) command and produces exactly the same output.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-numastat/">numastat</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
