---
title: "exfatlabel(8)"
name: "exfatlabel"
section: "8"
letter: "e"
url: "/docs/linux/man/8-exfatlabel/"
description: "exfatlabel – get or set an exFAT file system label"
---

<p><code>exfatlabel</code> &#8211; get or set an exFAT file system label</p>
<h2>Synopsis</h2>
<p><code>exfatlabel</code> [ <code>-V</code> ] <i>device</i> [ <i>label</i> ] </p>
<h2>Description</h2>
<p><code>exfatlabel</code> reads or changes an exFAT file system label (volume name). If <i>label</i> argument is present, <code>exfatlabel</code> sets the new volume name. Empty label (&#8221;) removes volume name. Label can be up to 15 characters. This limit is shorter if characters beyond Unicode BMP are used because internally label is stored in UTF-16. If <i>label</i> argument is omitted, <code>exfatlabel</code> just prints current volume name. </p>
<h2>Command Line Options</h2>
<p>Command line options available:</p>
<dl>
<dt><code>-V</code></p>
<dd>Print version and copyright. </p>
</dl>
<h2>Exit Codes</h2>
<p>Zero is returned on success. Any other code means an error.</p>
<h2>Author</h2>
<p>Andrew Nayenko</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkexfatfs/">mkexfatfs</a></code>(8) </p>
