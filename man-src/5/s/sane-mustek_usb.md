---
title: "sane-mustek_usb(5)"
name: "sane-mustek_usb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-mustek_usb/"
description: "sane-mustek_usb – SANE backend for Mustek USB flatbed scanners"
---

<p>sane-mustek_usb &#8211; SANE backend for Mustek USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-mustek_usb</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Mustek USB flatbed scanners (including a clone from Trust). At present, the following scanners are known to work more or less with this backend:</p>
<dl>
<dd>Mustek 600 CU<br />
 Mustek 1200 UB<br />
 Mustek 1200 CU<br />
 Mustek 1200 CU Plus<br />
 Trust Compact Scan USB 19200
</dl>
<p> More details can be found on the Mustek USB backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek_usb-backend/">http://www.meier-geinitz.de/sane/mustek_usb-backend/</a></i>. The Mustek BearPaw 1200 and 2400 scanners are supported by the plustek backend. See <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5) for details. The Mustek BearPaw 1200F is supported by the MA-1509 backend. See <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5) for details. Other Mustek USB scanners are supported by the gt68xx backend, see <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5). This backend can only work with scanners that are already detected by the operating system. See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for details. If you own a Mustek (or Trust) scanner other than the ones listed above that works with this backend, please let me know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i> or syslog) to me. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is a path-name for the special device that corresponds to a USB scanner. With Linux, such a device name could be <i>/dev/usb/scanner0</i> or <i>/dev/usbscanner1</i>, for example. </p>
<p> For FreeBSD use <i>/dev/uscanner0</i>.</p>
<h2>Configuration</h2>
<p>The contents of the <i>mustek_usb.conf</i> file is a list of options and device names that correspond to Mustek USB scanners. Empty lines and lines starting with a hash mark (#) are ignored. If a device name is placed in <i>mustek_usb.conf</i>, it must be followed by a line containing the keyword <code>option</code> and an option specifying the scanner type. The following options can be used: <code>600cu</code>, <code>1200cu</code>, <code>1200cu_plus</code>, <code>1200ub</code>. For the Trust Compact Scan USB 19200 use `option 1200ub&#8217;. </p>
<p> Instead of using the device name, the scanner can be autodetected by <code>usb vendor_id product_id</code> statements which are already included into <i>mustek_usb.conf</i>. This is only supported with Linux 2.4.8 and higher and all systems that support libsub. &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner. If this doesn&#8217;t work, a device name and the option specifying the scanner type must be placed in <i>mustek_usb.conf</i> as described above. </p>
<p> The global <code>option max_block_size</code> can be used to limit the amount of data acquired in one turn from the USB system. It may be worth trying, if USB errors occur. </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd># Comment<br />
 option max_block_size 1024<br />
 usb 0x055f 0x0001<br />
 /dev/usb/scanner0<br />
 option 600cu</dl>
<p> The first line is ignored. The second line sets the buffer size to a maximum of 1024 bytes. The third line tries to autodetect a scanner with vendor id 0x055f and product id 0x0001 (Mustek 1200 CU). The fourth line tells the backend to attach to <i>/dev/usb/scanner0</i> and the fifth line specifies that <i>/dev/usb/scanner0</i> is a Mustek 600 CU.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/mustek_usb.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_usb.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_usb.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MUSTEK_USB</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<pre>Value Description
0 no output
1 print fatal errors
2 print important messages
3 print non-fatal errors and less important messages
4 print all but debugging messages
5 print high level debugging messages
6 print medium level debugging messages
7 print low level debugging messages</pre>
<p>Example: export SANE_DEBUG_MUSTEK_USB=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5)<br />
 <i>/usr/share/doc/libsane/mustek_usb/mustek_usb.CHANGES</i>,<br />
 <i>/usr/share/doc/libsane/mustek_usb/mustek_usb.TODO</i><br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek_usb-backend/">http://www.meier-geinitz.de/sane/mustek_usb-backend/</a></i> </p>
<h2>Author</h2>
<p>Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;<br />
 This backend is based on the Mustek 1200ub backend from Mustek, maintained by Tom Wang.</p>
<h2>Bugs</h2>
<p>These devices have a hardware bug: Once data is written to them, they can&#8217;t be reset (toggle = DATA0). That means, any operation that tries to reset the device will result in running into timeouts. In earlier versions this backend failed when it was loaded the second time in some configurations. The only choice was to replug the scanner in this case. The backend uses a workaround for that bug now but it&#8217;s only tested on Linux. Reports for other operating systems are appreciated. More detailed bug information is available at the Mustek backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek_usb-backend/">http://www.meier-geinitz.de/sane/mustek_usb-backend/</a></i>. </p>
