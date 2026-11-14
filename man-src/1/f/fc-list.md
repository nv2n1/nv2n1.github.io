---
title: "fc-list(1)"
name: "fc-list"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-list/"
description: "fc-list – list available fonts"
---

<h2 class="name">NAME</h2>
<p> fc-list &#8211; list available fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>fc-list</code> [ <code>-vVh</code> ] [ <code>&#8211;verbose</code> ] [ <code> [ -f </code><i>format</i><code> ] [ &#8211;format </code><i>format</i><code> ] </code> ] [ <code> [ -q ] [ &#8211;quiet ] </code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;help</code> ] </p>
<p>&nbsp;[&nbsp;<i>pattern</i><code>&nbsp;<wbr>&nbsp;[&nbsp;</code><i>element</i><i>&#8230;</i><code>&nbsp;]&nbsp;<wbr>&nbsp;</code>&nbsp;]&nbsp;</p>
<h2>DESCRIPTION</h2>
<p> <code>fc-list</code> lists fonts and styles available on the system for applications using fontconfig. If any elements are specified, only those are printed. Otherwise family and style are printed, unless verbose output is requested.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-v</code></p>
<dd> Print verbose output of the whole font pattern for each match, or <i>element</i>s if any is provided.</p>
<dt><code>-f</code></p>
<dd> Format output according to the format specifier <i>format</i>.</p>
<dt><code>-q</code></p>
<dd> Suppress all normal output. returns 1 as the error code if no fonts matched.</p>
<dt><code>-V</code></p>
<dd> Show version of the program and exit.</p>
<dt><code>-h</code></p>
<dd> Show summary of options.</p>
<dt><i>pattern</i></p>
<dd> If this argument is set, only fonts matching <i>pattern</i> are displayed.</p>
<dt><i>element</i></p>
<dd> If set, the <i>element</i> property is displayed for matching fonts.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>fc-list</code></p>
<dd> Lists all font faces.</p>
<dt><code>fc-list :lang=hi</code></p>
<dd> Lists font faces that cover Hindi.</p>
<dt><code>fc-list : family style file spacing</code></p>
<dd> Lists the filename and spacing value for each font face. &#8220;:&#8221; is an empty pattern that matches all fonts.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fc-match/">fc-match</a></code>(1) <code><a href="/docs/linux/man/3-fcfontlist/">FcFontList</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-pattern/">fc-pattern</a></code>(1) <code><a href="/docs/linux/man/1-fc-query/">fc-query</a></code>(1) <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Keith Packard &lt;keithp [at] keithp.com&gt; and Josselin Mouette &lt;joss [at] debian.org&gt;. </p>
<h2>Index</h2>
