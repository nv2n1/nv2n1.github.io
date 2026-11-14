---
title: "sane-ma1509(5)"
name: "sane-ma1509"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-ma1509/"
description: "sane-ma1509 – SANE backend for Mustek BearPaw 1200F USB scanner"
---

<p>sane-ma1509 &#8211; SANE backend for Mustek BearPaw 1200F USB scanner</p>
<h2>Description</h2>
<p>The <code>sane-ma1509</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Mustek BearPaw 1200F USB flatbed scanner. This scanner is based on the MA-1509 chipset. Other scanners that use this chip (if they exist) may also work. This backend is ALPHA software. Be careful and remove the power plug immediately if your hear unusual noises. More details can be found on the <code>sane-ma1509</code> backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/ma1509-backend/">http://www.meier-geinitz.de/sane/ma1509-backend/</a></i>. Other Mustek USB scanners are supported by the <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5) and <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5) backends. This backend can only work with scanners that are already detected by the operating system. See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for details. If you own a scanner other than the Mustek BearPaw 1200F that works with this backend, please let me know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i> or syslog) to me. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is a path-name for the special device that corresponds to a USB scanner. With Linux, such a device name could be <i>/dev/usb/scanner0</i> or <i>libusb:001:002</i>, for example.</p>
<h2>Configuration</h2>
<p>The contents of the <i>ma1509.conf</i> file is a list of options and device names that correspond to Mustek BearPaw 1200F scanners. Empty lines and lines starting with a hash mark (#) are ignored. </p>
<p> Instead of using the device name, the scanner can be autodetected by <code>usb vendor_id product_id</code> statements which are already included into <i>ma1509.conf</i>. This is only supported with Linux 2.4.8 and higher and all systems that support libsub. &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner. If this doesn&#8217;t work, a device name must be placed in <i>ma1509.conf</i> as described above. </p>
<p> To set the time the lamp needs for warm-up, use <code>option</code> <code>warmup-time</code> in <i>ma1509.conf</i>. The time is given in seconds after the option. The default is 30 seconds.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/ma1509.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ma1509.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ma1509.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MA1509</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5),<br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/ma1509-backend/">http://www.meier-geinitz.de/sane/ma1509-backend/</a></i> </p>
<h2>Author</h2>
<p>Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;</p>
<h2>Bugs</h2>
<p>Resolutions higher than 600 dpi don&#8217;t work<br />
 Transparency adapter and automatic document feeder is not supported yet<br />
 No support for &quot;high-speed&quot; mode (jpeg) More detailed bug information is available at the MA-1509 backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/ma1509-backend/">http://www.meier-geinitz.de/sane/ma1509-backend/</a></i>. </p>
