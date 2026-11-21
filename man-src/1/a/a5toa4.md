---
title: "a5toa4(1)"
name: "a5toa4"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a5toa4/"
description: "a5toa4 – arrange A5 pages in a PDF onto A4 landscape paper"
---

<h2>SYNOPSIS</h2>
<p> <code>a5toa4</code> [<code>-b</code>|<code>-s</code>] [<code>-o</code>] <i>input.pdf</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> Arrange A5 pages in a PDF onto A4 landscape paper, either side-by-side (default) or as a booklet. </p>
<h2>OPTIONS</h2>
<h3>Processing options</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;booklet</code></dt>
<dd> Generate a booklet instead of only two pages side by side onto one page. The whole booklet will be one signature. </dd>
<dt><code>-s</code>, <code>&#8211;sidebyside</code></dt>
<dd> Generate only two pages side by side onto one page instead of a booklet. This is the default. </dd>
<dt><code>-o</code>, <code>&#8211;overwrite</code></dt>
<dd> Write the output to <i>input.pdf</i> instead of appending &quot;-sidebyside.pdf&quot; or &quot;-booklet.pdf&quot; to the basename of <i>input.pdf</i>. </dd>
</dl>
<h3>Getting help</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print a help message.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version information. </dd>
</dl>
<h2>AUTHORS</h2>
<p> <code>a5toa4</code> was written by Markus Kohm. </p>
<h2>COPYRIGHT</h2>
<p> <code>a5toa4</code> is distributed under the conditions of the LaTeX Project Public License, either version 1.3c or (at your option) any later version.. </p>
