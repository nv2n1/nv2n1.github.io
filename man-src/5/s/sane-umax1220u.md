---
title: "sane-umax1220u(5)"
name: "sane-umax1220u"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-umax1220u/"
description: "sane-umax1220u – SANE backend for the UMAX Astra 1220U and similar scanners"
---

<p>sane-umax1220u &#8211; SANE backend for the UMAX Astra 1220U and similar scanners</p>
<h2>Description</h2>
<p>The <code>sane-umax1220</code> library implements a SANE (Scanner Access Now Easy) backend for the the UMAX Astra 1220U and similar scanners. For more information on this backend, please visit <i><a rel="nofollow" href="http://umax1220u-sane.sourceforge.net/">http://umax1220u-sane.sourceforge.net/</a></i>. </p>
<h2>Umax Astra 1600U/2000U/2100U Support</h2>
<p>This backend is also able to drive the UMAX Astra 1600U/2000U/2100U. The 2100U is confirmed to work. For the other scanners no reports have been received yet. Please contact us and tell us if your scanner works (<i>sane-devel [at] alioth-lists.debian.net</i>).</p>
<h2>Configuration</h2>
<p>Usually, no manual configuration is necessary. The configuration file for this backend resides in <i>/etc/sane.d/umax1220u.conf</i>. </p>
<p> Its content is a list of device names that correspond to UMAX Astra scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<pre> #usb vendor product
 usb 0x1606 0x0010
 # Device list for non-linux systems
 /dev/scanner
 /dev/usb/scanner0</pre>
<p>See <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) for information on how to set the access permissions on the usb device files.</p>
<h2>Files</h2>
<dl>
<dt>The backend configuration file:</p>
<dd><i>/etc/sane.d/umax1220u.conf</i></p>
<dt>The static library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-umax1220u.a</i></p>
<dt>The shared library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-umax1220u.so</i> (present on systems that support dynamic loading) </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_UMAX1220U</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity: </p>
<p> <code>SANE_DEBUG_UMAX1220U</code> values: </p>
<pre>Number Remark
 1 print failures
 2 print information
 3 print high-level function calls
 4 print high-level function checkpoints
 9 print mid-level function calls
 10 print mid-level function checkpoints
 80 print protocol-level function entry
 90 print protocol-level function exit</pre>
<dt>Example:</p>
<dd>export SANE_DEBUG_UMAX1220U=10 </p>
</dl>
<h2>Known Bugs</h2>
<p>600 dpi scanning may fail for large image sizes. </p>
<p> If you keep getting I/O errors, try cycling the power on your scanner to reset it. </p>
<p> There is no way to cancel a scan, since the driver ignores <code>sane_cancel</code>(). </p>
<p> If you try scanning an image which is too small, you will get I/O errors. Be sure to adjust the scan area before doing a scan, since by default, the scan area is zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5)</p>
<dl>
<dt>(Old) homepage:</p>
<dd><i><a rel="nofollow" href="http://umax1220u-sane.sourceforge.net/">http://umax1220u-sane.sourceforge.net/</a></i> </p>
<h2>Author</h2>
<p>Marcio Luis Teixeira &lt;<i>marciot [at] users.sourceforge.net</i>&gt;</p>
<h2>Email-Contact</h2>
<p><i>sane-devel [at] alioth-lists.debian.net</i></p>
<h2>Reporting Bugs</h2>
<p>This backend isn&#8217;t actively maintained. Nevertheless, bug reports and comments should be sent to the sane-devel mailing list. When reporting bugs, please run the backend with <code>SANE_DEBUG_UMAX1220U</code> set to 10 and attach a copy of the log messages.</p>
