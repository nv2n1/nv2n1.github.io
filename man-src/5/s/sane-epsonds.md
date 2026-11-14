---
title: "sane-epsonds(5)"
name: "sane-epsonds"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-epsonds/"
description: "sane-epsonds – SANE backend for EPSON ESC/I-2 scanners"
---

<p>sane-epsonds &#8211; SANE backend for EPSON ESC/I-2 scanners</p>
<h2>Description</h2>
<p>The <code>sane-epsonds</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Epson ESC/I-2 scanners. Valid command line options and their syntax can be listed by using</p>
<dl>
<dd>scanimage &#8211;help -d epsonds</dl>
<p> Not all devices support all options.</p>
<dl>
<dt><i>Scan Mode</i></p>
<dd>The <code>&#8211;mode</code> switch selects the basic mode of operation of the scanner. Valid choices are Lineart, Gray and Color. The Lineart mode is black and white only, Gray will produce 256 levels of gray or more depending on the scanner and Color means 24 bit color mode or more depending on the scanner. Some scanners will internally use 36 bit color, their external interface however may only support 24 bits. The <code>&#8211;depth</code> option selects the bit depth the scanner is using. This option is only available for scanners that support more than one bit depth. Older scanners will always transfer the image in 8bit mode. Newer scanners allow one to select either 8 bits, 12 or 14 bits per color channel. For a color scan this means an effective color depth of 36 or 42 bits over all three channels. The valid choices depend on the scanner model. The <code>&#8211;resolution</code> switch selects the resolution for a scan. Some EPSON scanners will scan in any resolution between the lowest and highest possible value. The list reported by the scanner can be displayed using the &quot;&#8211;help -d epson&quot; parameters to <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1). The geometry options <code>-l -t -x -y</code> control the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters. The <code>&#8211;source</code> option selects the scan source. Valid options depend on the installed options. The default is &quot;Flatbed&quot;. The <code>&#8211;eject</code> option ejects the sheet in the ADF. The <code>&#8211;adf-mode</code> option select the ADF mode (simplex/duplex). </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/epsonds.conf</i> specifies the device(s) that the backend will use. Possible connection types are:</p>
<dl>
<dt><code>USB</code></p>
<dd>For not automatically detected USB scanners, their VENDOR and PRODUCT ID can be specified manually in the config file. More information about valid syntax for USB devices can be found in <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5).</p>
<dt><code>Network (not yet supported)</code></p>
<dd>Network scanners can be auto-discovered if <code>autodiscovery</code> is specified after <code>net</code> keyword. An IP address to connect to can also be used.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-epsonds.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-epsonds.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_EPSONDS</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. Values around 11-16 will usually be enough for a bug report. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Author</h2>
<p>The backend is written by Alessandro Zummo.</p>
