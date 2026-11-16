---
title: "check-language-support(1)"
name: "check-language-support"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check-language-support/"
description: "check-language-support – returns the list of missing packages in order to provide a complete language environment"
---

<h2 class="name">NAME</h2>
<p> <code>check-language-support</code> &#8211; returns the list of missing packages in order to provide a complete language environment </p>
<h2>SYNOPSIS</h2>
<p> <code>check-language-support</code> [<i>options</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-l</code> LANGUAGE, <code>&#8211;language</code>=<i>LANGUAGE</i></dt>
<dd> target language code &#8211; if omitted, check for all languages on the system</dd>
<dt><code>-d</code> DATADIR, <code>&#8211;datadir</code>=<i>DATADIR</i></dt>
<dd> use an alternative data directory instead of the default <code>/usr/share/language-selector</code></dd>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> check all available languages</dd>
<dt><code>&#8211;show-installed</code></dt>
<dd> show installed packages as well as missing ones</dd></dl>
<h2>AUTHOR</h2>
<p> This manpage has been written by Arne Goetje &lt;arne [at] ubuntu.com&gt; </p>
<h2>Index</h2>
