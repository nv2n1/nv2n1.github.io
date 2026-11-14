---
title: "dirfile-format(5)"
name: "dirfile-format"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dirfile-format/"
description: "dirfile-format — the dirfile database format specification file"
---

<p>dirfile-format &#8212; the dirfile database format specification file</p>
<h2>Description</h2>
<p>The <i>dirfile format</i> file fully specifies the raw and derived time streams and auxiliary information for a <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5) database. The format file is a case sensitive text file called <code>format</code> located in the dirfile directory. The explicit text encoding of the file is not specified by these standards, but must be 7-bit ASCII compatible. Examples of acceptable character encodings include all the ISO~8859 character sets (<i>i.e.</i> Latin-1 through Latin-10, among others), as well as the UTF-8 encoding of Unicode and UCS. </p>
<h2>Syntax</h2>
<p>The format file is composed of field specification lines and directive lines, optionally separated by blank lines or lines containing only whitespace. Lines are separated by the line-feed character (0x0A). Unless escaped (see below), the hash mark (<code>#</code>) is the comment delimiter; the comment delimiter, and any text following it to the end of the line, is ignored.</p>
<h3>Tokens</h3>
<p>Both field specification lines and directive lines consist of several tokens separated by whitespace. Whitespace consists of one or more whitespace characters. These are: space (0x20), horizontal tab (0x09), vertical tab (0x0B), form-feed (0x0C), and carriage return (0x0D). The first token of a directive line is always a <i>reserved word</i>. The first token of a field specification line is never a reserved word. Any amount of whitespace may precede the first token on a line. </p>
<p> Since tokens are separated by whitespace, to include a whitespace character in a token, it must either escaped by preceding it by a backslash character (<code>\</code>), or be replaced by a <i>character escape sequence</i> (see below), or else the token must be enclosed in quotation marks (). The quotation marks themselves will be stripped from the token. The <i>null-token</i> (that is, the token consisting of zero characters) may be specified by a pair of quotation marks with nothing between them (). To include a literal quotation mark in a token, it must be escaped (<code>\ ).</code> Similarly, a hash mark may be included in a token by including it in a quoted token or else by escaping it (<code>\#</code>), otherwise the hash mark will be understood as the comment delimiter. </p>
<p> It is a syntax error to have a line which contains unmatched quotation marks, or in which the last character is the backslash character. </p>
<p> Several characters when escaped by a preceding backslash character are interpreted as special characters in tokens. The character escape sequences are:</p>
<dl>
<dd>
<dl>
<dt><code></code></p>
<dd>an alert (bell) character (ASCII 0x07 / U+0007)</p>
<dt><code></code></p>
<dd>a backspace character (ASCII 0x08 / U+0008)</p>
<dt><code></code></p>
<dd>an escape character (ASCII 0x1B / U+001B)</p>
<dt><code></code></p>
<dd>a form-feed character (ASCII 0x0C / U+000C)</p>
<dt><code>
</code></p>
<dd>a line-feed character (ASCII 0x0A / U+000A)</p>
<dt><code></code></p>
<dd>a carriage return character (ASCII 0x0D / U+000D)</p>
<dt><code>	</code></p>
<dd>a horizontal tab character (ASCII 0x09 / U+0009)</p>
<dt><code></code></p>
<dd>a vertical tab character (ASCII 0x0B / U+000B)</p>
<dt><code>\</code></p>
<dd>a backslash character (ASCII 0x5C / U+005C)</p>
<dt><code>\</code><i>ooo</i></p>
<dd>the single byte given by the octal number <i>ooo</i>.</p>
<dt><code>
