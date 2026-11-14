---
title: "sane-genesys(5)"
name: "sane-genesys"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-genesys/"
description: "sane-genesys – SANE backend for GL646, GL841, GL843, GL847 and GL124 based USB flatbed scanners"
---

<p>sane-genesys &#8211; SANE backend for GL646, GL841, GL843, GL847 and GL124 based USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-genesys</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on the Genesys GL646, GL841, GL843, GL847 and GL124 chips. At present, the following scanners are known to work with this backend:</p>
<dl>
<dd>Canon LiDE 35/40/50/60/100/110/120/200/210/220/700<br />
 Hewlett-Packard HP2300C/HP2400/HP3670/HP3690/G4010/G4050<br />
 Medion MD5345/MD6228/MD6274<br />
 Panasonic KV-SS080<br />
 Plustek OpticBook 3600<br />
 Pentax DSmobile 600<br />
 Syscan/Ambir DocketPORT 467/485/487/665/685<br />
 Visioneer OneTouch 7100/Strobe XP100 (rev3)/XP200/XP300/Roadwarrior<br />
 Xerox Travel Scanner 100, OneTouch 2400</dl>
<p> This is stable software for supported models. But if you test new or untested scanners, keep your hand at the scanner&#8217;s plug and unplug it, if the head bumps at the end of the scan area. If you own a scanner other than the ones listed above that works with this backend, please let me know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i>, <i>sane-find-scanner</i> or syslog) to the sane-devel mailing list. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let me know. If you own a scanner that isn&#8217;t detected by the genesys backend but has a GL646, GL841, GL843, GL847 or GL124 chipset, you can try to add it to the backend. </p>
<h2>Calibration</h2>
<p>To give correct image quality, sheet fed scanners need to be calibrated using the calibration sheet sold with the scanner. To do calibration, you must insert this target in the feeder then start calibration either by passing the &#8211;calibrate option to scanimage or by clicking on the available &#8216;calibrate&#8217; button in the &#8216;advanced options&#8217; in a graphical frontend. The result of the calibration is stored in a file in the home directory of the user doing it. If you plug the scanner in another machine or use it with another account, calibration will have to be redone, unless you use the &#8211;calibration-file option. If no home directory is defined, <code>USERAPPPROFILE</code> will be used, then <code>TMPDIR</code> or <code>TMP.</code> If none of these directories exist, the backend will try to write in the current working directory. Flatbed scanners also make use of the calibration file as a cache to avoid calibration before each scan. Calibration file name is the name of the scanner model if only one scanner is detected. In the case of several identical model, the file name will be the name of the logical USB device name. The expiration time manages the time a calibration is valid in cache. A value of -1 means forever, 0 means no cache.</p>
<h2>Extras Scan Options</h2>
<dl>
<dt><code>&#8211;lamp-off-time number</code></p>
<dd>The lamp will be turned off after the given time (in minutes). A value of 0 means that the lamp won&#8217;t be turned off. </p>
<dt><code>&#8211;threshold percent</code></p>
<dd>0..100% (in steps of 1). Select minimum brightness to get a white point. Pixels with brightness below that value will be scanned as black. </p>
<dt><code>&#8211;brightness value</code></p>
<dd>-100..100 (in steps of 1). Set the brightness enhancement. 0 for no enhancement, negative values to decrease brightness, and positive values to increase it. </p>
<dt><code>&#8211;contrast value</code></p>
<dd>-100..100 (in steps of 1). Set the contrast enhancement. 0 for no enhancement, negative values to decrease contrast, and positive values to increase it. </p>
<dt><code>&#8211;disable-interpolation yes|no</code></p>
<dd>When using high resolutions where the horizontal resolution is smaller than vertical resolution, data is expanded by software to preserve picture geometry. This can be disabled by this option to get real scanned data. </p>
<dt><code>&#8211;disable-dynamic-lineart yes|no</code></p>
<dd>Disable use of a software adaptive algorithm to generate lineart and rely on hardware lineart. </p>
<dt><code>&#8211;color-filter None|Red|Green|Blue</code></p>
<dd>When using gray or lineart this option selects the used color. Using a color filter will give a monochrome scan. CIS based scanners can to true gray when no filter (None value) is selected. </p>
<dt><code>&#8211;lamp-off-scan</code></p>
<dd>The lamp will be turned off during the scan. Calibration is still done with lamp on. </p>
<dt><code>&#8211;clear-calibration</code></p>
<dd>Clear calibration cache data, triggering a new calibration for the device when the next scan will happen. </p>
<dt><code>&#8211;calibration-file</code></p>
<dd>Specify the calibration file name to use. At least the directory containing the file must exist, since it won&#8217;t be created. This option is disabled if the backend is run as root. It maybe used in case of sheet-fed scanners to share a calibration file for several users. </p>
<dt><code>&#8211;expiration-time</code></p>
<dd>Specify the time (in minutes) a cached calibration is considered valid. If older than the given value, a new calibration is done. A value of -1 means no expiration and cached value are kept forever unless cleared by userwith the calibration clear option. A value of 0 means cache is disabled. </p>
</dl>
<p> Additionally, several &#8216;software&#8217; options are exposed by the backend. These are reimplementations of features provided natively by larger scanners, but running on the host computer. This enables smaller machines to have similar capabilities. Please note that these features are somewhat simplistic, and may not perform as well as the native implementations. Note also that these features all require that the driver cache the entire image in memory. This will almost certainly result in a reduction of scanning speed. </p>
<dl>
<dt><code>&#8211;swcrop</code></p>
<dd>Requests the driver to detect the extremities of the paper within the larger image, and crop the empty edges. </p>
<dt><code>&#8211;swdeskew</code></p>
<dd>Requests the driver to detect the rotation of the paper within the larger image, and counter the rotation. </p>
<dt><code>&#8211;swdespeck &#8211;despeck X</code></p>
<dd>Requests the driver to find and remove dots of X diameter or smaller from the image, and fill the space with the average surrounding color. </p>
<dt><code>&#8211;swskip 0..100% (in steps of 1) [0]</code></p>
<dd>Request driver to discard pages with low numbers of dark pixels. </p>
<dt><code>&#8211;swderotate[=(yes|no)] [no]</code></p>
<dd>Request driver to detect and correct 90 degree image rotation. </p>
</dl>
<h2>System Issues</h2>
<p>This backend needs libusb-0.1.6 or later installed, and hasn&#8217;t tested in other configuration than a linux kernel 2.6.9 or higher. However, it should work any system with libusb where the SANE package can be compiled. For setting permissions and general USB information look at <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5).</p>
<h2>Configuration</h2>
<p>The contents of the <i>genesys.conf</i> file is a list of usb lines containing vendor and product ids that correspond to USB scanners. The file can also contain option lines. Empty lines and lines starting with a hash mark (#) are ignored. The scanners are autodetected by <code>usb vendor_id product_id</code> statements which are already included into <i>genesys.conf</i>. &quot;vendor_id&quot; and &quot;product_id&quot; are hexadecimal numbers that identify the scanner.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/genesys.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-genesys.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-genesys.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_GENESYS</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. If the debug level is set to 1 or higher, some debug options become available that are normally hidden. Handle them with care. This will print messages related to core genesys functions.</p>
<dt><code>SANE_DEBUG_GENESYS_IMAGE</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable enables logging of intermediate image data. To enable this mode, set the environmental variable to 1. </p>
<p> Example (full and highly verbose output for gl646):<br />
 export SANE_DEBUG_GENESYS=255 </p>
</dl>
<h2>Credits</h2>
<p>Jack McGill for donating several sheetfed and flatbed scanners, which made possible to add support for them in the genesys backend:</p>
<dl>
<dd>Hewlett-Packard HP3670<br />
 Visioneer Strobe XP100 (rev3)/XP200/XP300/Roadwarrior<br />
 Canon LiDE 200<br />
 Pentax DSmobile 600<br />
 Syscan/Ambir DocketPORT 467/485/487/665/685<br />
 Xerox Travel Scanner 100, Onetouch 2400</dl>
<dl>
<dt>cncsolutions</p>
<dd>(<i><a rel="nofollow" href="http://www.cncsolutions.com.br">http://www.cncsolutions.com.br</a></i>) sponsored and supported the work on the Panasonic KV-SS080. </p>
<dt>Brian Paavo from Benthic Science Limited for donating a Canoscan LiDE 700F.</p>
<dd>
<dt>Dany Qumsiyeh for donating a Canoscan LiDE 210 and a LiDE 220.</p>
<dd>
<dt>Luc Verhaegen for donating a Canoscan LiDE 120.</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) </p>
<h2>Author</h2>
<p>Oliver Rauch<br />
 Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;<br />
 Gerhard Jaeger &lt;<i>gerhard [at] gjaeger.de</i>&gt;<br />
 St&eacute;phane Voltz &lt;<i>stef.dev [at] free.fr</i>&gt;<br />
 Philipp Schmid &lt;<i>philipp8288 [at] web.de</i>&gt;<br />
 Pierre Willenbrock &lt;<i>pierre [at] pirsoft.dnsalias.org</i>&gt;<br />
 Alexey Osipov &lt;<i>simba [at] lerlan.ru</i>&gt; for HP2400 final support</p>
<h2>Limitations</h2>
<p>Powersaving isn&#8217;t implemented for gl646 based scanner. Dynamic (emulated from gray data and with dithering) isn&#8217;t enabled for gl646 scanners. Hardware lineart is limited up to 600 dpi for gl847 based scanners, due to the way image sensors are built. </p>
<p> This backend will be much slower if not using libusb-1.0. So be sure that sane-backends is built with the <code>&#8211;enable-libusb_1_0 option.</code></p>
<h2>Bugs</h2>
<p>For the LiDE 200, the scanned data at 4800 dpi is obtained &quot;as is&quot; from sensor. It seems the windows driver does some digital processing to improve it, which is not implemented in the backend. </p>
