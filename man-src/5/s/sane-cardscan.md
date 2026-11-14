---
title: "sane-cardscan(5)"
name: "sane-cardscan"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-cardscan/"
description: "sane-cardscan – SANE backend for Corex CardScan usb scanners"
---

<p>sane-cardscan &#8211; SANE backend for Corex CardScan usb scanners</p>
<h2>Description</h2>
<p>The <code>sane-cardscan</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to the Corex CardScan 800c &amp; 600c small-format scanners. The backend supports only grayscale and color modes and media of (theoretically) infinite length. This backend may support other scanners. The best way to determine level of support is to get a trace of the windows driver in action, and send it to the author. </p>
<h2>Options</h2>
<p>The cardscan backend supports the following options: </p>
<dl>
<dt><code>&#8211;mode Gray|Color</code></p>
<dd>Selects the mode for the scan. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>cardscan.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will use a set of compiled defaults, which are identical to the default configuration file shipped with SANE. </p>
<p> Scanners can be specified in the configuration file in 2 ways: </p>
<p> &quot;usb 0x04c5 0x1042&quot; (or other vendor/product ids)</p>
<dl>
<dd>Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a cardscan scanner.</dl>
<p> &quot;usb /dev/usb/scanner0&quot; (or other device file)</p>
<dl>
<dd>Some systems use a kernel driver to access usb scanners. This method is untested.</dl>
<p> Additionally, there are two configuration options that control the protocol used by the backend: </p>
<p> &quot;lines_per_block 16&quot; (or other number from 1 to 32)</p>
<dl>
<dd>Controls the number of lines of image data which will be acquired in each pass. Older scanners will require this number set lower, often 1.</dl>
<p> &quot;has_cal_buffer 1&quot; (1 or 0)</p>
<dl>
<dd>Causes the backend to get calibration data from scanner during initialization. Older scanners do not support this request, and must be set to 0.</dl>
<h2>Environment</h2>
<p>The backend uses a single environment variable, <code>SANE_DEBUG_CARDSCAN,</code> which enables debugging output to stderr. Valid values are: </p>
<dl>
<dd>5 Errors<br />
 10 Function trace<br />
 15 Function detail<br />
 20 Option commands<br />
 25 SCSI/USB trace<br />
 30 SCSI/USB detail<br />
 35 Useless noise</dl>
<h2>Known Issues</h2>
<dl>
<dd>The scanner does not seem to have much control possible, so the backend cannot set x/y coordinate values, resolutions, etc. These things could be simulated in the backend, but there are plenty of command line tools. </p>
<p> The backend also does not send all the commands that the windows driver does, so it may not function the same. </p>
<p> The backend does not have the calibration or ejection options of the windows driver. </p>
</dl>
<h2>Credits</h2>
<p>The hardware to build this driver was provided to the author by: Jeff Kowalczyk <i>&lt;jtk a t yahoo d o t com&gt;</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) </p>
<h2>Author</h2>
<p>m. allan noah: <i>&lt;kitno455 a t gmail d o t com&gt; .</i></p>
