---
title: "xml2pot(1)"
name: "xml2pot"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2pot/"
description: "xml2pot – Creates a PO template file from a DocBook XML file."
---

<h2 class="name">NAME</h2>
<p> xml2pot &#8211; Creates a PO template file from a DocBook XML file. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xml2pot</code> [<i>original-XML</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>xml2pot</code></p>
<dd>is a command-line tool that produces a gettext message template file from the DocBook XML file original-XML. The template file is sent to standard output. </p>
<p> The resulting template file can be used to create gettext message files (PO-files) for a variety of languages. These can then be used in conjunction with <code><a href="/docs/linux/man/1-po2xml/">po2xml</a></code>(1) to translate the original XML file into these other languages. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-po2xml/">po2xml</a>(1), <a href="/docs/linux/man/1-split2po/">split2po</a>(1), <a href="/docs/linux/man/1-swappo/">swappo</a>(1), <a href="/docs/linux/man/1-transxx/">transxx</a>(1)</p>
<h2>AUTHORS</h2>
<p> The PO XML tools were written by Stephan Kulow&lt;coolo [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
