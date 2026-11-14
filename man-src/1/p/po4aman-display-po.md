---
title: "po4aman-display-po(1)"
name: "po4aman-display-po"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4aman-display-po/"
description: "po4aman-display-po – display a translated man page according to a PO"
---

<h2 class="name">NAME</h2>
<p> po4aman-display-po &#8211; display a translated man page according to a PO </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>po4aman-display-po</code> <code>-p</code> <i>PO_FILE</i> [<code>-m</code>&nbsp;<wbr><i>MASTER_FILE</i>] [<code>-o</code>&nbsp;<wbr><i>PO4A_OPT</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>po4aman-display-po</code></p>
<dd>can be used by a translator who wants to check how the man page being translated in a PO will be displayed. </p>
<p> The manual page must be in one of the formats supported by the po4a&#8217;s <i>man</i> module. The manual page can be provided on the command line, or installed on the system. </p>
<p> Manual pages generated from other formats, like DocBook or POD, are not supported. See <code><a href="/docs/linux/man/1-po4apod-display-po/">po4apod-display-po</a></code>(1) for an equivalent supporting <i>POD</i> documents.</p>
<h2>OPTIONS</h2>
<p> <code>-p </code><i>PO_FILE</i></p>
<dl>
<dt>
<dd> The PO file containing the translations.</dl>
<p> <code>-m </code><i>MASTER_FILE</i></p>
<dl>
<dt>
<dd> The original man page. It can be the absolute or relative path to the original man page (gzipped or not), the name the man page or the name and section of the man page (using the man.section format). When the master document is not provided with the <code>-m</code> option, <code>po4aman-display-po</code> tries to find the original man page based on the line reference of the first string in the PO.</dl>
<p> <code>-o </code><i>PO4A_OPT</i></p>
<dl>
<dt>
<dd> Some options to pass to <code><a href="/docs/linux/man/1-po4a-translate/">po4a-translate</a></code>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-po4apod-display-po/">po4apod-display-po</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Thomas Huriaux </p>
<h2>Index</h2>
