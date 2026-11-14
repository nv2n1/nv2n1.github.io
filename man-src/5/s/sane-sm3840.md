---
title: "sane-sm3840(5)"
name: "sane-sm3840"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-sm3840/"
description: "sane-sm3840 – SANE backend for Microtek scanners with SCAN08 USB chip"
---

<p>sane-sm3840 &#8211; SANE backend for Microtek scanners with SCAN08 USB chip</p>
<h2>Description</h2>
<p>The <code>sane-sm3840</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some Microtek scanners with the SCAN08 USB chip. There exist backends for Microtek scanners with SCSI command set. Refer to <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5) and <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5) for details. There also exists a Microtek 3600 series driver, see <code><a href="/docs/linux/man/5-sane-sm3600/">sane-sm3600</a></code>(5) for details. At present, the following scanners are known positively to work with this backend:</p>
<dl>
<dd>
<pre>Vendor Product ID: Remark:
-------- -------------- -----------
Microtek ScanMaker 3840 All modes OK
Microtek ScanMaker 4800 All modes OK</pre>
</dl>
<p> If you own a Microtek scanner with the SCAN08 chip other than the ones listed above, it may or may not work with SANE. Feel free to contact the backend author (<i>earle [at] ziplabel.com</i>) to report results with scanners not on the list. </p>
<h2>Frontend Options</h2>
<p>The following options are supported by the <code>sane-sm3840</code> driver:</p>
<dl>
<dt><code>&#8211;mode color|gray|lineart|halftone</code></p>
<dd>Color or grayscale mode. </p>
<dt><code>&#8211;resolution 150|300|600|1200</code></p>
<dd>Pixels per inch for scans. </p>
<dt><code>&#8211;depth 8|16</code></p>
<dd>Note that the least significant bits of 16bpp mode may be noise. </p>
<dt><code>&#8211;brightness 1..4096</code></p>
<dd>Higher numbers increase brightness of returned image. </p>
<dt><code>&#8211;contrast 0.1..9.9</code></p>
<dd>Larger numbers decrease contrast of returned image. </p>
<dt><code>&#8211;lamp-timeout 1..15</code></p>
<dd>Time in minutes until the lamp is turned off after a scan. </p>
</dl>
<h2>Configuration</h2>
<p>This backend does not support a configuration file right now.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sm3840.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sm3840.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SM3840</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. To see error messages on stderr set <code>SANE_DEBUG_SM3840</code> to 1. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5), <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5), <code><a href="/docs/linux/man/5-sane-sm3600/">sane-sm3600</a></code>(5)<br />
 <i><a rel="nofollow" href="http://www.ziplabel.com/sm3840">http://www.ziplabel.com/sm3840</a></i> </p>
<h2>Author</h2>
<p>Earle F. Philhower III &lt;<i>earle [at] ziplabel.com</i>&gt;</p>
