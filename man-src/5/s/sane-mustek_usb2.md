---
title: "sane-mustek_usb2(5)"
name: "sane-mustek_usb2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-mustek_usb2/"
description: "sane-mustek_usb2 – SANE backend for SQ113 based USB flatbed scanners"
---

<p>sane-mustek_usb2 &#8211; SANE backend for SQ113 based USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-mustek_usb2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on the Service &amp; Quality SQ113 chipset. At the moment, only the Mustek BearPaw 2448 TA Pro is supported. It&#8217;s planned to add support for other scanners that are based on the SQ113 and maybe SQ11 chip. For more details, see the <code>sane-mustek_usb2</code> backend homepage: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek_usb2-backend/">http://www.meier-geinitz.de/sane/mustek_usb2-backend/</a></i>. This is BETA software. Especially if you test new or untested scanners, keep your hand at the scanner&#8217;s plug and unplug it, if the head bumps at the end of the scan area. If you own a scanner other than the ones listed on the mustek_usb2 homepage that works with this backend, please let me know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to me. Even if the scanner&#8217;s name is only slightly different from the models already listed as supported, please let me know. </p>
<h2>Libusb Issues</h2>
<p>Please use libusb-0.1.8 or later. Without libusb or with older libusb versions all kinds of trouble can be expected. The scanner should be found by <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) without further actions. For setting permissions and general USB information, look at <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_usb2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_usb2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_MUSTEK_USB2</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_MUSTEK_USB2=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1)<br />
 <i>/usr/share/doc/libsane/mustek_usb2/mustek_usb2.CHANGES</i><br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek_usb2-backend/">http://www.meier-geinitz.de/sane/mustek_usb2-backend/</a></i> </p>
<h2>Author</h2>
<p>The driver has been written Roy Zhou, Jack Xu, and Vinci Cen from Mustek.<br />
 Adjustments to SANE by Henning Meier-Geinitz.</p>
<h2>Bugs</h2>
<p>Please contact me if you find a bug or missing feature: &lt;<i>henning [at] meier-geinitz.de</i>&gt;.<br />
 Please send a debug log if your scanner isn&#8217;t detected correctly (see <code>SANE_DEBUG_MUSTEK_USB2</code> above). </p>
