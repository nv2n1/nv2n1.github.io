---
title: "sane-epson2(5)"
name: "sane-epson2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-epson2/"
description: "sane-epson2 – SANE backend for EPSON scanners"
---

<p>sane-epson2 &#8211; SANE backend for EPSON scanners</p>
<h2>Description</h2>
<p>The <code>sane-epson2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Epson flatbed scanners. This library supports a similar set of scanners as the sane-epson driver but was developed to support a wider range of connections to the scanner; include network access. </p>
<p> Because <code>sane-epson</code> and <code>sane-epson2</code> drivers support many of the same devices, if one driver gives you problems you may try disabling it to try the other. This can be done by removing the driver name from the <i>dll.conf</i> or perhaps by commenting out the options in <i>epson.conf</i> or <i>epson2.conf.</i> </p>
<p> At present, the following scanners are known to work with this backend: </p>
<dl>
<dd>
<pre>Model: Connection Type
--------------------------- -------------------
ActionScanner II SCSI, parallel
AcuLaser CX11 Series USB, Network
AcuLaser CX21 Series USB, Network
CX-3200 USB
CX-3600 USB
CX-3650 USB
CX-4050 USB
CX-4600 USB
CX-4800 USB
CX-5000 USB
CX-5200 USB
CX-5400 USB
CX-6300 USB
CX-6400 USB
CX-6500 USB
CX-6600 USB
DX-3800 USB
DX-5000 USB
DX-5050 USB
DX-6000 USB
DX-7400 USB
ES-300C SCSI, parallel
ES-300GS SCSI
ES-600C parallel
ES-1200C parallel
Expression 636 SCSI
Expression 800 SCSI
Expression 1600 USB, SCSI, IEEE-1394
Expression 1680 USB, SCSI, IEEE-1394
FilmScan 200 SCSI
GT-5000 SCSI, parallel
GT-5500 SCSI
GT-6000 parallel
GT-6500 parallel
GT-7000 SCSI
GT-8000 SCSI
GT-8500 SCSI
Perfection 610 USB
Perfection 636S SCSI
Perfection 636U USB
Perfection 640 USB
Perfection 1200S SCSI
Perfection 1200U USB
Perfection 1240 USB, SCSI
Perfection 1640 USB, SCSI
Perfection 1650 USB
Perfection 1660 USB
Perfection 2400 USB
Perfection 2450 USB, IEEE-1394
Perfection 3200 USB
Perfection 4870 USB
Perfection 4990 USB
RX-425 USB
RX-500 USB
RX-600 USB
RX-700 USB
V700 USB, IEEE-1394
V750 USB, IEEE-1394</pre>
<p>and many more. The official list is on the Sane web site.</dl>
<p> For other scanners the software may or may not work. Please send mail to the sane-backend mailing list to report success with scanners not on the list or problems with scanners that are listed.</p>
<h2>Options</h2>
<p>The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in programs like <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). </p>
<p> Valid command line options and their syntax can be listed by using </p>
<dl>
<dd>scanimage &#8211;help -d epson2</dl>
<p> Not all devices support all options.</p>
<dl>
<dt><i>Scan Mode</i></p>
<dd>The <code>&#8211;mode</code> switch selects the basic mode of operation of the scanner. Valid choices are Binary, Gray and Color. The Binary mode is black and white only, Gray will produce 256 levels of gray or more depending on the scanner and Color means 24 bit color mode or more depending on the scanner. Some scanners will internally use 36 bit color, their external interface however may only support 24 bits. </p>
<p> The <code>&#8211;depth</code> option selects the bit depth the scanner is using. This option is only available for scanners that support more than one bit depth. Older scanners will always transfer the image in 8bit mode. Newer scanners allow one to select either 8 bits, 12 or 14 bits per color channel. For a color scan this means an effective color depth of 36 or 42 bits over all three channels. The valid choices depend on the scanner model. </p>
<p> The <code>&#8211;halftoning</code> switch selects the mode that is used in Binary mode. Valid options are &quot;None&quot;, &quot;Halftone A (Hard Tone)&quot;, &quot;Halftone B (Soft Tone)&quot;, &quot;Halftone C (Net Screen)&quot;, &quot;Dither A (4&#215;4 Bayer)&quot;, &quot;Dither B (4&#215;4 Spiral)&quot;, &quot;Dither C (4&#215;4 Net Screen)&quot;, &quot;Dither D (8&#215;4 Net Screen)&quot;, &quot;Text Enhanced Technology&quot;, &quot;Download pattern A&quot;, and &quot;Download pattern B&quot;. </p>
<p> The <code>&#8211;dropout</code> switch selects the so called dropout color. Valid options are None, Red, Green and Blue. The default is None. The dropout color is used for monochrome scanning and selects the color that is not scanned. This can be used to e.g. scan an original with a colored background. </p>
<p> The <code>&#8211;brightness</code> switch controls the brightness of the scan. Valid options are integer values from -3 to 3. The default is 0. The larger the brightness value, the brighter the image gets. If a user defined table for the gamma correction is selected, the brightness parameter is not available. </p>
<p> The <code>&#8211;sharpness</code> switch sets the sharpness of the image data. Valid options are integer values from -2 to 2, with -2 meaning &quot;Defocus&quot;, -1 &quot;Defocus slightly&quot;, 0 &quot;Normal&quot;, 1 &quot;Sharpen slightly&quot; and 2 &quot;Sharpen&quot;. </p>
<p> The <code>&#8211;gamma-correction</code> switch controls the scanner&#8217;s internal gamma correction. Valid options are &quot;Default&quot;, &quot;User defined&quot;, &quot;High density printing&quot; &quot;Low density printing&quot; and &quot;High contrast printing&quot;. </p>
<p> The <code>&#8211;color-correction</code> switch controls the scanner&#8217;s internal color correction function. Valid options are &quot;No Correction&quot;, &quot;Impact-dot printers&quot;, &quot;Thermal printers&quot;, &quot;Ink-jet printers&quot; and &quot;CRT monitors&quot;. The default is &quot;CRT monitors&quot;. </p>
<p> The <code>&#8211;resolution</code> switch selects the resolution for a scan. Some EPSON scanners will scan in any resolution between the lowest and highest possible value. The list reported by the scanner can be displayed using the &quot;&#8211;help -d epson&quot; parameters to <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1). </p>
<p> The <code>&#8211;threshold</code> switch selects the minimum brightness to get a white point. </p>
<p> The <code>&#8211;mirror</code> option controls the way the image is scanned. By reading the image data from right to left the image is mirrored. Valid options are &quot;yes&quot; and &quot;no&quot;. The default is &quot;no&quot;. </p>
<p> The <code>&#8211;auto-area-segmentation</code> switch activates the automatic area segmentation for monochrome scans. The scanner will try to determine which areas are text and which contain images. The image areas will be halftoned, and the text will be improved. Valid options are &quot;yes&quot; and &quot;no&quot;. The default is &quot;yes&quot;. </p>
<p> The <code>&#8211;red-gamma-table</code> parameter can be used to download a user defined gamma table for the red channel. The valid options are the same as for &#8211;gamma-table. </p>
<p> The <code>&#8211;green-gamma-table</code> parameter can be used to download a user defined gamma table for the green channel. The valid options are the same as for &#8211;gamma-table. </p>
<p> The <code>&#8211;blue-gamma-table</code> parameter can be used to download a user defined gamma table for the blue channel. The valid options are the same as for &#8211;gamma-table. </p>
<p> The <code>&#8211;wait-for-button</code> parameter can be used to wait until the button on the scanner is pressed to actually start the scan process. </p>
<p> The color correction coefficients <code>&#8211;cct-1 &#8211;cct-2 &#8211;cct-3 &#8230; &#8211;cct-9</code> will install color correction coefficients for the user defined color correction. Values are specified as integers in the range -127..127. </p>
<p> The <code>&#8211;preview</code> option requests a preview scan. The frontend software automatically selects a low resolution. Valid options are &quot;yes&quot; and &quot;no&quot;. The default is &quot;no&quot;. </p>
<p> The geometry options <code>-l -t -x -y</code> control the scan area: <code>-l</code> sets the top left x coordinate, <code>-t</code> the top left y coordinate, <code>-x</code> selects the width and <code>-y</code> the height of the scan area. All parameters are specified in millimeters. </p>
<p> The <code>&#8211;source</code> option selects the scan source. Valid options depend on the installed options. The default is &quot;Flatbed&quot;. </p>
<p> The <code>&#8211;auto-eject</code> option will eject a page after scanning from the document feeder. </p>
<p> The <code>&#8211;film-type</code> option will select the film type for scans with the transparency unit. This option is only activated if the TPU is selected as scan source. Valid options are &quot;Negative Film&quot; and &quot;Positive Film&quot;. </p>
<p> The <code>&#8211;focus-position</code> option selects the focus position for all scans. Valid options are &quot;Focus 2.5mm above glass&quot; and &quot;Focus on glass&quot;. The focus on the 2.5mm point above the glass is necessary for scans with the transparency unit, so that the scanner can focus on the film if one of the film holders is used. This option is only functional for selected scanners, all other scanners will ignore this option. </p>
<p> The <code>&#8211;bay</code> option selects which bay to scan </p>
<p> The <code>&#8211;eject</code> option ejects the sheet in the ADF. </p>
<p> The <code>&#8211;adf-mode</code> option select the ADF mode (simplex/duplex). </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/epson2.conf</i> specifies the device(s) that the backend will use. Possible connection types are:</p>
<dl>
<dt><code>SCSI</code></p>
<dd>This is the default, and if nothing else is specified the backend software will open a given path as SCSI device. More information about valid syntax for SCSI devices can be found in <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5).<br />
 Usually SCSI scanners are configured with a line &quot;scsi EPSON&quot; in this file. In some cases it may be necessary to only use the string &quot;scsi&quot; (e.g. for the GT-6500).</p>
<dt><code>PIO &#8211; Parallel Interface</code></p>
<dd>The parallel interface can be configured in two ways: An integer value starting at the beginning of a line will be interpreted as the IO address of the parallel port. To make it clearer that a configured IO address is a parallel port the port address can be preceded by the string &quot;PIO&quot;. The PIO connection does not use a special device file in the <i>/dev</i> directory. The IO address can be specified in hex mode (prefixed with &quot;0x&quot;).</p>
<dt><code>USB</code></p>
<dd>For USB scanners not automatically detect, their VENDOR and PRODUCT ID can be specified manually in the config file. More information about valid syntax for USB devices can be found in <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5).</p>
<dt><code>Network</code></p>
<dd>Network scanners can be auto-discovered if <code>autodiscovery</code> is specified after <code>net</code> keyword. An IP address to connect to can also be used.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-epson2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-epson2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_EPSON2</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</p>
<dt><code>SANE_DEBUG_EPSON2_SCSI</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the SCSI related debug level for this backend. Only a value of 2 is supported.</p>
<dt><code>SANE_DEBUG_EPSON2_NET</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the network related debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</p>
<dt><code>SANE_EPSON2_CMD_LVL</code></p>
<dd>This allows one to override the function or command level that the backend uses to communicate with the scanner. The function level a scanner supports is determined during the initialization of the device. If the backend does not recognize the function level reported by the scanner it will default to function level B3. Valid function levels are A1, A2, B1, B2, B3, B4, B5, B6, B7, B8, D1 and F5. Use this feature only if you know what you are doing! </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Bugs</h2>
<p>None :-) At least none are currently known. </p>
<h2>Unsupported Devices</h2>
<p>The backend may be used with Epson scanners that are not yet listed under the list of supported devices. A scanner that is not recognized may default to the function level B3, which means that not all functions that the scanner may be capable of are accessible. </p>
<p> If the scanner is not even recognized as an Epson scanner this is probably because the device name reported by the scanner is not in the correct format. Please send this information to the backend maintainer (email address is in the AUTHOR section of this man page or in the AUTHORS file of the SANE distribution).</p>
<h2>Author</h2>
<p>The package is written by Alessandro Zummo and is based on previous work done by Karl Hienz Kremer in the epson package as well as based on work by Christian Bucher and Kazuhiro Sasayama.</p>
