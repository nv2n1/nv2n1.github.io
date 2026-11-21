---

title: "cbcodec(1)"
name: "cbcodec"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cbcodec/"
description: "cbcodec – popular encoders and decoders"
---

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
<dt><code>-d</code></dt>
<dd> perform decoding (unescaping), not encoding (escaping).</dd>
<dt><code>-br</code></dt>
<dd> break up URL into elements.</dd>
<dt><code>-rs</code></dt>
<dd> resolve relative URL.</dd>
<dt><code>-l</code></dt>
<dd> output the tailing newline.</dd>
<dt><code>-e </code><i>expr</i></dt>
<dd> specify input data directly.</dd>
<dt><code>-c </code><i>num</i></dt>
<dd> limit the number of columns of the encoded data.</dd>
<dt><code>-hd</code></dt>
<dd> parse MIME and extract headers in TSV format.</dd>
<dt><code>-bd</code></dt>
<dd> parse MIME and extract the body.</dd>
<dt><code>-part </code><i>num</i></dt>
<dd> parse MIME and extract a part.</dd>
<dt><code>-ec </code><i>code</i></dt>
<dd> specify the input encoding, which is UTF-8 by default.</dd>
<dt><code>-qp</code></dt>
<dd> use quoted-printable encoding, which is Base64 by default.</dd>
<dt><code>-dc</code></dt>
<dd> output the encoding name instead of the result string when decoding.</dd>
<dt><code>-t</code></dt>
<dd> parse CSV. Convert the data into TSV. Tab and new-line in a cell are deleted.</dd>
<dt><code>-html</code></dt>
<dd> parse CSV. Convert the data into HTML.</dd>
<dt><code>-p</code></dt>
<dd> parse XML. Show tags and text sections with dividing headers.</dd>
<dt><code>-tsv</code></dt>
<dd> parse XML. Show the result in TSV format. Characters of tabs and new-lines are URL-encoded.</dd>
<dt><code>-gz</code></dt>
<dd> use GZIP format.</dd>
<dt><code>-crc</code></dt>
<dd> output the CRC32 checksum as hexadecimal and big endian.</dd>
<dt><code>-ic </code><i>code</i></dt>
<dd> specify the input encoding, which is detected automatically by default.</dd>
<dt><code>-oc </code><i>code</i></dt>
<dd> specify the output encoding, which is UTF-8 by default.</dd>
<dt><code>-ol </code><i>ltype</i></dt>
<dd> convert line feed characters, with `unix'(LF), `dos'(CRLF), and `mac'(CR).</dd>
<dt><code>-cn</code></dt>
<dd> detect the input encoding and show its name.</dd>
<dt><code>-wc</code></dt>
<dd> count the number of characters of the input string of UTF-8.</dd>
<dt><code>-um</code></dt>
<dd> output mappings of UCS-2 characters and C strings of UTF-16BE and UTF-8.</dd>
<dt><code>-wf</code></dt>
<dd> output in W3CDTF format.</dd>
<dt><code>-rf</code></dt>
<dd> output in RFC 1123 format.</dd>
<dt><code>-utc</code></dt>
<dd> output the coordinate universal time.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>qdbm</code>(3), <code>cabin</code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
