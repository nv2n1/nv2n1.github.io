---
title: "po4apod-display-po(1)"
name: "po4apod-display-po"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4apod-display-po/"
description: "po4apod-display-po – man display of a translated POD file according to a PO"
---

<h2 class="name">NAME</h2>
<p> po4apod-display-po &#8211; man display of a translated POD file according to a PO </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>po4apod-display-po</code> <code>-p&nbsp;<wbr></code> <i>PO_FILE</i> <code>-m&nbsp;<wbr></code> <i>POD_FILE</i> [<code>-o&nbsp;<wbr></code>&nbsp;<wbr><i>PO4A_OPT</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>po4apod-display-po</code></p>
<dd>can be used by a translator who wants to check how the man page, generated from a POD file, being translated in a PO will be displayed. Generally, POD file is only available in source package or embedded in Perl script.</p>
<h2>OPTIONS</h2>
<p> <code>-p </code><i>PO_FILE</i></p>
<dl>
<dt>
<dd> The PO file containing the translations.</dl>
<p> <code>-m </code><i>POD_FILE</i></p>
<dl>
<dt>
<dd> The original POD file used by po4a to generate PO file.</dl>
<p> <code>-o </code><i>PO4A_OPT</i></p>
<dl>
<dt>
<dd> Some options to pass to <code><a href="/docs/linux/man/1-po4a-translate/">po4a-translate</a></code>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-po4aman-display-po/">po4aman-display-po</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Florentin Duneau </p>
<h2>Index</h2>
