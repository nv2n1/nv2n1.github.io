---
title: "sane-hpljm1005(5)"
name: "sane-hpljm1005"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hpljm1005/"
description: "sane-hpljm1005 – SANE backend for Hewlett-Packard LaserJet M1005 MFP Scanner"
---

<p>sane-hpljm1005 &#8211; SANE backend for Hewlett-Packard LaserJet M1005 MFP Scanner</p>
<h2>Description</h2>
<p>The <code>sane-hpljm1005</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard scanner: </p>
<dl>
<dd>LaserJet M1005</dl>
<p> If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i>, <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to us. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let us know.</p>
<h2>Configuration</h2>
<p>None required.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hpljm1005.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hpljm1005.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_HPLJM1005</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> There is not currently a great deal of diagnostic output, it being mainly confined to error conditions. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) </p>
<h2>Author</h2>
<p>Philippe R&eacute;tornaz &lt;<i>couriousous [at] mandriva.org</i>&gt;</p>
