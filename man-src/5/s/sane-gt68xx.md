---
title: "sane-gt68xx(5)"
name: "sane-gt68xx"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-gt68xx/"
description: "sane-gt68xx – SANE backend for GT-68XX based USB flatbed scanners"
---

<p>sane-gt68xx &#8211; SANE backend for GT-68XX based USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-gt68xx</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on the Grandtech GT-6801 and GT-6816 chips. A list of supported scanners can be found on the gt68xx backend homepage: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/gt68xx-backend/">http://www.meier-geinitz.de/sane/gt68xx-backend/</a></i>. This is BETA software. Especially if you test new or untested scanners, keep your hand at the scanner&#8217;s plug and unplug it, if the head bumps at the end of the scan area. If you own a scanner other than the ones listed on the gt68xx homepage that works with this backend, please let me know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to me. Even if the scanner&#8217;s name is only slightly different from the models already listed as supported, please let me know. If you own a scanner that isn&#8217;t detected by the gt68xx backend but has a GT-6801 or GT-6816 chipset, you can try to add it to the backend. Have a look at the following web page: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/gt68xx-backend/adding.html">http://www.meier-geinitz.de/sane/gt68xx-backend/adding.html</a></i> </p>
<h2>Libusb Issues</h2>
<p>Please use libusb-0.1.8 or later. Without libusb or with older libusb versions all kinds of trouble can be expected. The scanner should be found by <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) without further actions. For setting permissions and general USB information, look at <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5).</p>
<h2>Firmware File</h2>
<p>You need a firmware file for your scanner. That&#8217;s a small file containing software that will be uploaded to the scanner&#8217;s memory. It&#8217;s usually named *.usb, e.g. <i>PS1fw.usb</i>. It comes on the installation CD that was provided by the manufacturer, but it may be packaged together with the installation program in an .exe file. For Mustek scanners, the file can be downloaded from the gt68xx backend homepage. For other scanners, check the CD for .usb files. If you only find *.cab files, try <code><a href="/docs/linux/man/1-cabextract/">cabextract</a></code>(1) to unpack. If everything else fails, you must install the Windows driver and get the firmware from there (usually in the <i>windows/system</i> or <i>system32</i> directories). Put that firmware file into <i>/usr/share/sane/gt68xx/</i>. Make sure that it&#8217;s readable by everyone.</p>
<h2>Configuration</h2>
<p>The contents of the <i>gt68xx.conf</i> file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain option lines. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by <code>usb vendor_id product_id</code> statements which are already included into <i>gt68xx.conf</i>. &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner. </p>
<p> The <code>override</code>, <code>firmware</code>, <code>vendor</code>, <code>model</code>, and <code>afe</code> options must be placed after the <code>usb</code> line they refer to. </p>
<p> Option <code>override</code> is used to override the default model parameters. That&#8217;s necessary for some scanners that use the same vendor/product ids but are different. For these scanners there are already commented out override lines in the configuration file. <code>override mustek-scanexpress-1200-ub-plus</code> is necessary for the Mustek Scanexpress 1200 UB Plus, the Medion/Lifetec/Tevion LT 9452, and the Trust Compact Scan USB 19200. <code>override artec-ultima-2000</code> is used for the Artec Ultima 2000, the Boeder SmartScan Slim Edition, the Medion/ Lifetec/ Tevion/ Cytron MD/LT 9385, the Medion/ Lifetec/ Tevion MD 9458, and the Trust Flat Scan USB 19200. <code>override mustek-bearpaw-2400-cu</code> is necessary for the Mustek BearPaw 2400 CU and the Fujitsu 1200CUS. The <code>override</code> option must be the first one after the <code>usb</code> line. </p>
<p> Option <code>firmware</code> selects the name and path of the firmware file. It&#8217;s only necessary if the default (or override) doesn&#8217;t work. The default firmware directory is <i>/usr/share/sane/gt68xx/</i>. You may need to create this directory. If you want to place the firmware files at a different path, use a <code>firmware</code> line. </p>
<p> The <code>vendor</code> and <code>model</code> options are not absolutely necessary but for convenience. Quite a lot of scanners from different manufacturers share the same vendor/product ids so you can set the &quot;correct&quot; name here. </p>
<p> The <code>afe</code> option allows one to set custom offset and gain values for the Analog FrontEnd of the scanner. This option can be either used to select the AFE values if automatic coarse calibration is disabled, or to make automatic coarse calibration faster. For the latter usage, enable debug level 3 (see below), scan an image and look for debug line string with &quot;afe&quot;. Copy this line to <i>gt68xx.conf</i>. The option has six parameters: red offset, red gain, green offset, green gain, blue offset, and blue gain. </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd>usb 0x05d8 0x4002<br />
 override &quot;mustek-scanexpress-1200-ub-plus&quot;<br />
 firmware &quot;/opt/gt68xx/SBfw.usb&quot;<br />
 vendor &quot;Trust&quot;<br />
 model &quot;Compact Scan USB 19200&quot;<br />
 afe 0x20 0x02 0x22 0x03 0x1f 0x04</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/gt68xx.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-gt68xx.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-gt68xx.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_GT68XX</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. If the debug level is set to 1 or higher, some debug options become available that are normally hidden. Handle them with care. </p>
<p> Example: export SANE_DEBUG_GT68XX=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-artec_eplus48u/">sane-artec_eplus48u</a></code>(5) <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/1-cabextract/">cabextract</a></code>(1)<br />
 <i>/usr/share/doc/libsane/gt68xx/gt68xx.CHANGES</i><br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/gt68xx">http://www.meier-geinitz.de/sane/gt68xx</a></i> </p>
<h2>Author</h2>
<p>Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;<br />
 The original gt68xx driver was written by Sergey Vlasov, Andreas Nowack, and David Stevenson. Thanks for sending patches and answering questions to them and all the other contributors.</p>
<h2>Bugs</h2>
<p>The first few lines of the image are garbage for the 2400 TA Plus. Interpolation should be used instead of just copying data, when the X- and Y-resolution differ. Support for buttons is missing. More detailed bug information is available at the gt68xx backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/gt68xx-backend/">http://www.meier-geinitz.de/sane/gt68xx-backend/</a></i>.<br />
 Please contact us if you find a bug or missing feature: &lt;<i>sane-devel [at] alioth-lists.debian.net</i>&gt;.<br />
 Please send a debug log if your scanner isn&#8217;t detected correctly (see <code>SANE_DEBUG_GT68XX</code> above). </p>
