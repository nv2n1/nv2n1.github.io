---
title: "split2po(1)"
name: "split2po"
section: "1"
letter: "s"
url: "/docs/linux/man/1-split2po/"
description: "split2po – Creates a po file from two DocBook XML files"
---

<h2 class="name">NAME</h2>
<p> split2po &#8211; Creates a po file from two DocBook XML files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>split2po</code> {<i>Original-XML</i><i>Translated-XML</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>split2po</code></p>
<dd>is a command-line tool that takes the two given DocBook XML files and produces a <code>gettext</code> message file (PO-file) that represents the changes between them. The resulting PO-file is sent to standard output. </p>
<p> translated-XML must be the result of translating original-XML into another language. It is this translation that the resulting PO-file will represent. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-po2xml/">po2xml</a>(1), <a href="/docs/linux/man/1-swappo/">swappo</a>(1), <a href="/docs/linux/man/1-transxx/">transxx</a>(1), <a href="/docs/linux/man/1-xml2pot/">xml2pot</a>(1)</p>
<h2>AUTHORS</h2>
<p> The PO XML tools were written by Stephan Kulow&lt;coolo [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
