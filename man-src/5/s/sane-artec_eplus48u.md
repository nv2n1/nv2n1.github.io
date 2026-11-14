---
title: "sane-artec_eplus48u(5)"
name: "sane-artec_eplus48u"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-artec_eplus48u/"
description: "sane-artec_eplus48u – SANE backend for the scanner Artec E+ 48U and re-badged models"
---

<p>sane-artec_eplus48u &#8211; SANE backend for the scanner Artec E+ 48U and re-badged models</p>
<h2>Description</h2>
<p>The <code>sane-artec_eplus48u</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to several USB flatbed scanners using the GT6816 chipset like the Artec E+ 48U. These scanners have a contact image sensor (CIS). A complete list of supported devices can be found on <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i>. This is ALPHA software. Especially if you test new or untested scanners, keep your hand at the scanner&#8217;s plug and unplug it, if the head bumps at the end of the scan area. If you own a scanner other than the ones mentioned on the list that works with this backend, please let us know this by sending the scanner&#8217;s exact model name and the USB vendor and product ids (e.g. from <i>/proc/bus/usb/devices</i>, <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to me. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let me know. </p>
<h2>Kernel Issues</h2>
<p>If libusb-0.1.6 or later is installed, this section can be skipped. The scanner should be found by <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) without further actions. For setting permissions and general USB information look at <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5). </p>
<p> When you are using the scanner module, a Linux kernel 2.4.12 or newer is required.</p>
<h2>Firmware File</h2>
<p>You need a firmware file for your scanner. That&#8217;s a small file containing software that will be uploaded to the scanner&#8217;s memory. For the scanners mentioned above, it&#8217;s usually named <i>Artec48.usb</i> or <i>1200.usb</i>. You can find it on the installation CD that was provided by the manufacturer, normally in the directory Win98, WinMe or similar. If the Windows-driver is installed on your computer, then you can also find the firmware file under c:\windows\system32\drivers.</p>
<h2>Configuration</h2>
<p>The contents of the <i>artec_eplus48u.conf</i> file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain option lines. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by <i>usb vendor_id product_id</i> statements which are already included into <i>artec_eplus48u.conf .</i> &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner. </p>
<p> Every usb section can have additional options.</p>
<dl>
<dt><code>artecFirmwareFile /usr/share/sane/artec_eplus48u/Artec48.usb</code></p>
<dd>The path to the firmware file. This option is required.</p>
<dt><code>redGamma 1.0</code></p>
<dd>
<dt><code>greenGamma 1.0</code></p>
<dd>
<dt><code>blueGamma 1.0</code></p>
<dd>
<dt><code>masterGamma 1.9</code></p>
<dd>These are the default gamma values. If you set the &quot;Defaults&quot; option with a frontend, then the gamma options are reset to the values specified here.</p>
<dt><code>redOffset 0x28</code></p>
<dd>
<dt><code>greenOffset 0x2f</code></p>
<dd>
<dt><code>blueOffset 0x2f</code></p>
<dd>
<dt><code>redExposure 0xa7</code></p>
<dd>
<dt><code>greenExposure 0x116</code></p>
<dd>
<dt><code>blueExposure 0xdc</code></p>
<dd>These are the default values for offset and exposure time. You can change them (e.g. to speed up calibration) if you don&#8217;t want to save the calibration data permanently.</p>
<dt><code>vendorString Artec</code></p>
<dd>
<dt><code>modelString E+ 48U</code></p>
<dd>By default, the scanner is reported as &quot;Artec E+ 48U&quot;. If you don&#8217;t like this, e.g. because you have an Tevion MD 9693, then change the options accordingly.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/local/etc/sane.d/artec_eplus48u.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/local/lib/sane/libsane-artec_eplus48u.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/local/lib/sane/libsane-artec_eplus48u.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_ARTEC_EPLUS48U</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_ARTEC_EPLUS48U=3 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) </p>
<h2>Author</h2>
<p>Michael Herder.<br />
 This backend is based on the gt68xx test-program written by Sergey Vlasov, Andreas Nowack, and David Stevenson. Thanks to everyone who tested the backend or reported bugs.<br />
 This man page is based on man <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), written by Henning Meier-Geinitz.</p>
<h2>Bugs</h2>
<p>This backend has been tested on Linux only. If you are using it on a different platform, please contact us. Interpolation with 1200 dpi is weak. Support for buttons is missing due to missing support in SANE. Please contact us if you find a bug: <i><a rel="nofollow" href="http://www.sane-project.org/bugs.html">http://www.sane-project.org/bugs.html</a></i>. </p>
