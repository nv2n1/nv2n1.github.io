---
title: "sane-sm3600(5)"
name: "sane-sm3600"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-sm3600/"
description: "sane-sm3600 – SANE backend for Microtek scanners with M011 USB chip"
---

<p>sane-sm3600 &#8211; SANE backend for Microtek scanners with M011 USB chip</p>
<h2>Description</h2>
<p>The <code>sane-sm3600</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some Microtek scanners with the Toshiba M011 custom USB chip. This backend should be considered alpha. There are also backends for Microtek scanners with SCSI command set. Refer to <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5) and <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5) for details. At present, the following scanners are known positively to work with this backend:</p>
<dl>
<dd>
<pre>Vendor Product id: Remark:
-------- -------------- -----------
Microtek ScanMaker 3600 all modes ok
Microtek ScanMaker 3700 reported to work
Microtek ScanMaker 3750 reported to work</pre>
</dl>
<p> If you own a Microtek scanner with the M011 chip other than the ones listed above, it may or may not work with SANE! </p>
<h2>Frontend Options</h2>
<p>This backend dynamically enables the options for the frontend, that are supported by the scanner dependent on the scanning-mode and other options. Unsupported options are disabled. </p>
<p> The following options are supported by the <code>sane-sm3600</code> backend: Color, grayscale, halftone and lineart scans. Also contrast, brightness, and gamma correction.</p>
<h2>Device Names</h2>
<p>This backend does not support device names in a standardized form.</p>
<h2>Configuration</h2>
<p>This backend does not support a configuration file right now.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sm3600.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sm3600.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SM3600</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. To see error messages on stderr set <code>SANE_DEBUG_SM3600</code> to 1. </p>
<p> E.g. just say:<br />
 export SANE_DEBUG_SM3600=5 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7)<code>,</code> <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5), <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5)<br />
 <i><a rel="nofollow" href="http://sm3600.sourceforge.net">http://sm3600.sourceforge.net</a></i> </p>
<h2>Author</h2>
<p>Marian Eichholz &lt;<i>eichholz [at] computer.org</i>&gt;<br />
 Glenn Ramsey &lt;<i>glenn [at] componic.com</i>&gt;</p>
