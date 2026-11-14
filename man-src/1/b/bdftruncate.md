---
title: "bdftruncate(1)"
name: "bdftruncate"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bdftruncate/"
description: "bdftruncate – generate truncated BDF font from ISO 10646-1-encoded BDF font"
---

<h2 class="name">NAME</h2>
<p> bdftruncate &#8211; generate truncated BDF font from ISO 10646-1-encoded BDF font </p>
<h2>SYNOPSIS</h2>
<p> <code>bdftruncate</code> <i>threshold</i> <code>&lt;</code> <i>source.bdf</i> <code>&gt;</code> <i>destination.bdf</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bdftruncate</code> allows one to generate from an ISO10646-1 encoded BDF font other ISO10646-1 BDF fonts in which all characters above a threshold code value are stored unencoded. This is often desirable because the Xlib API and X11 protocol data structures used for representing font metric information are extremely inefficient when handling sparsely populated fonts.</p>
<h2>EXAMPLE</h2>
<p> The command</p>
<dl>
<dt>
<dd> bdftruncate 0x3200 &lt; 6&#215;13.bdf &gt; 6x13t.bdf</dl>
<p> will generate the file 6x13t.bdf in which all glyphs with codes &gt;= 0x3200 will only be stored unencoded (i.e., they are encoded at codepoint -1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ucs2any/">ucs2any</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>bdftruncate</code> was written by Markus Kuhn. </p>
<p> Branden Robinson wrote this manual page, originally for the Debian Project. </p>
<h2>Index</h2>
