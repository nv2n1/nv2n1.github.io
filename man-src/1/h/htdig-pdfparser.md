---
title: "htdig-pdfparser(1)"
name: "htdig-pdfparser"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htdig-pdfparser/"
description: "htdig-pdfparser – parse a PDF document (wrapper script for htdig)"
---

<h2 class="name">NAME</h2>
<p> htdig-pdfparser &#8211; parse a PDF document (wrapper script for htdig) </p>
<h2>SYNOPSIS</h2>
<p> <code>htdig-pdfparser</code></p>
<h2>DESCRIPTION</h2>
<p> This script acts as a wrapper script for the htdig program. The exact program that htdig uses to search in pdf documents for index words, can be set in the htdig config file. Set the program by using the <i>debian_pdf_parser</i> directive.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>acrobat</code></p>
<dd> Use the acroread utility to parse PDF documents</p>
<dt><code>xpdf</code></p>
<dd> Use the pstotext utility, part of the xpdf package, to parse PDF documents</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> Stijn de Bekker &lt;stijn [at] debian.org&gt; </p>
<h2>Index</h2>
