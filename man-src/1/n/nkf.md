---

title: "nkf(1)"
name: "nkf"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nkf/"
description: "nkf – Network Kanji Filter"
---

<p> nkf &#8211; Network Kanji Filter </p>
<h2>SYNOPSIS</h2>
<p> nkf <code>[-butjnesliohrTVvwWJESZxXFfmMBOcdILg]</code> <code>[</code><i>file &#8230;</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Nkf</code> is a yet another kanji code converter among networks, hosts and terminals. It converts input kanji code to designated kanji code such as ISO-2022-JP, Shift_JIS, EUC-JP, UTF-8, UTF-16 or UTF-32. </p>
<p> One of the most unique faculty of <code>nkf</code> is the guess of the input kanji encodings. It currently recognizes ISO-2022-JP, Shift_JIS, EUC-JP, UTF-8, UTF-16 and UTF-32. So users needn&#8217;t set the input kanji code explicitly. </p>
<p> By default, X0201 kana is converted into X0208 kana. For X0201 kana, SO/SI, SSO and ESC-(-I methods are supported. For automatic code detection, nkf assumes no X0201 kana in Shift_JIS. To accept X0201 in Shift_JIS, use <code>-X</code>, <code>-x</code> or <code>-S</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-J -S -E -W -W16 -W32 -j -s -e -w -w16 -w32</code></dt>
<dd> Specify input and output encodings. Upper case is input. cf. &#8211;ic and &#8211;oc.</dd>
<dl>
<dl>
<dt><code>-J</code></dt>
<dd> ISO-2022-JP (JIS code).</dd>
<dt><code>-S</code></dt>
<dd> Shift_JIS and JIS X 0201 kana. EUC-JP is recognized as X0201 kana. Without <code>-x</code> flag, JIS X 0201 Katakana (a.k.a.halfwidth kana) is converted into JIS X 0208. If you use Windows, see Windows-31J (CP932).</dd>
<dt><code>-E</code></dt>
<dd> EUC-JP.</dd>
<dt><code>-W</code></dt>
<dd> UTF-8N.</dd>
<dt><code>-W16[</code><code>BL</code><code>][0]</code></dt>
<dd> UTF-16. B or L gives whether Big Endian or Little Endian. 0 gives whther put BOM or not.</dd>
<dt><code>-W32[</code><code>BL</code><code>][0]</code></dt>
<dd> UTF-32. B or L gives whether Big Endian or Little Endian. 0 gives whther put BOM or not.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-b -u</code></dt>
<dd> Output is buffered (DEFAULT), Output is unbuffered.</dd>
<dt><code>-t</code></dt>
<dd> No conversion.</dd>
<dt><code>-i[@B]</code></dt>
<dd> Specify the escape sequence for JIS X 0208.</dd>
<dl>
<dl>
<dt><code>-i@</code></dt>
<dd> Use ESC ( @. (JIS X 0208-1978)</dd>
<dt><code>-iB</code></dt>
<dd> Use ESC ( B. (JIS X 0208-1983/1990 DEFAULT)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-o[</code><code>BJ</code><code>]</code></dt>
<dd> Specify the escape sequence for US-ASCII/JIS X 0201 Roman. (DEFAULT B)</dd>
<dt><code>-r</code></dt>
<dd> {de/en}crypt ROT13/47</dd>
<dt><code>-h[123] &#8211;hiragana &#8211;katakana &#8211;katakana-hiragana</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>-h1 &#8211;hiragana</code></dt>
<dd> Katakana to Hiragana conversion.</dd>
<dt><code>-h2 &#8211;katakana</code></dt>
<dd> Hiragana to Katakana conversion.</dd>
<dt><code>-h3 &#8211;katakana-hiragana</code></dt>
<dd> Katakana to Hiragana and Hiragana to Katakana conversion.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-T</code></dt>
<dd> Text mode output (MS-DOS)</dd>
<dt><code>-f[</code>m<code> [- </code>n<code>]]</code></dt>
<dd> Folding on <i>m</i> length with <i>n</i> margin in a line. Without this option, fold length is 60 and fold margin is 10.</dd>
<dt><code>-F</code></dt>
<dd> New line preserving line folding.</dd>
<dt><code>-Z[0-3]</code></dt>
<dd> Convert X0208 alphabet (Fullwidth Alphabets) to ASCII.</dd>
<dl>
<dl>
<dt><code>-Z -Z0</code></dt>
<dd> Convert X0208 alphabet to ASCII.</dd>
<dt><code>-Z1</code></dt>
<dd> Convert X0208 kankaku to single ASCII space.</dd>
<dt><code>-Z2</code></dt>
<dd> Convert X0208 kankaku to double ASCII spaces.</dd>
<dt><code>-Z3</code></dt>
<dd> Replacing fullwidth &gt;, &lt;, &quot;, &amp; into &#8216;&amp;gt;&#8217;, &#8216;&amp;lt;&#8217;, &#8216;&amp;quot;&#8217;, &#8216;&amp;amp;&#8217; as in HTML.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-X -x</code></dt>
<dd> With <code>-X</code> or without this option, X0201 is converted into X0208 Kana. With <code>-x</code>, try to preserve X0208 kana and do not convert X0201 kana to X0208. In JIS output, ESC-(-I is used. In EUC output, SS2 is used.</dd>
<dt><code>-B[0-2]</code></dt>
<dd> Assume broken JIS-Kanji input, which lost ESC. Useful when your site is using old B-News Nihongo patch.</dd>
<dl>
<dl>
<dt><code>-B1</code></dt>
<dd> allows any chars after ESC-( or ESC-$.</dd>
<dt><code>-B2</code></dt>
<dd> force ASCII after NL.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-I</code></dt>
<dd> Replacing non iso-2022-jp char into a geta character (substitute character in Japanese).</dd>
<dt><code>-m[</code><code>BQN0</code><code>]</code></dt>
<dd> MIME ISO-2022-JP/ISO8859-1 decode. (DEFAULT) To see ISO8859-1 (Latin-1) -l is necessary.</dd>
<dl>
<dl>
<dt><code>-mB</code></dt>
<dd> Decode MIME base64 encoded stream. Remove header or other part before conversion.</dd>
<dt><code>-mQ</code></dt>
<dd> Decode MIME quoted stream. &#8216;_&#8217; in quoted stream is converted to space.</dd>
<dt><code>-mN</code></dt>
<dd> Non-strict decoding. It allows line break in the middle of the base64 encoding.</dd>
<dt><code>-m0</code></dt>
<dd> No MIME decode.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-M</code></dt>
<dd> MIME encode. Header style. All ASCII code and control characters are intact.</dd>
<dl>
<dl>
<dt><code>-MB</code></dt>
<dd> MIME encode Base64 stream. Kanji conversion is performed before encoding, so this cannot be used as a picture encoder.</dd>
<dt><code>-MQ</code></dt>
<dd> Perform quoted encoding.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-l</code></dt>
<dd> Input and output code is ISO8859-1 (Latin-1) and ISO-2022-JP. <code>-s</code>, <code>-e</code> and <code>-x</code> are not compatible with this option.</dd>
<dt><code>-L[uwm] -d -c</code></dt>
<dd> Convert line breaks.</dd>
<dl>
<dl>
<dt><code>-Lu -d</code></dt>
<dd> unix (LF)</dd>
<dt><code>-Lw -c</code></dt>
<dd> windows (CRLF)</dd>
<dt><code>-Lm</code></dt>
<dd> mac (CR) </dd>
<p> Without this option, nkf doesn&#8217;t convert line breaks.</dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;fj &#8211;unix &#8211;mac &#8211;msdos &#8211;windows</code></dt>
<dd> Convert for these systems.</dd>
<dt><code>&#8211;jis &#8211;euc &#8211;sjis &#8211;mime &#8211;base64</code></dt>
<dd> Convert to named code.</dd>
<dt><code>&#8211;jis-input &#8211;euc-input &#8211;sjis-input &#8211;mime-input &#8211;base64-input</code></dt>
<dd> Assume input system</dd>
<dt><code>&#8211;ic=</code>input codeset<code> &#8211;oc=</code>output codeset</dt>
<dd> Set the input or output codeset. NKF supports following codesets and those codeset names are case insensitive.</dd>
<dl>
<dl>
<dt>ISO-2022-JP</dt>
<dd> a.k.a. RFC1468, 7bit JIS, JUNET</dd>
<dt>EUC-JP (eucJP-nkf)</dt>
<dd> a.k.a. AT&amp;T JIS, Japanese EUC, UJIS</dd>
<dt>eucJP-ascii</dt>
<dd>
</dd><dt>eucJP-ms</dt>
<dd>
</dd><dt>CP51932</dt>
<dd> Microsoft Version of EUC-JP.</dd>
<dt>Shift_JIS</dt>
<dd> a.k.a. SJIS, MS_Kanji</dd>
<dt>Windows-31J</dt>
<dd> a.k.a. CP932</dd>
<dt>UTF-8</dt>
<dd> same as UTF-8N</dd>
<dt>UTF-8N</dt>
<dd> UTF-8 without BOM</dd>
<dt>UTF-8-BOM</dt>
<dd> UTF-8 with BOM</dd>
<dt>UTF8-MAC (input only)</dt>
<dd> decomposed UTF-8</dd>
<dt>UTF-16</dt>
<dd> same as UTF-16BE</dd>
<dt>UTF-16BE</dt>
<dd> UTF-16 Big Endian without BOM</dd>
<dt>UTF-16BE-BOM</dt>
<dd> UTF-16 Big Endian with BOM</dd>
<dt>UTF-16LE</dt>
<dd> UTF-16 Little Endian without BOM</dd>
<dt>UTF-16LE-BOM</dt>
<dd> UTF-16 Little Endian with BOM</dd>
<dt>UTF-32</dt>
<dd> same as UTF-32BE</dd>
<dt>UTF-32BE</dt>
<dd> UTF-32 Big Endian without BOM</dd>
<dt>UTF-32BE-BOM</dt>
<dd> UTF-32 Big Endian with BOM</dd>
<dt>UTF-32LE</dt>
<dd> UTF-32 Little Endian without BOM</dd>
<dt>UTF-32LE-BOM</dt>
<dd> UTF-32 Little Endian with BOM</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;fb-{skip, html, xml, perl, java, subchar}</code></dt>
<dd> Specify the way that nkf handles unassigned characters. Without this option, &#8211;fb-skip is assumed.</dd>
<dt><code>&#8211;prefix=</code>escape charactertarget character<code>..</code></dt>
<dd> When nkf converts to Shift_JIS, nkf adds a specified escape character to specified 2nd byte of Shift_JIS characters. 1st byte of argument is the escape character and following bytes are target characters.</dd>
<dt><code>&#8211;no-cp932ext</code></dt>
<dd> Handle the characters extended in CP932 as unassigned characters.</dd>
<dt><code>&#8211;no-best-fit-chars</code></dt>
<dd> When Unicode to Encoded byte conversion, don&#8217;t convert characters which is not round trip safe. When Unicode to Unicode conversion, with this and -x option, nkf can be used as UTF converter. (In other words, without this and -x option, nkf doesn&#8217;t save some characters) </dd>
<p> When nkf converts strings that related to path, you should use this opion.</p>
<dt><code>&#8211;cap-input</code></dt>
<dd> Decode hex encoded characters.</dd>
<dt><code>&#8211;url-input</code></dt>
<dd> Unescape percent escaped characters.</dd>
<dt><code>&#8211;numchar-input</code></dt>
<dd> Decode character reference, such as &#8220;&amp;#&#8230;.;&#8221;.</dd>
<dt><code>&#8211;in-place[=</code><i></i><i>SUFFIX</i><i></i><code>]</code> <code>&#8211;overwrite[=</code><i></i><i>SUFFIX</i><i></i><code>]</code></dt>
<dd> Overwrite <code>original</code> listed files by filtered result. </dd>
<p> <code>Note</code> &#8211;overwrite preserves timestamps of original files.</p>
<dt><code>&#8211;guess=[12]</code></dt>
<dd> Print guessed encoding and newline. (2 is default, 1 is only encoding)</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print nkf&#8217;s help.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print nkf&#8217;s version.</dd>
<dt><code>&#8212;</code></dt>
<dd> Ignore rest of -option.</dd></dl>
<h2>AUTHOR</h2>
<p> Copyright (c) 1987, Fujitsu LTD. (Itaru ICHIKAWA). </p>
<p> Copyright (c) 1996-2013, The nkf Project. </p>
