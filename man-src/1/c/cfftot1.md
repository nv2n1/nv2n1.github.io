---

title: "cfftot1(1)"
name: "cfftot1"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cfftot1/"
description: "cfftot1 – convert PostScript font from CFF to Type 1"
---

<p> <code>cfftot1</code> [<code>-a</code>] [<i>input</i> [<i>output</i>]]</p>
<p> <code>Cfftot1</code> converts PostScript font programs in the Compact Font Format (CFF) into Type 1 font programs in PFB or PFA format, preserving all hints that can be represented in Type 1. The input file should be a raw CFF file or a PostScript-flavored OpenType font. If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code><i></i>, <code>&#8211;pfa</code></dt>
<dd> Output font in ASCII PFA format. </dd>
<dt><code>-b</code><i></i>, <code>&#8211;pfb</code></dt>
<dd> Output font in binary PFB format. This is the default. </dd>
<dt><code>-n</code><i> name</i>, <code>&#8211;name</code><i> name</i></dt>
<dd> Output the CFF&#8217;s component font named <i>name</i>. CFF files can contain more than one font, although few do. Use this option to select a particular font from a multi-font collection. By default cfftot1 chooses the collection&#8217;s first font. </dd>
<dt><code>-o</code><i> file</i>, <code>&#8211;output</code><i> file</i></dt>
<dd> Write output font to <i>file</i> instead of the standard output. </dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Do not generate any error messages. </dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print usage information and exit. </dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print the version number and some short non-warranty information and exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i> </p>
<p> Adobe Technical Notes #5176, <i>The Compact Font Format Specification</i>, and #5177, <i>The Type 2 Charstring Format</i> </p>
<p> <i>OpenType Specification</i>, Version 1.4</p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
