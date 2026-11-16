---
title: "basenc(1)"
name: "basenc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-basenc/"
description: "basenc – Encode/decode data and print to standard output"
---

<h2 class="name">NAME</h2>
<p> basenc &#8211; Encode/decode data and print to standard output </p>
<h2>SYNOPSIS</h2>
<p> <code>basenc</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> basenc encode or decode FILE, or standard input, to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;base64</code></dt>
<dd> same as &#8216;base64&#8217; program (RFC4648 section 4)</dd>
<dt><code>&#8211;base64url</code></dt>
<dd> file- and url-safe base64 (RFC4648 section 5)</dd>
<dt><code>&#8211;base32</code></dt>
<dd> same as &#8216;base32&#8217; program (RFC4648 section 6)</dd>
<dt><code>&#8211;base32hex</code></dt>
<dd> extended hex alphabet base32 (RFC4648 section 7)</dd>
<dt><code>&#8211;base16</code></dt>
<dd> hex encoding (RFC4648 section 8)</dd>
<dt><code>&#8211;base2msbf</code></dt>
<dd> bit string with most significant bit (msb) first</dd>
<dt><code>&#8211;base2lsbf</code></dt>
<dd> bit string with least significant bit (lsb) first</dd>
<dt><code>-d</code>, <code>&#8211;decode</code></dt>
<dd> decode data</dd>
<dt><code>-i</code>, <code>&#8211;ignore-garbage</code></dt>
<dd> when decoding, ignore non-alphabet characters</dd>
<dt><code>-w</code>, <code>&#8211;wrap</code>=<i>,COLS/</i></dt>
<dd> wrap encoded lines after COLS character (default 76). Use 0 to disable line wrapping</dd>
<dt><code>&#8211;z85</code></dt>
<dd> ascii85-like encoding (ZeroMQ spec:32/Z85); when encoding, input length must be a multiple of 4; when decoding, input length must be a multiple of 5</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> When decoding, the input may contain newlines in addition to the bytes of the formal alphabet. Use <code>&#8211;ignore-garbage</code> to attempt to recover from any other non-alphabet bytes in the encoded stream.</p>
<h2>ENCODINGS EXAMPLES</h2>
<pre><code>
$ printf '\376\117\202' | basenc-- base64 / k + C $ printf '\376\117\202' | basenc-- base64url _k - C $ printf '\376\117\202' | basenc-- base32 7ZHYE == =
                                                                                                                                                             $ printf '\376\117\202' | basenc-- base32hex
                                                                                                                                                                                               VP7O4 == =
                                                                                                                                                                                                            $ printf '\376\117\202' | basenc-- base16 FE4F82 $ printf '\376\117\202' | basenc-- base2lsbf 011111111111001001000001 $ printf '\376\117\202' | basenc-- base2msbf 111111100100111110000010 $ printf '\376\117\202
</code></pre>
