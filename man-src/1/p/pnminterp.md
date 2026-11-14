---
title: "pnminterp(1)"
name: "pnminterp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnminterp/"
description: "pamstretch – scale up a PNM or PAM image by interpolating between pixels"
---

<h2 class="name">NAME</h2>
<p> pamstretch &#8211; scale up a PNM or PAM image by interpolating between pixels </p>
<h2>SYNOPSIS</h2>
<p> <code>pamstretch</code> [<code>-xscale=</code><i>X</i>] [<code>-yscale=</code><i>Y</i>]<br />
 [<code>-blackedge</code>] [<code>-dropedge</code>] <i>N</i> [<i>infile</i>] </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> <code>pamstretch </code> scales up pictures by integer values, either vertically, horizontally, or both. <code>pamstretch </code> differs from <code>pnmscale</code> and <code>pnmenlarge</code> in that when it inserts the additional rows and columns, instead of making the new row or column a copy of its neighbor, <code>pamstretch</code> makes the new row or column an interpolation between its neighbors. In some images, this produces better looking output. </p>
<p> To scale up to non-integer pixel sizes, e.g. 2.5, try <code><a href="/docs/linux/man/1-pamstretch-gen/">pamstretch-gen</a></code>(1) instead. </p>
<p> Options let you select alternative methods of dealing with the right/bottom edges of the picture. Since the interpolation is done between the top-left corners of the scaled-up pixels, it&#8217;s not obvious what to do with the right/bottom edges. The default behaviour is to scale those up without interpolation (more precisely, the right edge is only interpolated vertically, and the bottom edge is only interpolated horizontally), but there are two other possibilities, selected by the <code>blackedge</code> and <code>dropedge</code> options. </p>
<h2>PARAMETERS</h2>
<p> The <i>N</i> parameter is the scale factor. It is valid only if you <i>don&#8217;t</i> specify <code>-xscale</code> or <code>-yscale</code>. In that case, <code>pamstretch</code> scales in both dimensions and by the scale factor <i>N</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-xscale=</code><i>X</i></p>
<dd> This is the horizontal scale factor. If you don&#8217;t specify this, but do specify a vertical scale factor, the horizontal scale factor is 1. </p>
<dt><code>-yscale=</code><i>Y</i></p>
<dd> This is the vertical scale factor. If you don&#8217;t specify this, but do specify a horizontal scale factor, the vertical scale factor is 1. </p>
</dl>
<dl>
<dt><code>-blackedge</code></p>
<dd> interpolate to black at right/bottom edges.</p>
<dt><code>-dropedge</code></p>
<dd> drop one (source) pixel at right/bottom edges. This is arguably more logical than the default behaviour, but it means producing output which is a slightly odd size. </p>
</dl>
<h2>BUGS</h2>
<p> Usually produces fairly ugly output for PBMs. For most PBM input you&#8217;ll probably want to reduce the `noise&#8217; first using something like <code><a href="/docs/linux/man/1-pnmnlfilt/">pnmnlfilt</a></code>(1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamstretch-gen/">pamstretch-gen</a></code>(1), <code><a href="/docs/linux/man/1-pnmenlarge/">pnmenlarge</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/1-pnmnlfilt/">pnmnlfilt</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Russell Marks (russell.marks [at] ntlworld.com). </p>
<h2>Index</h2>
