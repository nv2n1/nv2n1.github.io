---
title: "rdflib(1)"
name: "rdflib"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdflib/"
description: "rdflib – manage a library file for use with ldrdf(1)"
---

<h2>NAME</h2>
<p> rdflib &#8211; manage a library file for use with <a href="/docs/linux/man/1-ldrdf/">ldrdf</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>rdflib</code> <i>command</i> <i>arguments</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rdflib</code> manages a library file which can be used by <code><a href="/docs/linux/man/1-ldrdf/">ldrdf</a></code>(1). It is supplied with a shell script <code>makelib</code> which should probably be used to create libraries.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>c</code><i> library-file</i></p>
<dd> Create (or truncate) a library.</p>
<dt><code>a</code><i> library-file object-file module</i></p>
<dd> Add the <i>object-file</i> to the library under the name <i>module</i>.</p>
<dt><code>x</code><i> library-file module object-file</i></p>
<dd> Extract a <i>module</i> from the library to the file <i>object-file</i>.</p>
<dt><code>t library-file</code></p>
<dd> Display a list of modules in the library.</dl>
<h2>NOTES</h2>
<p> A remove command will be added soon.</p>
<h2>AUTHORS</h2>
<p> Julian Hall &lt;jules [at] earthcorp.com&gt;. </p>
<p> This manual page was written by Matej Vela &lt;vela [at] debian.org&gt;. </p>
<h2>Index</h2>
