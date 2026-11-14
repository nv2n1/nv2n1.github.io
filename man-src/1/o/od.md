---
title: "od(1)"
name: "od"
section: "1"
letter: "o"
url: "/docs/linux/man/1-od/"
description: "od – dump files in octal and other formats"
---

<h2 class="name">NAME</h2>
<p> od &#8211; dump files in octal and other formats </p>
<h2>SYNOPSIS</h2>
<p> <code>od</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;<br />
 <code>od</code> [<i>,-abcdfilosx/</i>]&#8230; [<i>,FILE/</i>] [[<i>,+/</i>]<i>,OFFSET/</i>[<i>,./</i>][<i>,b/</i>]]<br />
 <code>od</code> <i>,&#8211;traditional /</i>[<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>] [[<i>,+/</i>]<i>,OFFSET/</i>[<i>,./</i>][<i>,b/</i>] [<i>,+/</i>][<i>,LABEL/</i>][<i>,./</i>][<i>,b/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Write an unambiguous representation, octal bytes by default, of FILE to standard output. With more than one FILE argument, concatenate them in the listed order to form the input. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> If first and second call formats both apply, the second format is assumed if the last operand begins with + or (if there are 2 operands) a digit. An OFFSET operand means <code>-j</code> OFFSET. LABEL is the pseudo-address at first byte printed, incremented when dump is progressing. For OFFSET and LABEL, a 0x or 0X prefix indicates hexadecimal; suffixes may be . for octal and b for multiply by 512. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;address-radix</code>=<i>,RADIX/</i></p>
<dd> output format for file offsets; RADIX is one of [doxn], for Decimal, Octal, Hex or None</p>
<dt><code>&#8211;endian=</code>{big|little}</p>
<dd> swap input bytes according the specified order</p>
<dt><code>-j</code>, <code>&#8211;skip-bytes</code>=<i>,BYTES/</i></p>
<dd> skip BYTES input bytes first</p>
<dt><code>-N</code>, <code>&#8211;read-bytes</code>=<i>,BYTES/</i></p>
<dd> limit dump to BYTES input bytes</p>
<dt><code>-S</code> BYTES, <code>&#8211;strings</code>[=<i>,BYTES/</i>]</p>
<dd> output strings of at least BYTES graphic chars; 3 is implied when BYTES is not specified</p>
<dt><code>-t</code>, <code>&#8211;format</code>=<i>,TYPE/</i></p>
<dd> select output format or formats</p>
<dt><code>-v</code>, <code>&#8211;output-duplicates</code></p>
<dd> do not use * to mark line suppression</p>
<dt><code>-w[BYTES]</code>, <code>&#8211;width</code>[=<i>,BYTES/</i>]</p>
<dd> output BYTES bytes per output line; 32 is implied when BYTES is not specified</p>
<dt><code>&#8211;traditional</code></p>
<dd> accept arguments in third form above</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h3>Traditional format specifications may be intermixed; they accumulate:</h3>
<dl>
<dt><code>-a</code></p>
<dd> same as <code>-t</code> a, select named characters, ignoring high-order bit</p>
<dt><code>-b</code></p>
<dd> same as <code>-t</code> o1, select octal bytes</p>
<dt><code>-c</code></p>
<dd> same as <code>-t</code> c, select printable characters or backslash escapes</p>
<dt><code>-d</code></p>
<dd> same as <code>-t</code> u2, select unsigned decimal 2-byte units</p>
<dt><code>-f</code></p>
<dd> same as <code>-t</code> fF, select floats</p>
<dt><code>-i</code></p>
<dd> same as <code>-t</code> dI, select decimal ints</p>
<dt><code>-l</code></p>
<dd> same as <code>-t</code> dL, select decimal longs</p>
<dt><code>-o</code></p>
<dd> same as <code>-t</code> o2, select octal 2-byte units</p>
<dt><code>-s</code></p>
<dd> same as <code>-t</code> d2, select decimal 2-byte units</p>
<dt><code>-x</code></p>
<dd> same as <code>-t</code> x2, select hexadecimal 2-byte units</dl>
<h3>TYPE is made up of one or more of these specifications:</h3>
<dl>
<dt>a</p>
<dd> named character, ignoring high-order bit</p>
<dt>c</p>
<dd> printable character or backslash escape</p>
<dt>d[SIZE]</p>
<dd> signed decimal, SIZE bytes per integer</p>
<dt>f[SIZE]</p>
<dd> floating point, SIZE bytes per float</p>
<dt>o[SIZE]</p>
<dd> octal, SIZE bytes per integer</p>
<dt>u[SIZE]</p>
<dd> unsigned decimal, SIZE bytes per integer</p>
<dt>x[SIZE]</p>
<dd> hexadecimal, SIZE bytes per integer</dl>
<p> SIZE is a number. For TYPE in [doux], SIZE may also be C for sizeof(char), S for sizeof(short), I for sizeof(int) or L for sizeof(long). If TYPE is f, SIZE may also be F for sizeof(float), D for sizeof(double) or L for sizeof(long double). </p>
<p> Adding a z suffix to any type displays printable characters at the end of each output line.</p>
<h3>BYTES is hex with 0x or 0X prefix, and may have a multiplier suffix:</h3>
<dl>
<dt>b</p>
<dd> 512</p>
<dt>KB</p>
<dd> 1000</p>
<dt>K</p>
<dd> 1024</p>
<dt>MB</p>
<dd> 1000*1000</p>
<dt>M</p>
<dd> 1024*1024</dl>
<p> and so on for G, T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>od -A x -t x1z -v</code></p>
<dd> Display hexdump format output</p>
<dt><code>od -A o -t oS -w16</code></p>
<dd> The default output format used by od</dl>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/od">https://www.gnu.org/software/coreutils/od</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) od invocation&#8217; </p>
<h2>Index</h2>
