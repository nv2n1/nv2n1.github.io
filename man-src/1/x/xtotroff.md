---
title: "xtotroff(1)"
name: "xtotroff"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xtotroff/"
description: "xtotroff – convert X font metrics into GNU troff font metrics"
---

<h2 class="name">NAME</h2>
<p> xtotroff &#8211; convert X font metrics into GNU troff font metrics </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-r </code><i>resolution</i> ] [ <code>-s </code><i>point-size</i> ] <i>font-map</i> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>xtotroff</i> takes a <i>font-map</i>, which maps <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1) fonts to X11 fonts, creates GNU <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) metric files for all fonts listed. Each line in <i>font-map</i> consists of a <i>groff</i> font name and an X font name as a X Logical Font Description (XLFD) pattern, separated by whitespace. Example: </p>
<dl>
<dt>
<dd> TB -adobe-times-bold-r-normal&#8211;*-*-*-*-p-*-iso8859-1</dl>
<p> The wildcards in the patterns are filled with the arguments to the <code>-r</code> and <code>-s</code> switches. If a font name is still ambiguous, <i>xtotroff</i> aborts.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-r</code><i>resolution</i></p>
<dd> Set the resolution for all font patterns in <i>font-map</i>. The value is used for both the horizontal and vertical resolution. If not specified, a resolution of 75dpi is assumed.</p>
<dt><code>-s</code><i>point-size</i></p>
<dd> Set the point size for all font patterns in <i>font-map</i>. If not specified, a size of 10pt is assumed.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>BUGS</h2>
<p> The only supported font encodings are &#8220;iso8859-1&#8221; and &#8220;adobe-fontspecific&#8221;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-gxditview/">gxditview</a></i>(1), <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) </p>
<h2>Index</h2>
