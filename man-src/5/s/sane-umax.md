---
title: "sane-umax(5)"
name: "sane-umax"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-umax/"
description: "sane-umax – SANE backend for UMAX scanners"
---

<p>sane-umax &#8211; SANE backend for UMAX scanners</p>
<h2>About This File</h2>
<p>This file is only a brief description of the <code>sane-umax</code> backend for SANE! For detailed information take a look at sane-umax-doc.html (it is included in the sane source directory and in the <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) online help)!</p>
<h2>Description</h2>
<p>The <code>sane-umax</code> library implements a SANE backend that provides access to several UMAX-SCSI-scanners and some Linotype Hell SCSI-scanners, parallel- and USB-scanners are not (and probably will never be) supported! <code>I suggest you hold one hand on the power-button of the scanner while you try the first scans!</code> </p>
<h2>Configuration</h2>
<p>The configuration file for this backend resides in <i>/etc/sane.d/umax.conf</i>. </p>
<p> Its contents is a list of device names that correspond to UMAX and UMAX compatible scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<pre> # this is a comment
 #
 option scsi-maxqueue 4
 option scsi-buffer-size-min 65536
 option scsi-buffer-size-max 131072
 option scan-lines 40
 option preview-lines 10
 option scsi-maxqueue 2
 option execute-request-sense 0
 option force-preview-bit-rgb 0
 option slow-speed -1
 option care-about-smearing -1
 option calibration-full-ccd -1
 option calibration-width-offset -1
 option calibration-bytes-pixel -1
 option exposure-time-rgb-bind -1
 option invert-shading-data -1
 option lamp-control-available 0
 option gamma-lsb-padded 0
 /dev/sge
 #scsi Vendor Model Type Bus Channel ID LUN
 # The following scanner supports lamp control
 option lamp-control-available 1
 scsi UMAX * Scanner * * * * *
 # scanner on /dev/scanner does not support lamp control
 option lamp-control-available 0
 /dev/scanner</pre>
<dl>
<dt>execute-request-sense:</p>
<dd>values: 0 = disabled, 1 = enabled<br />
 default = 0<br />
 If set to 1, <code>umax_do_request_sense</code>() is called in <code>umax_do_calibration</code>(). This can hang the system, but has been enabled until this version.</p>
<dt>scsi-buffer-size-min, scsi-buffer-size-max:</p>
<dd>values: 4096-1048576<br />
 default min = 32768, max = 131072<br />
 Especially the minimum value is very important. If this value is set too small the backend is not able to send gamma tables to the scanner or to do a correct color calibration. This may result in strange color effects. If the minimum value is set too large then the backend is not able to allocate the requested SCSI buffer size and aborts with out of memory error. The default is 32KB, for some scanners it should be increased to 64KB.</p>
<dt>scan-lines, preview-lines:</p>
<dd>values: 1-65535<br />
 default: scan-lines = 40, preview-lines = 10<br />
 define the maximum number of lines that are scanned into one buffer</p>
<dt>force-preview-bit-rgb:</p>
<dd>values: 0 = disabled, 1 = enabled<br />
 default = 0<br />
 set preview bit in rgb real scan</p>
<dt>slow-speed, care-about-smearing:</p>
<dd>values: -1 = auto, 0 = disabled, 1 = enabled<br />
 default = -1<br />
 Dangerous options, needed for some scanners.<br />
 Do not change these options unless you really know what you are doing otherwise you may destroy your scanner with invalid values.</p>
<dt>calibration-full-ccd:</p>
<dd>values: -1 = auto, 0 = disabled, 1 = enabled<br />
 default = -1<br />
 do calibration for each pixel of ccd instead of selected image</p>
<dt>calibration-width-offset:</p>
<dd>values: -99999 = auto, &gt; -99999 set value<br />
 add an offset to the calculated width for image/ccd</p>
<dt>calibration-bytes-pixel:</p>
<dd>values: -1 = disabled, 0 = not set, 1 = 1 byte/pixel, 2 = 2 bytes/pixel<br />
 use # bytes per pixel for calibration</p>
<dt>exposure-time-rgb-bind:</p>
<dd>values: -1 = automatically set by driver &#8211; if known, 0 = disabled (own selection for red, green and blue), 1 = enabled (same values for red, green and blue)</p>
<dt>invert-shading-data:</p>
<dd>values: -1 = automatically set by driver &#8211; if known, 0 = disabled, 1 = enabled<br />
 default = -1<br />
 invert shading data before sending it back to the scanner</p>
<dt>lamp-control-available:</p>
<dd>values: 0 = automatically set by driver &#8211; if known, 1 = available<br />
 default = 0</p>
<dt>gamma-lsb-padded:</p>
<dd>values: -1 = automatically set by driver &#8211; if known, 0 = gamma data is msb padded, 1 = gamma data is lsb padded<br />
 default = -1</p>
<dt>handle-bad-sense-error:</p>
<dd>values: 0 = handle as device busy, 1 = handle as ok, 2 = handle as i/o error, 3 = ignore bad error code &#8211; continue sense handler<br />
 default = 0</p>
<dt>scsi-maxqueue:</p>
<dd>values: 1..# (maximum defined at compile time)<br />
 default = 2<br />
 most SCSI drivers allow internal command queueing with a depth of 2 commands. In most cases it does not improve anything when you increase this value. When your SCSI driver does not support any command queueing you can try to set this value to 1. </p>
</dl>
<p> The special device name must be a generic SCSI device or a symlink to such a device. To find out to which device your scanner is assigned and how you have to set the permissions of that device, have a look at <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5).</p>
<h2>Scsi Adapter Tips</h2>
<p>The ISA-SCSI-adapters that are shipped with some UMAX-scanners are not supported very well by Linux (I suggest not to use it), the PCI-SCSI-adapters that come with some UMAX-scanners are not supported at all (as far as I know). On other platforms these SCSI-adapters are not supported. So you typically need to purchase another SCSI-adapter that is supported by your platform. See the relevant hardware FAQs and HOWTOs for your platform for more information. </p>
<p> The UMAX-scanners do block the SCSI-bus for a few seconds while scanning. It is not necessary to connect the scanner to its own SCSI-adapter. But if you need short response time for your SCSI-harddisk (e.g. if your computer is a file-server) or other SCSI devices, I suggest you use an own SCSI-adapter for your UMAX-scanner. </p>
<p> If you have any problems with your UMAX scanner, check your SCSI chain (cable length, termination, &#8230;). </p>
<p> See also: <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5)</p>
<h2>Files</h2>
<dl>
<dt>The backend configuration file:</p>
<dd><i>/etc/sane.d/umax.conf</i></p>
<dt>The static library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-umax.a</i></p>
<dt>The shared library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-umax.so</i> (present on systems that support dynamic loading) </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_UMAX</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. <code>SANE_DEBUG_UMAX</code> values: </p>
<pre>Number Remark
 0 print important errors (printed each time)
 1 print errors
 2 print sense
 3 print warnings
 4 print scanner-inquiry
 5 print information
 6 print less important information
 7 print called procedures
 8 print reader_process messages
 10 print called sane-init-routines
 11 print called sane-procedures
 12 print sane infos
 13 print sane option-control messages</pre>
<dt>Example:</p>
<dd>export SANE_DEBUG_UMAX=8 </p>
</dl>
<h2>Bugs</h2>
<p>X-resolutions greater than 600 dpi sometimes cause problems. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>Oliver Rauch</p>
<h2>Email-Contact</h2>
<p><i>Oliver.Rauch [at] Rauch-Domain.DE</i></p>
