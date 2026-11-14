---
title: "sane-hp3500(5)"
name: "sane-hp3500"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hp3500/"
description: "sane-hp3500 – SANE backend for Hewlett-Packard ScanJet 3500 series scanners"
---

<p>sane-hp3500 &#8211; SANE backend for Hewlett-Packard ScanJet 3500 series scanners</p>
<h2>Description</h2>
<p>The <code>sane-hp3500</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard USB flatbed scanners: </p>
<dl>
<dd>ScanJet 3500C<br />
 ScanJet 3530C<br />
 ScanJet 3570C</dl>
<p> If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/proc/bus/usb/devices</i>, <code>sane-find-scanner (1)</code> or syslog) to us. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let us know.</p>
<h2>Configuration</h2>
<p>None required.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp3500.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hp3500.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<p><code>SANE_DEBUG_HP3500</code> If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_HP3500=4</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5),<br />
 <i><a rel="nofollow" href="http://projects.troy.rollo.name/rt-scanners/">http://projects.troy.rollo.name/rt-scanners/</a></i> </p>
<h2>Author</h2>
<p>Troy Rollo &lt;<i>sane [at] troy.rollo.name</i>&gt;</p>
