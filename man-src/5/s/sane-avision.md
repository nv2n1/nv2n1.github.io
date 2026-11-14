---
title: "sane-avision(5)"
name: "sane-avision"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-avision/"
description: "sane-avision – SANE backend for Avision branded and Avision OEM (HP, Minolta, Mitsubishi, UMAX and possibly more) flatbed and film scanners."
---

<p>sane-avision &#8211; SANE backend for Avision branded and Avision OEM (HP, Minolta, Mitsubishi, UMAX and possibly more) flatbed and film scanners.</p>
<h2>Description</h2>
<p>The <code>sane-avision</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to various Avision scanners and the Avision OEM scanners labelled by HP, Minolta, Mitsubishi or Fujitsu. It is fully big-endian aware and in everyday use on PowerPC and SPARC systems. <code>I suggest you hold one hand on the power-button of the scanner while</code> <code>you try the first scans &#8211; especially with film-scanners!</code> </p>
<h2>Configuration</h2>
<p>The configuration file for this backend resides in <i>/etc/sane.d/avision.conf</i>. </p>
<p> Its contents is a list of device names that correspond to Avision and Avision compatible scanners and backend-options. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<pre> # this is a comment
 option force-a4
 option force-a3
 option skip-adf
 option disable-gamma-table
 option disable-calibration
 #scsi Vendor Model Type Bus Channel ID LUN
 scsi AVISION
 scsi HP
 scsi /dev/scanner
 usb 0x03f0 0x0701</pre>
<dl>
<dt>force-a4:</p>
<dd>Forces the backend to overwrite the scanable area returned by the scanner to ISO A4. Scanner that are known to return bogus data are marked in the backend so if you need this option please report this to the backend maintainer. USE WITH CARE!</p>
<dt>force-a3:</p>
<dd>Forces the backend to overwrite the scanable area returned by the scanner to ISO A3. Scanner that are known to return bogus data are marked in the backend so if you need this option please report this to the backend maintainer. USE WITH CARE!</p>
<dt>skip-adf:</p>
<dd>Forces the backend to ignore an inconsistent ADF status returned by the scanner (ADF not present, but ADF model number non-zero). Without this option, the backend will make several attempts to reset the ADF and retry the query in this situation, and will fail with a &quot;not supported&quot; error if the ADF still doesn&#8217;t respond.</p>
<dt>disable-gamma-table:</p>
<dd>Disables the usage of the scanner&#8217;s gamma-table. You might try this if your scans hang or only produce random garbage.</p>
<dt>disable-calibration:</p>
<dd>Disables the scanner&#8217;s color calibration. You might try this if your scans hang or only produce random garbage.</p>
<dt>Note:</p>
<dd>Any option above modifies the default code-flow for your scanner. The options should only be used when you encounter problems with the default behavior of the backend. Please report the need of options to the backend-author so the backend can be fixed as soon as possible. </p>
</dl>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>scsi scsi-spec</i> </p>
<p> <i>usb usb-spec</i></dl>
<p> Where <i>scsi-spec</i> is the path-name to a special device or a device ID for the device that corresponds to a SCSI scanner. The special device name must be a generic SCSI device or a symlink to such a device, for example on Linux <i>/dev/sga</i> or <i>/dev/sg0</i>. The device ID is the ID returned by the scanner, for example &quot;HP&quot; or &quot;AVISION&quot;. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<dl>
<dt>Note:</p>
<dd>Since the backend now includes native USB access, it is no longer needed &#8211; even considered obsolete &#8211; to access USB scanner via the SCSI emulation (named hpusbscsi on Linux) for Avision USB devices such as the HP 53xx, HP 74xx or Minolta film-scanners.</dl>
<p> <i>usb-spec</i> is the USB device name, the vendor/product ID pair or the name used by libusb corresponding to the USB scanner. For example &quot;0x03f0 0x0701&quot; or &quot;libusb:002:003&quot;. See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for details. </p>
<p> The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct scsi or usb device name. </p>
<p> A list with supported devices is built into the avision backend so normally specifying an ID should not be necessary.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/avision.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-avision.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-avision.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_AVISION</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. The debug level 7 is the author&#8217;s preferred value to debug backend problems. </p>
<p> Example: export SANE_DEBUG_AVISION=7 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5)<br />
 <i><a rel="nofollow" href="http://exactcode.com/site/open_source/saneavision">http://exactcode.com/site/open_source/saneavision</a></i> </p>
<h2>Maintainer</h2>
<p>Ren&eacute; Rebe</p>
<h2>Author</h2>
<p>Ren&eacute; Rebe and Meino Christian Cramer</p>
