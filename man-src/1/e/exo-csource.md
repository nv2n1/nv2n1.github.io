---
title: "exo-csource(1)"
name: "exo-csource"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exo-csource/"
description: "exo-csource – C code generation utility for arbitrary data"
---

<h2 class="name">NAME</h2>
<p> exo-csource &#8211; C code generation utility for arbitrary data </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>exo-csource</code> [options] [file]</dt>
<dt> <code>exo-csource</code> [options] &#8211;build-list [[name]&nbsp;[file]&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>exo-csource</code></p>
<dd>is a small utility that generates C code containing arbitrary data, useful for compiling texts or other data directly into programs.</dd>
<h2>INVOCATION</h2>
<p> <code>exo-csource</code> either takes as input one file name to generate code for, or, using the <code>&#8211;build-list</code> option, a list of (<i>name</i>, <i>file</i>) pairs to generate code for a list of images into named variables.</p>
<h3>Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print brief help and exit.</dd></dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print version information and exit.</dd></dl>
<p> <code>&#8211;extern</code></p>
<dl>
<dt>
</dt><dd> Generate extern symbols.</dd></dl>
<p> <code>&#8211;static</code></p>
<dl>
<dt>
</dt><dd> Generate static symbols (default).</dd></dl>
<p> <code>&#8211;name=identifier</code></p>
<dl>
<dt>
</dt><dd> Specifies the <i>identifier</i> name (prefix) for the generated variables (only used if <code>&#8211;build-list</code> was not specified as well).</dd></dl>
<p> <code>&#8211;build-list</code></p>
<dl>
<dt>
</dt><dd> Enables (<i>name</i>, <i>file</i>) pair parsing mode.</dd></dl>
<p> <code>&#8211;output=identifier</code></p>
<dl>
<dt>
</dt><dd> Prints the output to <i>identifier</i> instead of stdout (only used if <code>&#8211;build-list</code> was not specified as well).</dd></dl>
<h2>SEE ALSO</h2>
<p> The <code>gdk-pixbuf-csource</code> utility which ships with the Gtk+ distribution, available from m[blue]<code><a rel="nofollow" href="http://www.gtk.org">www.gtk.org</a></code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>AUTHOR</h2>
<p> <code>exo-csource</code> was written by Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<p> This manual page was provided by Benedikt Meurer &lt;benny [at] xfce.org&gt;.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <a rel="nofollow" href="http://www.gtk.org">www.gtk.org</a></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gtk.org">http://www.gtk.org</a></dd></dl>
</dl>
<h2>Index</h2>
