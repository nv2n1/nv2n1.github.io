---
title: "splitfont(1)"
name: "splitfont"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splitfont/"
description: "splitfont – extract characters from an ISO-type font."
---

<h2 class="name">NAME</h2>
<p> splitfont &#8211; extract characters from an ISO-type font.</p>
<h2>SYNOPSIS</h2>
<p> <code>splitfont</code> <i>fontfile</i> <i>&lt;character range&gt;&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The command <code>splitfont</code> removes characters from a given font file; it removes all the specified characters from the named font file. </p>
<p> This works for Linux console fonts, without PSF headers, and containing just 256 characters. </p>
<p> The character range is of the form </p>
<dl>
<dt>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>17,23-30,
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) </p>
<h2>Index</h2>
