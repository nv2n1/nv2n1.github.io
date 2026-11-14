---
title: "sane-teco1(5)"
name: "sane-teco1"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-teco1/"
description: "sane-teco1 – SANE backend for TECO / RELISYS scanners"
---

<p>sane-teco1 &#8211; SANE backend for TECO / RELISYS scanners</p>
<h2>Description</h2>
<p>The <code>sane-teco1</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some TECO SCSI flatbed scanners. This backend should be considered <code>beta-quality</code> software! TECO scanners are sold under various brands like RELISYS, PIOTECH, TRUST. This backend may or may not support yours. The scanners that should work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model TECO model status
---------------------- -------------- -----------
 Relisys AVEC 2400 VM3520 tested
 Relisys AVEC 2412 VM3520+ tested
 Relisys AVEC 4800 VM4530 untested
 Relisys AVEC 4816 VM4530+ untested
 Relisys RELI 2400 VM3530 untested
 Relisys RELI 2412 VM3530+ tested
 Relisys RELI 2412 VM3530+ untested
 Relisys RELI 4816 VM4540 tested
 Relisys RELI 4830 VM4542 tested
 Relisys RELI 9600 VM6530 untested
 Relisys RELI 9612 VM6530* untested
 Relisys RELI 9624 VM6530+ untested
 Relisys RELI 9630 VM6540 untested
 Relisys RELI DS15 VM3440 untested
 Relisys RELI DS6 VM3420 untested
 Dextra DF-600P VM3510 tested
 Dextra DF-4830T VM4542 untested
 Dextra DF-1200T+ VM3530+ untested
 Dextra DF-9624 VM6530+ untested</pre>
</dl>
<p> Note that the untested scanner will not be directly supported. You should contact the author for that. The TECO VM number can usually be found at the back of the scanner. It is also part of the FCC ID. <i>sane-find-scanner -v</i> will also show the SCSI inquiry, and if it is a TECO scanner, the name will be there too. The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).<br />
 If you have any success with a scanner not listed here, or if you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list. Valid command line options and their syntax can be listed by using:</p>
<dl>
<dd>scanimage &#8211;help -d teco1</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode Black &amp; White|Grayscale|Color</code></p>
<dd>Selects the basic mode of operation of the scanner. Valid choices are <i>Black &amp; White</i>, <i>Grayscale</i> and <i>Color</i>. The <i>Black &amp; White</i> mode is for black and white only (1 bit). <i>Grayscale</i> will produce 256 levels of gray (8 bits). <i>Color</i> will produce a 24 bit color image.</p>
<dt><code>&#8211;resolution 1..600</code></p>
<dd>Selects the resolution for a scan. The scanner can do all resolutions between 1 and 600, in increments of 1.</p>
<dt><code>Geometry options</code></p>
<dd>
<dt><code>-l -t -x -y</code></p>
<dd>Controls the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters by default.</p>
<dt><code>Enhancement options</code></p>
<dd>
<dt><code>&#8211;custom-gamma</code></p>
<dd>(color mode only) allows the user to specify a gamma table (see the next 3 parameters).</p>
<dt><code>&#8211;red-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long. Color mode only.</p>
<dt><code>&#8211;green-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long. Color mode only.</p>
<dt><code>&#8211;blue-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long. Color mode only.</p>
<dt><code>&#8211;dither Line art|2&#215;2|3&#215;3|4&#215;4 bayer|4&#215;4 smooth|8&#215;8 bayer|8&#215;8 smooth|8&#215;8 horizontal|8&#215;8 vertical</code></p>
<dd>Select the dither mask to use. Black &amp; White only.</p>
<dt><code>&#8211;preview</code></p>
<dd>Requests a preview scan. The resolution used is 22 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is &quot;no&quot;. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/teco1.conf</i> supports only one item: the device name to use (eg <i>/dev/scanner</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco1.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco1.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_TECO1</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Limitations</h2>
<p>The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support.</p>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>The package is actively maintained by Frank Zago.</p>
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#teco">http://www.zago.net/sane/#teco</a></i> </p>
</dl>
<h2>Credits</h2>
<p>Thanks to Gerard Delafond for the VM4542 support. Thanks to Jean-Yves Simon for the VM3510 support.</p>
