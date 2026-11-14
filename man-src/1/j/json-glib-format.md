---
title: "json-glib-format(1)"
name: "json-glib-format"
section: "1"
letter: "j"
url: "/docs/linux/man/1-json-glib-format/"
description: "json-glib-format – JSON-GLib formatting tool"
---

<h2 class="name">NAME</h2>
<p> json-glib-format &#8211; JSON-GLib formatting tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>json-glib-format</code> [<code>-h</code>,&nbsp;<wbr><code>&#8211;help</code>] [<code>&#8211;prettify</code>] [<code>&#8211;indent-spaces</code>&nbsp;<wbr><i>SPACES</i>] URI [URI&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>json-glib-format</code></p>
<dd>offers a simple command line interface to format JSON data. It reads a list or URIs, applies the spacified formatting rules on the JSON data, and outputs the formatted JSON to the standard output. </p>
<p> The resources to operate on are specified by the <i>URI</i> argument.</p>
<h2>COMMANDS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints help and exits.</dl>
<p> <code>-p</code>, <code>&#8211;prettify</code></p>
<dl>
<dt>
<dd> Prettifies the output, by adding spaces and indentation. This argument is useful to improve the readability of JSON data, at the expense of its size.</dl>
<p> <code>&#8211;indent-spaces</code> <i>SPACES</i></p>
<dl>
<dt>
<dd> Changes the number of spaces using to indent the JSON data from the default of 2. This argument is only considered if <code>&#8211;prettify</code> is used.</dl>
<h2>Index</h2>
