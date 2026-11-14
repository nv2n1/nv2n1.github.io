---
title: "nkf(1)"
name: "nkf"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nkf/"
description: "nkf – Network Kanji Filter"
---

<h2 class="name">NAME</h2>
<p> nkf &#8211; Network Kanji Filter </p>
<h2>SYNOPSIS</h2>
<p> nkf <code>[-butjnesliohrTVvwWJESZxXFfmMBOcdILg]</code> <code>[</code><i>file &#8230;</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Nkf</code> is a yet another kanji code converter among networks, hosts and terminals. It converts input kanji code to designated kanji code such as <font SIZE="-1">ISO-2022-JP</font>, Shift_JIS, EUC-JP, <font SIZE="-1">UTF-8</font>, <font SIZE="-1">UTF-16</font> or <font SIZE="-1">UTF-32</font>. </p>
<p> One of the most unique faculty of <code>nkf</code> is the guess of the input kanji encodings. It currently recognizes <font SIZE="-1">ISO-2022-JP</font>, Shift_JIS, EUC-JP, <font SIZE="-1">UTF-8</font>, <font SIZE="-1">UTF-16</font> and <font SIZE="-1">UTF-32</font>. So users needn&#8217;t set the input kanji code explicitly. </p>
<p> By default, X0201 kana is converted into X0208 kana. For X0201 kana, <font SIZE="-1">SO/SI</font>, <font SIZE="-1">SSO</font> and <font SIZE="-1">ESC-</font>(-I methods are supported. For automatic code detection, nkf assumes no X0201 kana in Shift_JIS. To accept X0201 in Shift_JIS, use <code>-X</code>, <code>-x</code> or <code>-S</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-J -S -E -W -W16 -W32 -j -s -e -w -w16 -w32</code></p>
<dd> Specify input and output encodings. Upper case is input. cf. &#8211;ic and &#8211;oc.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-J</code></p>
<dd> <font SIZE="-1">ISO-2022-JP</font> (<font SIZE="-1">JIS</font> code).</p>
<dt><code>-S</code></p>
<dd> Shift_JIS and <font SIZE="-1">JIS</font> X 0201 kana. EUC-JP is recognized as X0201 kana. Without <code>-x</code> flag, <font SIZE="-1">JIS</font> X 0201 Katakana (a.k.a.halfwidth kana) is converted into <font SIZE="-1">JIS</font> X 0208. If you use Windows, see Windows-31J (<font SIZE="-1">CP932</font>).</p>
<dt><code>-E</code></p>
<dd> EUC-JP.</p>
<dt><code>-W</code></p>
<dd> <font SIZE="-1">UTF-8N</font>.</p>
<dt><code>-W16[</code><font SIZE="-1"><code>BL</code></font><code>][0]</code></p>
<dd> <font SIZE="-1">UTF-16</font>. B or L gives whether Big Endian or Little Endian. 0 gives whther put <font SIZE="-1">BOM</font> or not.</p>
<dt><code>-W32[</code><font SIZE="-1"><code>BL</code></font><code>][0]</code></p>
<dd> <font SIZE="-1">UTF-32</font>. B or L gives whether Big Endian or Little Endian. 0 gives whther put <font SIZE="-1">BOM</font> or not.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-b -u</code></p>
<dd> Output is buffered (<font SIZE="-1">DEFAULT</font>), Output is unbuffered.</p>
<dt><code>-t</code></p>
<dd> No conversion.</p>
<dt><code>-i[@B]</code></p>
<dd> Specify the escape sequence for <font SIZE="-1">JIS</font> X 0208.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-i@</code></p>
<dd> Use <font SIZE="-1">ESC</font> ( @. (<font SIZE="-1">JIS</font> X 0208-1978)</p>
<dt><code>-iB</code></p>
<dd> Use <font SIZE="-1">ESC</font> ( B. (<font SIZE="-1">JIS</font> X 0208-1983/1990 <font SIZE="-1">DEFAULT</font>)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-o[</code><font SIZE="-1"><code>BJ</code></font><code>]</code></p>
<dd> Specify the escape sequence for <font SIZE="-1">US-ASCII/JIS</font> X 0201 Roman. (<font SIZE="-1">DEFAULT</font> B)</p>
<dt><code>-r</code></p>
<dd> {de/en}crypt <font SIZE="-1">ROT13/47</font></p>
<dt><code>-h[123] &#8211;hiragana &#8211;katakana &#8211;katakana-hiragana</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-h1 &#8211;hiragana</code></p>
<dd> Katakana to Hiragana conversion.</p>
<dt><code>-h2 &#8211;katakana</code></p>
<dd> Hiragana to Katakana conversion.</p>
<dt><code>-h3 &#8211;katakana-hiragana</code></p>
<dd> Katakana to Hiragana and Hiragana to Katakana conversion.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-T</code></p>
<dd> Text mode output (MS-DOS)</p>
<dt><code>-f[</code>m<code> [- </code>n<code>]]</code></p>
<dd> Folding on <i>m</i> length with <i>n</i> margin in a line. Without this option, fold length is 60 and fold margin is 10.</p>
<dt><code>-F</code></p>
<dd> New line preserving line folding.</p>
<dt><code>-Z[0-3]</code></p>
<dd> Convert X0208 alphabet (Fullwidth Alphabets) to <font SIZE="-1">ASCII</font>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-Z -Z0</code></p>
<dd> Convert X0208 alphabet to <font SIZE="-1">ASCII</font>.</p>
<dt><code>-Z1</code></p>
<dd> Convert X0208 kankaku to single <font SIZE="-1">ASCII</font> space.</p>
<dt><code>-Z2</code></p>
<dd> Convert X0208 kankaku to double <font SIZE="-1">ASCII</font> spaces.</p>
<dt><code>-Z3</code></p>
<dd> Replacing fullwidth &gt;, &lt;, &quot;, &amp; into &#8216;&amp;gt;&#8217;, &#8216;&amp;lt;&#8217;, &#8216;&amp;quot;&#8217;, &#8216;&amp;amp;&#8217; as in <font SIZE="-1">HTML</font>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-X -x</code></p>
<dd> With <code>-X</code> or without this option, X0201 is converted into X0208 Kana. With <code>-x</code>, try to preserve X0208 kana and do not convert X0201 kana to X0208. In <font SIZE="-1">JIS</font> output, <font SIZE="-1">ESC-</font>(-I is used. In <font SIZE="-1">EUC</font> output, <font SIZE="-1">SS2</font> is used.</p>
<dt><code>-B[0-2]</code></p>
<dd> Assume broken JIS-Kanji input, which lost <font SIZE="-1">ESC</font>. Useful when your site is using old B-News Nihongo patch.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-B1</code></p>
<dd> allows any chars after <font SIZE="-1">ESC-</font>( or <font SIZE="-1">ESC-$</font>.</p>
<dt><code>-B2</code></p>
<dd> force <font SIZE="-1">ASCII</font> after <font SIZE="-1">NL</font>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-I</code></p>
<dd> Replacing non iso-2022-jp char into a geta character (substitute character in Japanese).</p>
<dt><code>-m[</code><font SIZE="-1"><code>BQN0</code></font><code>]</code></p>
<dd> <font SIZE="-1">MIME</font> <font SIZE="-1">ISO-2022-JP/ISO8859-1</font> decode. (<font SIZE="-1">DEFAULT</font>) To see <font SIZE="-1">ISO8859-1</font> (Latin-1) -l is necessary.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-mB</code></p>
<dd> Decode <font SIZE="-1">MIME</font> base64 encoded stream. Remove header or other part before conversion.</p>
<dt><code>-mQ</code></p>
<dd> Decode <font SIZE="-1">MIME</font> quoted stream. &#8216;_&#8217; in quoted stream is converted to space.</p>
<dt><code>-mN</code></p>
<dd> Non-strict decoding. It allows line break in the middle of the base64 encoding.</p>
<dt><code>-m0</code></p>
<dd> No <font SIZE="-1">MIME</font> decode.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-M</code></p>
<dd> <font SIZE="-1">MIME</font> encode. Header style. All <font SIZE="-1">ASCII</font> code and control characters are intact.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-MB</code></p>
<dd> <font SIZE="-1">MIME</font> encode Base64 stream. Kanji conversion is performed before encoding, so this cannot be used as a picture encoder.</p>
<dt><code>-MQ</code></p>
<dd> Perform quoted encoding.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-l</code></p>
<dd> Input and output code is <font SIZE="-1">ISO8859-1</font> (Latin-1) and <font SIZE="-1">ISO-2022-JP</font>. <code>-s</code>, <code>-e</code> and <code>-x</code> are not compatible with this option.</p>
<dt><code>-L[uwm] -d -c</code></p>
<dd> Convert line breaks.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-Lu -d</code></p>
<dd> unix (<font SIZE="-1">LF</font>)</p>
<dt><code>-Lw -c</code></p>
<dd> windows (<font SIZE="-1">CRLF</font>)</p>
<dt><code>-Lm</code></p>
<dd> mac (<font SIZE="-1">CR</font>) </p>
<p> Without this option, nkf doesn&#8217;t convert line breaks.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;fj &#8211;unix &#8211;mac &#8211;msdos &#8211;windows</code></p>
<dd> Convert for these systems.</p>
<dt><code>&#8211;jis &#8211;euc &#8211;sjis &#8211;mime &#8211;base64</code></p>
<dd> Convert to named code.</p>
<dt><code>&#8211;jis-input &#8211;euc-input &#8211;sjis-input &#8211;mime-input &#8211;base64-input</code></p>
<dd> Assume input system</p>
<dt><code>&#8211;ic=</code>input codeset<code> &#8211;oc=</code>output codeset</p>
<dd> Set the input or output codeset. <font SIZE="-1">NKF</font> supports following codesets and those codeset names are case insensitive.</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">ISO-2022-JP</font></p>
<dd> a.k.a. <font SIZE="-1">RFC1468</font>, 7bit <font SIZE="-1">JIS</font>, <font SIZE="-1">JUNET</font></p>
<dt>EUC-JP (eucJP-nkf)</p>
<dd> a.k.a. <font SIZE="-1">AT&amp;T</font> <font SIZE="-1">JIS</font>, Japanese <font SIZE="-1">EUC</font>, <font SIZE="-1">UJIS</font></p>
<dt>eucJP-ascii</p>
<dd>
<dt>eucJP-ms</p>
<dd>
<dt><font SIZE="-1">CP51932</font></p>
<dd> Microsoft Version of EUC-JP.</p>
<dt>Shift_JIS</p>
<dd> a.k.a. <font SIZE="-1">SJIS</font>, MS_Kanji</p>
<dt>Windows-31J</p>
<dd> a.k.a. <font SIZE="-1">CP932</font></p>
<dt><font SIZE="-1">UTF-8</font></p>
<dd> same as <font SIZE="-1">UTF-8N</font></p>
<dt><font SIZE="-1">UTF-8N</font></p>
<dd> <font SIZE="-1">UTF-8</font> without <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-8-BOM</font></p>
<dd> <font SIZE="-1">UTF-8</font> with <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF8-MAC</font> (input only)</p>
<dd> decomposed <font SIZE="-1">UTF-8</font></p>
<dt><font SIZE="-1">UTF-16</font></p>
<dd> same as <font SIZE="-1">UTF-16BE</font></p>
<dt><font SIZE="-1">UTF-16BE</font></p>
<dd> <font SIZE="-1">UTF-16</font> Big Endian without <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-16BE-BOM</font></p>
<dd> <font SIZE="-1">UTF-16</font> Big Endian with <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-16LE</font></p>
<dd> <font SIZE="-1">UTF-16</font> Little Endian without <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-16LE-BOM</font></p>
<dd> <font SIZE="-1">UTF-16</font> Little Endian with <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-32</font></p>
<dd> same as <font SIZE="-1">UTF-32BE</font></p>
<dt><font SIZE="-1">UTF-32BE</font></p>
<dd> <font SIZE="-1">UTF-32</font> Big Endian without <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-32BE-BOM</font></p>
<dd> <font SIZE="-1">UTF-32</font> Big Endian with <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-32LE</font></p>
<dd> <font SIZE="-1">UTF-32</font> Little Endian without <font SIZE="-1">BOM</font></p>
<dt><font SIZE="-1">UTF-32LE-BOM</font></p>
<dd> <font SIZE="-1">UTF-32</font> Little Endian with <font SIZE="-1">BOM</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;fb-{skip, html, xml, perl, java, subchar}</code></p>
<dd> Specify the way that nkf handles unassigned characters. Without this option, &#8211;fb-skip is assumed.</p>
<dt><code>&#8211;prefix=</code>escape charactertarget character<code>..</code></p>
<dd> When nkf converts to Shift_JIS, nkf adds a specified escape character to specified 2nd byte of Shift_JIS characters. 1st byte of argument is the escape character and following bytes are target characters.</p>
<dt><code>&#8211;no-cp932ext</code></p>
<dd> Handle the characters extended in <font SIZE="-1">CP932</font> as unassigned characters.</p>
<dt><code>&#8211;no-best-fit-chars</code></p>
<dd> When Unicode to Encoded byte conversion, don&#8217;t convert characters which is not round trip safe. When Unicode to Unicode conversion, with this and -x option, nkf can be used as <font SIZE="-1">UTF</font> converter. (In other words, without this and -x option, nkf doesn&#8217;t save some characters) </p>
<p> When nkf converts strings that related to path, you should use this opion.</p>
<dt><code>&#8211;cap-input</code></p>
<dd> Decode hex encoded characters.</p>
<dt><code>&#8211;url-input</code></p>
<dd> Unescape percent escaped characters.</p>
<dt><code>&#8211;numchar-input</code></p>
<dd> Decode character reference, such as &#8220;&amp;#&#8230;.;&#8221;.</p>
<dt><code>&#8211;in-place[=</code><i></i><font SIZE="-1"><i>SUFFIX</i></font><i></i><code>]</code> <code>&#8211;overwrite[=</code><i></i><font SIZE="-1"><i>SUFFIX</i></font><i></i><code>]</code></p>
<dd> Overwrite <code>original</code> listed files by filtered result. </p>
<p> <code>Note</code> &#8211;overwrite preserves timestamps of original files.</p>
<dt><code>&#8211;guess=[12]</code></p>
<dd> Print guessed encoding and newline. (2 is default, 1 is only encoding)</p>
<dt><code>&#8211;help</code></p>
<dd> Print nkf&#8217;s help.</p>
<dt><code>&#8211;version</code></p>
<dd> Print nkf&#8217;s version.</p>
<dt><code>&#8212;</code></p>
<dd> Ignore rest of -option.</dl>
<h2>AUTHOR</h2>
<p> Copyright (c) 1987, Fujitsu <font SIZE="-1">LTD</font>. (Itaru <font SIZE="-1">ICHIKAWA</font>). </p>
<p> Copyright (c) 1996-2013, The nkf Project. </p>
<h2>Index</h2>
