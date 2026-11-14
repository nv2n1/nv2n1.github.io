---
title: "kcc(1)"
name: "kcc"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcc/"
description: "kcc – Kanji code coverter with encoding auto detection"
---

<h2>NAME</h2>
<p> kcc &#8211; Kanji code coverter with encoding auto detection</p>
<h2>SYNOPSIS</h2>
<p> <code>kcc</code> [ <code>&#8211;</code><i>IO</i><code>chnvxz</code> ] [ <code>-b</code><i> bufsize</i> ] [<i> file </i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>kcc</code> is a filter that reads <i>file</i> sequencially, converts kanji encodings and output to stdou. If no file is specified, or specified <code>&#8211;</code> as filename, it read from stdin. You can specify kanji encodings for input/output. However, <code>kcc</code> detect input encodig automatically, if you don&#8217;t specify input encoding. </p>
<p> Available kanji encodings are <font SIZE="-1">JIS (7 bit and/or 8 bit), Shift</font> <font SIZE="-1">JIS</font><font SIZE="-1">EUC</font><font SIZE="-1">DEC</font>. For input encoding, you can mix when these are pair of one of <font SIZE="-1">EUC</font> <font SIZE="-1">DEC</font> or Shift <font SIZE="-1">JIS</font> and 7 bit <font SIZE="-1">JIS.</font> <font SIZE="-1"><code>SI</code></font>/<font SIZE="-1"><code>SO</code></font><font SIZE="-1">ESC</font>(I are recognized as halfwidth of <font SIZE="-1">JIS</font>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code><i>O</i></p>
<dd>
<dt><code>&#8211;</code><i>IO</i></p>
<dd> <i>I</i> for input kanji encoding¡¤<i>O</i> for output kanji encoding. When no input encoding specified, it will be detected automatically, and if both of input/output aren&#8217;t specified, output encoding is 7 bit <font SIZE="-1">JIS.</font></p>
<dt>
<dd> You can specify one of the followings for the input encoding option, <i>I.</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>e</code></p>
<dd> <font SIZE="-1">EUC</font>(available with 7 bit <font SIZE="-1">JIS</font> )</p>
<dt><code>d</code></p>
<dd> <font SIZE="-1">DEC</font>(available with 7 bit <font SIZE="-1">JIS</font> )</p>
<dt><code>s</code></p>
<dd> Shift <font SIZE="-1">JIS</font>(available with 7 bit <font SIZE="-1">JIS</font> )</p>
<dt><code>j</code>7<code> or </code>k</p>
<dd> 7 bit <font SIZE="-1">JIS</font></p>
<dt><code>8</code></p>
<dd> 8 bit <font SIZE="-1">JIS</font></dl>
</dl>
<dl>
<dt>
<dd> You can specify one of the followings for output encoding option, <i>O.</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>e</code></p>
<dd> <font SIZE="-1">EUC</font></p>
<dt><code>d</code></p>
<dd> <font SIZE="-1">DEC</font></p>
<dt><code>s</code></p>
<dd> Shift <font SIZE="-1">JIS</font></p>
<dt><code>j</code><i>XY</i> or <code>7</code><i>XY</i></p>
<dd> 7 bit <font SIZE="-1">JIS</font>(using<font SIZE="-1"><code>SI</code></font>/<font SIZE="-1"><code>SO</code></font> for <font SIZE="-1">JIS</font> kana designation)</p>
<dt><code>k</code><i>XY</i></p>
<dd> 7 bit <font SIZE="-1">JIS</font>(using<font SIZE="-1"><code>ESC</code></font><code>(I</code> for <font SIZE="-1">JIS</font> kana designation)</p>
<dt><code>8</code><i>XY</i></p>
<dd> 8 bit <font SIZE="-1">JIS</font></dl>
</dl>
<dl>
<dt>
<dd> By <i>XY</i> in <i>O</i> option, You can specify which escape sequence used in <font SIZE="-1">JIS</font> encoding. <code>BJ</code> is default. Supplimental kanji designation is fixed to <font SIZE="-1"><code>ESC</code></font><code>$(D</code></dl>
<dl>
<dt>
<dd>
<dl>
<dt><i>X</i></p>
<dd> Kanji is designated by:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>B</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>$B</code>(JIS X0208-1983)</p>
<dt><code>@</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>$@</code>(JIS X0208-1978)</p>
<dt><code>+</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>&amp;@</code><font SIZE="-1"><code>ESC</code></font><code>$B</code>(JIS X0212-1990)</dl>
</dl>
<dt><i>Y</i></p>
<dd> Alpha Numerical is designated by:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>B</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>(B</code>(ASCII)</p>
<dt><code>J</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>(J</code>(JIS Roman; JIS X0201)</p>
<dt><code>H</code></p>
<dd> <font SIZE="-1"><code>ESC</code></font><code>(H</code>(Swedish; strongly deprecated)</dl>
</dl>
</dl>
</dl>
<dl>
<dt><code>-v</code></p>
<dd> outputs result of input encoding detection to stderr.</p>
<dt><code>-x</code></p>
<dd> Extension mode. By auto detection of input encodings, recognize user-defined characters and extended character region ( out of range of <font SIZE="-1">EUC</font>, undefined halfwidth kana, control character, <font SIZE="-1">C1</font> area and/or extended character region Shift <font SIZE="-1">C1</font> <font SIZE="-1">JIS</font> ). Distinguish between <font SIZE="-1">DEC</font> and <font SIZE="-1">EUC</font> is done in this mode.</p>
<dt><code>-z</code></p>
<dd> Shrink mode. Don&#8217;t recognize halfwidth kana (except 7 bit <font SIZE="-1">JIS</font> ) with input encoding detection. With this option, accuracy of auto detection of input encodings becomes much better for file without halfwidth kana.</p>
<dt><code>-h</code></p>
<dd> Normally, When converted halfwidth kana to <font SIZE="-1">DEC</font> , it becomes fullwidth Katakana. With this option, it becomes Hiragana.</p>
<dt><code>-n</code></p>
<dd> user-defined characters, extended characters and supplimental kanji characters areconverted to fullwidth white box, and undefined region of halfwidth kana are converted to halfwidth centered dot.</p>
<dt><code>-b</code><i> bufsize</i></p>
<dd> specify buffer size. 8kbytes is default.</p>
<dt><code>-c</code></p>
<dd> don&#8217;t convert but check input encoding and print result to stdout. Different with normal auto-detection, whole contents of file is checked. However, when inconsistency of encodings is found, abort reading and print &quot;data&quot;. Options except <code>-x</code>¡¤<code>-z</code> are ignored.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>% kcc -e </code><i>file</p>
<dd> Input encoding are detect automatically, and output is in </i><font SIZE="-1"><i>EUC</i></font><i> encoding.</p>
<dt></i><code>% kcc -sj </code><i>file1 file2</p>
<dd> Two files in Shift </i><font SIZE="-1"><i>JIS</i></font><i> concatinated with converting to </i><font SIZE="-1"><i>JIS.</i></font><i></p>
<dt></i><code>% </code><i>command</i><code> | kcc -k+J</p>
<dd> output of </code><i>command are converted to </i> <font SIZE="-1">JIS</font>(<font SIZE="-1">JIS</font> JIS X0208 <font SIZE="-1">JIS</font> JIS Roman¡¤<font SIZE="-1"><code>ESC</code></font><code>(I</code> Halfwidth Kana <font SIZE="-1">JIS</font> )</p>
<dt><code>% kcc -c </code><i>file</p>
<dd> Encoding of contents of file</i> is detected(no conversion)</dl>
<h2>BUG</h2>
<p> Auto detection of input encoding is well done for normal case, however, it has the following problems. </p>
<p> 7 bit <font SIZE="-1">JIS</font> is recognized by escape sequence in certain. <font SIZE="-1">EUC</font> and <font SIZE="-1">DEC</font> are the same (refered as <font SIZE="-1">EUC</font> series). Halfwidth kana of 8 bit <font SIZE="-1">JIS</font> is the same as halfwidth kana of Shift <font SIZE="-1">JIS</font> (refered as Shift <font SIZE="-1">JIS</font> series). However, <font SIZE="-1">EUC</font> series and <font SIZE="-1">JIS</font> , which are both 8 bit encoding, are sharing the same regions widely. So, the problem in auto detection is detection of these 2 encodings. </p>
<p> Detection of <font SIZE="-1">EUC</font> series/Shift <font SIZE="-1">JIS</font> series is done in line by line, When it is found that it&#8217;s not Shift <font SIZE="-1">JIS</font> series, or it&#8217;s not <font SIZE="-1">EUC</font> series, encoding is determined. When inconsistensy found, it will be treated as &quot;data&quot; and contents of output is not guaranteed. </p>
<p> While determined between <font SIZE="-1">EUC</font> series/Shift <font SIZE="-1">JIS</font> series after 8bit code found, conversions are pending and put input data in buffer, however, buffer is fulled, it assumes it&#8217;s <font SIZE="-1">EUC</font> series and forces to start conversion. Rationale. Usually, we can assume that documents with kanji include <font SIZE="-1">JIS</font> non-kanji or <font SIZE="-1">JIS</font> first standard, it can be detected in certain if it is Shift <font SIZE="-1">JIS</font> , which does not share region with <font SIZE="-1">EUC.</font> So if it can&#8217;t be determined, it&#8217;s very likely to be <font SIZE="-1">EUC.</font> </p>
<p> 8 bit <font SIZE="-1">JIS</font> and it has always even number of halfwidth kana sequences, then it will be wrongly detected as <font SIZE="-1">EUC</font> kanji. Be ceraful. </p>
<p> If input encoding doesn&#8217;t have halfwidth kana, use <code>-z</code> and accuracy of detection become much better. This is because shared region are restricted to area of <font SIZE="-1">JIS</font> second standards. </p>
<p> Extended region of Shift <font SIZE="-1">JIS</font> user-defined area of <font SIZE="-1">EUC</font>, control characters <font SIZE="-1">C1</font> of <font SIZE="-1">EUC</font>, undefined region of halfwidth kana of <font SIZE="-1">EUC</font> are out of range of auto detection, so it will fails to detect encodings if input has these characters. Use <code>-x</code> option to specify extended mode, or specify input code.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1)</p>
<h2>NOTES</h2>
<p> Usually, user-defined characters, extended characters, supplimental kanji characters are mapped respectively. However characters that is out of range of extended characters become FCFC in hexadecimal when converted to Shift <font SIZE="-1">JIS.</font> Although control character region <font SIZE="-1">C1</font> of <font SIZE="-1">EUC</font> and <font SIZE="-1">DEC</font> remains when converted to <font SIZE="-1">JIS</font> , these will be deleted when converted to Shift <font SIZE="-1">JIS</font> Undefined area of halfwidth kana become halfwidth centered dot when convered to Shift <font SIZE="-1">JIS</font> Halfwidth kana become fullwidth kana when converted to <font SIZE="-1">DEC.</font> </p>
<p> When output is <font SIZE="-1">JIS</font> encoding, control characters such as newline, TAB, DEL and white space (halfwidth) will be output in ASCII mode. </p>
<p> When encoding of input is detected wrongly, or input undefined character for expected character sets, output is indefined. </p>
<p> This manual are translated by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt; for Debian system, but you can use it for any purpose. </p>
<h2>Index</h2>
