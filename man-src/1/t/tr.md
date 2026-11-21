---

title: "tr(1)"
name: "tr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tr/"
description: "tr – translate or delete characters"
---

<p> tr &#8211; translate or delete characters </p>
<h2>SYNOPSIS</h2>
<p> <code>tr</code> [<i>,OPTION/</i>]&#8230; <i>,SET1 /</i>[<i>,SET2/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Translate, squeeze, and/or delete characters from standard input, writing to standard output.</p>
<dl>
<dt><code>-c</code>, <code>-C</code>, <code>&#8211;complement</code></dt>
<dd> use the complement of SET1</dd>
<dt><code>-d</code>, <code>&#8211;delete</code></dt>
<dd> delete characters in SET1, do not translate</dd>
<dt><code>-s</code>, <code>&#8211;squeeze-repeats</code></dt>
<dd> replace each sequence of a repeated character that is listed in the last specified SET, with a single occurrence of that character</dd>
<dt><code>-t</code>, <code>&#8211;truncate-set1</code></dt>
<dd> first truncate SET1 to length of SET2</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> SETs are specified as strings of characters. Most represent themselves. Interpreted sequences are:</p>
<dl>
<dt>\NNN</dt>
<dd> character with octal value NNN (1 to 3 octal digits)</dd>
<dt>\</dt>
<dd> backslash</dd>
<dt></dt>
<dd> audible BEL</dd>
<dt></dt>
<dd> backspace</dd>
<dt></dt>
<dd> form feed</dd>
<dt>
</dt>
<dd> new line</dd>
<dt>
</dt>
<dd> return</dd>
<dt>	</dt>
<dd> horizontal tab</dd>
<dt></dt>
<dd> vertical tab</dd>
<dt>CHAR1-CHAR2</dt>
<dd> all characters from CHAR1 to CHAR2 in ascending order</dd>
<dt>[CHAR*]</dt>
<dd> in SET2, copies of CHAR until length of SET1</dd>
<dt>[CHAR*REPEAT]</dt>
<dd> REPEAT copies of CHAR, REPEAT octal if starting with 0</dd>
<dt>[:alnum:]</dt>
<dd> all letters and digits</dd>
<dt>[:alpha:]</dt>
<dd> all letters</dd>
<dt>[:blank:]</dt>
<dd> all horizontal whitespace</dd>
<dt>[:cntrl:]</dt>
<dd> all control characters</dd>
<dt>[:digit:]</dt>
<dd> all digits</dd>
<dt>[:graph:]</dt>
<dd> all printable characters, not including space</dd>
<dt>[:lower:]</dt>
<dd> all lower case letters</dd>
<dt>[:print:]</dt>
<dd> all printable characters, including space</dd>
<dt>[:punct:]</dt>
<dd> all punctuation characters</dd>
<dt>[:space:]</dt>
<dd> all horizontal or vertical whitespace</dd>
<dt>[:upper:]</dt>
<dd> all upper case letters</dd>
<dt>[:xdigit:]</dt>
<dd> all hexadecimal digits</dd>
<dt>[=CHAR=]</dt>
<dd> all characters which are equivalent to CHAR</dd></dl>
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
