---
title: "pnmcut(1)"
name: "pnmcut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmcut/"
description: "pnmcut – cut a rectangle out of a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmcut &#8211; cut a rectangle out of a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmcut</code> [<code>-left </code><i>leftcol</i>] [<code>-right </code><i>rightcol</i>] [<code>-top </code><i>toprow</i>] [<code>-bottom </code><i>bottomrow</i>] [<code>-width </code><i>width</i>] [<code>-height </code><i>height</i>] [<code>-pad</code>] [<code>-verbose</code>] [ <i>left top width height</i> ] [<i>pnmfile</i>] </p>
<p> All options may be abbreviated to the shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PBM, PGM, or PPM image as input. Extracts the specified rectangle, and produces the same kind of image as output. </p>
<p> There are two ways to specify the rectangle to cut: arguments and options. Options are easier to remember and read, more expressive, and allow you to use defaults. Arguments were the only way available before July 2000. </p>
<p> If you use both options and arguments, the two specifications get mixed in an unspecified way. </p>
<p> To use options, just code any mixture of the <code>-left</code>, <code>-right</code>, <code>-top</code>, <code>-bottom</code>, <code>-width</code>, and <code>-height</code> options. What you don&#8217;t specify defaults. It is an error to overspecify, i.e. to specify all three of <code>-left</code>, <code>-right</code>, and <code>-width</code> or <code>-top</code>, <code>-bottom</code>, and <code>-height</code>. </p>
<p> To use arguments, specify all four of the <i>left</i>, <i>top</i>, <i>width</i>, and <i>height</i> arguments. <i>left</i> and <i>top</i> have the same effect as specifying them as the argument of a <code>-left</code> or <code>-top</code> option, respectively. <i>width</i> and <i>height</i> have the same effect as specifying them as the argument of a <code>-width</code> or <code>-height</code> option, respectively, where they are positive. Where they are not positive, they have the same effect as specifying one less than the value as the argument to a <code>-right</code> or <code>-bottom</code> option, respectively. (E.g. <i>width </i> = 0 makes the cut go all the way to the right edge). Before July 2000, negative numbers were not allowed for <i>width</i> and <i>height</i>. </p>
<p> Input is from Standard Input if you don&#8217;t specify the input file <i>pnmfile</i>. </p>
<p> Output is to Standard Output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-left</code></p>
<dd> The column number of the leftmost column to be in the output. If a nonnegative number, it refers to columns numbered from 0 at the left, increasing to the right. If negative, it refers to columns numbered -1 at the right, decreasing to the left.</p>
<dt><code>-right</code></p>
<dd> The column number of the rightmost column to be in the output, numbered the same as for <code>-left.</code></p>
<dt><code>-top</code></p>
<dd> The row number of the topmost row to be in the output. If a nonnegative number it refers to rows numbered from 0 at the top, increasing downward. If negative, it refers to columns numbered -1 at the bottom, decreasing upward.</p>
<dt><code>-bottom</code></p>
<dd> The row number of the bottom-most row to be in the output, numbered the same as for <code>-top</code>.</p>
<dt><code>-width</code></p>
<dd> The number of columns to be in the output. Must be positive.</p>
<dt><code>-height</code></p>
<dd> The number of rows to be in the output. Must be positive.</p>
<dt><code>-pad</code></p>
<dd> If the rectangle you specify is not entirely within the input image, <code>pnmcut</code> fails unless you also specify <code>-pad</code>. In that case, it pads the output with black up to the edges you specify. You can use this option if you need to have an image of certain dimensions and have an image of arbitrary dimensions. </p>
<p> <code>pnmpad</code> can also fill an image out to a specified dimension, and gives you more explicit control over the padding. </p>
<dt><code>-verbose</code></p>
<dd> Print information about the processing to Standard Error. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcrop/">pnmcrop</a></code>(1), <code><a href="/docs/linux/man/1-pnmpad/">pnmpad</a></code>(1), <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1), <code><a href="/docs/linux/man/1-pgmslice/">pgmslice</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
