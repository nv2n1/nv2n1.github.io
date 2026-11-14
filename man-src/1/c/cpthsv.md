---
title: "cpthsv(1)"
name: "cpthsv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpthsv/"
description: "cpthsv – modify hue, saturation and colour value of GMT colour palette tables."
---

<h2 class="name">NAME</h2>
<p> cpthsv &#8211; modify hue, saturation and colour value of GMT colour palette tables. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cpthsv</code> -T&nbsp;<wbr><i>transform</i> [-h] [-o&nbsp;<wbr><i>file</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cpthsv</code> utility reads the RGB colour palette in the input, converts its colours to the HSV colour-space, modifies these values in some simple ways, then converts back to RGB colour space and outputs a cpt file. So <code>cpthsv</code> can (de)saturate, brighten, darken or hue-shift. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified. </p>
<p> The hue value is taken to be between 0 and 360, while the saturation and value components are taken to be between 0 and 1,</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-T</code>, <code>&#8211;transform</code> <i>string</i></p>
<dl>
<dt>
<dd> Specify a transformation to perform. One of <code>h</code>, <code>s</code> or <code>v</code> followed by a <i>number</i> and optional <i>operation</i>. The effect of the number depends on the operation: one of <code>x</code> (multiply by <i>number</i>), <code>%</code> (scale by percentage) or <code>+</code>/<code>&#8211;</code> (add or subtract value). An RGB colour with saturation 0.5 would be transformed to one with saturation 0.55 by applying <code>s1.1x</code> or <code>s110%</code> or <code>s0.05+</code>. If the operator is not given then <code>%</code> is assumed. </p>
<p> Transforms which take colours outside the HSV colour-space are permitted, the result is truncation (eg, increasing a saturation of 0.8 with <code>s0.3+</code> results in a saturation of 1.0). The exception is hue, which is taken modulo 360. </p>
<p> Multiple transforms can be applied by separating transforms with commas. This is to be preferred over multiple calls to the program since the conversion between colour-spaces is necessarily lossy. Multiple trnsformations are applied in the order given in the argument.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLE</h2>
<p> Lighten by 10% and desaturate by 20%: </p>
<dl>
<dt>
<dd>
<pre>
  cpthsv -v -T s80,v110 -o new.cpt old.cpt
</pre>
</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1). </p>
<h2>Index</h2>
