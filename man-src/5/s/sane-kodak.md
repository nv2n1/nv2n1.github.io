---
title: "sane-kodak(5)"
name: "sane-kodak"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-kodak/"
description: "sane-kodak – SANE backend for big Kodak flatbed and ADF scanners"
---

<p>sane-kodak &#8211; SANE backend for big Kodak flatbed and ADF scanners</p>
<h2>Description</h2>
<p>The <code>sane-kodak</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to large Kodak flatbed and ADF scanners. This document describes backend version 7, which shipped with SANE 1.0.21. </p>
<h2>Supported Hardware</h2>
<p>This version should support models which speak the Kodak SCSI and Firewire protocols. The i1860 was used to develop the backend, but other models may work with only minimal modifications. Please see the list at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> for an updated list. </p>
<p> If you have a machine not on that list, or reported as &#8216;untested&#8217;: the best way to determine level of support is to test the scanner directly, or to collect a trace of the windows driver in action. Please contact the author for help or with test results.</p>
<h2>Unsupported Hardware</h2>
<p>Most of the recent Kodak consumer or workgroup level machines are based on other chipsets and are not supported by this backend. Some of these scanners may be supported by another backend.</p>
<h2>Options</h2>
<p>Effort has been made to expose the basic hardware options, including: </p>
<p> <code>&#8211;source s</code></p>
<dl>
<dd>Selects the source for the scan. Options may include &quot;Flatbed&quot;, &quot;ADF Front&quot;, &quot;ADF Back&quot;, &quot;ADF Duplex&quot;.</dl>
<p> <code>&#8211;mode m</code></p>
<dl>
<dd>Selects the mode for the scan. Options may include &quot;Lineart&quot;, &quot;Halftone&quot;, &quot;Gray&quot;, and &quot;Color&quot;.</dl>
<p> <code>&#8211;resolution</code></p>
<dl>
<dd>Controls scan resolution. Available choices may be limited by mode.</dl>
<p> <code>&#8211;tl-x</code>, <code>&#8211;tl-y</code>, <code>&#8211;br-x</code>, <code>&#8211;br-y</code></p>
<dl>
<dd>Sets scan area upper left and lower right coordinates. These are renamed <code>-t</code>, <code>-l</code>, <code>-x</code>, <code>-y</code> by some frontends.</dl>
<p> <code>&#8211;page-width</code>, <code>&#8211;page-height</code></p>
<dl>
<dd>Sets paper size. Used by scanner to determine centering of scan coordinates when using the ADF (Automatic Document Feeder) and to detect double feed errors.</dl>
<p> Other options will be available based on the capabilities of the scanner. Use <i>scanimage &#8211;help</i> to get a list, but be aware that some options may be settable only when another option has been set, and that advanced options may be hidden by some frontend programs.</p>
<h2>Configuration File</h2>
<p>The configuration file <i>kodak.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will use a set of compiled defaults, which are identical to the default configuration file shipped with SANE. </p>
<p> Scanners can be specified in the configuration file in 2 ways: </p>
<p> &quot;scsi KODAK&quot;</p>
<dl>
<dd>Requests backend to search all scsi buses in the system for a device which reports itself to be a scanner made by &#8216;KODAK&#8217;.</dl>
<p> &quot;scsi /dev/sg0&quot; (or other scsi device file)</p>
<dl>
<dd>Requests backend to open the named scsi device. Only useful if you have multiple compatible scanners connected to your system, and need to specify one. Probably should not be used with the other &quot;scsi&quot; line above.</dl>
<p> The only configuration option supported is &quot;buffer-size=xxx&quot;, allowing you to set the number of bytes in the data buffer to something other than the compiled-in default, 32768 (32K). Some users report that their scanner will &quot;hang&quot; mid-page, or fail to transmit the image if the buffer is not large enough. </p>
<p> Note: This option may appear multiple times in the configuration file. It only applies to scanners discovered by &#8216;scsi/usb&#8217; lines that follow this option. </p>
<p> Note: The backend does not place an upper bound on this value, as some users required it to be quite large. Values above the default are not recommended, and may crash your OS or lockup your scsi card driver. You have been warned.</p>
<h2>Environment</h2>
<p>The backend uses a single environment variable, <code>SANE_DEBUG_KODAK</code>, which enables debugging output to stderr. Valid values are: </p>
<dl>
<dd>5 Errors<br />
 10 Function trace<br />
 15 Function detail<br />
 20 Option commands<br />
 25 SCSI trace<br />
 30 SCSI detail<br />
 35 Useless noise</dl>
<h2>Known Issues</h2>
<p>Most hardware options are either not supported or not exposed for control by the user, including: multifeed detection, image compression, autocropping, endorser, thresholding, multi-stream, etc.</p>
<h2>Credits</h2>
<p>The various authors of the <code><a href="/docs/linux/man/5-sane-fujitsu/">sane-fujitsu</a></code>(5) backend provided useful code.<br />
 Kodak provided access to hardware, documentation and personnel.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>Author</h2>
<p>m. allan noah: &lt;<i>kitno455 a t gmail d o t com</i>&gt;</p>
