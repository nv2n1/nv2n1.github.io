---
title: "paps(1)"
name: "paps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-paps/"
description: "paps – UTF-8 to PostScript converter using Pango"
---

<h2 class="name">NAME</h2>
<p> paps &#8211; UTF-8 to PostScript converter using Pango </p>
<h2>SYNOPSIS</h2>
<p> <code>paps</code> [<i>options</i>]<i> files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>paps</code> reads a UTF-8 encoded file and generates a PostScript language rendering of the file. The rendering is done by creating outline curves through the pango ft2 backend.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>&#8211;landscape</code></dt>
<dd> Landscape output. Default is portrait.</dd>
<dt><code>&#8211;columns=cl</code></dt>
<dd> Number of columns output. Default is 1.</dd>
<dt><code>&#8211;font=desc</code></dt>
<dd> Set the font description. Default is Monospace 12.</dd>
<dt><code>&#8211;rtl</code></dt>
<dd> Do rtl layout.</dd>
<dt><code>&#8211;paper ps</code></dt>
<dd> Choose paper size. Known paper sizes are legal, letter, a4. Default is A4.</dd>
<dt><code>&#8211;bottom-margin=bm</code></dt>
<dd> Set bottom margin in postscript points (1/72 inch). Default is 36.</dd>
<dt><code>&#8211;top-margin=tm</code></dt>
<dd> Set top margin. Default is 36.</dd>
<dt><code>&#8211;left-margin=lm</code></dt>
<dd> Set left margin. Default is 36.</dd>
<dt><code>&#8211;right-margin=rm</code></dt>
<dd> Set right margin. Default is 36.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;header</code></dt>
<dd> Draw page header for each page.</dd>
<dt><code>&#8211;markup</code></dt>
<dd> Interpret the text as pango markup.</dd>
<dt><code>&#8211;encoding=ENCODING</code></dt>
<dd> Assume the documentation encoding is ENCODING.</dd>
<dt><code>&#8211;lpi</code></dt>
<dd> Set the lines per inch. This determines the line spacing.</dd>
<dt><code>&#8211;cpi</code></dt>
<dd> Set the characters per inch. This is an alternative method of specifying the font size.</dd>
<dt><code>&#8211;stretch-chars</code></dt>
<dd> Indicates that characters should be stretched in the y-direction to fill up their vertical space. This is similar to the texttops behaviour.
</dd></dl>
<h2>AUTHOR</h2>
<p> paps was written by Dov Grobgeld &lt;dov.grobgeld [at] gmail.com&gt;. </p>
<p> This manual page was written by Lior Kaplan &lt;kaplan [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
