---
title: "fc-validate(1)"
name: "fc-validate"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-validate/"
description: "fc-validate – validate font files"
---

<h2 class="name">NAME</h2>
<p> fc-validate &#8211; validate font files </p>
<h2>SYNOPSIS</h2>
<p> <code>fc-validate</code> [ <code>-Vhv</code> ] </p>
<p>&nbsp;[&nbsp;<code>&nbsp;[&nbsp;-i&nbsp;</code><i>index</i><code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;&#8211;index&nbsp;</code><i>index</i><code>&nbsp;]&nbsp;</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&nbsp;[&nbsp;-l&nbsp;</code><i>lang</i><code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;&#8211;lang&nbsp;</code><i>lang</i><code>&nbsp;]&nbsp;</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&#8211;verbose</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&#8211;version</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&#8211;help</code>&nbsp;]&nbsp;<wbr>&nbsp;<i>font-file</i><i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>fc-validate</code> validates <i>font-file</i>(s) if each fonts satisfies the language coverage according to the orthography files in fontconfig. If <code>&#8211;index</code> is given, only one face of each file is validated, otherwise all faces are validated.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-i</code></p>
<dd> Only query face indexed <i>index</i> of each file.</p>
<dt><code>-l</code></p>
<dd> Set <i>lang</i> as a language instead of current locale. this is used for <code>-m</code>.</p>
<dt><code>-v</code></p>
<dd> Show more detailed information.</p>
<dt><code>-V</code></p>
<dd> Show version of the program and exit.</p>
<dt><code>-h</code></p>
<dd> Show summary of options.</p>
<dt><i>font-file</i></p>
<dd> Query <i>font-file</i> for font faces.</dl>
<h2>RETURN CODES</h2>
<p> <code>fc-validate</code> returns error code 0 for successful parsing, or 1 if any errors occured or if at least one font face could not be opened.</p>
<h2>AUTHOR</h2>
<p> This manual page was updated by Akira TAGOH &lt;akira [at] tagoh.org&gt;. </p>
<h2>Index</h2>
