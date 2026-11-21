---
title: "transform(1)"
name: "transform"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transform/"
description: "transform – apply geometric transformations to the input."
---

<h2>SYNOPSIS</h2>
<p> <code>transform</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;<i>file.gts</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>transform</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-r&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;rx=</code><i>ANGLE</i></dt>
<dd> Rotate around x-axis (<i>ANGLE</i> in degrees).</dd>
<dt><code>-m&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;ry=</code><i>ANGLE</i></dt>
<dd> Rotate around y-axis.</dd>
<dt><code>-m&nbsp;</code><i>ANGLE</i>,&nbsp;<code>&#8211;rz=</code><i>ANGLE</i></dt>
<dd> Rotate around z-axis.</dd>
<dt><code>-s&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;scale=</code><i>FACTOR</i></dt>
<dd> Scale by <i>FACTOR</i>.</dd>
<dt><code>-R&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sx=</code><i>FACTOR</i></dt>
<dd> Scale x-axis by <i>FACTOR</i>.</dd>
<dt><code>-M&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sy=</code><i>FACTOR</i></dt>
<dd> Scale y-axis by <i>FACTOR</i>.</dd>
<dt><code>-N&nbsp;</code><i>FACTOR</i>,&nbsp;<code>&#8211;sz=</code><i>FACTOR</i></dt>
<dd> Scale z-axis by <i>FACTOR</i>.</dd>
<dt><code>-t&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;tx=</code><i>V</i></dt>
<dd> Translate of <i>V</i> along x-axis.</dd>
<dt><code>-u&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;ty=</code><i>V</i></dt>
<dd> Translate of <i>V</i> along y-axis.</dd>
<dt><code>-w&nbsp;</code><i>V</i>,&nbsp;<code>&#8211;tz=</code><i>V</i></dt>
<dd> Translate of <i>V</i> along z-axis.</dd>
<dt><code>-i</code>,&nbsp;<code>&#8211;revert</code></dt>
<dd> Turn surface inside out.</dd>
<dt><code>-o</code>,&nbsp;<code>&#8211;normalize</code></dt>
<dd> Fit the resulting surface in a cube of size 1 centered at the origin.</dd>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></dt>
<dd> Print statistics about the surface.</dd>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></dt>
<dd> Display the help and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> transform was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
