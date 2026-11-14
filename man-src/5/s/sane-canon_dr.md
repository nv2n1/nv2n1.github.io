---
title: "sane-canon_dr(5)"
name: "sane-canon_dr"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-canon_dr/"
description: "sane-canon_dr – SANE backend for Canon DR-series scanners"
---

<p>sane-canon_dr &#8211; SANE backend for Canon DR-series scanners</p>
<h2>Description</h2>
<p>The <code>sane-canon_dr</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to some Canon DR-series scanners. This document describes backend version 60, which shipped with SANE 1.0.32. </p>
<h2>Supported Hardware</h2>
<p>This version has only been tested with a few scanner models. Please see <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> for the most recent list. </p>
<p> This backend may support other Canon scanners. The best way to determine level of support is to test the scanner directly, or to collect a trace of the windows driver in action. Please contact the author for help or with test results. </p>
<p> In general, the larger machines (DR-4000 and up) which have been tested use a fairly complete protocol, with hardware support for many modes, resolutions and features. The smaller machines have many limitations, like missing horizontal resolutions, missing binary mode, always scanning full-width, etc. There is code in the backend to address these problems, but there seems to be no way to detect if they are required, so they must be hard-coded.</p>
<h2>Options</h2>
<p>Effort has been made to expose most hardware options, including:</p>
<dl>
<dt><code>&#8211;source Flatbed|ADF Front|ADF Back|ADF Duplex</code></p>
<dd>Selects the source for the scan. </p>
<dt><code>&#8211;mode Lineart|Halftone|Gray|Color</code></p>
<dd>Selects the mode for the scan. </p>
<dt><code>&#8211;resolution</code></p>
<dd>Controls scan resolution. </p>
<dt><code>&#8211;tl-x, &#8211;tl-y, &#8211;br-x, &#8211;br-y</code></p>
<dd>Sets scan area upper left and lower right coordinates. These are renamed <code>-t</code>, <code>-l</code>, <code>-x</code>, <code>-y</code> by some frontends. </p>
<dt><code>&#8211;page-width, &#8211;page-height</code></p>
<dd>Sets paper size. Used by scanner to determine centering of scan coordinates when using the ADF (Automatic Document Feeder) and to detect double feed errors. </p>
</dl>
<p> Other options will be available based on the capabilities of the scanner: enhancement, compression, buttons and sensors, etc. </p>
<p> Additionally, several &#8216;software&#8217; options are exposed by the backend. These are reimplementations of features provided natively by larger scanners, but running on the host computer. This enables smaller machines to have similar capabilities. Please note that these features are somewhat simplistic, and may not perform as well as the native implementations. Note also that these features all require that the driver cache the entire image in memory. This will almost certainly result in a reduction of scanning speed. </p>
<dl>
<dt><code>&#8211;swcrop</code></p>
<dd>Requests the driver to detect the extremities of the paper within the larger image, and crop the empty edges. </p>
<dt><code>&#8211;swdeskew</code></p>
<dd>Requests the driver to detect the rotation of the paper within the larger image, and counter the rotation. </p>
<dt><code>&#8211;swdespeck X</code></p>
<dd>Requests the driver to find and remove dots of X diameter or smaller from the image, and fill the space with the average surrounding color. </p>
<p> Use &#8216;scanimage &#8211;help&#8217; to get a list, but be aware that some options may be settable only when another option has been set, and that advanced options may be hidden by some frontend programs. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>canon_dr.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will fail to run. </p>
<p> Scanners can be specified in the configuration file in 4 ways: </p>
<p> &quot;scsi CANON DR&quot;</p>
<dl>
<dd>Requests backend to search all scsi buses in the system for a device which reports itself to be a scanner made by &#8216;CANON&#8217;, with a model name starting with &#8216;DR&#8217;.</dl>
<p> &quot;scsi /dev/sg0&quot; (or other scsi device file)</p>
<dl>
<dd>Requests backend to open the named scsi device. Only useful if you have multiple compatible scanners connected to your system, and need to specify one. Probably should not be used with the other &quot;scsi&quot; line above.</dl>
<p> &quot;usb 0x04a9 0x1603&quot; (or other vendor/product ids)</p>
<dl>
<dd>Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a Canon scanner.</dl>
<p> &quot;usb /dev/usb/scanner0&quot; (or other device file)</p>
<dl>
<dd>Some systems use a kernel driver to access usb scanners. This method is untested.</dl>
<p> Besides the &#8216;scsi&#8217; and &#8216;usb&#8217; lines, the configuration file supports the following &#8216;option&#8217; lines: </p>
<p> &quot;option buffer-size [number of bytes]&quot;</p>
<dl>
<dd>Set the number of bytes in the data buffer to something other than the compiled-in default of 4MB. Large values may cause timeouts or hangs, small values may cause slow scans. </p>
<p> Note: The backend does not place an upper bound on this value, as some users required it to be quite large. Values above the default are not recommended, and may crash your OS or lockup your scsi card driver. You have been warned.</dl>
<p> &quot;option vendor-name [string of text]&quot;<br />
 &quot;option model-name [string of text]&quot;<br />
 &quot;option version-name [string of text]&quot;</p>
<dl>
<dd>These options can be used collectively to override the values provided by the scanner, or to provide the values when the scanner cannot.</dl>
<p> &quot;option padded-read [0|1]&quot;</p>
<dl>
<dd>Some scanners prepend all data transmitted to host with 12 bytes. Enable this option if the scanner fails to respond to commands.</dl>
<p> &quot;option duplex-offset [integer]&quot;</p>
<dl>
<dd>Some scanners pad the upper edge of one side of a duplex scan. There is some variation in the amount of padding. Modify this option if your unit shows an unwanted band of image data on only one side.</dl>
<p> <code>NOTE</code>: &quot;option&quot; lines may appear multiple times in the configuration file. They only apply to scanners discovered by the next &#8216;scsi/usb&#8217; line.</p>
<h2>Environment</h2>
<p>The backend uses a single environment variable, <code>SANE_DEBUG_CANON_DR</code>, which enables debugging output to stderr. Valid values are: </p>
<dl>
<dd>5 Errors<br />
 10 Function trace<br />
 15 Function detail<br />
 20 Option commands<br />
 25 SCSI/USB trace<br />
 30 SCSI/USB detail<br />
 35 Useless noise</dl>
<h2>Known Issues</h2>
<p>This backend was entirely reverse engineered from usb traces of the proprietary driver. Various advanced features of the machines may not be enabled. Many machines have not been tested. Their protocol is unknown.</p>
<h2>Credits</h2>
<p>The various authors of the <code><a href="/docs/linux/man/5-sane-fujitsu/">sane-fujitsu</a></code>(5) backend provided useful code.<br />
 Yabarana Corp. <i><a rel="nofollow" href="http://www.yabarana.com">www.yabarana.com</a></i> provided significant funding.<br />
 EvriChart, Inc. <i><a rel="nofollow" href="http://www.evrichart.com">www.evrichart.com</a></i> provided funding and loaned equipment.<br />
 Canon, USA. <i><a rel="nofollow" href="http://www.usa.canon.com">www.usa.canon.com</a></i> loaned equipment.<br />
 HPrint <i>hprint.com.br</i> provided funding and testing for DR-2510 support.<br />
 Stone-IT <i><a rel="nofollow" href="http://www.stone-it.com">www.stone-it.com</a></i> provided funding for DR-2010 and DR-2050 support.<br />
 Gerhard Pfeffer provided access and testing for P-208 and P-215.<br />
 Special thanks to: Alejandro Imass, Andre Shimakawa, Martijn van Brummelen, Thanos Diacakis and Junren Shi for testing and feedback.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a>(5)</code> </p>
<h2>Author</h2>
<p>m. allan noah: <i>&lt;kitno455 a t gmail d o t com&gt;</i>.</p>
