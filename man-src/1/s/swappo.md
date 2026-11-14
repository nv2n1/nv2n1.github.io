---
title: "swappo(1)"
name: "swappo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swappo/"
description: "swappo – swap msgid and msgstr fields in a PO file"
---

<h2 class="name">NAME</h2>
<p> swappo &#8211; swap msgid and msgstr fields in a PO file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>swappo</code> [<i>filename.po</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>swappo</code></p>
<dd>reads the given PO-file and swaps the msgid and msgstr fields for every message. The result is a new PO-file that translates in the opposite direction. For example, if PO-file translates from English to French, the new PO-file will translate from French to English. </p>
<p> The new PO-file will be written to standard output. The old PO-file will remain untouched. </p>
<p> This utility is part of the KDE Software Development Kit</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-po2xml/">po2xml</a>(1), <a href="/docs/linux/man/1-split2po/">split2po</a>(1), <a href="/docs/linux/man/1-transxx/">transxx</a>(1), <a href="/docs/linux/man/1-xml2pot/">xml2pot</a>(1)</p>
<h2>AUTHORS</h2>
<p> The PO-XML tools were written by Stephan Kulow&lt;coolo [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
