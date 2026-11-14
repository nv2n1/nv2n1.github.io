---
title: "abiword(1)"
name: "abiword"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abiword/"
description: "abiword — flexible cross-platform word processor"
---

<h2>NAME</h2>
<p> abiword &#8212; flexible cross-platform word processor</p>
<h2>SYNOPSIS</h2>
<p> <code>abiword</code> [<i>OPTIONS</i>] [<i>FILENAME&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> AbiWord is a full-featured, efficient word processing application suitable for a wide range of word processing tasks, and extensible with a variety of plugins. It integrates with <code><a href="/docs/linux/man/1-enchant/">enchant</a></code>(1) to provide spell-checking.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g </code><i>W</i>x<i>H</i>[+<i>X</i>+<i>Y</i>]<code>, &#8211;geometry=</code><i>W</i>x<i>H</i>[+<i>X</i>+<i>Y</i>]</p>
<dd> Specifies window geometry at startup.</p>
<dt><code>-E </code><i>PLUGIN</i><code>, &#8211;plugin=</code><i>PLUGIN</i></p>
<dd> Execute the specified plugin instead of the main application.</p>
<dt><code>&#8211;import-extension=</code><i>EXT</i></p>
<dd> Import the given file as if it had extension <i>EXT</i>, overriding automatic file type detection.</p>
<dt><code>-u </code><i>PROFILE</i><code>, &#8211;userprofile=</code><i>PROFILE</i></p>
<dd> Use <i>PROFILE</i> instead of the default ~/.AbiSuite/AbiWord.Profile to read and store settings.</p>
<dt><code>-t </code><i>DEST</i><code>, &#8211;to=</code><i>DEST</i></p>
<dd> Convert the given file to another format, writing the result to <i>DEST</i>. The format of <i>DEST</i> is determined by its extension.<br />
 See also <code>&#8211;to=</code><i>FORMAT</i> and <code>&#8211;to-name</code>.</p>
<dt><code>-t </code><i>FORMAT</i><code>, &#8211;to=</code><i>FORMAT</i></p>
<dd> Convert the given files(s) to the given format. Unless explicitly specified with <code>&#8211;to-name</code>, the original filename will be used (with a different extension, if necessary). See also <code>EXAMPLES</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>The more popular values for <i>FORMAT</i> include:</p>
<dd>
<table>
<tr VALIGN=top>
<td><code>abw</code></td>
<td> Abiword XML format (<code>zabw</code> for gzip, <code>bzabw</code> for bzip2 compression)
</td>
</tr>
<tr VALIGN=top>
<td><code>dbk</code></td>
<td>DocBook XML
</td>
</tr>
<tr VALIGN=top>
<td><code>doc</code></td>
<td>Microsoft Word binary format
</td>
</tr>
<tr VALIGN=top>
<td><code>docx</code></td>
<td> Office Open XML (newer Microsoft Word versions)
</td>
</tr>
<tr VALIGN=top>
<td><code>html</code></td>
<td>Hypertext Markup Language
</td>
</tr>
<tr VALIGN=top>
<td><code>kwd</code></td>
<td>KWord
</td>
</tr>
<tr VALIGN=top>
<td><code>odt</code></td>
<td>OpenDocument Text
</td>
</tr>
<tr VALIGN=top>
<td><code>pdf</code></td>
<td>Portable Document Format
</td>
</tr>
<tr VALIGN=top>
<td><code>rtf</code></td>
<td>Rich Text Format
</td>
</tr>
<tr VALIGN=top>
<td><code>sxw</code></td>
<td>OpenOffice.org Writer 1.0
</td>
</tr>
<tr VALIGN=top>
<td><code>txt</code></td>
<td>Plain text
</td>
</tr>
</table>
</dl>
</dl>
<dt><code>&#8211;to-name=</code><i>DEST</i></p>
<dd> Only useful in conjunction with <code>&#8211;to=</code><i>FORMAT</i>. Specifies where the converted document shall be written to.</p>
<dt><code>&#8211;verbose=</code><i>LEVEL</i></p>
<dd> Set level of verbosity [0-2], 2 giving the most detailed output.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a short help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Report the version of AbiWord.</dl>
<h2>EXAMPLES</h2>
<p> To convert the document <i>example.abw</i> to RTF: abiword &#8211;to=rtf example.abw The resulting file will be named <i>example.rtf</i>. To print a document: abiword &#8211;to=ps &#8211;to-name=fd://1 <i>FILENAME</i> | lp</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Bugzilla bug tracking system at &lt;<i><a rel="nofollow" href="http://bugzilla.abisource.com">http://bugzilla.abisource.com</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-enchant/">enchant</a></code>(1)</p>
<h2>HISTORY</h2>
<p> AbiWord was started in 1998 by AbiSource Inc., a company founded by SourceGear corporation. The initial plan was to build a free office suite named AbiSuite, encompassing word processing, spreadsheet and presentation applications. As they didn’t have a usable product when their venture capital was up, the code already developed (namely AbiWord) was made open source. AbiWord development was subsequently taken over by volunteers and is driven by the community to date. </p>
<h2>Index</h2>
