---
title: "psfxtable(1)"
name: "psfxtable"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psfxtable/"
description: "psfxtable – handle Unicode character tables for console fonts"
---

<h2 class="name">NAME</h2>
<p> psfxtable &#8211; handle Unicode character tables for console fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>psfxtable</code> [<code>-i</code> <i>infont</i>] [<code>-o</code> <i>outfont</i>] [<code>-it</code> <i>intable</i>] [<code>-ot</code> <i>outtable</i>] [<code>-nt</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>psfxtable</code> handles the embedded Unicode character table for .psf format console fonts. It reads a font and possibly a table and writes a font and/or a table. <code><a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a></code>(1), <code><a href="/docs/linux/man/1-psfgettable/">psfgettable</a></code>(1) and <code><a href="/docs/linux/man/1-psfstriptable/">psfstriptable</a></code>(1) are links to it. </p>
<p> Each of the filenames <i>infont</i>, <i>outfont</i>, <i>intable</i>, and <i>outtable</i> may be replaced by a single dash (-), in which case standard input or standard output is used. If no <i>-i</i> option is given, the font is read from standard input. If no <i>-it</i> or <i>-o</i> or <i>-ot</i> option is given, no input table is read or no output font or output table is written. </p>
<p> By default the output font (if any) will have a Unicode table when either the input font has one, or an explicit table (which overrides an input font table) has been provided. The option <i>-nt</i> causes output of a font without table. When <i>outfont</i> is requested it will get a psf1 header when infont has a psf1 header and <i>intable</i> does not have sequences and a psf2 header otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a></code>(1), <code><a href="/docs/linux/man/1-psfgettable/">psfgettable</a></code>(1), <code><a href="/docs/linux/man/1-psfstriptable/">psfstriptable</a></code>(1) </p>
<h2>Index</h2>
