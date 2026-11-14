---
title: "cvtenc(1)"
name: "cvtenc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvtenc/"
description: "cvtenc – file encoding converter"
---

<h2>NAME</h2>
<p> cvtenc &#8211; file encoding converter </p>
<h2>SYNOPSIS</h2>
<p> <code>cvtenc</code> [<code>-Encoding</code> <i>encoding</i>] [<code>-EscapeIn</code> <i>yes|NO</i>] [<code>-EscapeOut</code> <i>yes|NO</i>]<br />
&nbsp;<wbr><i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> Converts a file encoded in a specified or default non-unicode encoding to unicode (UTF16), or, if the file is already in unicode, converts it to a specified or default non-unicode encoding. The converted text is printed to standard out. If the filename is a hyphen then this tool reads from standard input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Encoding</code> <i> encoding</i></p>
<dd> Specify non-unicode encoding to be used. The direction of conversion depends on whether the file given as input is recognized as unicode (from the higher order bytes). To get a list of available encodings, enter &quot;list&quot; for the encoding. If this is not specified, the default encoding for the current locale is used.</p>
<dt><code>-EscapeIn</code> <i>YES|NO</i></p>
<dd> Specify &#8216;-EscapeIn YES&#8217; (the default is &#8216;NO&#8217;) to parse the input for 
