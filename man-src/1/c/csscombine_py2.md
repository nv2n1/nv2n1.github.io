---
title: "csscombine_py2(1)"
name: "csscombine_py2"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csscombine_py2/"
description: "csscombine – Utility to combine several stylesheets into one."
---

<h2 class="name">NAME</h2>
<p> <code>csscombine</code> &#8211; Utility to combine several stylesheets into one. </p>
<h2>SYNOPSIS</h2>
<p> <code>csscombine</code> [<i>options</i>&#8230;] <i>path</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>csscombine</code> may be used to combine several sheets loaded from a main sheet via <code>@import</code> rules. Nested <code>@import</code> rules are resolved since cssutils 0.9.6a1. </p>
<p> The resulting combined sheet (optionally minified) is sent to stdout, info and error messages are handled by the normal cssutils log. </p>
<p> <code>csscombine</code> may also be used to change the encoding of the stylesheet if a target encoding is given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help message and exit.</p>
<dt><code>-m</code>, <code>&#8211;minify</code></p>
<dd> Saves minified version of combined files, default is false.</p>
<dt><code>-s</code><i> SOURCEENCODING</i>, <code>&#8211;sourceencoding</code>=<i>SOURCEENCODING</i></p>
<dd> Encoding of input, defaulting to &quot;css&quot;. If given, overwrites other encoding information like @charset declarations.</p>
<dt><code>-t</code><i> TARGETENCODING</i>, <code>&#8211;targetencoding</code>=<i>TARGETENCODING</i></p>
<dd> Encoding of output, defaulting to &quot;UTF-8&quot;.</p>
<dt><code>-u</code><i> URL</i>, <code>&#8211;url</code>=<i>URL</i></p>
<dd> <i>URL</i> to parse, path&#8230; is ignored if <i>URL</i> is given.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>/usr/share/doc/python-cssutils-doc/docs/html/docs/index.html</p>
<dd>
</dl>
<h2>Index</h2>
