---
title: "get_encoding(3)"
name: "get_encoding"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_encoding/"
description: "get_encoding — report the binary encoding of data in a dirfile"
---

<h2>NAME</h2>
<p> get_encoding &#8212; report the binary encoding of data in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned long get_encoding(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_encoding</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the binary encoding for the fragment indexed by <i>fragment_index</i>. The binary encoding of a fragment indicate the encoding of data stored in binary files associated with <code>RAW</code> fields defined in the specified fragment. The encoding of a fragment containing no <code>RAW</code> fields is ignored. </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_encoding</code>() returns the binary encoding of the specified fragment, which will one of the following symbols:</p>
<dl>
<dt>
<dd> <code>GD_UNENCODED</code>,~<code>GD_TEXT_ENCODED</code>,~<code>GD_SLIM_ENCODED</code>,~ <code>GD_GZIP_ENCODED</code>,~<code>GD_BZIP2_ENCODED</code>,~<code>GD_LZMA_ENCODED</code>,~ <code>GD_ENC_UNSUPPORTED</code>. See <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3) and <a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a>(5) for the meanings of these symbols and details on the supported encoding schemes. If the encoding scheme specified in the dirfile metadata is unknown to GetData, <code>GD_ENC_UNSUPPORTED</code> will be returned. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_encoding/">dirfile_alter_encoding</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
