---
title: "sane-teco2(5)"
name: "sane-teco2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-teco2/"
description: "sane-teco2 – SANE backend for TECO / RELISYS scanners"
---

<p>sane-teco2 &#8211; SANE backend for TECO / RELISYS scanners</p>
<h2>Description</h2>
<p>The <code>sane-teco2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some TECO SCSI flatbed scanners. This backend should be considered <code>beta-quality</code> software! TECO scanners are sold under various brands like Mustek, Relisys, Piotech, Primax, TRUST. This backend may or may not support yours. The scanners that should work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model TECO model status
--------------------------- -------------- -----------
 Mustek ScanMagic 4830S VM3575 untested
 Primax Jewel 4800 VM356A good
 Primax Profi 9600 VM6575 basic
 Primax Profi 19200 VM6586 good
 Relisys APOLLO Express 3 VM356A basic
 Relisys APOLLO Express 6 VM6565 good
 Relisys APOLLO Express 12 ? untested
 Relisys AVEC II S3 VM3564 good
 Relisys AVEC Super 3 VM3575 basic
 Relisys SCORPIO Pro VM6575 good
 Relisys SCORPIO Pro-S VM6586 untested
 Relisys SCORPIO Super 3 VM3575 good</pre>
</dl>
<p> For all these scanners, lineart and gray mode work well. However, most of them do not support more than a handful of resolutions in color mode. See the backend home page (under AUTHOR) for the exact status of each scanner. Note that the untested scanner will not be directly supported. You should contact the author for that. The TECO VM number can usually be found at the back of the scanner. It is also part of the FCC ID. The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/1-quiteinsane/">quiteinsane</a></code>(1) or <code><a href="/docs/linux/man/1-kooka/">kooka</a></code>(1).<br />
 If you have any success with a scanner not listed here, or if you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list. </p>
<h2>Options</h2>
<p>Valid command line options and their syntax can be listed by using: </p>
<dl>
<dd>scanimage &#8211;help -d teco2</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode Lineart|Gray|Color</code></p>
<dd>selects the basic mode of operation of the scanner. The <i>Lineart</i> mode is black and white only (1 bit). <i>Gray</i> mode will produce 256 levels of gray (8 bits). <i>Color</i> will produce a 24 bits color image. </p>
<dt><code>&#8211;resolution 1..600</code></p>
<dd>Selects the resolution for a scan. The scanner can do all resolutions between 1 and 600, in increments of 1, for <i>Lineart</i> and <i>Gray</i>. For <i>Color</i>, a restricted set of resolutions are available. </p>
<p> <code>Note:</code> All values with ydpi &gt; 300 (300 x 600) or 600 (600 x 1200) result in a wrong proportion for the scan. The proportion can be adjusted with the following <code><a href="/docs/linux/man/1-convert/">convert</a></code>(1) command from imagemagick:<br />
 <i>convert -geometry (dpi/max_xdpi * 100%)x100%</i><br />
 max_xdpi is for the vm3575 constant with 300 dpi e.g. 600dpi adjust with: convert -geometry 200%x100% </p>
<dt><code>&#8211;preview</code></p>
<dd>requests a preview scan. The resolution used for that scan is 50 dpi (for VM356A and VM6575 75 dpi) and the scan area is the maximum allowed. The scan mode is user selected. The default is &quot;no&quot;. </p>
<dt><code>Geometry options</code></p>
<dd>
<dt><code>-l, -t, -x, -y</code></p>
<dd>Control the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters by default. </p>
<dt><code>Enhancement options</code></p>
<dd>
<dt><code>&#8211;custom-gamma (no custom gamma option for the VM3564 and VM356A)</code></p>
<dd>(color mode only) allows the user to specify a gamma table (see the next 3 parameters). </p>
</dl>
<h2>Options For Color Mode</h2>
<p>These options are valid for scan mode <i>Color</i> only. </p>
<dl>
<dt><code>&#8211;red-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the red channel. The table must be 256 bytes long. </p>
<dt><code>&#8211;green-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the green channel. The table must be 256 bytes long. </p>
<dt><code>&#8211;blue-gamma-table</code></p>
<dd>Can be used to download a user defined gamma table for the blue channel. The table must be 256 bytes long. </p>
</dl>
<h2>OPTIONS ONLY FOR VM3564, VM356A, VM3575 and VM6575</h2>
<p>These options are only available for VM3564, VM356A, VM3575 and VM6575 models.</p>
<dl>
<dt><code>&#8211;white-level-r 0..64</code></p>
<dd>Selects what red radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration value loaded into the scanner. Scale 0..64 in steps of 1. </p>
<dt><code>&#8211;white-level-g 0..64</code></p>
<dd>Selects what green radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration value loaded into the scanner. Scale 0..64 in steps of 1. </p>
<dt><code>&#8211;white-level-b 0..64</code></p>
<dd>Selects what blue radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration value loaded into the scanner. Scale 0..64 in steps of 1. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/teco2.conf</i> supports only one item: the device name to use (eg <i>/dev/scanner</i>).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-teco2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_TECO2</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</p>
<dt><code>SANE_TECO2_CAL_ALGO</code></p>
<dd>Either 0 or 1. Selects the algorithm for the calibration. A value of 1 seems to give better scans on the VM356A, VM3575. Feedback on it is welcome. For VM3564, VM356A, VM3575, VM6575 default 1. For other supported types default 0. </p>
</dl>
<h2>Limitations</h2>
<p>The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support.</p>
<h2>Bugs</h2>
<p>Plenty. Parts of this backend are still under development. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Authors</h2>
<dl>
<dt>Frank Zago</p>
<dd><i><a rel="nofollow" href="http://www.zago.net/sane/#teco2">http://www.zago.net/sane/#teco2</a></i></p>
<dt>The package is actively maintained by Gerard Klaver.</p>
<dd><i><a rel="nofollow" href="http://gkall.hobby.nl/teco2.html">http://gkall.hobby.nl/teco2.html</a></i> </p>
</dl>
<h2>Credits</h2>
<p>Thanks to:</p>
<dl>
<dt>Gerard Klaver for his relentless VM3575 testings and contributed a patch to support the VM3564 and VM356A.</p>
<dd>
<dt>Mark Plowman for providing the first SCSI traces from a VM3575.</p>
<dd>
<dt>Andreas Klaedtke for providing the first SCSI traces from a VM6586 and for his testing, and to Stefan von Dombrowski for his testing.</p>
<dd>
<dt>Nicolas Peyresaubes for providing the first SCSI traces from a VM656A and for his testing.</p>
<dd>
<dt>Dave Parker for testing the support for the VM6575.</p>
<dd>
<dt>Michael Hoeller for testing the support for the VM356A.</p>
<dd>
<dt>Christoph Hoeffner for testing the support for the VM3564 (Relisys AVEC II S3 firmware 1.09).</p>
<dd></dl>
