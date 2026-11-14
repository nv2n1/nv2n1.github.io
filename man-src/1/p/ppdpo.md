---
title: "ppdpo(1)"
name: "ppdpo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppdpo/"
description: "ppdpo – ppd message catalog generator (deprecated)"
---

<h2 class="name">NAME</h2>
<p> ppdpo &#8211; ppd message catalog generator (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>ppdpo</code> [ <code>-D </code><i>name</i>[<code>=</code><i>value</i>] ] [ <code>-I</code> <i>include-directory</i> ] [ <code>-o</code> <i>output-file</i> ] <i>source-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ppdpo</code> extracts UI strings from PPDC source files and updates either a GNU gettext or macOS strings format message catalog source file for translation. <code>This program is deprecated and will be removed in a future release of CUPS.</code></p>
<h2>OPTIONS</h2>
<p> <code>ppdpo</code> supports the following options:</p>
<dl>
<dt><code>-D </code><i>name</i>[<code>=</code><i>value</i>]</p>
<dd> Sets the named variable for use in the source file. It is equivalent to using the <i>#define</i> directive in the source file.</p>
<dt><code>-I </code><i>include-directory</i></p>
<dd> Specifies an alternate include directory. Multiple <i>-I</i> options can be supplied to add additional directories.</p>
<dt><code>-o </code><i>output-file</i></p>
<dd> Specifies the output file. The supported extensions are <i>.po</i> or <i>.po.gz</i> for GNU gettext format message catalogs and <i>.strings</i> for macOS strings files.</dl>
<h2>NOTES</h2>
<p> PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppdc/">ppdc</a></code>(1), <code><a href="/docs/linux/man/1-ppdhtml/">ppdhtml</a></code>(1), <code><a href="/docs/linux/man/1-ppdi/">ppdi</a></code>(1), <code><a href="/docs/linux/man/1-ppdmerge/">ppdmerge</a></code>(1), <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a>(5),</code> CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
