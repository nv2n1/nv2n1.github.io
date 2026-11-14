---
title: "sane-leo(5)"
name: "sane-leo"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-leo/"
description: "sane-leo – SANE backend for LEO Technologies scanners"
---

<p>sane-leo &#8211; SANE backend for LEO Technologies scanners</p>
<h2>Description</h2>
<p>The <code>sane-leo</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some LEO SCSI flatbed scanners. This backend should be considered <code>beta-quality</code> software! LEO scanners were also sold under the Across Technologies brand. The scanners that should work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model status
---------------------- -----------
 Across FS-1130 tested
 LEO S3 tested</pre>
</dl>
<p> The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).<br />
 If you have any strange behavior, please report to the backend maintainer or to the SANE mailing list. Valid command line options and their syntax can be listed by using</p>
<dl>
<dd>scanimage &#8211;help -d leo</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode</code></p>
<dd>selects the basic mode of operation of the scanner. Valid choices are <i>Black &amp; White</i>, <i>Grayscale</i> and <i>Color</i>. The <i>Black &amp; White</i> mode is black and white only (1 bit). <i>Grayscale</i> mode will produce 256 levels of gray (8 bits). <i>Color</i> mode will produce a 24 bit color image.</p>
<dt><code>&#8211;resolution</code></p>
<dd>selects the resolution for a scan. The scanner can do all resolutions between 1 and 300, in increments of 1.</p>
<dt><code>Geometry options</code></p>
<dd>
<dt><code>-l -t -x -y</code></p>
<dd>control the scan area: -l sets the top left x coordinate, -t the top left y coordinate, -x selects the width and -y the height of the scan area. All parameters are specified in millimeters by default.</p>
<dt><code>Enhancement options</code></p>
<dd>
<dt><code>&#8211;custom-gamma</code></p>
<dd>(grayscale and color mode only) allows the user to specify a gamma table (see the next 3 parameters).</p>
<dt><code>&#8211;red-gamma-table</code></p>
<dd>(color mode only) can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long.</p>
<dt><code>&#8211;green-gamma-table</code></p>
<dd>(color mode only) can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long.</p>
<dt><code>&#8211;blue-gamma-table</code></p>
<dd>(color mode only) can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long.</p>
<dt><code>&#8211;halftone</code></p>
<dd>(Black &amp; White only) select the halftone mask to use. Possible values are <i>Diamond</i>, <i>8&#215;8 Coarse Fatting</i>, <i>8&#215;8 Fine Fatting</i>, <i>8&#215;8 Bayer</i> and <i>8&#215;8 Vertical Line</i>.</p>
<dt><code>&#8211;preview</code></p>
<dd>requests a preview scan. The resolution used for that scan is 28 dpi and the scan area is the maximum allowed. The scan mode is user selected. The default is &quot;no&quot;. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/leo.conf</i> supports only one information: the device name to use (eg <i>/dev/scanner</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-leo.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-leo.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_LEO</code></p>
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
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#leo">http://www.zago.net/sane/#leo</a></i> </p>
</dl>
