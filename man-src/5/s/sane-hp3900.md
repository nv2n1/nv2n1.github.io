---
title: "sane-hp3900(5)"
name: "sane-hp3900"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hp3900/"
description: "sane-hp3900 – SANE backend for RTS8822 chipset based scanners"
---

<p>sane-hp3900 &#8211; SANE backend for RTS8822 chipset based scanners</p>
<h2>Description</h2>
<p>The <code>sane-hp3900</code> library implements a SANE (Scanner Access Now Easy) backend that provides access at least to the following USB flatbed scanners:</p>
<dl>
<dd>
<pre>Model: Chipset:
------ --------
HP ScanJet 3800 RTS8822BL-03A
HP ScanJet 3970 RTS8822L-01H
HP ScanJet 4070 Photosmart RTS8822L-01H
HP ScanJet 4370 RTS8822L-02A
HP ScanJet G2710 RTS8822BL-03A
HP ScanJet G3010 RTS8822L-02A
HP ScanJet G3110 RTS8822L-02A
UMAX Astra 4900/4950 RTS8822L-01H *
BenQ 5550 RTS8823L-01E *</pre>
</dl>
<p> More details can be found on the <code><a href="/docs/linux/man/5-sane-hp3900/">sane-hp3900</a></code>(5) backend homepage <i><a rel="nofollow" href="http://sourceforge.net/projects/hp3900-series/">http://sourceforge.net/projects/hp3900-series/</a></i>. This is ALPHA software. Keep your hand at the scanner&#8217;s plug and unplug it, if scanner does not start to scan. See also the <code>BUGS</code> section. If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i>, <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to us. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let us know. </p>
<h2>Configuration</h2>
<p>The contents of the <i>hp3900.conf</i> file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain the names of device files that correspond to an HP 39XX scanner. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by <code>usb vendor_id product_id</code> statements which are already included into <i>hp3900.conf</i>. &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner. If autodetection does not work, add the device name of your scanner to the configuration file,</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/hp3900.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp3900.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp3900.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (<i>.</i>) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_HP3900</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_HP3900=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1),<br />
 <i><a rel="nofollow" href="http://sourceforge.net/projects/hp3900-series/">http://sourceforge.net/projects/hp3900-series/</a></i><br />
 <i><a rel="nofollow" href="http://jkdsoftware.dyndns.org/drupal/?q=es/books/151">http://jkdsoftware.dyndns.org/drupal/?q=es/books/151</a></i> </p>
<h2>Author</h2>
<p>Jonathan Bravo Lopez &lt;<i>jkdsoft [at] gmail.com</i>&gt;</p>
<h2>Bugs</h2>
<p>Scanning is only tested with Linux/ix86/gcc. Be careful when testing on other operating systems and especially on big-endian platforms. The scanner may get wrong data. </p>
