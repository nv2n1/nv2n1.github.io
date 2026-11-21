---

title: "preconv(1)"
name: "preconv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-preconv/"
description: "preconv – convert encoding of input files to something GNU troff understands"
---

<p> preconv &#8211; convert encoding of input files to something GNU troff understands </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-dr</code> ] [ <code>-D </code><i>default_encoding</i> ] [ <code>-e </code><i>encoding</i> ] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>preconv</code> reads <i>files</i> and converts its encoding(s) to a form GNU <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) can process, sending the data to standard output. Currently, this means ASCII characters and &#8216;\[uXXXX]&#8217; entities, where &#8216;XXXX&#8217; is a hexadecimal number with four to six digits, representing a Unicode input code. Normally, <code>preconv</code> should be invoked with the <code>-k</code> and <code>-K</code> options of <code>groff</code>.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-d</code></dt>
<dd> Emit debugging messages to standard error (mainly the used encoding).</dd>
<dt><code>-D</code><i>encoding</i></dt>
<dd> Specify default encoding if everything fails (see below).</dd>
<dt><code>-e</code><i>encoding</i></dt>
<dd> Specify input encoding explicitly, overriding all other methods. This corresponds to <code>groff</code>&#8216;s <code>-K</code><i>encoding</i> option. Without this switch, <code>preconv</code> uses the algorithm described below to select the input encoding.</dd>
<dt><code>&#8211;help</code></dt>
<dd> <code>-h</code> Print a help message and exit.</dd>
<dt><code>-r</code></dt>
<dd> Do not add .lf requests.</dd>
<dt><code>&#8211;version</code></dt>
<dd> <code>-v</code> Print the version number and exit.</dd></dl>
<h2>USAGE</h2>
<p> <code>preconv</code> tries to find the input encoding with the following algorithm.</p>
<dl>
<dt>1.</dt>
<dd> If the input encoding has been explicitly specified with option <code>-e</code>, use it.</dd>
<dt>2.</dt>
<dd> Otherwise, check whether the input starts with a <i>Byte Order Mark</i> (BOM, see below). If found, use it.</dd>
<dt>3.</dt>
<dd> Otherwise, check whether there is a known <i>coding tag</i> (see below) in either the first or second input line. If found, use it.</dd>
<dt>4</dt>
<dd> Finally, if the <code>uchardet</code> library (an encoding detector library available on most major distributions) is available on the system, use it to try to detect the encoding of the file.</dd>
<dt>5.</dt>
<dd> If everything fails, use a default encoding as given with option <code>-D</code>, by the current locale, or &#8216;latin1&#8217; if the locale is set to &#8216;C&#8217;, &#8216;POSIX&#8217;, or empty (in that order).</dd></dl>
<p> Note that the <code>groff</code> program supports a <i>GROFF_ENCODING</i> environment variable which is eventually expanded to option <code>-k</code>.</p>
<h3>Byte Order Mark</h3>
<p> The Unicode Standard defines character U+FEFF as the Byte Order Mark (BOM). On the other hand, value U+FFFE is guaranteed not be a Unicode character at all. This allows detection of the byte order within the data stream (either big-endian or little-endian), and the MIME encodings &#8216;UTF-16&#8217; and &#8216;UTF-32&#8217; mandate that the data stream starts with U+FEFF. Similarly, the data stream encoded as &#8216;UTF-8&#8217; might start with a BOM (to ease the conversion from and to UTF-16 and UTF-32). In all cases, the byte order mark is <i>not</i> part of the data but part of the encoding protocol; in other words, <code>preconv</code>&#8216;s output doesn&#8217;t contain it. </p>
<p> Note that U+FEFF not at the start of the input data actually is emitted; it has then the meaning of a &#8216;zero width no-break space&#8217; character &#8211; something not needed normally in <code>groff</code>.</p>
<h3>Coding Tags</h3>
<p> Editors which support more than a single character encoding need tags within the input files to mark the file&#8217;s encoding. While it is possible to guess the right input encoding with the help of heuristic algorithms for data which represents a greater amount of a natural language, it is still just a guess. Additionally, all algorithms fail easily for input which is either too short or doesn&#8217;t represent a natural language. </p>
<p> For these reasons, <code>preconv</code> supports the coding tag convention (with some restrictions) as used by <code>GNU Emacs</code> and <code>XEmacs</code> (and probably other programs too). </p>
<p> Coding tags in <code>GNU Emacs</code> and <code>XEmacs</code> are stored in so-called <i>File Variables</i>. <code>preconv</code> recognizes the following syntax form which must be put into a troff comment in the first or second line.</p>
<dl>
<dt>
</dt><dd>
<p> -*- <i>tag1</i>: <i>value1</i>; <i>tag2</i>: <i>value2</i>; &#8230; -*-</dd></dl>
<p> The only relevant tag for <code>preconv</code> is &#8216;coding&#8217; which can take the values listed below. Here an example line which tells <code>Emacs</code> to edit a file in troff mode, and to use latin2 as its encoding.</p>
<dl>
<dt>
</dt><dd>
<p> .\&quot; -*- mode: troff; coding: latin-2 -*-</dd></dl>
<p> The following list gives all MIME coding tags (either lowercase or uppercase) supported by <code>preconv</code>; this list is hard-coded in the source.</p>
<dl>
<dt>
</dt><dd>
<p> big5, cp1047, euc-jp, euc-kr, gb2312, iso-8859-1, iso-8859-2, iso-8859-5, iso-8859-7, iso-8859-9, iso-8859-13, iso-8859-15, koi8-r, us-ascii, utf-8, utf-16, utf-16be, utf-16le</dd></dl>
<p> In addition, the following hard-coded list of other tags is recognized which eventually map to values from the list above.</p>
<dl>
<dt>
</dt><dd>
<p> ascii, chinese-big5, chinese-euc, chinese-iso-8bit, cn-big5, cn-gb, cn-gb-2312, cp878, csascii, csisolatin1, cyrillic-iso-8bit, cyrillic-koi8, euc-china, euc-cn, euc-japan, euc-japan-1990, euc-korea, greek-iso-8bit, iso-10646/utf8, iso-10646/utf-8, iso-latin-1, iso-latin-2, iso-latin-5, iso-latin-7, iso-latin-9, japanese-euc, japanese-iso-8bit, jis8, koi8, korean-euc, korean-iso-8bit, latin-0, latin1, latin-1, latin-2, latin-5, latin-7, latin-9, mule-utf-8, mule-utf-16, mule-utf-16be, mule-utf-16-be, mule-utf-16be-with-signature, mule-utf-16le, mule-utf-16-le, mule-utf-16le-with-signature, utf8, utf-16-be, utf-16-be-with-signature, utf-16be-with-signature, utf-16-le, utf-16-le-with-signature, utf-16le-with-signature</dd></dl>
<p> Those tags are taken from <code>GNU Emacs</code> and <code>XEmacs</code>, together with some aliases. Trailing &#8216;-dos&#8217;, &#8216;-unix&#8217;, and &#8216;-mac&#8217; suffixes of coding tags (which give the end-of-line convention used in the file) are stripped off before the comparison with the above tags happens.</p>
<h3>Iconv Issues</h3>
<p> <code>preconv</code> by itself only supports three encodings: latin-1, cp1047, and UTF-8; all other encodings are passed to the <code>iconv</code> library functions. At compile time it is searched and checked for a valid <code>iconv</code> implementation; a call to &#8216;preconv &#8211;version&#8217; shows whether <code>iconv</code> is used.</p>
<h2>BUGS</h2>
<p> <code>preconv</code> doesn&#8217;t support <i>local variable lists</i> yet. This is a different syntax form to specify local variables at the end of a file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)<br />
 the <code>GNU Emacs</code> and <code>XEmacs</code> info pages </p>
