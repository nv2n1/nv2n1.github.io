---

title: "mewdecode(1)"
name: "mewdecode"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mewdecode/"
description: "mewencode, mewdecode, mewcat – MIME encoder/decoder"
---

<p> <code>mewencode</code>, <code>mewdecode</code>, <code>mewcat</code> &#8211; MIME encoder/decoder </p>
<p> <code>mewencode</code> [<code>-options</code>] [<i>infile</i> [<i>outfile</i>]] </p>
<p> <code>mewdecode</code> [<code>-options</code>] [<i>infile</i> [<i>outfile</i>]] </p>
<p> <code>mewcat</code> [<code>-options</code>] [<i>infile</i>]</p>
<p> The <code>mewencode</code> utility encode/decode MIME objects. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-e</code></dt>
<dd> Encoding.</dd>
<dt><code>-d</code></dt>
<dd> Decoding.</dd>
<dt><code>-8</code></dt>
<dd> See if any 8bit characters are contained.</dd>
<dt><code>-b</code></dt>
<dd> MIME base64 en/decoding.</dd>
<dt><code>-q</code></dt>
<dd> MIME quoted-printable en/decoding.</dd>
<dt><code>-g</code></dt>
<dd> MIME gzip64 en/decoding(not yet specified in RFC).</dd>
<dt><code>-z</code></dt>
<dd> The same as -g.</dd>
<dt><code>-u</code></dt>
<dd> Uudecoding.</dd>
<dt><code>-l</code><i> length</i></dt>
<dd> Line <i>length</i> into which base64/quoted-printable/gzip64 encoding truncate.</dd>
<dt><code>-t</code></dt>
<dd> On base64/gzip64 encoding, local newline is treated as CRLF. On base/gzip64 decoding, any newline is translated into local newline. Specify this option only when the input is a line based object(e.g. Content-Type: is text/plain or application/postscript).</dd>
<dt><code>-h</code></dt>
<dd> Display this help message.</dd>
<dt><code>-v</code></dt>
<dd> Display the version. </dd>
</dl>
