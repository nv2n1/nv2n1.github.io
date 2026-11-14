---
title: "base64(1)"
name: "base64"
section: "1"
letter: "b"
url: "/docs/linux/man/1-base64/"
description: "base64 – base64 encode/decode data and print to standard output"
---

<h2 class="name">NAME</h2>
<p> base64 &#8211; base64 encode/decode data and print to standard output </p>
<h2>SYNOPSIS</h2>
<p> <code>base64</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Base64 encode or decode FILE, or standard input, to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;decode</code></p>
<dd> decode data</p>
<dt><code>-i</code>, <code>&#8211;ignore-garbage</code></p>
<dd> when decoding, ignore non-alphabet characters</p>
<dt><code>-w</code>, <code>&#8211;wrap</code>=<i>,COLS/</i></p>
<dd> wrap encoded lines after COLS character (default 76). Use 0 to disable line wrapping</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The data are encoded as described for the base64 alphabet in RFC 4648. When decoding, the input may contain newlines in addition to the bytes of the formal base64 alphabet. Use <code>&#8211;ignore-garbage</code> to attempt to recover from any other non-alphabet bytes in the encoded stream.</p>
<h2>AUTHOR</h2>
<p> Written by Simon Josefsson.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/base64">https://www.gnu.org/software/coreutils/base64</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) base64 invocation&#8217; </p>
<h2>Index</h2>
