---
title: "dvi2fax(1)"
name: "dvi2fax"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvi2fax/"
description: "dvi2fax – convert a TeX DVI file to G3 fax format"
---

<h2 class="name">NAME</h2>
<p> dvi2fax &#8211; convert a TeX DVI file to G3 fax format </p>
<h2>SYNOPSIS</h2>
<p> <code>dvi2fax</code> [<code>-hi</code>|<code>-lo</code>] <i>file</i>[.dvi] [<i>options for dvips</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dvi2fax</code> uses <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1) to convert a TeX DVI file to PostScript, then <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to convert the PostScript to G3 fax file format.</p>
<h2>OPTIONS</h2>
<p> <code>-hi</code> use high fax resolution (204&#215;196 dpi) (default). </p>
<p> <code>-lo</code> use low fax resolution (204&#215;98). </p>
<p> <code>dvips</code> options can follow the file name.</p>
<h2>EXAMPLE</h2>
<p> Example: dvi2fax foo -l 2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1). </p>
<h2>Index</h2>
