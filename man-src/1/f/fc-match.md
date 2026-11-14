---
title: "fc-match(1)"
name: "fc-match"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-match/"
description: "fc-match – match available fonts"
---

<h2 class="name">NAME</h2>
<p> fc-match &#8211; match available fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>fc-match</code> [ <code>-asvVh</code> ] [ <code>&#8211;all</code> ] [ <code>&#8211;sort</code> ] [ <code>&#8211;verbose</code> ] [ <code> [ -f </code><i>format</i><code> ] [ &#8211;format </code><i>format</i><code> ] </code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;help</code> ] </p>
<p>&nbsp;[&nbsp;<i>pattern</i><code>&nbsp;<wbr>&nbsp;[&nbsp;</code><i>element</i><i>&#8230;</i><code>&nbsp;]&nbsp;<wbr>&nbsp;</code>&nbsp;]&nbsp;</p>
<h2>DESCRIPTION</h2>
<p> <code>fc-match</code> matches <i>pattern</i> (empty pattern by default) using the normal fontconfig matching rules to find the best font available. If <code>&#8211;sort</code> is given, the sorted list of best matching fonts is displayed. The <code>&#8211;all</code> option works like <code>&#8211;sort</code> except that no pruning is done on the list of fonts. </p>
<p> If any elements are specified, only those are printed. Otherwise short file name, family, and style are printed, unless verbose output is requested.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-a</code></p>
<dd> Displays sorted list of best matching fonts, but do not do any pruning on the list.</p>
<dt><code>-s</code></p>
<dd> Displays sorted list of best matching fonts.</p>
<dt><code>-v</code></p>
<dd> Print verbose output of the whole font pattern for each match, or <i>element</i>s if any is provided.</p>
<dt><code>-f</code></p>
<dd> Format output according to the format specifier <i>format</i>.</p>
<dt><code>-V</code></p>
<dd> Show version of the program and exit.</p>
<dt><code>-h</code></p>
<dd> Show summary of options.</p>
<dt><i>pattern</i></p>
<dd> Displays fonts matching <i>pattern</i> (uses empty pattern by default).</p>
<dt><i>element</i></p>
<dd> If set, the <i>element</i> property is displayed for matching fonts.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1) <code><a href="/docs/linux/man/3-fcfontmatch/">FcFontMatch</a></code>(3) <code><a href="/docs/linux/man/3-fcfontsort/">FcFontSort</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-pattern/">fc-pattern</a></code>(1) <code><a href="/docs/linux/man/1-fc-query/">fc-query</a></code>(1) <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was updated by Patrick Lam &lt;plam [at] csail.mit.edu&gt;. </p>
<h2>Index</h2>
