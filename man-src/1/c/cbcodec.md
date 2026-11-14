---
title: "cbcodec(1)"
name: "cbcodec"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cbcodec/"
description: "cbcodec – popular encoders and decoders"
---

<h2 class="name">NAME</h2>
<p> cbcodec &#8211; popular encoders and decoders </p>
<h2>SYNOPSIS</h2>
<p> <code>cbcodec url</code> [-d] [-br] [-rs <i>base</i> <i>target</i>] [-l] [-e <i>expr</i>] [<i>file</i>]<br />
 <code>cbcodec base</code> [-d] [-l] [-c <i>num</i>] [-e <i>expr</i>] [<i>file</i>]<br />
 <code>cbcodec quote</code> [-d] [-l] [-c <i>num</i>] [-e <i>expr</i>] [<i>file</i>]<br />
 <code>cbcodec mime</code> [-d] [-hd] [-bd] [-part <i>num</i>] [-l] [-ec <i>code</i>] [-qp] [-dc] [-e <i>expr</i>] [<i>file</i>]<br />
 <code>cbcodec csv</code> [-d] [-t] [-l] [-e <i>expr</i>] [-html] [<i>file</i>]<br />
 <code>cbcodec xml</code> [-d] [-p] [-l] [-e <i>expr</i>] [-tsv] [<i>file</i>]<br />
 <code>cbcodec zlib</code> [-d] [-gz] [-crc] [<i>file</i>]<br />
 <code>cbcodec lzo</code> [-d] [<i>file</i>]<br />
 <code>cbcodec bzip</code> [-d] [<i>file</i>]<br />
 <code>cbcodec iconv</code> [-ic <i>code</i>] [-oc <i>code</i>] [-ol <i>ltype</i>] [-cn] [-wc] [-um] [<i>file</i>]<br />
 <code>cbcodec date</code> [-wf] [-rf] [-utc] [<i>str</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>cbcodec</code> commands. </p>
<p> <code>cbcodec</code> is a tool to use encoding and decoding features provided by Cabin. This command is used in the above format. <i>file</i> specifies a input file. If it is omitted, the standard input is read.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#cabincli.</p>
<dl>
<dt><code>-d</code></p>
<dd> perform decoding (unescaping), not encoding (escaping).</p>
<dt><code>-br</code></p>
<dd> break up URL into elements.</p>
<dt><code>-rs</code></p>
<dd> resolve relative URL.</p>
<dt><code>-l</code></p>
<dd> output the tailing newline.</p>
<dt><code>-e </code><i>expr</i></p>
<dd> specify input data directly.</p>
<dt><code>-c </code><i>num</i></p>
<dd> limit the number of columns of the encoded data.</p>
<dt><code>-hd</code></p>
<dd> parse MIME and extract headers in TSV format.</p>
<dt><code>-bd</code></p>
<dd> parse MIME and extract the body.</p>
<dt><code>-part </code><i>num</i></p>
<dd> parse MIME and extract a part.</p>
<dt><code>-ec </code><i>code</i></p>
<dd> specify the input encoding, which is UTF-8 by default.</p>
<dt><code>-qp</code></p>
<dd> use quoted-printable encoding, which is Base64 by default.</p>
<dt><code>-dc</code></p>
<dd> output the encoding name instead of the result string when decoding.</p>
<dt><code>-t</code></p>
<dd> parse CSV. Convert the data into TSV. Tab and new-line in a cell are deleted.</p>
<dt><code>-html</code></p>
<dd> parse CSV. Convert the data into HTML.</p>
<dt><code>-p</code></p>
<dd> parse XML. Show tags and text sections with dividing headers.</p>
<dt><code>-tsv</code></p>
<dd> parse XML. Show the result in TSV format. Characters of tabs and new-lines are URL-encoded.</p>
<dt><code>-gz</code></p>
<dd> use GZIP format.</p>
<dt><code>-crc</code></p>
<dd> output the CRC32 checksum as hexadecimal and big endian.</p>
<dt><code>-ic </code><i>code</i></p>
<dd> specify the input encoding, which is detected automatically by default.</p>
<dt><code>-oc </code><i>code</i></p>
<dd> specify the output encoding, which is UTF-8 by default.</p>
<dt><code>-ol </code><i>ltype</i></p>
<dd> convert line feed characters, with `unix'(LF), `dos'(CRLF), and `mac'(CR).</p>
<dt><code>-cn</code></p>
<dd> detect the input encoding and show its name.</p>
<dt><code>-wc</code></p>
<dd> count the number of characters of the input string of UTF-8.</p>
<dt><code>-um</code></p>
<dd> output mappings of UCS-2 characters and C strings of UTF-16BE and UTF-8.</p>
<dt><code>-wf</code></p>
<dd> output in W3CDTF format.</p>
<dt><code>-rf</code></p>
<dd> output in RFC 1123 format.</p>
<dt><code>-utc</code></p>
<dd> output the coordinate universal time.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/3-cabin/">cabin</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
