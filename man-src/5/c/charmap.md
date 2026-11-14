---
title: "charmap(5)"
name: "charmap"
section: "5"
letter: "c"
url: "/docs/linux/man/5-charmap/"
description: "charmap – character set description file"
---

<p>charmap &#8211; character set description file</p>
<h2>Description</h2>
<p>A character set description (charmap) defines all available characters and their encodings in a character set. <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1) can use charmaps to create locale variants for different character sets.</p>
<h3>Syntax</h3>
<p>The charmap file starts with a header that may consist of the following keywords:</p>
<dl>
<dt>&lt;<i>code_set_name</i>&gt;</p>
<dd>is followed by the name of the character map.</p>
<dt>&lt;<i>comment_char</i>&gt;</p>
<dd>is followed by a character that will be used as the comment character for the rest of the file. It defaults to the number sign (#).</p>
<dt>&lt;<i>escape_char</i>&gt;</p>
<dd>is followed by a character that should be used as the escape character for the rest of the file to mark characters that should be interpreted in a special way. It defaults to the backslash (\).</p>
<dt>&lt;<i>mb_cur_max</i>&gt;</p>
<dd>is followed by the maximum number of bytes for a character. The default value is 1.</p>
<dt>&lt;<i>mb_cur_min</i>&gt;</p>
<dd>is followed by the minimum number of bytes for a character. This value must be less than or equal than &lt;<i>mb_cur_max</i>&gt;. If not specified, it defaults to &lt;<i>mb_cur_max</i>&gt;.</dl>
<p> The character set definition section starts with the keyword <i>CHARMAP</i> in the first column. </p>
<p> The following lines may have one of the two following forms to define the character set:</p>
<dl>
<dt>&lt;<i>character</i>&gt;&nbsp;<i>byte-sequence comment</i></p>
<dd>This form defines exactly one character and its byte sequence, <i>comment</i> being optional.</p>
<dt>&lt;<i>character</i>&gt;..&lt;<i>character</i>&gt;&nbsp;<i>byte-sequence comment</i></p>
<dd>This form defines a character range and its byte sequence, <i>comment</i> being optional.</dl>
<p> The character set definition section ends with the string <i>END CHARMAP</i>. </p>
<p> The character set definition section may optionally be followed by a section to define widths of characters. </p>
<p> The <i>WIDTH_DEFAULT</i> keyword can be used to define the default width for all characters not explicitly listed. The default character width is 1. </p>
<p> The width section for individual characters starts with the keyword <i>WIDTH</i> in the first column. </p>
<p> The following lines may have one of the two following forms to define the widths of the characters:</p>
<dl>
<dt>&lt;<i>character</i>&gt;&nbsp;<i>width</i></p>
<dd>This form defines the width of exactly one character.</p>
<dt>&lt;<i>character</i>&gt;&#8230;&lt;<i>character</i>&gt;&nbsp;<i>width</i></p>
<dd>This form defines the width for all the characters in the range.</dl>
<p> The width definition section ends with the string <i>END WIDTH</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/i18n/charmaps</i></p>
<dd>Usual default character map path.</dl>
<h2>Conforming To</h2>
<p>POSIX.2.</p>
<h2>Examples</h2>
<p>The Euro sign is defined as follows in the <i>UTF-8</i> charmap: </p>
<pre>&lt;U20AC&gt; /xe2/x82/xac EURO SIGN</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
