---
title: "ppdmerge(1)"
name: "ppdmerge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppdmerge/"
description: "ppdmerge – merge ppd files (deprecated)"
---

<h2 class="name">NAME</h2>
<p> ppdmerge &#8211; merge ppd files (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>ppdmerge</code> [ <code>-o</code> <i>output-ppd-file</i> ] <i>ppd-file</i> <i>ppd-file</i> [ &#8230; <i>ppd-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ppdmerge</code> merges two or more PPD files into a single, multi-language PPD file. <code>This program is deprecated and will be removed in a future release of CUPS.</code></p>
<h2>OPTIONS</h2>
<p> <code>ppdmerge</code> supports the following options:</p>
<dl>
<dt><code>-o </code><i>output-ppd-file</i></p>
<dd> Specifies the PPD file to create. If not specified, the merged PPD file is written to the standard output. If the output file already exists, it is silently overwritten.</dl>
<h2>NOTES</h2>
<p> PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1). </p>
<p> <code>ppdmerge</code> does not check whether the merged PPD files are for the same device. Merging of different device PPDs will yield unpredictable results.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppdc/">ppdc</a></code>(1), <code><a href="/docs/linux/man/1-ppdhtml/">ppdhtml</a></code>(1), <code><a href="/docs/linux/man/1-ppdi/">ppdi</a></code>(1), <code><a href="/docs/linux/man/1-ppdpo/">ppdpo</a></code>(1), <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
