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
<dt><code>&#8211;landscape</code></p>
<dd> Landscape output. Default is portrait.</p>
<dt><code>&#8211;columns=cl</code></p>
<dd> Number of columns output. Default is 1.</p>
<dt><code>&#8211;font=desc</code></p>
<dd> Set the font description. Default is Monospace 12.</p>
<dt><code>&#8211;rtl</code></p>
<dd> Do rtl layout.</p>
<dt><code>&#8211;paper ps</code></p>
<dd> Choose paper size. Known paper sizes are legal, letter, a4. Default is A4.</p>
<dt><code>&#8211;bottom-margin=bm</code></p>
<dd> Set bottom margin in postscript points (1/72 inch). Default is 36.</p>
<dt><code>&#8211;top-margin=tm</code></p>
<dd> Set top margin. Default is 36.</p>
<dt><code>&#8211;left-margin=lm</code></p>
<dd> Set left margin. Default is 36.</p>
<dt><code>&#8211;right-margin=rm</code></p>
<dd> Set right margin. Default is 36.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;header</code></p>
<dd> Draw page header for each page.</p>
<dt><code>&#8211;markup</code></p>
<dd> Interpret the text as pango markup.</p>
<dt><code>&#8211;encoding=ENCODING</code></p>
<dd> Assume the documentation encoding is ENCODING.</p>
<dt><code>&#8211;lpi</code></p>
<dd> Set the lines per inch. This determines the line spacing.</p>
<dt><code>&#8211;cpi</code></p>
<dd> Set the characters per inch. This is an alternative method of specifying the font size.</p>
<dt><code>&#8211;stretch-chars</code></p>
<dd> Indicates that characters should be stretched in the y-direction to fill up their vertical space. This is similar to the texttops behaviour.
</dl>
<h2>AUTHOR</h2>
<p> paps was written by Dov Grobgeld &lt;dov.grobgeld [at] gmail.com&gt;. </p>
<p> This manual page was written by Lior Kaplan &lt;kaplan [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
