---
title: "acpisrc(1)"
name: "acpisrc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpisrc/"
description: "acpisrc – ACPICA source code conversion utility"
---

<h2 class="name">NAME</h2>
<p> acpisrc &#8211; ACPICA source code conversion utility </p>
<h2>SYNOPSIS</h2>
<p> <code>acpisrc</code> [<i>-c</i>|<i>-l</i>|<i>-u]</i>[-d]<i>[-s]</i>[-v]<i>[-y]</i>&lt;source-dir&gt;<i>&lt;dest-dir&gt;</i> &lt;aml-file&gt; </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpisrc</code> command. The option list is taken from the acpisrc interactive help. </p>
<p> <code>acpisrc</code> converts the ACPICA into various forms for use with different operating systems. Source for ACPICA may be obtained from <a rel="nofollow" href="http://www.acpica.org/source/.">http://www.acpica.org/source/.</a> </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Generate cleaned version of the source</p>
<dt><code>-h</code></p>
<dd> Insert dual-license header into all module</p>
<dt><code>-l</code></p>
<dd> Generate Linux version of the source</p>
<dt><code>-u</code></p>
<dd> Generate custom source translation</p>
<dt><code>-d</code></p>
<dd> Leave debug statements in code</p>
<dt><code>-s</code></p>
<dd> Generate source statistics only</p>
<dt><code>-v</code></p>
<dd> Verbose mode</p>
<dt><code>-y</code></p>
<dd> Suppress file overwrite prompts </p>
</dl>
<h2>AUTHOR</h2>
<p> acpisrc was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
