---
title: "sane-epjitsu(5)"
name: "sane-epjitsu"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-epjitsu/"
description: "sane-epjitsu – SANE backend for Epson-based Fujitsu USB scanners."
---

<p>sane-epjitsu &#8211; SANE backend for Epson-based Fujitsu USB scanners.</p>
<h2>Description</h2>
<p>The <code>sane-epjitsu</code> library implements a SANE (Scanner Access Now Easy) backend which provides basic access the Fujitsu fi-60F/fi-65F and ScanSnap S300/S1300(i)/S1100(i) scanners. </p>
<h2>Hardware Support</h2>
<p>These scanners are fairly limited, only supporting a couple of modes and resolutions, and always scanning full width. The backend supports missing modes (binary, grayscale) and intermediate resolutions in software, but provides only minimal scan area controls. See <code>KNOWN ISSUES.</code> </p>
<p> This backend may support other scanners. If physical inspection reveals an Epson chipset, please contact the author for instructions on collecting a USB trace under Windows to verify.</p>
<h2>Options</h2>
<p>A limited effort has been made to expose the standard options to the API. This allows a frontend to set resolution, color mode, and choose the ADF setting. The <code>sane-epjitsu</code> backend supports the following basic options for most scanners: </p>
<p> <code>source</code>s</p>
<dl>
<dd>Selects the source for the scan. Options may include &quot;Flatbed&quot;, &quot;ADF Front&quot;, &quot;ADF Back&quot;, &quot;ADF Duplex&quot;.</dl>
<p> <code>mode</code>m</p>
<dl>
<dd>Selects the mode for the scan. Options may include &quot;Lineart&quot;, &quot;Gray&quot;, &quot;Color&quot;.</dl>
<p> <code>resolution</code>,<code>y-resolution</code></p>
<dl>
<dd>Controls scan resolution. Setting <code>&#8211;resolution</code> also sets <code>&#8211;y-resolution, though this behavior is overridden by some frontends.</code></dl>
<p> Other options will be available based on the capabilities of the scanner. Use <i>&#8216;scanimage &#8211;help&#8217;</i> to get a list. Be aware that some options may appear only when another option has been set, and that advanced options may be hidden by the frontend.</p>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/epjitsu.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will not work. </p>
<p> Scanners can be specified in the configuration file in two ways: </p>
<p> &quot;usb 0x04c5 0x10c7&quot; (or other vendor/product ids)</p>
<dl>
<dd>Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a supported scanner.</dl>
<p> &quot;usb /dev/usb/scanner0&quot; (or other device file)</p>
<dl>
<dd>Some systems use a kernel driver to access usb scanners. This method is untested.</dl>
<p> The only configuration option supported is &quot;firmware /PATH/TO/FILE&quot;, allowing you to set the location of the firmware file you have extracted from the Windows driver. </p>
<p> <code>Note:</code> This firmware is a copyrighted work of Fujitsu, so cannot be provided by the backend or the author. Please do not ask. </p>
<p> <code>Note:</code> These scanners REQUIRE a firmware file to function. See the supplied configuration file for more detail. </p>
<p> <code>Note:</code> This option may appear multiple times in the configuration file. It only applies to scanners discovered by &#8216;usb&#8217; lines that follow this option.</p>
<h2>Environment</h2>
<p>The backend uses a single environment variable, <code>SANE_DEBUG_EPJITSU,</code> which enables debugging output to stderr. Valid values are: </p>
<dl>
<dd>5 Errors<br />
 10 Function trace<br />
 15 Function detail<br />
 20 Option commands<br />
 25 USB trace<br />
 30 USB detail<br />
 35 Useless noise</dl>
<h2>Known Issues</h2>
<dl>
<dd>Only limited scan area options are exposed. </p>
<p> fi-60F and fi-65F hardware grayscale mode is not used, because the calibration code is not finished.</dl>
<h2>Credits</h2>
<p>S300 support funded by Microdea, Inc. and Archivista, GmbH.<br />
 fi-60F support funded by TrueCheck, Inc.<br />
 Improved calibration code provided by Richard Goedeken.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>Author</h2>
<p>m. allan noah: &lt;<i>kitno455 a t gmail d o t com</i>&gt;</p>
