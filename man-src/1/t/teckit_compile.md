---
title: "teckit_compile(1)"
name: "teckit_compile"
section: "1"
letter: "t"
url: "/docs/linux/man/1-teckit_compile/"
description: "teckit_compile – manual page for command line error at –version"
---

<h2 class="name">NAME</h2>
<p> teckit_compile &#8211; manual page for command line error at &#8211;version </p>
<h2>SYNOPSIS</h2>
<p> <code>teckit_compile</code> [<i>,-u/</i>] [<i>,-x/</i>] [<i>,-z/</i>] <i>,mapping_description /</i>[<i>,-o compiled_table/</i>]</p>
<h2>OPTIONS</h2>
<p> Required argument:</p>
<dl>
<dt>
</dt><dd> <code>source</code> mapping description (.map) file</dd></dl>
<p> Optional arguments:</p>
<dl>
<dt><code>-o</code>file</dt>
<dd> output compiled table (.tec) file (&quot;-&quot; for stdout)</dd>
<dt><code>-u</code></dt>
<dd> read source text as UTF8 even if no BOM found</dd>
<dt><code>-x</code></dt>
<dd> generate XML representation rather than compiled table</dd>
<dt><code>-z</code></dt>
<dd> generate uncompressed table format</dd></dl>
<h2>Further Information</h2>
<p> For further information see the document TECkit_Tools.pdf. A description of the mapping description language used by the compiler, with examples, is found in TECkit_Language.pdf. On a Debian system, these can be found in /usr/share/doc/teckit. </p>
<h2>Index</h2>
