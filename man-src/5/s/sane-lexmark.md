---
title: "sane-lexmark(5)"
name: "sane-lexmark"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-lexmark/"
description: "sane-lexmark – SANE backend for Lexmark X1100/X1200 Series scanners"
---

<p>sane-lexmark &#8211; SANE backend for Lexmark X1100/X1200 Series scanners</p>
<h2>Description</h2>
<p>The <code>sane-lexmark</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the scanner part of Lexmark X1100/X1200 AIOs. This backend should be considered <code>beta-quality</code> software! The scanners that should work with this backend are:</p>
<dl>
<dd>
<pre> Vendor Model status
---------------------- -----------
 Lexmark X74 good
 Lexmark X1110 untested
 Lexmark X1140 untested
 Lexmark X1150 good
 Lexmark X1170 good
 Lexmark X1180 good
 Lexmark X1185 complete
 Lexmark X12xx good in USB1.1,
 not fully tested in USB2.0
 Dell A920 good</pre>
</dl>
<p> The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).<br />
 If you notice any strange behavior, please report to the backend maintainer or to the SANE mailing list. Valid command line options and their syntax can be listed by using</p>
<dl>
<dd>scanimage &#8211;help -d lexmark:usb:&lt;usb port&gt;</dl>
<dl>
<dt><code>Scan Mode Options</code></p>
<dd>
<dt><code>&#8211;mode</code></p>
<dd>selects the basic mode of operation of the scanner. Valid choices are <i>Color</i>, <i>Gray</i> and <i>Lineart</i>. The default mode is <i>Color</i>. The <i>Lineart</i> mode is black and white only (1 bit). <i>Gray</i> mode will produce 256 levels of gray (8 bits). <i>Color</i> mode allows for over 16 million different colors produced from 24 bits of color information.</p>
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
 1200 600dpi 1200dpi (only for X11xx models with 'B2' sensor)</pre>
</dl>
<dl>
<dt><code>&#8211;preview</code></p>
<dd>requests a preview scan. The resolution used for that scan is 75 dpi and the scan area and the scan mode are as specified through their options, or the default if not specified. The default value for preview mode is &quot;no&quot;.</p>
<dt><code>&#8211;threshold</code></p>
<dd>selects the minimum-brightness to get a white point. The threshold is only used with Lineart mode scans. It is specified as a percentage in the range 0..100% (in steps of 1). The default value of the threshold option is 50. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/lexmark.conf</i> contains only the usb device id (eg usb 0x043d 0x007c).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-lexmark.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-lexmark.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_LEXMARK</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity.</p>
<dt><code>SANE_DEBUG_LEXMARK_LOW</code></p>
<dd>Provides debug output for low level Lexmark functions. </p>
</dl>
<h2>Limitations</h2>
<p>The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the scanner can support. For instance, shading correction (vertical stripes due to sensor variation across its width) is done in software. Head park position is also detected by software. The data compression isn&#8217;t supported for the X1200 series on USB 1.1, leading to slow scans.</p>
<h2>Bugs</h2>
<p>No bugs currently known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<dl>
<dt>The backend was originally written by Fred Odendaal.</p>
<dd><i><a rel="nofollow" href="http://ca.geocities.com/freshshelf@rogers.com/">http://ca.geocities.com/freshshelf@rogers.com/</a></i></p>
<dt>The new version is currently developed by St&eacute;phane Voltz.</p>
<dd><i><a rel="nofollow" href="http://stef.dev.free.fr/sane/lexmark">http://stef.dev.free.fr/sane/lexmark</a></i></p>
<dt>X74 support was written by Torsten Houwaart</p>
<dd>&lt;<i>ToHo [at] gmx.de</i>&gt; </p>
</dl>
<h2>Credits</h2>
<dl>
<dt>Many thanks go to:</p>
<dd>Julien Furgerot who lent me a Dell A920. Robert Price, Dani Ele and Dalai Felinto for the time they spent recording USB activity and testing the experimental version. </p>
</dl>
