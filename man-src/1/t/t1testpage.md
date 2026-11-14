---
title: "t1testpage(1)"
name: "t1testpage"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1testpage/"
description: "t1testpage – create a PostScript proof for a Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1testpage &#8211; create a PostScript proof for a Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1testpage</code> [<i>font&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>T1testpage</code> creates a PostScript proof document for the specified Type 1 font file and writes it to the standard output. The proof shows every glyph in the font, including its glyph name and encoding. The <i>font</i> argument should be the name of a PFA or PFB font file. If more than one <i>font</i> is given, the output proof contains all the fonts in order. If <i>font</i> is omitted, t1testpage will read a font file from the standard input. </p>
<p> T1testpage is preliminary software.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code> <i>glyphs</i>, <code>&#8211;glyph=</code><i>glyphs</i></p>
<dd> Print only glyphs matching <i>glyphs</i>. The argument is a glyph pattern, using shell-like matching rules; thus, <code>-g </code>&#8216;A*&#8217; will match the glyphs &#8216;A&#8217;, &#8216;Atilde&#8217;, and &#8216;Ampersand&#8217;, among others. You can give this option multiple times, or supply multiple space-separated patterns in a single option. </p>
<dt><code>-s</code>, <code>&#8211;smoke</code></p>
<dd> Print smoke proofs, one glyph per page. This option is preliminary. </p>
<dt><code>-o</code> <i>file</i>, <code>&#8211;output=</code><i>file</i></p>
<dd> Write the output proof to <i>file</i> instead of the standard output. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
