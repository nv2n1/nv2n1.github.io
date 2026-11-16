---
title: "ascii(1)"
name: "ascii"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ascii/"
description: "ascii – report character aliases"
---

<h2 class="name">NAME</h2>
<p> ascii &#8211; report character aliases </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ascii</code> [-dxohv] [-t] [<i>char-alias</i>&#8230;]</dt></dl>
<h2>OPTIONS</h2>
<dd>Called with no options, <code>ascii</code> behaves like `ascii -h&#8217;. Options are as follows: </dd>
<p> -t</p>
<dl>
<dt>
</dt><dd> Script-friendly mode, emits only ISO/decimal/hex/octal/binary encodings of the character.</dd></dl>
<p> -s</p>
<dl>
<dt>
</dt><dd> Parse multiple characters. Convenient way of parsing strings.</dd></dl>
<p> -d</p>
<dl>
<dt>
</dt><dd> Ascii table in decimal.</dd></dl>
<p> -x</p>
<dl>
<dt>
</dt><dd> Ascii table in hex.</dd></dl>
<p> -o</p>
<dl>
<dt>
</dt><dd> Ascii table in octal.</dd></dl>
<p> -h, -?</p>
<dl>
<dt>
</dt><dd> Show summary of options and a simple ASCII table.</dd></dl>
<p> -v</p>
<dl>
<dt>
</dt><dd> Show version of program.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Characters in the ASCII set can have many aliases, depending on context. A character&#8217;s possible names include: </p>
<dl>
<dt>
</dt><dd> &bull; Its bit pattern (binary representation).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its hex, decimal and octal representations.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its teletype mnemonic and caret-notation form (for control chars).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its backlash-escape form in C (for some control chars).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its printed form (for printables).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its full ISO official name in English.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its ISO/ECMA code table reference.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Its name as an HTML/SGML entity.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Slang and other names in wide use for it among hackers.</dd></dl>
<p> This utility accepts command-line strings and tries to interpret them as one of the above. When it finds a value, it prints <i>all</i> of the names of the character. The constructs in the following list can be used to specify character values. If an argument could be interpreted in two or more ways, names for all the different characters it might be are dumped. </p>
<p> <i>character</i></p>
<dl>
<dt>
</dt><dd> Any character not described by one of the following conventions represents the character itself.</dd></dl>
<p> <code>^</code><i>character</i></p>
<dl>
<dt>
</dt><dd> A caret followed by a character.</dd></dl>
<p> <code>\</code><i>[abfnrtv0]</i></p>
<dl>
<dt>
</dt><dd> A backslash followed by certain special characters (abfnrtv).</dd></dl>
<p> <i>mnemonic</i></p>
<dl>
<dt>
</dt><dd> An ASCII teletype mnemonic.</dd></dl>
<p> <i>hexadecimal</i></p>
<dl>
<dt>
</dt><dd> A hexadecimal (hex) sequence consists of one or two case-insensitive hex digit characters (01234567890abcdef). To ensure hex interpretation use <i>hex</i><code>h</code><i>,</i><code>0x</code><i>hex,</i><code>x</code><i>hex</i> or <code>
</dd></dl>
</code>
