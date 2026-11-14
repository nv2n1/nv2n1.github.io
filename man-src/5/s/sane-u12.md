---
title: "sane-u12(5)"
name: "sane-u12"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-u12/"
description: "sane-u12 – SANE backend for Plustek USB flatbed scanners, based on older parport designs"
---

<p>sane-u12 &#8211; SANE backend for Plustek USB flatbed scanners, based on older parport designs</p>
<h2>Description</h2>
<p>The <code>sane-u12</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on Plusteks&#8217; ASIC 98003 (parallel-port ASIC) and a GeneSys Logics&#8217; USB-parport bridge chip. </p>
<h2>Supported Devices</h2>
<p>The backend is able to support some early Plustek USB scanners that based their old parport design around the ASIC 98003 and other rebadged Plustek devices. The following tables will give you a short overview. </p>
<p> If your Plustek scanner has another Product ID, then the device is <code>NOT</code> supported by this backend. </p>
<p> Vendor Plustek &#8211; ID: 0x07B3 </p>
<pre>----------------------------------------------------------
Model: Vendor-ID: Product-ID:
----------------------------------------------------------
OpticPro U12 0x07B3 0x0001
OpticPro U1212 0x07B3 0x0001
OpticPro UT12 0x07B3 0x0001</pre>
<p>Vendor KYE/Genius </p>
<pre>--------------------------------------------------------
USB Model: Vendor-ID: Product-ID:
--------------------------------------------------------
ColorPage Vivid III USB 0x07B3 0x0001
ColorPage HR6 V1 0x0458 0x2004</pre>
<h2>Configuration</h2>
<p>To use your scanner with this backend, you need at least two entries in the configuration file <i>/etc/sane.d/u12.conf</i> </p>
<dl>
<dd><i>[usb] vendor-id product-id</i><br />
 <i>device /dev/usbscanner</i></dl>
<p> <i>[usb]</i> tells the backend, that the following devicename (here <i>/dev/usbscanner</i>) has to be interpreted as USB scanner device. If vendor- and product-id has not been specified, the backend tries to detect this by its own. If device is set to <i>auto</i> then the next matching device is used. </p>
<p> <code>The Options:</code> </p>
<p> option warmup t</p>
<dl>
<dd><i>t</i> specifies the warmup period in seconds</dl>
<p> option lampOff t</p>
<dl>
<dd><i>t</i> is the time in seconds for switching off the lamps in standby mode</dl>
<p> option lOffonEnd b</p>
<dl>
<dd><i>b</i> specifies the behaviour when closing the backend, 1 &#8211;&gt; switch lamps off, 0 &#8211;&gt; do not change lamp status</dl>
<p> See the <i>u12.conf</i> file for examples. </p>
<p> <code>Note:</code> You have to make sure, that the USB subsystem is loaded correctly and you have access to the device-node. For more details see <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) manpage. You might use <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) to check that you have access to your device. </p>
<p> <code>Note:</code><br />
 If there&#8217;s no configuration file, the backend defaults to <code>device auto</code></p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/u12.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-u12.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-u12.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_U12</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_U12=10 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1)<br />
 <i>/usr/share/doc/libsane/u12/U12.changes</i> </p>
<h2>Contact And Bug-Reports</h2>
<p>Please send any information and bug-reports to:<br />
 <code>SANE Mailing List</code> </p>
<p> Additional info and hints can be obtained from our<br />
 Mailing-List archive at:<br />
 <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> </p>
<p> To obtain debug messages from the backend, please set the environment-variable <code>SANE_DEBUG_U12</code> before calling your favorite scan-frontend (i.e. <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)), i.e.: </p>
<p> <i>export SANE_DEBUG_U12=20 ; xscanimage</i> </p>
<p> The value controls the verbosity of the backend.</p>
<h2>KNOWN BUGS &amp; RESTRICTIONS</h2>
<p>* The driver is in alpha state, so please don&#8217;t expect too much!!! </p>
<p> * When using libusb, it might be, that the backend hangs. In that case, reconnect the scanner.</p>
