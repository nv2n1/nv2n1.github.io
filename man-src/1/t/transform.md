---
title: "transform(1)"
name: "transform"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transform/"
description: "transform – apply geometric transformations to the input."
---

<h2 class="name">NAME</h2>
<p> transform &#8211; apply geometric transformations to the input.</p>
<h2>SYNOPSIS</h2>
<p> <code>transform</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;<i>file.gts</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>transform</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-r&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;rx=</code><i>ANGLE</i></p>
<dd> Rotate around x-axis (<i>ANGLE</i> in degrees).</p>
<dt><code>-m&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;ry=</code><i>ANGLE</i></p>
<dd> Rotate around y-axis.</p>
<dt><code>-m&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;rz=</code><i>ANGLE</i></p>
<dd> Rotate around z-axis.</p>
<dt><code>-s&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;scale=</code><i>FACTOR</i></p>
<dd> Scale by <i>FACTOR</i>.</p>
<dt><code>-R&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sx=</code><i>FACTOR</i></p>
<dd> Scale x-axis by <i>FACTOR</i>.</p>
<dt><code>-M&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sy=</code><i>FACTOR</i></p>
<dd> Scale y-axis by <i>FACTOR</i>.</p>
<dt><code>-N&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sz=</code><i>FACTOR</i></p>
<dd> Scale z-axis by <i>FACTOR</i>.</p>
<dt><code>-t&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;tx=</code><i>V</i></p>
<dd> Translate of <i>V</i> along x-axis.</p>
<dt><code>-u&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;ty=</code><i>V</i></p>
<dd> Translate of <i>V</i> along y-axis.</p>
<dt><code>-w&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;tz=</code><i>V</i></p>
<dd> Translate of <i>V</i> along z-axis.</p>
<dt><code>-i</code>,&nbsp;<code>&#8211;revert</code></p>
<dd> Turn surface inside out.</p>
<dt><code>-o</code>,&nbsp;<code>&#8211;normalize</code></p>
<dd> Fit the resulting surface in a cube of size 1 centered at the origin.</p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Print statistics about the surface.</p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display the help and exit. </p>
</dl>
<h2>AUTHOR</h2>
<p> transform was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
