---

title: "cvtenc(1)"
name: "cvtenc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvtenc/"
description: "cvtenc – file encoding converter"
---

<p> cvtenc - file encoding converter </p>
<h2>SYNOPSIS</h2>
<p> <code>cvtenc</code> [<code>-Encoding</code> <i>encoding</i>] [<code>-EscapeIn</code> <i>yes|NO</i>] [<code>-EscapeOut</code> <i>yes|NO</i>] <br/>
&nbsp;<wbr><i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> Converts a file encoded in a specified or default non-unicode encoding to unicode (UTF16), or, if the file is already in unicode, converts it to a specified or default non-unicode encoding. The converted text is printed to standard out. If the filename is a hyphen then this tool reads from standard input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Encoding</code><i> encoding</i></dt>
<dd> <p> Specify non-unicode encoding to be used. The direction of conversion depends on whether the file given as input is recognized as unicode (from the higher order bytes). To get a list of available encodings, enter &quot;list&quot; for the encoding. If this is not specified, the default encoding for the current locale is used. </p>
 </dd>
<dt><code>-EscapeIn</code><i>YES|NO</i></dt>
<dd> <p> Specify &#8216;-EscapeIn YES&#8217; (the default is &#8216;NO&#8217;) to parse the input for \u escape sequences (as in property lists). </p>
 </dd>
<dt><code>-EscapeOut</code><i>YES|NO</i></dt>
<dd> <p> Specify &#8216;-EscapeOut YES&#8217; (the default is &#8216;NO&#8217;) to generate \u escape sequences (as in property lists) in the output. Note, this might produce unexpected results for some encodings. </p>
 </dd>
<dt><code>-Unicode</code><i>IN|OUT</i></dt>
<dd> <p> Specify &#8216;-Unicode IN&#8217; (or &#8216;-Unicode OUT&#8217;) to control the direction of conversion rather than having the tool guess it on the basis of the content it reads. Using &#8216;-Unicode IN&#8217; means that the tool reads UTF16 data and writes C-String data, while using &#8216;-Unicode OUT&#8217; merans that the tool reads C-String data and writes UTF16 data. </p>
 </dd></dl>
<h2>HISTORY</h2>
<dl>
<dd> <p> Written in 2002. Minr update in 2010. </p>
<p> This manual page first appeared in gnustep-base 1.9.2 (March 2004). </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> <code>cvtenc</code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt; </p>
