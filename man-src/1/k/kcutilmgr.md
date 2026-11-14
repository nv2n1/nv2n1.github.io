---
title: "kcutilmgr(1)"
name: "kcutilmgr"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcutilmgr/"
description: "kcutilmgr – command line interface of miscellaneous utilities"
---

<h2 class="name">NAME</h2>
<p> kcutilmgr &#8211; command line interface of miscellaneous utilities</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcutilmgr</code>&#8216; is a tool of miscellaneous utilities, and to show the configuration. This command is used in the following format. `<i>file</i>&#8216; specifies a input file. If it is omitted, the standard input is read. If it begins with &quot;@&quot;, the trailing substring is treated as the input. `<i>pattern</i>&#8216; specifies an matching pattern. </p>
<dl>
<dt>
<dd>
 <code>kcutilmgr hex </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Performs hexadecimal encoding and its decoding.</dl>
<p> <code>kcutilmgr enc </code>[<code>-hex</code>|<code>-url</code>|<code>-quote</code>][<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Performs Base64 encoding and its decoding.</dl>
<p> <code>kcutilmgr ciph </code>[<code>-key </code><i>str</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Performs Arcfour cipher and its decipher.</dl>
<p> <code>kcutilmgr comp </code>[<code>-def</code>|<code>-gz</code>|<code>-lzo</code>|<code>-lzma</code>][<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Performs ZLIB encoding and its decoding. By default, use the raw format.</dl>
<p> <code>kcutilmgr hash </code>[<code>-fnv</code>|<code>-path</code>|<code>-crc</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Calculates the hash value. By default, use MurMur hashing.</dl>
<p> <code>kcutilmgr regex </code>[<code>-alt </code><i>str</i>][<code>-ic</code>]<i>pattern</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Prints lines matching a regular expression.</dl>
<p> <code>kcutilmgr conf </code>[<code>-v</code>|<code>-i</code>|<code>-l</code>|<code>-p</code>]</p>
<dl>
<dt>
<dd> Shows the configuration of Kyoto Cabinet.</dl>
<p> <code>kcutilmgr version</code></p>
<dl>
<dt>
<dd> Shows the version information of Kyoto Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-d</code> : perform decoding (unescaping), not encoding (escaping).<br />
 <code>-hex</code> : use hexadecimal encoding.<br />
 <code>-url</code> : use URL encoding.<br />
 <code>-quote</code> : use Quoted-printable encoding.<br />
 <code>-key </code><i>str</i> : set the cipher key.<br />
 <code>-def</code> : use the deflate format.<br />
 <code>-gz</code> : use the gzip format.<br />
 <code>-lzo</code> : use LZO encoding.<br />
 <code>-lzma</code> : use LZMA encoding.<br />
 <code>-fnv</code> : use FNV hashing.<br />
 <code>-path</code> : use the path hashing of the directory database.<br />
 <code>-crc</code> : calculate the CRC32 checksum.<br />
 <code>-alt </code><i>str</i> : replaces matching substring with the alternative string.<br />
 <code>-ic</code> : ignores difference between upper and lower cases.<br />
 <code>-v</code> : show the version number of Kyoto Cabinet.<br />
 <code>-i</code> : show options to include the headers of Tokyo Cabinet.<br />
 <code>-l</code> : show options to link the library of Tokyo Cabinet.<br />
 <code>-p</code> : show the directory path of the commands.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcutiltest/">kcutiltest</a></code>(1) </p>
<h2>Index</h2>
