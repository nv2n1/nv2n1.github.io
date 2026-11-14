---
title: "ucs2any(1)"
name: "ucs2any"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ucs2any/"
description: "ucs2any – generate BDF fonts containing subsets of ISO 10646-1 codepoints"
---

<h2 class="name">NAME</h2>
<p> ucs2any &#8211; generate BDF fonts containing subsets of ISO 10646-1 codepoints </p>
<h2>SYNOPSIS</h2>
<p> <code>ucs2any</code> [ <code>+d</code> | <code>-d</code> ] <i>source-name</i> { <i>mapping-file</i> <i>registry-encoding</i> } &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ucs2any</code> allows one to generate from an ISO 10646-1 encoded BDF font other BDF fonts in any possible encoding. This way, one can derive from a single ISO 10646-1 master font a whole set of 8-bit fonts in all ISO 8859 and various other encodings.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>+d</code></p>
<dd> puts DEC VT100 graphics characters in the C0 range (default for upright, character-cell fonts).</p>
<dt><code>-d</code></p>
<dd> omits DEC VT100 graphics characters from the C0 range (default for all font types except upright, character-cell fonts).</dl>
<h2>OPERANDS</h2>
<dl>
<dt><i>source-name</i></p>
<dd> is the name of an ISO 10646-1 encoded BDF file.</p>
<dt><i>mapping-file</i></p>
<dd> is the name of a character set table like those at <code>&lt;<a href="ftp://ftp.unicode.org/Public/MAPPINGS/">ftp://ftp.unicode.org/Public/MAPPINGS/</a>&gt;</code>. These files can also typically be found installed in the <i>/usr/share/fonts/X11/util</i> directory.</p>
<dt><i>registry-encoding</i></p>
<dd> are the CHARSET_REGISTRY and CHARSET_ENCODING field values for the font name (XLFD) of the target font, separated by a hyphen.</dl>
<p> Any number of <i>mapping-file</i> and <i>registry-encoding</i> operand pairs may be specified.</p>
<h2>EXAMPLE</h2>
<p> The command</p>
<dl>
<dt>
<dd> ucs2any 6&#215;13.bdf 8859-1.TXT iso8859-1 8859-2.TXT iso8859-2</dl>
<p> will generate the files <i>6&#215;13-iso8859-1.bdf</i> and <i>6&#215;13-iso8859-2.bdf</i>.</p>
<h2>FUTURE DIRECTIONS</h2>
<p> Hopefully a future release will have a facility similar to <code>ucs2any</code> built into the server, and reencode ISO 10646-1 on the fly, because storing the same fonts in many different encodings is clearly a waste of storage capacity.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bdftruncate/">bdftruncate</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>ucs2any</code> was written by Markus Kuhn. </p>
<p> Branden Robinson wrote this manual page, originally for the Debian Project. </p>
<h2>Index</h2>
