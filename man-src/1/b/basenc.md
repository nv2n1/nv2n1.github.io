---

title: "basenc(1)"
name: "basenc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-basenc/"
description: "basenc – Encode/decode data and print to standard output"
---

<p> <code>basenc</code> [<i>,OPTION/</i>]... [<i>,FILE/</i>]  </p>
<p> basenc encode or decode FILE, or standard input, to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too. </p>
<dl>
<dt><code>--base64</code></dt>
<dd> <p> same as &#8216;base64&#8217; program (RFC4648 section 4) </p>
 </dd>
<dt><code>--base64url</code></dt>
<dd> <p> file- and url-safe base64 (RFC4648 section 5) </p>
 </dd>
<dt><code>--base32</code></dt>
<dd> <p> same as &#8216;base32&#8217; program (RFC4648 section 6) </p>
 </dd>
<dt><code>--base32hex</code></dt>
<dd> <p> extended hex alphabet base32 (RFC4648 section 7) </p>
 </dd>
<dt><code>--base16</code></dt>
<dd> <p> hex encoding (RFC4648 section 8) </p>
 </dd>
<dt><code>--base2msbf</code></dt>
<dd> <p> bit string with most significant bit (msb) first </p>
 </dd>
<dt><code>--base2lsbf</code></dt>
<dd> <p> bit string with least significant bit (lsb) first </p>
 </dd>
<dt><code>-d</code>, <code>--decode</code></dt>
<dd> <p> decode data </p>
 </dd>
<dt><code>-i</code>, <code>--ignore-garbage</code></dt>
<dd> <p> when decoding, ignore non-alphabet characters </p>
 </dd>
<dt><code>-w</code>, <code>--wrap</code>=<i>,COLS/</i></dt>
<dd> <p> wrap encoded lines after COLS character (default 76). Use 0 to disable line wrapping </p>
 </dd>
<dt><code>--z85</code></dt>
<dd> <p> ascii85-like encoding (ZeroMQ spec:32/Z85); when encoding, input length must be a multiple of 4; when decoding, input length must be a multiple of 5 </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> display this help and exit </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> output version information and exit </p>
 </dd></dl>
<p> When decoding, the input may contain newlines in addition to the bytes of the formal alphabet. Use <code>--ignore-garbage</code> to attempt to recover from any other non-alphabet bytes in the encoded stream.  </p>
<h2>ENCODINGS EXAMPLES</h2>
<pre><code>
<dl>
<dd> $ printf '\376\117\202' | basenc --base64
/k+C
$ printf '\376\117\202' | basenc --base64url
_k-C
$ printf '\376\117\202' | basenc --base32
7ZHYE===
$ printf '\376\117\202' | basenc --base32hex
VP7O4===
$ printf '\376\117\202' | basenc --base16
FE4F82
$ printf '\376\117\202' | basenc --base2lsbf
011111111111001001000001
$ printf '\376\117\202' | basenc --base2msbf
111111100100111110000010
$ printf '\376\117\202\000' | basenc --z85
@.FaC
 </dd></dl>

</code></pre>
<h2>AUTHOR</h2>
<p> Written by Simon Josefsson and Assaf Gordon.  </p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt; <br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;. <br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.  </p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/basenc">https://www.gnu.org/software/coreutils/basenc</a>&gt; <br />
 or available locally via: info &#8216;(coreutils) basenc invocation&#8217; </p>
