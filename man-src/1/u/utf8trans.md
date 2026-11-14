---
title: "utf8trans(1)"
name: "utf8trans"
section: "1"
letter: "u"
url: "/docs/linux/man/1-utf8trans/"
description: "utf8trans – Transliterate UTF-8 characters according to a table"
---

<h2>NAME</h2>
<p> utf8trans &#8211; Transliterate UTF-8 characters according to a table</p>
<h2>SYNOPSIS</h2>
<p> <code>utf8trans</code> <i>charmap</i> [<i>file</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>utf8trans</code> transliterates characters in the specified files (or standard input, if they are not specified) and writes the output to standard output. All input and output is in the UTF-8 encoding. </p>
<p> This program is usually used to render characters in Unicode text files as some markup escapes or ASCII transliterations. (It is not intended for general charset conversions.) It provides functionality similar to the character maps in XSLT 2.0 (XML Stylesheet Language &#8211; Transformations, version 2.0).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code>, <code>&#8211;modify</code></p>
<dd> Modifies the given files in-place with their transliterated output, instead of sending it to standard output. </p>
<p> This option is useful for efficient transliteration of many files at once.</p>
<dt><code>&#8211;help</code></p>
<dd> Show brief usage information and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version and exit.</dl>
<h2>USAGE</h2>
<p> The translation is done according to the rules in the &#8216;character map&#8217;, named in the file <i>charmap</i>. It has the following format:</p>
<dl>
<dt>1.</p>
<dd> Each line represents a translation entry, except for blank lines and comment lines, which are ignored.</p>
<dt>2.</p>
<dd> Any amount of whitespace (space or tab) may precede the start of an entry.</p>
<dt>3.</p>
<dd> Comment lines begin with #. Everything on the same line is ignored.</p>
<dt>4.</p>
<dd> Each entry consists of the Unicode codepoint of the character to translate, in hexadecimal, followed <i>one</i> space or tab, followed by the translation string, up to the end of the line.</p>
<dt>5.</p>
<dd> The translation string is taken literally, including any leading and trailing spaces (except the delimeter between the codepoint and the translation string), and all types of characters. The newline at the end is not included.</dl>
<p> The above format is intended to be restrictive, to keep <code>utf8trans</code> simple. But if a XML-based format is desired, there is a <i>xmlcharmap2utf8trans</i> script that comes with the docbook2X distribution, that converts character maps in XSLT 2.0 format to the <code>utf8trans</code> format.</p>
<h2>LIMITATIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>utf8trans</code> does not work with binary files, because malformed UTF-8 sequences in the input are substituted with U+FFFD characters. However, null characters in the input are handled correctly. This limitation may be removed in the future.</p>
<dt>&bull;</p>
<dd> There is no way to include a newline or null in the substitution string.</dl>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
