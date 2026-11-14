---
title: "cptcss(1)"
name: "cptcss"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptcss/"
description: "cptcss – create CSS fragment for colouring HTML tables."
---

<h2 class="name">NAME</h2>
<p> cptcss &#8211; create CSS fragment for colouring HTML tables. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cptcss</code> [-h] [-f&nbsp;<wbr><i>format</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cptcss</code> utility prints a fragment of CSS which can be used to colour the cells of an HTML table, the colours specified by a colour palette table (cpt) file. </p>
<p> The cpt file to use is specified by the final argument. If no cpt file is specified then the program will read from stdin. Output is written to stdout. </p>
<p> The input cpt should be a discrete (since the output CSS is) and each colour level in the file will lead to a CSS class directive for the &lt;td&gt; element. The class name can be modified from the default &quot;cptcss-%i&quot; by using the <code>-f</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-f</code>, <code>&#8211;format</code> <i>string</i></p>
<dl>
<dt>
<dd> The format to use for the &lt;td&gt; class name, which should include a single integer specifier &quot;%i&quot; which will enumerate the classes. The default value is &quot;cptcss-%i&quot;.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-svgcss3/">svgcss3</a></code>(1). </p>
<h2>Index</h2>
