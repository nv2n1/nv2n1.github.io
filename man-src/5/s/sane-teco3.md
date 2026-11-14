---
title: "sane-teco3(5)"
name: "sane-teco3"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-teco3/"
description: "sane-teco3 – SANE backend for TECO / RELISYS scanners"
---

<p>sane-teco3 &#8211; SANE backend for TECO / RELISYS scanners</p>
<h2>Description</h2>
<p>The <code>sane-teco3</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some TECO SCSI flatbed scanners. This backend should be considered <code>alpha-quality</code> software! TECO scanners are sold under various brands like RELYSIS, PIOTECH, TRUST. This backend may or may not support yours. The scanners that should work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model TECO model status
 --------------------------- ---------- ----------
 Relisys Scorpio VM3552 tested
 Plustek OpticPro 2400SP VM3552 untested
 PIOTECH Splendeur 3024 VM3552 tested
 Trust Imagery 2400 SP VM3552 tested
 Trust Imagery 4800 SP+ VM3552 tested
 Trust Imagery 9600 SP VM3552 untested</pre>
</dl>
<p> The TECO VM number can usually be found at the back of the scanner. It is also part of the FCC ID. The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).<br />
 If you have any success with a scanner not listed here, or if you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list. </p>
<h2>Options</h2>
<p>Valid command line options and their syntax can be listed by using: </p>
<dl>
<dd>scanimage &#8211;help -d teco3</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode Black &amp; White|Grayscale|Color</code></p>
<dd>Selects the basic mode of operation of the scanner. The <i>Black &amp; White</i> mode is black and white only (1 bit). <i>Grayscale</i> will produce 256 levels of gray (8 bits). <i>Color</i> will produce a 24-bit color image. </p>
<dt><code>&#8211;resolution 1..1200</code></p>
<dd>Selects the resolution for a scan. The scanner can do all resolutions between 1 and 1200, in increments of 1. </p>
<dt><code>&#8211;preview</code></p>
<dd>Requests a preview scan. The resolution used for that scan is 22 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is &quot;no&quot;. </p>
<dt><code>Geometry options</code></p>
<dd>
<dt><code>-l -t -x -y</code></p>
<dd>Control the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters by default. </p>
</dl>
<h2>Options For Color Mode Only</h2>
<dl>
<dt><code>&#8211;custom-gamma</code></p>
<dd>Allows the user to specify a gamma table (see the next 3 parameters). </p>
<dt><code>&#8211;red-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the red channel. The table must be 1024 bytes long. </p>
<dt><code>&#8211;green-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the green channel. The table must be 1024 bytes long. </p>
<dt><code>&#8211;blue-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the blue channel. The table must be 1024 bytes long. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/teco3.conf</i> supports only one item: the device name to use (eg <i>/dev/scanner</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco3.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco3.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_TECO3</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Limitations</h2>
<p>The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support.</p>
<h2>Bugs</h2>
<p>Not much. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>The package is actively maintained by Frank Zago.</p>
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#teco3">http://www.zago.net/sane/#teco3</a></i> </p>
</dl>
