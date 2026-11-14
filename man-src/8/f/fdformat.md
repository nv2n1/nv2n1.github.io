---
title: "fdformat(8)"
name: "fdformat"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fdformat/"
description: "fdformat – low-level format a floppy disk"
---

<p>fdformat &#8211; low-level format a floppy disk</p>
<h2>Synopsis</h2>
<p><code>fdformat</code> [options]<i> device</i></p>
<h2>Description</h2>
<p><code>fdformat</code> does a low-level format on a floppy disk. <i>device</i> is usually one of the following (for floppy devices the major = 2, and the minor is shown for informational purposes only): </p>
<pre><dl><dt><dd>/dev/fd0d360 (minor = 4)
/dev/fd0h1200 (minor = 8)
/dev/fd0D360 (minor = 12)
/dev/fd0H360 (minor = 12)
/dev/fd0D720 (minor = 16)
/dev/fd0H720 (minor = 16)
/dev/fd0h360 (minor = 20)
/dev/fd0h720 (minor = 24)
/dev/fd0H1440 (minor = 28)
/dev/fd1d360 (minor = 5)
/dev/fd1h1200 (minor = 9)
/dev/fd1D360 (minor = 13)
/dev/fd1H360 (minor = 13)
/dev/fd1D720 (minor = 17)
/dev/fd1H720 (minor = 17)
/dev/fd1h360 (minor = 21)
/dev/fd1h720 (minor = 25)
/dev/fd1H1440 (minor = 29)
</dl></pre>
<p>The generic floppy devices, /dev/fd0 and /dev/fd1, will fail to work with <code>fdformat</code> when a non-standard format is being used, or if the format has not been autodetected earlier. In this case, use <code><a href="/docs/linux/man/8-setfdprm/">setfdprm</a></code>(8) to load the disk parameters.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;from</code> <i>N</i></p>
<dd>Start at the track <i>N</i> (default is 0).</p>
<dt><code>-t</code>, <code>&#8211;to</code> <i>N</i></p>
<dd>Stop at the track <i>N</i>.</p>
<dt><code>-r</code>, <code>&#8211;repair</code> <i>N</i></p>
<dd>Try to repair tracks failed during the verification (max <i>N</i> retries).</p>
<dt><code>-n</code>, <code>&#8211;no-verify</code></p>
<dd>Skip the verification that is normally performed after the formatting.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help text and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-fd/">fd</a></code>(4), <code><a href="/docs/linux/man/8-emkfs/">emkfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-setfdprm/">setfdprm</a></code>(8)</p>
<h2>Author</h2>
<p>Werner Almesberger (almesber [at] nessie.cs.id.ethz.ch)</p>
<h2>Availability</h2>
<p>The fdformat command is part of the util-linux package and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
