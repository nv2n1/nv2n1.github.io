---
title: "sane-fujitsu(5)"
name: "sane-fujitsu"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-fujitsu/"
description: "sane-fujitsu – SANE backend for Fujitsu flatbed and ADF scanners"
---

<p>sane-fujitsu &#8211; SANE backend for Fujitsu flatbed and ADF scanners</p>
<h2>Description</h2>
<p>The <code>sane-fujitsu</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to most Fujitsu flatbed and ADF scanners. This document describes backend version 137, which shipped with SANE 1.0.32. </p>
<h2>Supported Hardware</h2>
<p>This version supports every known model which speaks the Fujitsu SCSI and SCSI-over-USB protocols. Specifically, the SCSI M309x and M409x series, the SCSI fi-series, most of the USB fi-series, the USB ScanSnap S5xx/S15xx, and the USB iX1xx/5xx series scanners are supported. Please see the list at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> for details. </p>
<p> This backend may support other Fujitsu scanners. The best way to determine level of support is to test the scanner directly, or to collect a trace of the windows driver in action. Please contact the author for help or with test results.</p>
<h2>Unsupported Hardware</h2>
<p>The following scanners are known NOT to work with this backend, either because they have a non-fujitsu chipset, or an unsupported interface type. Some of these scanners may be supported by another backend. </p>
<dl>
<dd>
<pre>--------------------------------------
SCSI: SERIAL: USB:
------------ ------------ ------------
ScanStation M3093E/DE/EX fi-4110EOX/2
ScanPartner M3096EX fi-4010CU
SP-Jr M3097E+/DE S300/S300M
SP-10/10C M3099A/EH/EX S1300/S1100
SP-15C/300C fi-60F/65F
SP-600C/620C fi-5015C
 SP-2x/3x</pre>
</dl>
<h2>Options</h2>
<p>Effort has been made to expose all hardware options, including: </p>
<p> <code>source s</code></p>
<dl>
<dd>Selects the source for the scan. Options may include &quot;Flatbed&quot;, &quot;ADF Front&quot;, &quot;ADF Back&quot;, &quot;ADF Duplex&quot;, &quot;Card Front&quot;, &quot;Card Back&quot;, &quot;Card Duplex&quot;.</dl>
<p> <code>mode m</code></p>
<dl>
<dd>Selects the mode for the scan. Options may include &quot;Lineart&quot;, &quot;Halftone&quot;, &quot;Gray&quot;, and &quot;Color&quot;.</dl>
<p> <code>resolution, y-resolution</code></p>
<dl>
<dd>Controls scan resolution. Setting <code>&#8211;resolution</code> also sets <code>&#8211;y-resolution,</code> though this behavior is overridden by some frontends.</dl>
<p> <code>tl-x, tl-y, br-x, br-y</code></p>
<dl>
<dd>Sets scan area upper left and lower right coordinates. These are renamed <code>t, l, x, y</code> by some frontends.</dl>
<p> <code>page-width, page-height</code></p>
<dl>
<dd>Sets paper size. Used by scanner to determine centering of scan coordinates when using the ADF (Automatic Document Feeder) and to detect double feed errors.</dl>
<p> Other options will be available based on the capabilities of the scanner: machines with IPC or DTC will have additional enhancement options, those with CMP will have compression options, those with a printer will have a group of endorser options. </p>
<p> Additionally, several &#8216;software&#8217; options are exposed by the backend. These are reimplementations of features provided natively by larger scanners, but running on the host computer. This enables smaller machines to have similar capabilities. Please note that these features are somewhat simplistic, and may not perform as well as the native implementations. Note also that these features all require that the driver cache the entire image in memory. This will almost certainly result in a reduction of scanning speed. </p>
<p> swcrop</p>
<dl>
<dd>Requests the driver to detect the extremities of the paper within the larger image, and crop the empty edges.</dl>
<p> swdeskew</p>
<dl>
<dd>Requests the driver to detect the rotation of the paper within the larger image, and counter the rotation.</dl>
<p> swdespeck X</p>
<dl>
<dd>Requests the driver to find and remove dots of X diameter or smaller from the image, and fill the space with the average surrounding color.</dl>
<p> Use <i>&#8216;scanimage &#8211;help&#8217;</i> to get a list, but be aware that some options may be settable only when another option has been set, and that advanced options may be hidden by some frontend programs.</p>
<h2>Configuration File</h2>
<p>The configuration file <i>fujitsu.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts. If the configuration file is missing, the backend will be unable to locate any scanners. </p>
<p> Scanners can be specified in the configuration file in 4 ways: </p>
<p> &quot;scsi FUJITSU&quot;</p>
<dl>
<dd>Requests backend to search all scsi buses in the system for a device which reports itself to be a scanner made by &#8216;FUJITSU&#8217;.</dl>
<p> &quot;scsi /dev/sg0&quot; (or other scsi device file)</p>
<dl>
<dd>Requests backend to open the named scsi device. Only useful if you have multiple compatible scanners connected to your system, and need to specify one. Probably should not be used with the other &quot;scsi&quot; line above.</dl>
<p> &quot;usb 0x04c5 0x1042&quot; (or other vendor/product ids)</p>
<dl>
<dd>Requests backend to search all usb buses in the system for a device which uses that vendor and product id. The device will then be queried to determine if it is a Fujitsu scanner.</dl>
<p> &quot;usb /dev/usb/scanner0&quot; (or other device file)</p>
<dl>
<dd>Some systems use a kernel driver to access usb scanners. This method is untested.</dl>
<p> The only configuration option supported is &quot;buffer-size=xxx&quot;, allowing you to set the number of bytes in the data buffer to something other than the compiled-in default, 65536 (64K). Some users report that their scanner will &quot;hang&quot; mid-page, or fail to transmit the image if the buffer is not large enough. </p>
<p> Note: This option may appear multiple times in the configuration file. It only applies to scanners discovered by &#8216;scsi/usb&#8217; lines that follow this option. </p>
<p> Note: The backend does not place an upper bound on this value, as some users required it to be quite large. Values above the default are not recommended, and may crash your OS or lockup your scsi card driver. You have been warned.</p>
<h2>Environment</h2>
<p>The backend uses a single environment variable, <code>SANE_DEBUG_FUJITSU</code>, which enables debugging output to stderr. Valid values are: </p>
<dl>
<dd>5 Errors<br />
 10 Function trace<br />
 15 Function detail<br />
 20 Option commands<br />
 25 SCSI/USB trace<br />
 30 SCSI/USB writes<br />
 31 SCSI/USB reads<br />
 35 Useless noise</dl>
<h2>Known Issues</h2>
<p>Flatbed units may fail to scan at maximum area, particularly at high resolution. </p>
<p> Any model that does not support VPD during inquiry will not function until an override is added to the backend. </p>
<p> CCITT Fax compression used by older scanners is not supported. </p>
<p> JPEG output is supported by the backend, but not by the SANE protocol, so is disabled in this release. It can be enabled if you rebuild from source.</p>
<h2>Credits</h2>
<p>m3091 backend: Frederik Ramm &lt;<i>frederik a t remote d o t org</i>&gt;<br />
 m3096g backend: Randolph Bentson &lt;<i>bentson a t holmsjoen d o t com</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;(with credit to the unnamed author of the coolscan driver)<br />
 fujitsu backend, m3093, fi-4340C, ipc, cmp, long-time maintainer: </p>
<p>&nbsp;<wbr>&nbsp;Oliver Schirrmeister &lt;<i>oschirr a t abm d o t de</i>&gt;<br />
 m3092: Mario Goppold &lt;<i>mgoppold a t tbzpariv d o t tcc-chemnitz dot de</i>&gt;<br />
 fi-4220C and basic USB support: Ron Cemer &lt;<i>ron a t roncemer d o t com</i>&gt;<br />
 fi-4120, fi-series color, backend re-write, jpeg, current maintainer:<br />
&nbsp;<wbr>&nbsp;m. allan noah: &lt;<i>kitno455 a t gmail d o t com</i>&gt; </p>
<p> JPEG output and low memory usage support funded by:<br />
&nbsp;<wbr>&nbsp;Archivista GmbH <i><a rel="nofollow" href="http://www.archivista.ch">www.archivista.ch</a></i> </p>
<p> Endorser support funded by:<br />
&nbsp;<wbr>&nbsp;O A S Oilfield Accounting Service Ltd<br />
&nbsp;<wbr>&nbsp;1500, 840 &#8211; 7th Avenue S.W.<br />
&nbsp;<wbr>&nbsp;Calgary, Alberta<br />
&nbsp;<wbr>&nbsp;T2P 3G2 Canada<br />
&nbsp;<wbr>&nbsp;1-403-263-2600 <i><a rel="nofollow" href="http://www.oas.ca">www.oas.ca</a></i> </p>
<p> Automatic length detection support funded by:<br />
&nbsp;<wbr>&nbsp;Martin G. Miller <i>mgmiller at optonline.net</i> </p>
<p> Hardware donated, software image enhancement and fi-6/7xxx support funded by:<br />
&nbsp;<wbr>&nbsp;Fujitsu Computer Products of America, Inc. <i><a rel="nofollow" href="http://www.fcpa.com">www.fcpa.com</a></i> </p>
<p> iX500 support funded by:<br />
&nbsp;<wbr>&nbsp;Prefix Computer Services <i><a rel="nofollow" href="http://www.prefixservice.com">www.prefixservice.com</a></i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-sp15c/">sane-sp15c</a></code>(5), <code><a href="/docs/linux/man/5-sane-avision/">sane-avision</a></code>(5), <code><a href="/docs/linux/man/5-sane-epjitsu/">sane-epjitsu</a></code>(5) </p>
<h2>Author</h2>
<p>m. allan noah: &lt;kitno455 a t gmail d o t com&gt;</p>
