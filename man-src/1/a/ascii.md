---

title: "ascii(1)"
name: "ascii"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ascii/"
description: "ascii – report character aliases"
---

<p> ascii - report character aliases </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>ascii</code> [-dxohv] [-t] [<i>char-alias</i>...] </dt>
</dl>
<h2>OPTIONS</h2>
<dd> <p> Called with no options, <code>ascii</code> behaves like `ascii -h&#8217;. Options are as follows: </p>
<p> -t </p>
 </dd>
<dl>
<dd> <p> Script-friendly mode, emits only ISO/decimal/hex/octal/binary encodings of the character. </p>
 </dd></dl>
<p> -s </p>
<dl>
<dd> <p> Parse multiple characters. Convenient way of parsing strings. </p>
 </dd></dl>
<p> -d </p>
<dl>
<dd> <p> Ascii table in decimal. </p>
 </dd></dl>
<p> -x </p>
<dl>
<dd> <p> Ascii table in hex. </p>
 </dd></dl>
<p> -o </p>
<dl>
<dd> <p> Ascii table in octal. </p>
 </dd></dl>
<p> -h, -? </p>
<dl>
<dd> <p> Show summary of options and a simple ASCII table. </p>
 </dd></dl>
<p> -v </p>
<dl>
<dd> <p> Show version of program. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Characters in the ASCII set can have many aliases, depending on context. A character&#8217;s possible names include: </p>
<dl>
<dd> <p> &bull; Its bit pattern (binary representation). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its hex, decimal and octal representations. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its teletype mnemonic and caret-notation form (for control chars). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its backlash-escape form in C (for some control chars). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its printed form (for printables). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its full ISO official name in English. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its ISO/ECMA code table reference. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Its name as an HTML/SGML entity. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Slang and other names in wide use for it among hackers. </p>
 </dd></dl>
<p> This utility accepts command-line strings and tries to interpret them as one of the above. When it finds a value, it prints <i>all</i> of the names of the character. The constructs in the following list can be used to specify character values. If an argument could be interpreted in two or more ways, names for all the different characters it might be are dumped. </p>
<p> <i>character</i> </p>
<dl>
<dd> <p> Any character not described by one of the following conventions represents the character itself. </p>
 </dd></dl>
<p> <code>^</code><i>character</i> </p>
<dl>
<dd> <p> A caret followed by a character. </p>
 </dd></dl>
<p> <code>\</code><i>[abfnrtv0]</i> </p>
<dl>
<dd> <p> A backslash followed by certain special characters (abfnrtv). </p>
 </dd></dl>
<p> <i>mnemonic</i> </p>
<dl>
<dd> <p> An ASCII teletype mnemonic. </p>
 </dd></dl>
<p> <i>hexadecimal</i> </p>
<dl>
<dd> <p> A hexadecimal (hex) sequence consists of one or two case-insensitive hex digit characters (01234567890abcdef). To ensure hex interpretation use <i>hex</i><code>h</code><i>,</i><code>0x</code><i>hex,</i><code>x</code><i>hex</i> or <code>\x</code><i>hex.</i> </p>
 </dd></dl>
<p> <i>decimal</i> </p>
<dl>
<dd> <p> A decimal sequence consists of one, two or three decimal digit characters (0123456789). To ensure decimal interpretation use <code>\0d</code><i>decimal,</i><code>d</code><i>decimal,</i> or <code>\d</code><i>decimal.</i> </p>
 </dd></dl>
<p> <i>octal</i> </p>
<dl>
<dd> <p> An octal sequence consists of one, two or three octal digit characters (01234567). To ensure octal interpretation use <code>\</code><i>&lt;octal&gt;,</i><code>0o</code><i>&lt;octal&gt;,</i><code>o</code><i>&lt;octal&gt;,</i> or <code>\o</code><i>&lt;octal&gt;.</i> </p>
 </dd></dl>
<p> <i>bit pattern</i> </p>
<dl>
<dd> <p> A bit pattern (binary) sequence consists of one to eight binary digit characters (01). To ensure bit interpretation use <code>0b</code><i>&lt;bit pattern&gt;,</i><code>b</code><i>&lt;bit pattern&gt;</i> or <code>\b</code><i>&lt;bit pattern&gt;.</i> </p>
 </dd></dl>
<p> <i>ISO</i>/<i>ECMA code</i> </p>
<dl>
<dd> <p> An ISO/ECMA code sequence consists of one or two decimal digit characters, a slash, and one or two decimal digit characters. </p>
 </dd></dl>
<p> <i>name</i> </p>
<dl>
<dd> <p> An official ASCII or (unofficial) slang name. </p>
 </dd></dl>
<p> The slang names recognized and printed out are from a rather comprehensive list that first appeared on USENET in early 1990 and has been continuously updated since. Mnemonics recognized and printed include the official ASCII set, some official ISO names (where those differ) and a few common-use alternatives (such as NL for LF). HTML/SGML entity names are also printed when applicable. All comparisons are case-insensitive, and dashes are mapped to spaces. Any unrecognized arguments or out of range values are silently ignored. Note that the <code>-s</code> option will not recognize &#8216;long&#8217; names, as it cannot differentiate them from other parts of the string. </p>
<p> For correct results, be careful to stringize or quote shell metacharacters in arguments (especially backslash). </p>
<p> This utility is particularly handy for interpreting <a href="/docs/linux/man/1-cc/">cc</a>(1)&#8216;s ugly octal `invalid-character&#8217; messages, or when coding anything to do with serial communications. As a side effect it serves as a handy base-converter for random 8-bit values.  </p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;; November 1990 (home page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/">http://www.catb.org/~esr/</a></code>m[]). Reproduce, use, and modify as you like as long as you don&#8217;t remove this authorship notice. Ioannis E. Tambouras &lt;ioannis [at] debian.org&gt; added command options and minor enhancements. Brian J. Ginsbach &lt;ginsbach [at] sgi.com&gt; fixed several bugs and expanded the man page. David N. Welton &lt;davidw [at] efn.org&gt; added the <code>-s</code> option. Matej Vela corrected the ISO names. Dave Capella contributed the idea of listing HTML/SGML entities. </p>
