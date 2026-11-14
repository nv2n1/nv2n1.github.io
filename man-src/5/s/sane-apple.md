---
title: "sane-apple(5)"
name: "sane-apple"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-apple/"
description: "sane-apple – SANE backend for Apple flatbed scanners"
---

<p>sane-apple &#8211; SANE backend for Apple flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-apple</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Apple flatbed scanners. At present, the following scanners are supported from this backend: </p>
<pre>--------------- ----- ------------------ ------
AppleScanner 4bit 16 Shades of Gray
OneScanner 8bit 256 Shades of Gray
ColorOneScanner 24bit RGB color 3-pass</pre>
<p>If you own a Apple scanner other than the ones listed above that works with this backend, please let us know by sending the scanner&#8217;s model name, SCSI id, and firmware revision to <i>sane-devel [at] alioth-lists.debian.net</i>. See <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details on how to subscribe to sane-devel. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The <i>apple.conf</i> file is a list of options and device names that correspond to Apple scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name. </p>
<p> Options come in two flavors: global and positional ones. Global options apply to all devices managed by the backend, whereas positional options apply just to the most recently mentioned device. Note that this means that the order in which the options appear matters!</p>
<h2>Scsi Adapter Tips</h2>
<p>SCSI scanners are typically delivered with an ISA SCSI adapter. Unfortunately, that adapter is not worth much since it is not interrupt driven. It is sometimes possible to get the supplied card to work, but without an interrupt line, scanning will put so much load on the system that it becomes almost unusable for other tasks.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/apple.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-apple.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-apple.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable is list of directories where SANE looks for the configuration file. On *NIX systems, directory names are separated by a colon (`:&#8217;), under OS/2 by a semi-colon (`;&#8217;). If SANE_CONFIG_DIR is not set, SANE defaults to searching the current working directory (&quot;.&quot;) and then <i>/etc/sane.d</i>. If the value of $SANE_CONFIG_DIR ends with the separator character, the default directories are searched after the directory list. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in that order).</p>
<dt><code>SANE_DEBUG_APPLE</code></p>
<dd>Controls the debug level. A value of 255 prints all debug output. Smaller values reduce verbosity. Requires a library compiled with debug support. </p>
</dl>
<h2>Current Status</h2>
<p>The apple backend is now in version 0.3 (Tue Jul 21 1998). Since I only have the AppleScanner and not the other models (OneScanner, ColorOneScanner) I can only develop/test for the AppleScanner effectively. However with this release I almost completed the GUI part of all scanners. Most of the functionality is there. At least OneScanner should scan at the AppleScanner&#8217;s compatible modes (LineArt, HalfTone, Gray16). My personal belief is that with a slight touch of debugging the OneScanner could be actually usable. The ColorOneScanner needs more work. AppleScanner is of course almost fully supported.</p>
<h2>Missing Functionality</h2>
<p>Currently all three models lack upload/download support.</p>
<dl>
<dt><code>AppleScanner</code></p>
<dd>Cannot up/download a halftone pattern.</p>
<dt><code>OneScanner</code></p>
<dd>Cannot up/download halftone patterns or calibration vectors.</p>
<dt><code>ColorOneScanner</code></p>
<dd>Cannot up/download halftone patterns, calibration vectors, custom Color Correction Tables (CCT) and of course custom gamma tables.</p>
<dt><code>Park/UnPark (OneScanner, ColorOneScanner)</code></p>
<dd>Some capabilities are missing.</dl>
<p> The above functionalities are missing because I don&#8217;t have the hardware to experiment on. Another reason is my lack of understanding as to how or if the SANE API provide means to describe any array type besides gamma.</p>
<h2>Unsupported Features</h2>
<p>The following &quot;features&quot; will never be supported, at least while I maintain the sane-apple backend.</p>
<dl>
<dt><code>NoHome (AppleScanner)</code></p>
<dd>The scanner lamp stays on and the carriage assembly remains where it stops at the end of the scan. After two minutes, if the scanner does not receive another SCAN command, the lamp goes off and the carriage returns to the home position.</p>
<dt><code>Compression (AppleScanner)</code></p>
<dd>The Scanner can compress data with CCITT Group III one dimensional algorithm (fax) and the Skip White Line algorithm.</p>
<dt><code>Multiple Windows (AppleScanner)</code></p>
<dd>AppleScanner may support multiple windows. It would be a cool feature and a challenge for me to code if it could intermix different options for different windows (scan areas). This way it could scan a document in LineArt mode but the figures in it in Gray and at a different resolution. Unfortunately this is impossible.</p>
<dt><code>Scan Direction (OneScanner)</code></p>
<dd>It controls the scan direction. (?)</p>
<dt><code>Status/Reset Button (OneScanner)</code></p>
<dd>This option controls the status of the button on the OneScanner model. You can also reset the button status by software. </p>
</dl>
<h2>Bugs</h2>
<p>SANE backend bugs are divided in two classes. We have <code>GUI</code> bugs and <code>scanner specific</code> bugs. We know we have a GUI bug when a parameter is not showing up when it should (active) or vice versa. Finding out which parameters are active across various Apple modes and models from the documentation <i><a href="ftp://ftpdev.info.apple.com/devworld/Technical_Documentation/Peripherals_Documentation/">ftp://ftpdev.info.apple.com/devworld/Technical_Documentation/Peripherals_Documentation/</a></i> is an interesting exercise. I may have missed some dependencies. For example of the threshold parameter the Apple Scanners Programming Guide says nothing. I had to assume it is valid only in LineArt mode. Scanner specific bugs are mostly due to mandatory round-offs in order to scan. In the documentation in one place states that the width of the scan area should be a byte multiple. In another place it says that the width of the scan area should be an even byte multiple. Go figure&#8230; Other sources of bugs are due to scsi communication, scsi connects and disconnects. However the classical bugs are still there. So you may encounter buffer overruns, null pointers, memory corruption and <code>SANE</code> API violations.</p>
<dl>
<dt><code>SIGSEGV on SliceBars</code></p>
<dd>When you try to modify the scan area from the slice bar you have a nice little cute core dump. I don&#8217;t know why. If you select the scan area from the preview window or by hand typing the numbers everything is fine. The SIGSEGV happens deep in gtk library (gdk). I really cannot debug it.</p>
<dt><code>Options too much</code></p>
<dd>It is possible, especially for the ColorOneScanner, for the backend&#8217;s options panel to extend beyond your screen. It happens with mine and I am running my X Server at 1024&#215;768. What can I say? Try smaller fonts in the X server, or virtual screens.</p>
<dt><code>Weird SCSI behaviour</code></p>
<dd>I am quoting David Myers Here&#8230; &gt;&gt; OS: FreeBSD 2.2.6<br />
 &gt;&gt; CC: egcs-1.02<br />
 Just wanted to follow up on this&#8230; I recently changed my SCSI card from the Adaptec 2940UW to a dual-channel Symbios 786 chipset. When I started up SANE with your driver, I managed to scan line art drawings okay, but Gray16 scans led to a stream of SCSI error messages on the console, ultimately hanging with a message saying the scanner wasn&#8217;t releasing the SCSI bus. This may be that the Symbios is simply less tolerant of ancient hardware, or may be bugs in your driver or in SANE itself&#8230; </p>
<h2>Debug</h2>
<p>If you encounter a GUI bug please set the environmental variable <code>SANE_DEBUG_APPLE</code> to 255 and rerun the exact sequence of keystrokes and menu selections to reproduce it. Then send me a report with the log attached. </p>
<p> If you have an Apple Macintosh with the AppleScanners driver installed, reporting to me which options are grayed out (inactive) in what modes would be very helpful. </p>
<p> If you want to offer some help but you don&#8217;t have a scanner, or you don&#8217;t have the model you would like to help with, or you are a SANE developer and you just want to take a look at how the apple backend looks like, goto to <i>apple.h</i> and #define the <code>NEUTRALIZE_BACKEND</code> macro. You can select the scanner model through the APPLE_MODEL_SELECT macro. Available options are <code>APPLESCANNER</code>, <code>ONESCANNER</code>, and <code>COLORONESCANNER</code>. </p>
<p> If you encounter a SCSI bus error or trimmed and/or displaced images please set the environment variable SANE_DEBUG_SANEI_SCSI to 255 before sending me the report.</p>
<h2>Todo</h2>
<dl>
<dt><code>Non Blocking Support</code></p>
<dd>Make <code>sane-apple</code> a non blocking backend. Properly support <code>sane_set_io_mode</code>() and <code>sane_get_select_fd</code>()</p>
<dt><code>Scan</code></p>
<dd>Make scanning possible for all models in all supported modes.</dl>
<p> Add other missing functionality</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>The <code>sane-apple</code> backend was written not entirely from scratch by Milon Firikis. It is mostly based on the <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5) backend from David Mosberger and Andreas Czechanowski</p>
