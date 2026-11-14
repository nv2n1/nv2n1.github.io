---
title: "sane-hp(5)"
name: "sane-hp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hp/"
description: "sane-hp – SANE backend for HP ScanJet scanners"
---

<p>sane-hp &#8211; SANE backend for HP ScanJet scanners</p>
<h2>Description</h2>
<p>The <code>sane-hp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to HP ScanJet scanners which support SCL (Scanner Control Language by HP). The following scanners are known positively to work with this backend:</p>
<dl>
<dd>
<pre>Model: Product id: Interface:
---------- ----------- ----------
ScanJet Plus C9195A HP Parallel Interface Card
ScanJet IIc C1750A 3226 SCSI
ScanJet IIcx C2500A 3332 SCSI
ScanJet IIp C1790A SCSI
ScanJet 3C C2520A 3503 SCSI
ScanJet 3P C2570A 3406 SCSI
ScanJet 4C C2520A SCSI
ScanJet 4P C1130A 3540 SCSI
ScanJet 4100C C6290A USB
ScanJet 5P C5110A SCSI
ScanJet 5100C C5190A parallel port
ScanJet 5200C C7190A 3846 parallel port/USB
ScanJet 6100C C2520A 3644 SCSI
ScanJet 6200C C6270A 3828 SCSI/USB
ScanJet 6250C C6270A 3828 SCSI/USB
ScanJet 6300C C7670A SCSI/USB
ScanJet 6350C C7670A SCSI/USB
ScanJet 6390C C7670A SCSI/USB
PhotoSmart C5100A R029,R030,R032 SCSI</pre>
</dl>
<p> Support for models 5100C/5200C connected to the parallel port requires the ppSCSI driver available at <i><a rel="nofollow" href="http://cyberelk.net/tim/parport/ppscsi.html">http://cyberelk.net/tim/parport/ppscsi.html</a></i> and <i><a rel="nofollow" href="http://penguin-breeder.org/kernel/download/">http://penguin-breeder.org/kernel/download/</a></i>. Support for models 5200C/62X0C/63X0C connected to the USB require the kernel scanner driver or libusb. See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for more details. The <code>sane-hp</code> backend no longer supports OfficeJet multi-function peripherals. For these devices use the external &quot;hpoj&quot; backend in version 0.90 and later of the &quot;HP OfficeJet Linux driver&quot;, available at<br />
 <i><a rel="nofollow" href="http://hpoj.sourceforge.net">http://hpoj.sourceforge.net</a></i> Because Hewlett-Packard does no longer produce scanners that support SCL (beside the OfficeJets), the above list of supported scanners is complete. Other HP scanners are not supported by the <code>sane-hp</code> backend, but might be supported by another one. See <i><a rel="nofollow" href="http://www.sane-project.org/">http://www.sane-project.org/</a></i>. You can also watch the sane-devel mailing list at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i>. More details about the hp backend can be found on its homepage <i><a rel="nofollow" href="http://www.kirchgessner.net/sane.html">http://www.kirchgessner.net/sane.html</a></i>. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the scanner. For SCSI scanners the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sg2</i>, for example. If the special device name contains &quot;usb&quot;, &quot;uscanner&quot; or &quot;ugen&quot;, it is assumed that the scanner is connected by USB. For the HP ScanJet Plus the special device name must be the device that corresponds to the parallel interface card that was shipped with the scanner. That is <i>/dev/hpscan</i>. A special driver is required for this card. See <i><a href="ftp://rvs.ctrl-c.liu.se/pub/wingel/hpscan">ftp://rvs.ctrl-c.liu.se/pub/wingel/hpscan</a></i> for details. If the link does not work, try <i><a href="ftp://sunsite.unc.edu/pub/Linux/kernel/patches/scanners">ftp://sunsite.unc.edu/pub/Linux/kernel/patches/scanners</a></i>.</p>
<h2>Configuration</h2>
<p>The contents of the <i>hp.conf</i> file is a list of options and device names that correspond to HP ScanJet scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) and <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) on details of what constitutes a valid device name. </p>
<p> Options specified in front of the first line that contains a device name are defaults for all devices. Options specified below a line that contains a device name apply just to the most recently mentioned device. </p>
<p> Supported options are <code>connect-scsi</code>, <code>connect-device</code>, <code>enable-image-buffering</code>, and <code>dumb-read</code>. </p>
<p> Option <code>connect-scsi</code> specifies that the scanner is connected to the system by SCSI. Input/output is performed using SCSI-commands. This is the default. But if your SCSI device name contains &quot;usb&quot;, &quot;uscanner&quot; or &quot;ugen&quot;, option connect-scsi must be specified. Otherwise it is assumed that the scanner is connected by USB. </p>
<p> Option <code>connect-device</code> specifies that the scanner is connected to the system by a special device. Input/output is performed by <code>read</code>()/<code>write</code>()-operations on the device. This option must be used for HP ScanJet Plus or scanners connected to USB which are accessed through a named device (e.g. <i>/dev/usb/scanner0</i>). For device names that contain &quot;usb&quot;, &quot;uscanner&quot; or &quot;ugen&quot;, it is not necessary to specify option connect-device. </p>
<p> Option <code>enable-image-buffering</code> stores the scanned image in memory before passing it to the frontend. Could be used in case of forward/backward moving scanner lamp. </p>
<p> Option <code>dumb-read</code> can be used to work around problems with &quot;Error during device I/O&quot;. These problems may occur with certain SCSI-to-USB converters or Buslogic SCSI cards. The option should not be used for SCSI devices which are working correctly. Otherwise startup of frontends and changing parameters might be slower. </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd>
<pre>/dev/scanner
# this is a comment
/dev/hpscan
option connect-device</pre>
</dl>
<p> <i>/dev/scanner</i> is typically a symlink to the actual SCSI scanner device.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/hp.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</p>
<dt><i>$HOME/.sane/calib-hp:&lt;device&gt;.dat</i></p>
<dd>Calibration data for HP PhotoSmart PhotoScanner that is retrieved from the scanner after calibration. The data is uploaded to the scanner at start of the backend if it is in media mode &#8216;print media&#8217; or if the media mode is changed to &#8216;print media&#8217;.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (<i>.</i>) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_HP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</p>
<dt><code>SANE_HOME_HP</code></p>
<dd>Only used for OS/2 and along with use of HP PhotoSmart PhotoScanner. Must be set to the directory where the directory .sane is located. Is used to save and read the calibration file.</p>
<dt><code>SANE_HP_KEEPOPEN_SCSI</code></p>
<dd>
<dt><code>SANE_HP_KEEPOPEN_USB</code></p>
<dd>
<dt><code>SANE_HP_KEEPOPEN_DEVICE</code></p>
<dd>For each type of connection (connect-scsi, connect-usb, connect-device) it can be specified if the connection to the device should be kept open (&quot;1&quot;) or not (&quot;0&quot;). Usually the connections are closed after an operation is performed. Keeping connection open to SCSI-devices can result in errors during device IO when the scanner has not been used for some time. By default, USB-connections are kept open. Other connections are closed.</p>
<dt><code>SANE_HP_RDREDO</code></p>
<dd>Specifies number of retries for read operation before returning an EOF error. Only supported for non-SCSI devices. Default: 1 retry. Time between retries is 0.1 seconds. </p>
</dl>
<h2>Bugs</h2>
<dl>
<dt><code>HP PhotoSmart PhotoScanner</code></p>
<dd>In media mode &#8216;slide&#8217; and &#8216;negative&#8217;, scan resolutions are rounded to multiple of 300 dpi. The scanner does not scale the data correctly on other resolutions. Some newer models (firmware code R030 and later) do not support adjustment of contrast/intensity level and tone map. The backend will simulate this by software, but only for gray and 24 bit color.</p>
<dt><code>Automatic Document Feeder (ADF)</code></p>
<dd>For use of the ADF with <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), first place paper in the ADF and then change option scan source to &#8216;ADF&#8217;. Press &#8216;change document&#8217; to load a sheet. Then press &#8216;scan&#8217; to start a scan. Maybe it is sufficient to press &#8216;scan&#8217; without &#8216;change document&#8217; for repeated scans. The use of the preview window is not recommended when working with the ADF. Setting a window to scan from ADF is not supported with <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1). Try <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1).</p>
<dt><code>Immediate actions</code></p>
<dd>Some actions in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) (i.e. unload, select media, calibrate) have an immediate effect on the scanner without starting a scan. These options can not be used with <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1). </p>
<h2>Todo</h2>
<dl>
<dt><code>HP PhotoSmart PhotoScanner</code></p>
<dd>PhotoScanners with firmware release R030 and up have no firmware support for contrast/brightness/gamma table. In the current backend this is simulated by software on 24 bits data. Simulation on 30 bits should give better results.</p>
<dt><code>Data widths greater than 8 bits</code></p>
<dd>Custom gamma table does not work.</p>
<dt><code>Parallel scanner support</code></p>
<dd>Beside the ScanJet Plus which came with its own parallel interface card, currently only the HP ScanJet 5100C/5200C are supported. These scanners are using an internal parallel-to-SCSI converter which is supported by the ppSCSI-driver (see above). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>Author</h2>
<p>The sane-hp backend was written by Geoffrey T. Dairiki.<br />
 HP PhotoSmart PhotoScanner support by Peter Kirchgessner.</p>
