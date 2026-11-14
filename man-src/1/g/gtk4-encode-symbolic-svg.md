---
title: "gtk4-encode-symbolic-svg(1)"
name: "gtk4-encode-symbolic-svg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk4-encode-symbolic-svg/"
description: "gtk4-encode-symbolic-svg – Symbolic icon conversion utility"
---

<h2 class="name">NAME</h2>
<p> gtk4-encode-symbolic-svg &#8211; Symbolic icon conversion utility </p>
<h2>SYNOPSIS</h2>
<pre>
<code>gtk4-encode-symbolic-svg</code> [OPTIONS...] &lt;PATH&gt; &lt;WIDTH&gt;x&lt;HEIGHT&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> <code>gtk4-encode-symbolic-svg</code> converts symbolic SVG icons into specially prepared PNG files. GTK can load and recolor these PNGs, just like original SVGs, but loading them is much faster. </p>
<p> <code>PATH</code> is the name of a symbolic SVG file, <code>WIDTH</code> x <code>HEIGHT</code> are the desired dimensions for the generated PNG file. </p>
<p> To distinguish them from ordinary PNGs, the generated files have the extension <code>.symbolic.png</code>.</p>
<h2>OPTIONS</h2>
<p> <code>-o, &#8211;output DIRECTORY</code> Write png files to <code>DIRECTORY</code> instead of the current working directory. </p>
<p> <code>&#8211;debug</code> Generate PNG files of the various channels during the conversion. If these files are not monochrome green, they are often helpful in pinpointing the problematic parts of the source SVG. </p>
<h2>Index</h2>
