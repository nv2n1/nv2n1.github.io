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
<dt><code>-c</code></dt>
<dd> Generate cleaned version of the source</dd>
<dt><code>-h</code></dt>
<dd> Insert dual-license header into all module</dd>
<dt><code>-l</code></dt>
<dd> Generate Linux version of the source</dd>
<dt><code>-u</code></dt>
<dd> Generate custom source translation</dd>
<dt><code>-d</code></dt>
<dd> Leave debug statements in code</dd>
<dt><code>-s</code></dt>
<dd> Generate source statistics only</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode</dd>
<dt><code>-y</code></dt>
<dd> Suppress file overwrite prompts </dd>
</dl>
<h2>AUTHOR</h2>
<p> acpisrc was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
