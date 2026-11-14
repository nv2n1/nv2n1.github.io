---
title: "sane-matsushita(5)"
name: "sane-matsushita"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-matsushita/"
description: "sane-matsushita – SANE backend for Panasonic KV-SS high speed scanners"
---

<p>sane-matsushita &#8211; SANE backend for Panasonic KV-SS high speed scanners</p>
<h2>Description</h2>
<p>The <code>sane-matsushita</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some Panasonic KV-SS high speed scanners. This backend is stable. At present, the following scanners are known to work with this backend:</p>
<dl>
<dd>
<pre> Product id
--------------
 KV-SS25
 KV-SS25D
 KV-SS55EX (*)
 KV-S2025C (*)
 KV-S2045C (*)
 KV-S2065L (*)</pre>
</dl>
<p> (*) WARNING: None of the advanced options of these scanners are available (ie no color, no high resolution, no automatic cropping). Basically, the driver does no more than what it does for the KV-SS25. I don&#8217;t have access to such scanners, and thus cannot add these options. Other Panasonic high speed scanners may or may not work with that backend. Valid command line options and their syntax can be listed by using</p>
<dl>
<dd>scanimage &#8211;help -d matsushita</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode</code></p>
<dd>selects the basic mode of operation of the scanner.</p>
<dt><code>&#8211;resolution</code></p>
<dd>selects the resolution for a scan. Each model supports all or a subset of these resolutions: 100, 150, 200, 240, 300, 360, 400.</p>
<dt><code>&#8211;duplex</code></p>
<dd>indicates whether to scan both side of the sheet.</p>
<dt><code>&#8211;feeder-mode</code></p>
<dd>selects the number of pages to scan (one or until the tray is empty).</p>
<dt><code>Geometry</code></p>
<dd>
<dt><code>&#8211;paper-size A4|&#8230;|Legal|Letter [A4]</code></p>
<dd>options selects the area to scan. It adjust the <code>-l -t -x -y</code> options accordingly. It does not need to be the real size of the paper.</p>
<dt><code>-l -t -x -y</code></p>
<dd>control the scan area: -l sets the top left x coordinate, -t the top left y coordinate, -x selects the width and -y the height of the scan area. All parameters are specified in millimeters. It is possible to use the option <i>&#8211;paper-size</i> instead.</p>
<dt><code>Enhancement</code></p>
<dd>
<dt><code>&#8211;brightness</code></p>
<dd>controls the brightness of the acquired image. The value varies from 1 to 255, or less, depending on the scanner model.</p>
<dt><code>&#8211;contrast</code></p>
<dd>controls the contrast of the acquired image. Some models do not support that option.</p>
<dt><code>&#8211;automatic-threshold</code></p>
<dd>automatically sets brightness, contrast, white level, gamma, noise reduction and image emphasis. These options are not available when automatic-threshold is in use.</p>
<dt><code>&#8211;halftone-pattern</code></p>
<dd>option sets the tonal gradation for the halftone mode. Pattern downloading is not implemented by the backend.</p>
<dt><code>&#8211;autoseparation</code></p>
<dd>provides automatic separation of text and images.</p>
<dt><code>&#8211;white-level</code></p>
<dd>option indicate the source of the white base.</p>
<dt><code>&#8211;noise-reduction</code></p>
<dd>reduces the isolated dot noise. This option is not supported by all scanners.</p>
<dt><code>&#8211;image-emphasis</code></p>
<dd>option sets the image emphasis. Some selection are not available on all scanners.</p>
<dt><code>&#8211;gamma</code></p>
<dd>options set the gamma curve. It is only valid for Gray modes, and is not available on all scanners. Gamma downloading is not implemented by the backend. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/matsushita.conf</i> supports the device name to use (eg <i>/dev/scanner</i>) and the SCSI option to auto-detect the scanners supported.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-matsushita.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-matsushita.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_MATSUSHITA</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Limitations</h2>
<dl>
<dt><code>Memory in the KV-SS 25</code></p>
<dd>The KV-SS 25 has not enough internal memory to scan a whole A4 page in duplex mode at high resolution. The frontend will return a memory error in that case. Apparently, the KV-SS 25D has not that problem.</p>
<dt><code>Pattern and gamma downloading</code></p>
<dd>The scanner, with the proper firmware, can download a halftone pattern and a gamma table. This is not implemented.</p>
<dt><code>Sub-areas</code></p>
<dd>The scanner can support up to 3 sub-areas on each side to define some more precise enhancement options. This is not implemented.</p>
<dt><code>Duplex mode</code></p>
<dd>The backend does not support the setting of different options for each side. The scan will occur with the same options (halftone pattern, brightness, image emphasis) for both sides. </p>
</dl>
<h2>Scanning Example</h2>
<p>To date, the only frontend capable of using this scanner at full speed is <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1). </p>
<p> A <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1) command line would be: </p>
<p> scanadf -d matsushita &#8211;output-file scan%04d.pbm &#8211;start-count 0 &#8211;duplex &#8211;resolution 300 &#8211;feeder-mode=&quot;All pages&quot; &#8211;paper-size=&quot;A4&quot;</p>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>The package is actively maintained by Frank Zago.</p>
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#matsushita">http://www.zago.net/sane/#matsushita</a></i> </p>
</dl>
