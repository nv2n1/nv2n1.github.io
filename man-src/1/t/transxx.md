---
title: "transxx(1)"
name: "transxx"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transxx/"
description: "transxx – Create a pseudo translated PO file from a PO template file"
---

<h2 class="name">NAME</h2>
<p> transxx &#8211; Create a pseudo translated PO file from a PO template file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>transxx</code> [<i>template.pot</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>transxx</code></p>
<dd>is a command-line tool that produces a basic fleshed-out PO-file from a PO-template file. Some of the formatting and structure of the msgid strings will be copied to the msgstr strings, but otherwise text will be translated to &#8220;xx&#8221;. </p>
<p> The fleshed-out PO-file is sent to standard output. </p>
<p> Running your software with the language &#8220;xx&#8221; will quickly show you any user visible strings that are not translatable. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>AUTHORS</h2>
<p> The PO-XML tools were written by Stephan Kulow&lt;coolo [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
