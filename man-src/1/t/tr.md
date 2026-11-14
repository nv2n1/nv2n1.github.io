---
title: "tr(1)"
name: "tr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tr/"
description: "tr – translate or delete characters"
---

<h2 class="name">NAME</h2>
<p> tr &#8211; translate or delete characters </p>
<h2>SYNOPSIS</h2>
<p> <code>tr</code> [<i>,OPTION/</i>]&#8230; <i>,SET1 /</i>[<i>,SET2/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Translate, squeeze, and/or delete characters from standard input, writing to standard output.</p>
<dl>
<dt><code>-c</code>, <code>-C</code>, <code>&#8211;complement</code></p>
<dd> use the complement of SET1</p>
<dt><code>-d</code>, <code>&#8211;delete</code></p>
<dd> delete characters in SET1, do not translate</p>
<dt><code>-s</code>, <code>&#8211;squeeze-repeats</code></p>
<dd> replace each sequence of a repeated character that is listed in the last specified SET, with a single occurrence of that character</p>
<dt><code>-t</code>, <code>&#8211;truncate-set1</code></p>
<dd> first truncate SET1 to length of SET2</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> SETs are specified as strings of characters. Most represent themselves. Interpreted sequences are:</p>
<dl>
<dt>\NNN</p>
<dd> character with octal value NNN (1 to 3 octal digits)</p>
<dt>\</p>
<dd> backslash</p>
<dt></p>
<dd> audible BEL</p>
<dt></p>
<dd> backspace</p>
<dt></p>
<dd> form feed</p>
<dt>
</p>
<dd> new line</p>
<dt></p>
<dd> return</p>
<dt>	</p>
<dd> horizontal tab</p>
<dt></p>
<dd> vertical tab</p>
<dt>CHAR1-CHAR2</p>
<dd> all characters from CHAR1 to CHAR2 in ascending order</p>
<dt>[CHAR*]</p>
<dd> in SET2, copies of CHAR until length of SET1</p>
<dt>[CHAR*REPEAT]</p>
<dd> REPEAT copies of CHAR, REPEAT octal if starting with 0</p>
<dt>[:alnum:]</p>
<dd> all letters and digits</p>
<dt>[:alpha:]</p>
<dd> all letters</p>
<dt>[:blank:]</p>
<dd> all horizontal whitespace</p>
<dt>[:cntrl:]</p>
<dd> all control characters</p>
<dt>[:digit:]</p>
<dd> all digits</p>
<dt>[:graph:]</p>
<dd> all printable characters, not including space</p>
<dt>[:lower:]</p>
<dd> all lower case letters</p>
<dt>[:print:]</p>
<dd> all printable characters, including space</p>
<dt>[:punct:]</p>
<dd> all punctuation characters</p>
<dt>[:space:]</p>
<dd> all horizontal or vertical whitespace</p>
<dt>[:upper:]</p>
<dd> all upper case letters</p>
<dt>[:xdigit:]</p>
<dd> all hexadecimal digits</p>
<dt>[=CHAR=]</p>
<dd> all characters which are equivalent to CHAR</dl>
<p> Translation occurs if <code>-d</code> is not given and both SET1 and SET2 appear. <code>-t</code> may be used only when translating. SET2 is extended to length of SET1 by repeating its last character as necessary. Excess characters of SET2 are ignored. Only [:lower:] and [:upper:] are guaranteed to expand in ascending order; used in SET2 while translating, they may only be used in pairs to specify case conversion. <code>-s</code> uses the last specified SET, and occurs after translation or deletion.</p>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/tr">https://www.gnu.org/software/coreutils/tr</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) tr invocation&#8217; </p>
<h2>Index</h2>
