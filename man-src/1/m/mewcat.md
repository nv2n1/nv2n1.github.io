---
title: "mewcat(1)"
name: "mewcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mewcat/"
description: "mewencode, mewdecode, mewcat – MIME encoder/decoder"
---

<h2 class="name">NAME</h2>
<p> <code>mewencode</code>, <code>mewdecode</code>, <code>mewcat</code> &#8211; MIME encoder/decoder </p>
<h2>SYNOPSIS</h2>
<p> <code>mewencode</code> [<code>-options</code>] [<i>infile</i> [<i>outfile</i>]] </p>
<p> <code>mewdecode</code> [<code>-options</code>] [<i>infile</i> [<i>outfile</i>]] </p>
<p> <code>mewcat</code> [<code>-options</code>] [<i>infile</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mewencode</code> utility encode/decode MIME objects. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-e</code></p>
<dd> Encoding.</p>
<dt><code>-d</code></p>
<dd> Decoding.</p>
<dt><code>-8</code></p>
<dd> See if any 8bit characters are contained.</p>
<dt><code>-b</code></p>
<dd> MIME base64 en/decoding.</p>
<dt><code>-q</code></p>
<dd> MIME quoted-printable en/decoding.</p>
<dt><code>-g</code></p>
<dd> MIME gzip64 en/decoding(not yet specified in RFC).</p>
<dt><code>-z</code></p>
<dd> The same as -g.</p>
<dt><code>-u</code></p>
<dd> Uudecoding.</p>
<dt><code>-l</code><i> length</i></p>
<dd> Line <i>length</i> into which base64/quoted-printable/gzip64 encoding truncate.</p>
<dt><code>-t</code></p>
<dd> On base64/gzip64 encoding, local newline is treated as CRLF. On base/gzip64 decoding, any newline is translated into local newline. Specify this option only when the input is a line based object(e.g. Content-Type: is text/plain or application/postscript).</p>
<dt><code>-h</code></p>
<dd> Display this help message.</p>
<dt><code>-v</code></p>
<dd> Display the version. </p>
</dl>
<h2>Index</h2>
