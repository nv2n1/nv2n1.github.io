---
title: "sane-stv680(5)"
name: "sane-stv680"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-stv680/"
description: "sane-stv680 – SANE backend for STV680 camera’s"
---

<p>sane-stv680 &#8211; SANE backend for STV680 camera&#8217;s</p>
<h2>Description</h2>
<p>The <code>sane-stv680</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to some STV680 cameras. This backend should be considered <code>beta-quality</code> software! STV680 cameras are sold under various brands like Aiptek. This backend may or may not support yours. The cameras that should work with this backend are: </p>
<pre>Vendor Model USB vendor id USB product id status
------------------------ ------------- -------------- --------
AIPTEK stv680 0x0553 0x0202 basic
Konica e-mini 0x04c8 0x0722 untested
DigitalDream l'espion XS 0x1183 0x0001 untested
Creative WebCam Go mini 0x041e 0x4007 untested</pre>
<p>For all these cameras, see the backend home page (under AUTHOR) for the exact status of each camera. For startup of this backend check that if present the stv680 kernel module is removed or disabled.<br />
 Also before using, enable the backend by editing the <i>/etc/sane.d/dll.conf</i> file, change #stv680 to stv680. For problems with the untested cameras, you should contact the author for that. The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1). For both programs use the <code>-B</code> option needed for size buffer. Some frontends examples:<br />
 <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1)</p>
<dl>
<dd>xcam -B</dl>
<p> <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1): for writing in batch mode to a file or to a new file each time: </p>
<pre><code>scanimage -B -d stv680:libusb:001:002 --batch=out.ppm --batch-count 5 --mode &quot;Color RGB&quot;



scanimage -B -d stv680:libusb:001:002 --batch=out%d.ppm --batch-count 5 --mode &quot;Color RGB&quot;</code></pre>
<p> If you have any success with a camera not listed here, or if you observe any strange behavior, please report to the backend maintainer or to the SANE mailing list. Valid command line options and their syntax can be listed by using:</p>
<dl>
<dd>scanimage &#8211;help -d stv680</dl>
<dl>
<dt><code>Scan Mode</code></p>
<dd>
<dt><code>&#8211;mode</code></p>
<dd>selects the basic mode of operation of the webcams valid choices. The read resolution mode is 8 bits, output resolution is 24 bits. Selects the resolution for a scan. The camera can do only the resolutions listed.</p>
<dt><code>&#8211;Raw</code></p>
<dd>In this mode raw data is displayed</p>
<dt><code>&#8211;Color</code></p>
<dd>In this mode the bayer unshuffle is done but no color correction</p>
<dt><code>&#8211;Color_RGB</code></p>
<dd>Bayer unshuffle, color correction</p>
<dt><code>&#8211;Color_RGB_TXT</code></p>
<dd>Bayer unshuffle, color correction, textline with date and time is added</p>
<dt><code>Enhancement options</code></p>
<dd>
<dt><code>&#8211;white-level-r -32..+32</code></p>
<dd>Selects what red radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1.</p>
<dt><code>&#8211;white-level-g -32..+32</code></p>
<dd>Selects what green radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration i value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1.</p>
<dt><code>&#8211;white-level-b -32..+32</code></p>
<dd>Selects what blue radiance level should be considered &quot;white&quot;, when scanning some sheets by changing the calibration value loaded into the scanner. Scale -32 .. 0 .. +32 in steps of 1. </p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/stv680.conf</i> supports only one item: the device name to use (eg usb 0x&#8230;. 0x&#8230;.).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-stv680.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-stv680.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_STV680</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Limitations</h2>
<p>The windows TWAIN driver has many more options than this SANE backend. However they are only software adjustments. This backend only implements what the webcam can support.</p>
<h2>Bugs</h2>
<dl>
<dt>Plenty. Parts of this backend are still under development.</p>
<dd>1. Some untested cameras.<br />
 2. Video streaming slow and stops sometimes (scanimage).<br />
 3. Sometimes 1/3 of image is NOK (xcam). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1) </p>
<h2>Authors</h2>
<p>Gerard Klaver <i><a rel="nofollow" href="http://gkall.hobby.nl/stv680-aiptek.html">http://gkall.hobby.nl/stv680-aiptek.html</a></i></p>
<h2>Credits</h2>
<dl>
<dt>Thanks to developers of the other stv680 programs:</p>
<dd>STV680 kernel module<br />
 pencam2 program<br />
 <code><a href="/docs/linux/man/3-libghoto2/">libghoto2</a></code>(3) program (camlib stv0680) </p>
</dl>
