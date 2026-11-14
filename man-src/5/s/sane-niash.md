---
title: "sane-niash(5)"
name: "sane-niash"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-niash/"
description: "sane-niash – SANE backend for scanners based on the NIASH chipset"
---

<p>sane-niash &#8211; SANE backend for scanners based on the NIASH chipset</p>
<h2>Description</h2>
<p>The <code>sane-niash</code> implements a SANE (Scanner Access Now Easy) backend that provides access to NIASH chipset based scanners. This backend will try to support the following models: </p>
<pre>MANUFACTURER: MODEL: USB ID:
--------------- ---------------- ---------
Agfa Snapscan Touch 06BD-0100 (1)(a)
Trust Office Scan 19200 047B-1000 (1)(a)
Hewlett-Packard Scanjet 3300c 03F0-0205 (1)(a)(b)
Hewlett-Packard Scanjet 3400c 03F0-0405 (2)(b)
Hewlett-Packard Scanjet 4300c 03F0-0305 (2)(a)
Silitek ScanJet 4300c 047B-1002 (2)(b)</pre>
<p>ASIC: (1) &#8211; NIASH00012/00013/00014 / (2) &#8211; NIASH00019<br />
 ANALOG FRONT-END: (a) &#8211; ESIC ES8100QA / (b) &#8211; WM8143-12 </p>
<h2>Configuration</h2>
<p>The <i>niash.conf</i> file is meant for future configuration options. Empty lines and lines starting with a hash mark (#) are ignored. Currently no configuration options exist.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-niash.a</i></p>
<dd>The static library implementing this backend. </p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-niash.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Caveats</h2>
<p>If you use a<br />
 Hewlett-Packard Scanjet 3400c or<br />
 Hewlett-Packard Scanjet 4300c<br />
 together with Linux kernel <code>2.6</code>, kernel version <code>2.6.8</code> or newer is necessary.</p>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_NIASH</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_NIASH=255 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5)<br />
 <i><a rel="nofollow" href="http://www.sourceforge.net/projects/hp3300backend">http://www.sourceforge.net/projects/hp3300backend</a></i></p>
<h2>Author</h2>
<p>Bertrik Sikken &lt;<i>bertrik [at] zonnet.nl</i>&gt;</p>
