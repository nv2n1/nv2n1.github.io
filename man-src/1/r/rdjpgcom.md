---
title: "rdjpgcom(1)"
name: "rdjpgcom"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdjpgcom/"
description: "rdjpgcom – display text comments from a JPEG file"
---

<h2 class="name">NAME</h2>
<p> rdjpgcom &#8211; display text comments from a JPEG file </p>
<h2>SYNOPSIS</h2>
<p> <code>rdjpgcom</code> [ <code>-raw</code> ] [ <code>-verbose</code> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>rdjpgcom</code> reads the named JPEG/JFIF file, or the standard input if no file is named, and prints any text comments found in the file on the standard output. </p>
<p> The JPEG standard allows &quot;comment&quot; (COM) blocks to occur within a JPEG file. Although the standard doesn&#8217;t actually define what COM blocks are for, they are widely used to hold user-supplied text strings. This lets you add annotations, titles, index terms, etc to your JPEG files, and later retrieve them as text. COM blocks do not interfere with the image stored in the JPEG file. The maximum size of a COM block is 64K, but you can have as many of them as you like in one JPEG file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-raw</code></p>
<dd> Normally <code>rdjpgcom</code> escapes non-printable characters in comments, for security reasons. This option avoids that.</dl>
<p> <code>-verbose</code> Causes <code>rdjpgcom</code> to also display the JPEG image dimensions. </p>
<p> Switch names may be abbreviated, and are not case sensitive.</p>
<h2>HINTS</h2>
<p> <code>rdjpgcom</code> does not depend on the IJG JPEG library. Its source code is intended as an illustration of the minimum amount of code required to parse a JPEG file header correctly. </p>
<p> In <code>-verbose</code> mode, <code>rdjpgcom</code> will also attempt to print the contents of any &quot;APP12&quot; markers as text. Some digital cameras produce APP12 markers containing useful textual information. If you like, you can modify the source code to print other APPn marker types as well.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Independent JPEG Group </p>
<h2>Index</h2>
