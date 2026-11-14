---
title: "t1dotlessj(1)"
name: "t1dotlessj"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1dotlessj/"
description: "t1dotlessj – create a dotless-j PostScript Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1dotlessj &#8211; create a dotless-j PostScript Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1dotlessj</code> [OPTIONS&#8230;] <i>font</i> [<i>outputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>T1dotlessj</code> creates a PostScript Type~1 font whose only character is a dotless &#8216;j&#8217; matching the input font&#8217;s design. It works simply by removing the dot from the input font&#8217;s &#8216;j&#8217;. The output font has three characters: &#8216;.notdef&#8217;, &#8216;space&#8217;, and &#8216;uni0237&#8217;, where &#8216;uni0237&#8217; is the dotless &#8216;j&#8217;. The command fails if the input font already has a dotless &#8216;j&#8217; character, or if there seems to be no dot to remove. T1dotlessj writes the created PFA or PFB font to the standard output (but see the <code>&#8211;output</code> option); if no input file is supplied, it reads a PFA or PFB font from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;output</code>=<i>file</i>, <code>-o</code> <i>file</i></p>
<dd> Send output to <i>file</i> instead of standard output. </p>
<dt><code>&#8211;pfb</code>, <code>-b</code></p>
<dd> Output a PFB font. This is the default. </p>
<dt><code>&#8211;pfa</code>, <code>-a</code></p>
<dd> Output a PFA font. </p>
<dt><code>&#8211;name</code>=<i>name</i>, <code>-n</code> <i>name</i></p>
<dd> Set the output font&#8217;s PostScript name to <i>name</i>. The default is <i>InputFontName</i>LCDFJ. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not generate any error messages. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>RETURN VALUES</h2>
<p> <code>T1dotlessj</code> exits with one of the following values:</p>
<dl>
<dt>0</p>
<dd> A dotless-j font was successfully generated.</p>
<dt>1</p>
<dd> The font already contained a dotless-j character.</p>
<dt>2</p>
<dd> The font&#8217;s &quot;j&quot; character had no dot to remove.</p>
<dt>3</p>
<dd> The font had no &quot;j&quot; character.</p>
<dt>&gt;3</p>
<dd> An error occurred.</dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i></p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
