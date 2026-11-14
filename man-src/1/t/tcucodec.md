---
title: "tcucodec(1)"
name: "tcucodec"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcucodec/"
description: "tcucodec – popular encoders and decoders"
---

<h2 class="name">NAME</h2>
<p> tcucodec &#8211; popular encoders and decoders</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcucodec</code>&#8216; is a tool to use encoding and decoding features. This command is used in the following format. `<i>file</i>&#8216; specifies a input file. If it is omitted, the standard input is read. </p>
<dl>
<dt>
<dd>
 <code>tcucodec url </code>[<code>-d</code>][<code>-br</code>][<code>-rs </code><i>base</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform URL encoding and its decoding.</dl>
<p> <code>tcucodec base </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform Base64 encoding and its decoding.</dl>
<p> <code>tcucodec quote </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform quoted-printable encoding and its decoding.</dl>
<p> <code>tcucodec mime </code>[<code>-d</code>][<code>-en </code><i>name</i>][<code>-q</code>][<code>-on</code>][<code>-hd</code>][<code>-bd</code>][<code>-part </code><i>num</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform MIME encoding and its decoding.</dl>
<p> <code>tcucodec hex </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform hexadecimal encoding and its decoding.</dl>
<p> <code>tcucodec pack </code>[<code>-d</code>][<code>-bwt</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform Packbits encoding and its decoding.</dl>
<p> <code>tcucodec tcbs </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform TCBS encoding and its decoding.</dl>
<p> <code>tcucodec zlib </code>[<code>-d</code>][<code>-gz</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform ZLIB encoding and its decoding.</dl>
<p> <code>tcucodec bzip </code>[<code>-d</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform BZIP2 encoding and its decoding.</dl>
<p> <code>tcucodec xml </code>[<code>-d</code>][<code>-br</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Process XML. By default, escape meta characters.</dl>
<p> <code>tcucodec cstr </code>[<code>-d</code>][<code>-js</code>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform C-string escaping and its unescaping.</dl>
<p> <code>tcucodec ucs </code>[<code>-d</code>][<code>-un</code>][<code>-kw </code><i>str</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Convert UTF-8 string into UCS-2 array.</dl>
<p> <code>tcucodec hash </code>[<code>-crc</code>][<code>-ch </code><i>num</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Calculate the hash value. By default, use MD5 function.</dl>
<p> <code>tcucodec cipher </code>[<code>-key </code><i>str</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform stream cipher and its decipher.</dl>
<p> <code>tcucodec date </code>[<code>-ds </code><i>str</i>][<code>-jl </code><i>num</i>][<code>-wf</code>][<code>-rf</code>]</p>
<dl>
<dt>
<dd> Process date string. By default, print the current UNIX time.</dl>
<p> <code>tcucodec tmpl </code>[<code>-var </code><i>name</i><i>value</i>][<i>file</i>]</p>
<dl>
<dt>
<dd> Perform template serialization.</dl>
<p> <code>tcucodec conf </code>[<code>-v</code>|<code>-i</code>|<code>-l</code>|<code>-p</code>]</p>
<dl>
<dt>
<dd> Print some configurations.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-d</code> : perform decoding (unescaping), not encoding (escaping).<br />
 <code>-br</code> : break up URL or XML into elements.<br />
 <code>-rs </code><i>base</i> : specify the base URL and resolve the relative URL.<br />
 <code>-en </code><i>name</i> : specify the input encoding, which is UTF-8 by default.<br />
 <code>-q</code> : use quoted-printable encoding, which is Base64 by default.<br />
 <code>-on</code> : output the charset name when decoding.<br />
 <code>-bd</code> : perform MIME parsing and output the body.<br />
 <code>-hd</code> : perform MIME parsing and output the headers.<br />
 <code>-part </code><i>num</i> : perform MIME parsing and output the specified part.<br />
 <code>-bwt</code> : convert by BWT as preprocessing.<br />
 <code>-gz</code> : use GZIP format.<br />
 <code>-crc</code> : use CRC32 function.<br />
 <code>-js</code> : use JSON compatible format.<br />
 <code>-un</code> : perform UCS normalization.<br />
 <code>-kw </code><i>str</i> : generate KWIC string.<br />
 <code>-ch </code><i>num</i> : use consistent hashing function.<br />
 <code>-key </code><i>str</i> : specify the cipher key.<br />
 <code>-ds </code><i>str</i> : specify the time.<br />
 <code>-jl </code><i>num</i> : specify the jet lag.<br />
 <code>-wf</code> : format the output in W3CDTF.<br />
 <code>-rf</code> : format the output in RFC 1123 format.<br />
 <code>-var </code><i>name</i> <i>value</i> : specify a template variable.<br />
 <code>-v</code> : show the version number of Tokyo Cabinet.<br />
 <code>-i</code> : show options to include the headers of Tokyo Cabinet.<br />
 <code>-l</code> : show options to link the library of Tokyo Cabinet.<br />
 <code>-p</code> : show the directory path of the commands of Tokyo Cabinet.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcutest/">tcutest</a></code>(1), <code><a href="/docs/linux/man/1-tcumttest/">tcumttest</a></code>(1), <code><a href="/docs/linux/man/3-tcutil/">tcutil</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
