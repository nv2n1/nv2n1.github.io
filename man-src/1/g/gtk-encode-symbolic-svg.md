---
title: "gtk-encode-symbolic-svg(1)"
name: "gtk-encode-symbolic-svg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-encode-symbolic-svg/"
description: "gtk-encode-symbolic-svg – Symbolic icon conversion utility"
---

<h2 class="name">NAME</h2>
<p> gtk-encode-symbolic-svg &#8211; Symbolic icon conversion utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-encode-symbolic-svg</code> [OPTION&#8230;] <i>PATH</i> <i>WIDTH</i>x<i>HEIGHT</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-encode-symbolic-svg</code></p>
<dd>converts symbolic svg icons into specially prepared png files. GTK+ can load and recolor these pngs, just like original svgs, but loading them is much faster. </p>
<p> <i>PATH</i> is the name of a symbolic svg file, <i>WIDTH</i>x<i>HEIGHT</i> are the desired dimensions for the generated png file. </p>
<p> To distinguish them from ordinary pngs, the generated files have the extension .symbolic.png.</p>
<h2>OPTIONS</h2>
<p> -o <i>DIRECTORY</i>, &#8211;output <i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Write png files to <i>DIRECTORY</i> instead of the current working directory.</dl>
<h2>Index</h2>
