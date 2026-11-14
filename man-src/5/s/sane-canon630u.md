---
title: "sane-canon630u(5)"
name: "sane-canon630u"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-canon630u/"
description: "sane-canon630u – SANE backend for the Canon 630u USB flatbed scanner"
---

<p>sane-canon630u &#8211; SANE backend for the Canon 630u USB flatbed scanner</p>
<h2>Description</h2>
<p>The <code>sane-canon630u</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Canon flatbed scanners:</p>
<dl>
<dd>CanoScan 630u<br />
 CanoScan 636u
</dl>
<p> Color scanning is supported at 75, 150, 300, and 600 dpi, and gamma and analog gain are adjustable. TESTERS ARE WELCOME. Send your bug reports and comments to Nathan Rutman <i>&lt;nthn1 [at] yahoo.com&gt;</i>. </p>
<h2>Configuration</h2>
<p>The contents of the <i>canon630u.conf</i> file is a list of device names that correspond to Canon USB scanners. Empty lines and lines starting with a hash mark (#) are ignored. Only one device name can be listed in <i>canon630u.conf</i>. The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct device. Under Linux, such a device name could be <i>/dev/usb/scanner0</i> for example. See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for details. </p>
<p> This product-specific scanner driver uses the lower-level kernel USB driver &quot;scanner&quot;. Check for &quot;Driver=usbscanner&quot; under <i>/proc/bus/usb/devices</i>. If &quot;Driver=(none)&quot;, try forcing it with <i>insmod scanner vendor=0x04a9 product=0x2204</i></p>
<h2>Notes</h2>
<p>Due to Canon&#8217;s unwillingness to provide scanner documentation, this software was developed by analyzing the USB traffic of the Windows 2000 driver. So things like the calibration procedure I kind of made up; it seems to work for my scanner. If you have complaints, let me know. This driver requires the ability to send USB Control Messages, available in kernel 2.4.12 or later. Some users have reported that this driver doesn&#8217;t work at all. This seems to be a hardware specific issue, although I dsane-uson&#8217;t know what exactly the problem is. If you are having problems, please send me the info in <i>/proc/bus/usb/devices</i>, <i>/proc/pci</i>, the kernel <i>scanner.c</i> driver version from <i>/var/log/messages</i>, and the output from <i>SANE_DEBUG_CANON630U=12 scanimage &gt; /dev/null</i> </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/canon630u.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon630u.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon630u.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</p>
<dt><i>/tmp/canon.cal</i></p>
<dd>The calibration file used to normalize pixel brightness. This is calculated every time the scanner is first used after it has lost power. Deleting this file will force recalibration.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_CANON630U</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example:<br />
 SANE_DEBUG_CANON630U=12 scanimage &gt; /dev/null</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1)<br />
 <i><a rel="nofollow" href="http://canon-fb630u.sourceforge.net/">http://canon-fb630u.sourceforge.net/</a></i></p>
<h2>Author</h2>
<p>Nathan Rutman</p>
