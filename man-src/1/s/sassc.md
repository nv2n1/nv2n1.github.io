---
title: "sassc(1)"
name: "sassc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sassc/"
description: "sassc: – Sass compiles CSS from SASS or SCSS files"
---

<h2>SYNOPSIS</h2>
<p> <code>sassc</code> [<i>,options/</i>] [<i>,INPUT/</i>] [<i>,OUTPUT/</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;stdin</code></dt>
<dd> Read input from standard input instead of an input file.</dd>
<dt><code>-t</code>, <code>&#8211;style</code> NAME</dt>
<dd> Output style. Can be: nested, expanded, compact, compressed.</dd>
<dt><code>-l</code>, <code>&#8211;line-numbers</code></dt>
<dd> Emit comments showing original line numbers.</dd>
<dt> <code>&#8211;line-comments</code></dt>
<dt><code>-I</code>, <code>&#8211;load-path</code> PATH</dt>
<dd>
</dd><dd>Set Sass import path.</dd>
<dt><code>-P</code>, <code>&#8211;plugin-path</code> PATH</dt>
<dd> Set path to autoload plugins.</dd>
<dt><code>-m</code>, <code>&#8211;sourcemap</code>[=<i>,TYPE/</i>]</dt>
<dd> Emit source map (auto or inline).</dd>
<dt><code>-M</code>, <code>&#8211;omit-map-comment</code></dt>
<dd> Omits the source map url comment.</dd>
<dt><code>-p</code>, <code>&#8211;precision</code></dt>
<dd> Set the precision for numbers.</dd>
<dt><code>-a</code>, <code>&#8211;sass</code></dt>
<dd> Treat input as indented syntax.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display compiled versions.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display this help message.</dd></dl>
<p> libsass: 3.6.5 sass2scss: 1.1.1 sass: 3.5 </p>
