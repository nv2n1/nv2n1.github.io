---

title: "mm3d(1)"
name: "mm3d"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mm3d/"
description: "mm3d – Misfit Model 3D"
---

<p> mm3d &#8211; Misfit Model 3D</p>
<h2>SYNOPSIS</h2>
<p> <code>mm3d</code> [<i>options</i>]<i> files</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>mm3d</code> command. </p>
<p> <code>mm3d</code> is an OpenGL-based 3D model editor that works with triangle-based models. It supports multi-level undo, skeletal animations, simple texturing, scripting, command-line batch processing, and a plugin system for adding new model and image filters. Complete online help is included. It is designed to be easy to use and easy to extend with plugins and scripts.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. For a complete description, see the Info files.</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print command line help and exit</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Print version information and exit</dd>
<dt><code>-b, &#8211;batch</code></dt>
<dd> Batch mode (exit after processing command line)</dd>
<dt><code>-s, &#8211;save</code></dt>
<dd> Save command line changes to model files</dd>
<dt><code>&#8211;convert [format]</code></dt>
<dd> Save models to format [format]</dd>
<dt><code>&#8211;no-plugins</code></dt>
<dd> Disable all plugins</dd>
<dt><code>&#8211;no-plugin [foo]</code></dt>
<dd> Disable plugin [foo]</dd>
<dt><code>&#8211;sysinfo</code></dt>
<dd> Display system information (for bug reports)</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Display debug messages in console</dd>
<dt><code>&#8211;warnings</code></dt>
<dd> Display warning messages in console</dd>
<dt><code>&#8211;errors</code></dt>
<dd> Display error messages in console</dd>
<dt><code>&#8211;no-debug</code></dt>
<dd> Do not display debug messages in console</dd>
<dt><code>&#8211;no-warnings</code></dt>
<dd> Do not display warning messages in console</dd>
<dt><code>&#8211;no-errors</code></dt>
<dd> Do not display error messages in console</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-blender/">blender</a></code>(1), <code>wings3d</code>(1).</p>
<h2>AUTHOR</h2>
<p> mm3d was written by Kevin Worcester. </p>
<p> This manual page was written by G[:u]rkan Seng[:u]n &lt;gurkan [at] linuks.mine.nu&gt;, for the Debian project (but may be used by others). </p>
