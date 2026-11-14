---
title: "ppdi(1)"
name: "ppdi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppdi/"
description: "ppdi – import ppd files (deprecated)"
---

<h2 class="name">NAME</h2>
<p> ppdi &#8211; import ppd files (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>ppdi</code> [ <code>-I</code> <i>include-directory</i> ] [ <code>-o</code> <i>source-file</i> ] <i>ppd-file</i> [ &#8230; <i>ppd-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ppdi</code> imports one or more PPD files into a PPD compiler source file. Multiple languages of the same PPD file are merged into a single printer definition to facilitate accurate changes for all localizations. <code>This program is deprecated and will be removed in a future release of CUPS.</code></p>
<h2>OPTIONS</h2>
<p> <code>ppdi</code> supports the following options:</p>
<dl>
<dt><code>-I </code><i>include-directory</i></p>
<dd> Specifies an alternate include directory. Multiple <i>-I</i> options can be supplied to add additional directories.</p>
<dt><code>-o </code><i>source-file</i></p>
<dd> Specifies the PPD source file to update. If the source file does not exist, a new source file is created. Otherwise the existing file is merged with the new PPD file(s) on the command-line. If no source file is specified, the filename <i>ppdi.drv</i> is used.</dl>
<h2>NOTES</h2>
<p> PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppdc/">ppdc</a></code>(1), <code><a href="/docs/linux/man/1-ppdhtml/">ppdhtml</a></code>(1), <code><a href="/docs/linux/man/1-ppdmerge/">ppdmerge</a></code>(1), <code><a href="/docs/linux/man/1-ppdpo/">ppdpo</a></code>(1), <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
