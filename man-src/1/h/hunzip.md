---
title: "hunzip(1)"
name: "hunzip"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hunzip/"
description: "hunzip – decompress and decrypt hzip files to the standard output"
---

<h2 class="name">NAME</h2>
<p> hunzip &#8211; decompress and decrypt hzip files to the standard output </p>
<h2>SYNOPSIS</h2>
<p> hunzip [-h] file.hz [password]</p>
<h2>DESCRIPTION</h2>
<p> <i>Hunzip</i> is the decompression and decryption program of hzip format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display short help description.</dl>
<h2>EXAMPLE</h2>
<p> <code>hunzip file.hz &gt;file</code></p>
<h2>NOTES</h2>
<p> Redirection of the standard output results platform-specific line terminating, so a compressed hzip file with new line terminators would be bigger with the extra CR characters of the decompression on Windows platforms.</p>
<h2>SEE ALSO</h2>
<p> <code>hunzip (1), <a href="/docs/linux/man/1-hunspell/">hunspell</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> László Németh. </p>
<h2>Index</h2>
