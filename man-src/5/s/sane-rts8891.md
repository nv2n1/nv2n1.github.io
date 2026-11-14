---
title: "sane-rts8891(5)"
name: "sane-rts8891"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-rts8891/"
description: "sane-rts8891 – SANE backend for rts8891 based scanners"
---

<p>sane-rts8891 &#8211; SANE backend for rts8891 based scanners</p>
<h2>Description</h2>
<p>The <code>sane-rts8891</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to scanners based on the rts8891 ASIC. The scanners that work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model status
---------------------- -----------
 Umax Astra 4400 untested
 Umax Astra 4450 untested
 HP scanjet 4000c good
 HP scanjet 4470c good</pre>
</dl>
<p> The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).<br />
 If you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list. Valid command line options and their syntax can be listed by using</p>
<dl>
<dd>scanimage &#8211;help -d rts8891</dl>
<dl>
<dt><code>Scan Mode Options</code></p>
<dd>
<dt><code>&#8211;mode</code></p>
<dd>selects the basic mode of operation of the scanner. Valid choices are <i>Color</i>, <i>Gray</i> and <i>Lineart</i>. The default mode is <i>Color</i>. The <i>Lineart</i> mode is for black and white only (1 bit). <i>Gray</i> will produce 256 levels of gray (8 bits). <i>Color</i> mode allows for over 16 million different colors produced from 24 bits of color information.</p>
<dt><code>&#8211;resolution</code></p>
<dd>selects the resolution for a scan. The horizontal and vertical resolutions are set by the value of this option. The scanner is capable of the following resolutions for the specified option value:</dl>
<dl>
<dd>
<pre> Value Hor. Resolution Vert. Resolution
 ----- --------------- -------------------
 75 75dpi 75dpi
 150 150dpi 150dpi
 300 300dpi 300dpi
 600 600dpi 600dpi
 1200 1200dpi 1200dpi</pre>
</dl>
<dl>
<dt><code>&#8211;preview</code></p>
<dd>requests a preview scan. The resolution used for that scan is 75 dpi and the scan area and the scan mode are as specified through their options, or the default if not specified. The default value for preview mode is &quot;no&quot;.</p>
<dt><code>&#8211;threshold</code></p>
<dd>selects the minimum-brightness to get a white point. The threshold is only used with Lineart mode scans. It is specified as a percentage in the range 0..100% (in steps of 1). The default value of the threshold option is 50. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/rts8891.conf</i> contains the usb device ids of supported scanners (eg usb 0x043d 0x007c) and scanner configuration options. Empty lines and lines starting with a hash mark (#) are ignored. </p>
<p> The options supported are <code>allowsharing</code>, <code>modelnumber</code> </p>
<p> Option</p>
<dl>
<dt><code>allowsharing</code></p>
<dd>enables or not the sharing of the scanner between multiple frontends at the same time.</p>
<dt><code>modelnumber</code></p>
<dd>is used to force the reported model by the backend and is only useful in the case of a scanner which NVRAM has been erased. </p>
<dl>
<dd>
<pre>0 to report a HP4470c.
1 to report a HP4400c.
2 to report an Astra 4400.</pre>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-rts8891.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-rts8891.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_RTS8891 SANE_DEBUG_RTS8891_LOW SANE_DEBUG_RTS88XX_LIB</code></p>
<dd>If the library was compiled with debug support enabled, these environment variables control the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Limitations</h2>
<p>Scanners of the same model exist with different sensors, due to lack of data (ie USB logs) some sensors are better supported than others. At least 75 dpi mode is working for any model. Sharing the scanner between several frontends at the same time (allowsharing option) may not work on some USB controllers. </p>
<p> XPA is not (yet) supported.</p>
<h2>Bugs</h2>
<p>No bugs currently known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>This backend has been developed by St&eacute;phane Voltz.</p>
<dd><i><a rel="nofollow" href="http://stef.dev.free.fr/sane/rts8891">http://stef.dev.free.fr/sane/rts8891</a></i> </p>
</dl>
<h2>Credits</h2>
<dl>
<dt>Many thanks go to:</p>
<dd>Laurent Fournier who donated me a HP4470c. Vladimir Sysoev and &quot;TheUnruly Squash&quot; for the time they spent recording USB activity and testing the experimental version on HP4400 models. </p>
</dl>
