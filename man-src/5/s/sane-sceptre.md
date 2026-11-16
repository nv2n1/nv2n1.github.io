---
title: "sane-sceptre(5)"
name: "sane-sceptre"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-sceptre/"
description: "sane-sceptre – SANE backend for SCEPTRE scanners"
---

<p>sane-sceptre &#8211; SANE backend for SCEPTRE scanners</p>
<h2>Description</h2>
<p>The <code>sane-sceptre</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Sceptre flatbed scanners. This backend should be considered <code>beta-quality</code> software! Please report any strange behavior to the maintainer of the backend or to the SANE mailing list. </p>
<p> At present, only one scanner is known to work with this backend: </p>
<dl>
<dd>
<pre>Model Connection Type
--------------------------- -------------------
Sceptre VividScan S1200 SCSI</pre>
</dd></dl>
<p> The make of this scanner is KINPO, so other scanners from that manufacturer may also work (eg. the S600).</p>
<h2>Options</h2>
<p>The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code>xscanimage</code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). </p>
<p> Valid command line options and their syntax can be listed by using </p>
<dl>
<dd>scanimage &#8211;help -d sceptre</dd></dl>
<dl>
<dt><code>Scan Mode</code></dt>
<dd>
</dd><dt><code>&#8211;mode Lineart|Halftone|Gray|Color</code></dt>
<dd>Selects the basic mode of operation of the scanner. The <i>Lineart</i> and <i>Halftone</i> mode are black and white only (1 bit). <i>Gray</i> will produce 256 levels of gray (8 bits). <i>Color</i> will produce a 24 bits color image. The scanner supports 30 bits internally but it only exports 24. </dd>
<dt><code>&#8211;resolution 50..1200</code></dt>
<dd>Selects the resolution for a scan. The scanner can do several resolutions between 50 and 1200. </dd>
<dt><code>&#8211;halftone-pattern 1|2|3|4</code></dt>
<dd>Selects the pattern mode that is used in <i>Halftone</i> mode. </dd>
<dt><code>&#8211;gamma-correction Default|User Defined|High Density Printing|Low density printing|High contrast printing</code></dt>
<dd>controls the scanner internal gamma correction. </dd>
<dt><code>&#8211;custom-gamma</code></dt>
<dd>Allows the user to specify a gamma table (see the next 3 parameters). <i>Color</i> mode only. </dd>
<dt><code>&#8211;red-gamma-table</code></dt>
<dd>Can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long. <i>Color</i> mode only. </dd>
<dt><code>&#8211;green-gamma-table</code></dt>
<dd>Can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long. <i>Color</i> mode only. </dd>
<dt><code>&#8211;blue-gamma-table</code></dt>
<dd>Can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long. <i>Color</i> mode only. </dd>
<dt><code>&#8211;threshold 0..255</code></dt>
<dd>Sets the threshold for black and white pixels in <i>Lineart</i> mode. Possible values are from 0 (darker) to 255 (lighter). </dd>
<dt><code>&#8211;preview</code></dt>
<dd>Requests a preview scan. The resolution used for that scan is 30 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is &quot;no&quot;. </dd>
<dt><code>The geometry options</code></dt>
<dd>
</dd><dt><code>-l -t -x -y</code></dt>
<dd>control the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters by default. </dd>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/sceptre.conf</i> supports only one item: the device name to use (eg <i>/dev/scanner</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sceptre.a</i></dt>
<dd>The static library implementing this backend.</dd>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sceptre.so</i></dt>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </dd>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SCEPTRE</code></dt>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </dd>
</dl>
<h2>Limitations</h2>
<dl>
<dt><code>Resolutions</code></dt>
<dd>The windows TWAIN driver can be set to any resolution between 50 to 1200 (excluding software interpolation). This backend cannot. Only a handful of resolution are available, although they should be numerous enough. </dd>
</dl>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code>xscanimage</code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>The package is actively maintained by Frank Zago.</dt>
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#sceptre">http://www.zago.net/sane/#sceptre</a></i> </dd>
</dl>
