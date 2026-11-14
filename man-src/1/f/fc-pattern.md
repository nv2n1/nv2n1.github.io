---
title: "fc-pattern(1)"
name: "fc-pattern"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-pattern/"
description: "fc-pattern – parse and show pattern"
---

<h2 class="name">NAME</h2>
<p> fc-pattern &#8211; parse and show pattern </p>
<h2>SYNOPSIS</h2>
<p> <code>fc-pattern</code> [ <code>-cdVh</code> ] [ <code>&#8211;config</code> ] [ <code>&#8211;default</code> ] [ <code> [ -f </code><i>format</i><code> ] [ &#8211;format </code><i>format</i><code> ] </code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;help</code> ] </p>
<p>&nbsp;[&nbsp;<i>pattern</i><code>&nbsp;<wbr>&nbsp;[&nbsp;</code><i>element</i><i>&#8230;</i><code>&nbsp;]&nbsp;<wbr>&nbsp;</code>&nbsp;]&nbsp;</p>
<h2>DESCRIPTION</h2>
<p> <code>fc-pattern</code> parses <i>pattern</i> (empty pattern by default) and shows the parsed result. If <code>&#8211;config</code> is given, config substitution is performed on the pattern before being displayed. If <code>&#8211;default</code> is given, default substitution is performed on the pattern before being displayed. </p>
<p> If any elements are specified, only those are printed.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-c</code></p>
<dd> Perform config substitution on pattern.</p>
<dt><code>-d</code></p>
<dd> Perform default substitution on pattern.</p>
<dt><code>-f</code></p>
<dd> Format output according to the format specifier <i>format</i>.</p>
<dt><code>-V</code></p>
<dd> Show version of the program and exit.</p>
<dt><code>-h</code></p>
<dd> Show summary of options.</p>
<dt><i>pattern</i></p>
<dd> Parses and displays <i>pattern</i> (uses empty pattern by default).</p>
<dt><i>element</i></p>
<dd> If set, the <i>element</i> property is displayed for parsed pattern.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fcnameparse/">FcNameParse</a></code>(3) <code><a href="/docs/linux/man/3-fcconfigsubstitute/">FcConfigSubstitute</a></code>(3) <code><a href="/docs/linux/man/3-fcdefaultsubstitute/">FcDefaultSubstitute</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternprint/">FcPatternPrint</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1) <code><a href="/docs/linux/man/1-fc-match/">fc-match</a></code>(1) <code><a href="/docs/linux/man/1-fc-query/">fc-query</a></code>(1) <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was updated by Behdad Esfahbod &lt;behdad [at] behdad.org&gt;. </p>
<h2>Index</h2>
