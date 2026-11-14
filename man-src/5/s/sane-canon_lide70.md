---
title: "sane-canon_lide70(5)"
name: "sane-canon_lide70"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-canon_lide70/"
description: "sane-canon_lide70 – SANE backend for the Canon LiDE 70 and 600(F) USB flatbed scanners"
---

<p>sane-canon_lide70 &#8211; SANE backend for the Canon LiDE 70 and 600(F) USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>canon_lide70</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Canon Inc. CanoScan LiDE 70 and 600(F) flatbed scanners. The film unit of the LiDE 600F is not supported. Due to Canon&#8217;s unwillingness to provide scanner documentation, this software was developed by analyzing the USB traffic of the Windows XP driver. The precise meaning of the individual commands that are sent to the scanner is known only to a very limited extent. Some sophistication present in the Windows XP driver has been left out. There is, for example, no active calibration. Testers and reviewers are welcome. Send your bug reports and comments to the sane-devel mailing list <i>&lt;sane-devel [at] alioth-lists.debian.net&gt;</i>. </p>
<h2>Configuration</h2>
<p>The <i>/etc/sane.d/canon_lide70.conf</i> file identifies the LiDE 70 by its vendor code 0x04a9 and its product code 0x2225. For the LiDE 600(f) the product code is 0x2224.</p>
<h2>Backend Specific Options</h2>
<p><code>Scan Mode:</code> </p>
<dl>
<dt><code>&#8211;resolution 75|150|300|600|1200 [default 600]</code></p>
<dd>Sets the resolution of the scanned image in dots per inch. Scanning at 1200 dpi is not available on the LiDE 600(F) and it is very slow on the LiDE 70. </p>
<dt><code>&#8211;mode Color|Gray|Lineart [default: Color]</code></p>
<dd>Selects the scan mode. Lineart means fully black and fully white pixels only. </p>
<dt><code>&#8211;threshold 0..100 (in steps of 1) [default 75]</code></p>
<dd>Select minimum-brightness percentage to get a white point, relevant only for Lineart </p>
<dt><code>&#8211;non-blocking[=(yes|no)] [inactive]</code></p>
<dd>This option has not yet been implemented. Scans are captured in a temporary file with a typical size of 100MB. </p>
</dl>
<p> <code>Geometry:</code></p>
<dl>
<dt><code>-l 0..216.069 [default 0]</code></p>
<dd>Top-left x position of scan area in millimeters.</p>
<dt><code>-t 0..297 [default 0]</code></p>
<dd>Top-left y position of scan area in millimeters.</p>
<dt><code>-x 0..216.069 [default 80]</code></p>
<dd>Width of scan-area in millimeters.</p>
<dt><code>-y 0..297 [default 100]</code></p>
<dd>Height of scan-area in millimeters. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/canon_lide70.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon_lide70.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon_lide70.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_CANON_LIDE70</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example:<br />
 SANE_DEBUG_CANON_LIDE70=128 scanimage &gt; /dev/null</dl>
<h2>Known Problems</h2>
<p>At low resolutions (75 and 150 dpi, implying high slider speeds) the LiDE 70 misses the top one millimeter of the scan area. This can be remedied by shifting the document one millimeter downward, in cases where such precision matters. Note that <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) uses the 75 dpi mode for prescans. The problem is worse on the LiDE 600(F), where the offset is five millimeters.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1),<br />
 <a rel="nofollow" href="http://www.juergen-ernst.de/info_sane.html">http://www.juergen-ernst.de/info_sane.html</a> </p>
<h2>Author</h2>
<p>pimvantend, building upon pioneering work by Juergen Ernst.</p>
