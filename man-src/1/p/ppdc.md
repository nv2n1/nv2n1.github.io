---
title: "ppdc(1)"
name: "ppdc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppdc/"
description: "ppdc – cups ppd compiler (deprecated)"
---

<h2 class="name">NAME</h2>
<p> ppdc &#8211; cups ppd compiler (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>ppdc</code> [ <code>-D </code><i>name</i>[<code>=</code><i>value</i>] ] [ <code>-I</code> <i>include-directory</i> ] [ <code>-c</code> <i>message-catalog</i> ] [ <code>-d</code> <i>output-directory</i> ] [ <code>-l</code> <i>language(s)</i> ] [ <code>-m</code> ] [ <code>-t</code> ] [ <code>-v</code> ] [ <code>-z</code> ] [ <code>&#8211;cr</code> ] [ <code>&#8211;crlf</code> ] [ <code>&#8211;lf</code> ] <i>source-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ppdc</code> compiles PPDC source files into one or more PPD files. <code>This program is deprecated and will be removed in a future release of CUPS.</code></p>
<h2>OPTIONS</h2>
<p> <code>ppdc</code> supports the following options:</p>
<dl>
<dt><code>-D </code><i>name</i>[<code>=</code><i>value</i>]</p>
<dd> Sets the named variable for use in the source file. It is equivalent to using the <i>#define</i> directive in the source file.</p>
<dt><code>-I </code><i>include-directory</i></p>
<dd> Specifies an alternate include directory. Multiple <i>-I</i> options can be supplied to add additional directories.</p>
<dt><code>-c </code><i>message-catalog</i></p>
<dd> Specifies a single message catalog file in GNU gettext (filename.po) or Apple strings (filename.strings) format to be used for localization.</p>
<dt><code>-d </code><i>output-directory</i></p>
<dd> Specifies the output directory for PPD files. The default output directory is &quot;ppd&quot;.</p>
<dt><code>-l </code><i>language(s)</i></p>
<dd> Specifies one or more languages to use when localizing the PPD file(s). The default language is &quot;en&quot; (English). Separate multiple languages with commas, for example &quot;de_DE,en_UK,es_ES,es_MX,es_US,fr_CA,fr_FR,it_IT&quot; will create PPD files with German, UK English, Spanish (Spain, Mexico, and US), French (France and Canada), and Italian languages in each file.</p>
<dt><code>-m</code></p>
<dd> Specifies that the output filename should be based on the ModelName value instead of FileName or PCFileName.</p>
<dt><code>-t</code></p>
<dd> Specifies that PPD files should be tested instead of generated.</p>
<dt><code>-v</code></p>
<dd> Specifies verbose output, basically a running status of which files are being loaded or written. <code>-z</code> Generates compressed PPD files (filename.ppd.gz). The default is to generate uncompressed PPD files.</p>
<dt><code>&#8211;cr</code></p>
<dd>
<dt><code>&#8211;crlf</code></p>
<dd>
<dt><code>&#8211;lf</code></p>
<dd> Specifies the line ending to use &#8211; carriage return, carriage return and line feed, or line feed alone. The default is to use the line feed character alone.</dl>
<h2>NOTES</h2>
<p> PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppdhtml/">ppdhtml</a></code>(1), <code><a href="/docs/linux/man/1-ppdi/">ppdi</a></code>(1), <code><a href="/docs/linux/man/1-ppdmerge/">ppdmerge</a></code>(1), <code><a href="/docs/linux/man/1-ppdpo/">ppdpo</a></code>(1), <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
