---
title: "prtstat(1)"
name: "prtstat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prtstat/"
description: "prtstat – print statistics of a process"
---

<h2 class="name">NAME</h2>
<p> prtstat &#8211; print statistics of a process </p>
<h2>SYNOPSIS</h2>
<p> <code>prtstat</code> [<code>-r</code>|<code>&#8211;raw</code>] <i>pid</i><br />
 <code>prtstat</code> <code>-V</code>|<code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>prtstat</code> prints the statistics of the specified process. This information comes from the <code>/proc/</code><i>pid</i><code>/stat</code> file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code>,<code>&nbsp;&#8211;raw</code></p>
<dd> Print the information in raw format.</p>
<dt><code>-V</code>,<code>&nbsp;&#8211;version</code></p>
<dd> Show the version information for <code>prtstat</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/proc/</code><i>pid</i><code>/stat</code></p>
<dd> source of the information <code>prtstat</code> uses. </p>
</dl>
<h2>Index</h2>
