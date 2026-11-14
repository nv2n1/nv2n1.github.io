---
title: "dumpexfat(8)"
name: "dumpexfat"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dumpexfat/"
description: "dumpexfat – dump exFAT file system"
---

<p><code>dumpexfat</code> &#8211; dump exFAT file system</p>
<h2>Synopsis</h2>
<p><code>dumpexfat</code> [ <code>-s</code> ] [ <code>-u</code> ] [ <code>-f</code> <i>file</i> ] [ <code>-V</code> ] <i>device</i> </p>
<h2>Description</h2>
<p><code>dumpexfat</code> dumps details about exFAT file system including low-level info. All sizes are in bytes. </p>
<h2>Options</h2>
<p>Command line options available:</p>
<dl>
<dt><code>-s</code></p>
<dd>Dump only info from super block. May be useful for heavily corrupted file systems.</p>
<dt><code>-u</code></p>
<dd>Dump ranges of used sectors starting from 0 and separated with spaces. May be useful for backup tools.</p>
<dt><code>-f file</code></p>
<dd>Print out a list of fragments that compose the given file. Each fragment is printed on its own line, as the start offset (in bytes) into the file system, and the length (in bytes).</p>
<dt><code>-V</code></p>
<dd>Print version and copyright. </p>
</dl>
<h2>Exit Codes</h2>
<p>Zero is returned on success. Any other code means an error.</p>
<h2>Author</h2>
<p>Andrew Nayenko</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkexfatfs/">mkexfatfs</a></code>(8) </p>
