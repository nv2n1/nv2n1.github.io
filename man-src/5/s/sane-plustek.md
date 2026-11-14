---
title: "sane-plustek(5)"
name: "sane-plustek"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-plustek/"
description: "sane-plustek – SANE backend for LM983[1/2/3] based USB flatbed scanners"
---

<p>sane-plustek &#8211; SANE backend for LM983[1/2/3] based USB flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-plustek</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on National Semiconductor Merlin chipsets (LM9831, 9832 and 9833). If you&#8217;re looking for parallel-port support for Plustek scanner please refer to the <code><a href="/docs/linux/man/5-sane-plustek_pp/">sane-plustek_pp</a></code>(5) backend. </p>
<h2>Supported Devices</h2>
<p>The Backend is able to support USB scanner based on the National Semiconductor chipsets LM9831, LM9832 and LM9833. The following tables show various devices which are currently reported to work. If your Plustek scanner has another Product ID, then the device is <code>NOT</code> supported by this backend. </p>
<p> Vendor Plustek &#8211; ID: 0x07B3 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
OpticPro U12 LM9831 600x1200dpi 42bit 512Kb 0x0010
OpticPro UT12 LM9831 600x1200dpi 42bit 512Kb 0x0013
OpticPro UT12 LM9832 600x1200dpi 42bit 512Kb 0x0017
OpticPro UT16 LM9832 600x1200dpi 42bit 512Kb 0x0017
OpticPro U24 LM9831 1200x2400dpi 42bit 2Mb 0x0011
OpticPro U24 LM9832 1200x2400dpi 42bit 2Mb 0x0015
OpticPro UT24 LM9832 1200x2400dpi 42bit 2Mb 0x0017</pre>
<p>Vendor KYE/Genius &#8211; ID: 0x0458 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
Colorpage HR6 V2 LM9832 600x1200dpi 42bit 512Kb 0x2007
Colorpage HR6 V2 LM9832 600x1200dpi 42bit 512Kb 0x2008
Colorpage HR6A LM9832 600x1200dpi 42bit 512Kb 0x2009
Colorpage HR7 LM9832 600x1200dpi 42bit 512Kb 0x2013
Colorpage HR7LE LM9832 600x1200dpi 42bit 512Kb 0x2015
Colorpage HR6X LM9832 600x1200dpi 42bit 512Kb 0x2016</pre>
<p>Vendor Hewlett-Packard &#8211; ID: 0x03F0 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
ScanJet 2100C LM9831 600x1200dpi 42bit 512Kb 0x0505
ScanJet 2200C LM9832 600x1200dpi 42bit 512Kb 0x0605</pre>
<p>Vendor Mustek &#8211; ID: 0x0400 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
BearPaw 1200 LM9831 600x1200dpi 42bit 512Kb 0x1000
BearPaw 1200 LM9832 600x1200dpi 42bit 512Kb 0x1001*
BearPaw 2400 LM9832 1200x2400dpi 42bit 2Mb 0x1001</pre>
<p>* see also description for model override switch below! </p>
<p> Vendor UMAX &#8211; ID: 0x1606 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
UMAX 3400 LM9832 600x1200dpi 42bit 512Kb 0x0050
UMAX 3400/3450 LM9832 600x1200dpi 42bit 512Kb 0x0060
UMAX 5400 LM9832 1200x2400dpi 42bit 512Kb 0x0160</pre>
<p>Vendor COMPAQ &#8211; ID: 0x049F </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
S4-100 LM9832 600x1200dpi 42bit 512Kb 0x001A</pre>
<p>Vendor Epson &#8211; ID: 0x04B8 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
Perfection 1250 LM9832 1200x2400dpi 42bit 512Kb 0x010F
Perfection 1260 LM9832 1200x2400dpi 42bit 512Kb 0x011D</pre>
<p>Vendor CANON &#8211; ID: 0x04A9 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
CanoScan N650/656U LM9832 600x1200dpi 42bit 512Kb 0x2206
CanoScan N1220U LM9832 1200x2400dpi 42bit 512Kb 0x2207
CanoScan D660U LM9832 600x1200dpi 42bit 512Kb 0x2208
CanoScan N670/676U LM9833 600x1200dpi 48bit 512Kb 0x220D
CanoScan N1240U LM9833 1200x2400dpi 48bit 512Kb 0x220E
CanoScan LIDE20 LM9833 600x1200dpi 48bit 512Kb 0x220D
CanoScan LIDE25 LM9833 1200x2400dpi 48bit 512Kb 0x2220
CanoScan LIDE30 LM9833 1200x2400dpi 48bit 512Kb 0x220E</pre>
<p>Vendor Syscan &#8211; ID: 0x0A82 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
Travelscan 662 LM9833 600x1200dpi 48bit 512Kb 0x6620
Travelscan 464 LM9833 600x1200dpi 48bit 512Kb 0x4600</pre>
<p>Vendor Portable Peripheral Co., Ltd. &#8211; ID: 0x0A53 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
Q-Scan USB001 LM9832 300x600dpi 42bit 512Kb 0x1000
Q-Scan USB201 LM9832 300x600dpi 42bit 512Kb 0x2000</pre>
<p>Vendor Visioneer &#8211; ID: 0x04A7 </p>
<pre>----------------------------------------------------------
USB Model: ASIC: Properties: Prod-ID
----------------------------------------------------------
Strobe XP100 LM9833 600x1200dpi 48bit 512Kb 0x0427</pre>
<h2>Other Plustek Scanners</h2>
<p>For parallelport device support see the <code><a href="/docs/linux/man/5-sane-plustek_pp/">sane-plustek_pp</a></code>(5) backend.<br />
 The SCSI scanner OpticPro 19200S is a rebadged Artec AM12S scanner and is supported by the <code><a href="/docs/linux/man/5-sane-artec/">sane-artec</a></code>(5) backend.<br />
 Only the National Semiconductor LM983[1/2/] based devices of Plustek are supported by this backend. Older versions of the U12, the UT12, the U1212 and U1248 (GrandTech chipset) are not supported. </p>
<pre>Model Chipset backend
------------------------------------
U1248 GrandTech gt68xx
UT16B GrandTech gt68xx
OpticSlim 1200 GrandTech gt68xx
OpticSlim 2400 GrandTech gt68xx
U12 P98003 u12
UT12 P98003 u12
1212U P98003 u12</pre>
<p>For a more complete and up to date list see: <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i>.</p>
<h2>Configuration</h2>
<p>To use your scanner with this backend, you need at least two entries in the configuration file <i>/etc/sane.d/plustek.conf</i></p>
<dl>
<dd><i>[usb] vendor-id product-id</i><br />
 <i>device /dev/usbscanner</i></dl>
<p> <i>[usb]</i> tells the backend, that the following devicename (here <i>/dev/usbscanner</i>) has to be interpreted as USB scanner device. If vendor- and product-id has not been specified, the backend tries to detect this by its own. If device is set to <i>auto</i> then the next matching device is used.<br />
 The following options can be used for a default setup of your device. Most of them are also available through the frontend. </p>
<p> <code>The Options:</code> </p>
<p> option warmup t</p>
<dl>
<dd><i>t</i> specifies the warmup period in seconds, if set to -1, the automatic warmup function will be used</dl>
<p> option lampOff t</p>
<dl>
<dd><i>t</i> is the time in seconds for switching off the lamps in standby mode</dl>
<p> option lOffonEnd b</p>
<dl>
<dd><i>b</i> specifies the behaviour when closing the backend, 1 &#8211;&gt; switch lamps off, 0 &#8211;&gt; do not change lamp status</dl>
<p> option mov m</p>
<dl>
<dd><i>m</i> is the model override switch. It works only with Mustek BearPaw devices. </p>
<pre>m/PID | 0x1000 | 0x1001
------+--------------+--------------
 0 | BearPaw 1200 | BearPaw 2400
 1 | no function | BearPaw 1200</pre>
</dl>
<p> option invertNegatives b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; do not invert the picture during negative scans,<br />
 1 &#8211;&gt; invert picture</dl>
<p> option cacheCalData b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; do not save calibration results,<br />
 1 &#8211;&gt; save results of calibration in <i>~/.sane/</i> directory</dl>
<p> option altCalibration b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; use standard calibration routines,<br />
 1 &#8211;&gt; use alternate calibration (only non Plustek devices, standard for CIS devices)</dl>
<p> option skipFine b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; perform fine calibration,<br />
 1 &#8211;&gt; skip fine calibration (only non Plustek devices)</dl>
<p> option skipFineWhite b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; perform white fine calibration,<br />
 1 &#8211;&gt; skip white fine calibration (only non Plustek devices)</dl>
<p> option skipDarkStrip b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; perform dark calibration, with enabled lamp using the dark calibration strip of the scanner. If the scanner does not have such a strip, the alternative way is to switch off the lamp during this step.<br />
 1 &#8211;&gt; always switch off the lamp for dark calibration, even a black strip is available</dl>
<p> option skipCalibration b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; perform calibration,<br />
 1 &#8211;&gt; skip calibration (only non Plustek devices)</dl>
<p> option enableTPA b</p>
<dl>
<dd><i>b</i> 0 &#8211;&gt; default behaviour, specified by the internal tables,<br />
 1 &#8211;&gt; override internal tables and allow TPA mode (EPSON/UMAX only)</dl>
<p> option posOffX x<br />
 option posOffY y<br />
 option tpaOffX x<br />
 option tpaOffY y<br />
 option negOffX x<br />
 option negOffY y</p>
<dl>
<dd><i>x y</i> By using this settings, the user can adjust the given image positions. <code>Please note, that there&#8217;s no internal range checking for</code> <code>this feature.</code></dl>
<p> option posShadingY p<br />
 option tpaShadingY p<br />
 option negShadingY p</p>
<dl>
<dd><i>p</i> overrides the internal shading position. The values are in steps. <code>Please note, that there&#8217;s no internal range checking for</code> <code>this feature.</code></dl>
<p> option redGamma r<br />
 option greenGamma g<br />
 option blueGamma b<br />
 option grayGamma gr</p>
<dl>
<dd><i>r g b gr</i></dl>
<p> By using these values, the internal linear gamma table (r,g,b,gr = 1.0) can be adjusted. </p>
<p> option red_gain r<br />
 option red_offset ro<br />
 option green_gain g<br />
 option green_offset go<br />
 option blue_gain b<br />
 option blue_offset bo</p>
<dl>
<dd><i>r g b ro go bo</i> These values can be used to set the gain and offset values of the AFE for each channel. The range is between 0 and 63. -1 means autocalibration.</dl>
<p> See the plustek.conf file for examples. </p>
<p> <code>Note:</code><br />
 You have to make sure, that the USB subsystem is loaded correctly and you have access to the device-node. For more details see <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) manpage. You might use <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) to check that you have access to your device. </p>
<p> <code>Note:</code><br />
 If there&#8217;s no configuration file, the backend defaults to <code>device auto</code></p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/plustek.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-plustek.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-plustek.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_PLUSTEK</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_PLUSTEK=10 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-u12/">sane-u12</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1)<br />
 <i>/usr/share/doc/libsane/plustek/Plustek-USB.changes</i> </p>
<h2>Contact And Bug-Reports</h2>
<p>Please send any information and bug-reports to:<br />
 <code>SANE Mailing List</code> </p>
<p> Additional info and hints can be obtained from our<br />
 Mailing-List archive at:<br />
 <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> </p>
<p> To obtain debug messages from the backend, please set the environment-variable <code>SANE_DEBUG_PLUSTEK</code> before calling your favorite scan-frontend (i.e. <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1)),<code>i.e.:</code> </p>
<p> <i>export SANE_DEBUG_PLUSTEK=20 ; scanimage</i> </p>
<p> The value controls the verbosity of the backend. Please note, that values greater than 24 force the backend to output raw data files, which could be rather large. The ending of these files is &quot;.raw&quot;. For problem reports it should be enough the set the verbosity to 13.</p>
<h2>KNOWN BUGS &amp; RESTRICTIONS</h2>
<p>* The driver does not support these manic scalings up to 16 times the physical resolution. The only scaling is done on resolutions between the physical resolution of the CCD-/CIS-sensor and the stepper motor i.e. you have a 600&#215;1200 dpi scanner and you are scanning using 800dpi, so scaling is necessary, because the sensor only delivers 600dpi but the motor is capable to perform 1200dpi steps. </p>
<p> * Plusteks&#8217; model policy is somewhat inconsistent. They sell technically different devices under the same product name. Therefore it is possible that some devices like the UT12 or U12 won&#8217;t work &#8211; please check the model list above and compare the product-id to the one your device has. </p>
<p> * Negative/Slide scanning quality is poor.</p>
