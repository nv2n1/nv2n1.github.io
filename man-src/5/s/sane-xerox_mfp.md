---
title: "sane-xerox_mfp(5)"
name: "sane-xerox_mfp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-xerox_mfp/"
description: "sane-xerox_mfp – SANE backend for Xerox Phaser 3200MFP device et al."
---

<p>sane-xerox_mfp &#8211; SANE backend for Xerox Phaser 3200MFP device et al.</p>
<h2>Description</h2>
<p>The <code>sane-xerox_mfp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to several Samsung-based Samsung, Xerox, and Dell scanners. Please see full list of supported devices at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i>. </p>
<h2>Configuration</h2>
<dl>
<dt><i>/etc/sane.d/xerox_mfp.conf</i></p>
<dd>USB scanners do not need any configuration. </p>
<p> For SCX-4500W in network mode you need to specify</dl>
<dl>
<dd><code>tcp host_address [port]</code></dl>
<p> The <code>host_address</code> is passed through resolver, thus can be a dotted quad or a name from <i>/etc/hosts</i> or resolvable through DNS.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/xerox_mfp.conf</i></p>
<dd>The backend configuration file. By default all scanner types/models are enabled, you may want to comment out unwanted entries.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-xerox_mfp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-xerox_mfp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_XEROX_MFP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_XEROX_MFP=4 </p>
</dl>
<h2>Limitations</h2>
<p>Multicast autoconfiguration for LAN scanners is not implemented yet. IPv6 addressing has never been tested.</p>
<h2>Bugs And Support</h2>
<p>If you have found a bug or need support please follow open-source way of acquiring support via mail-lists <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> or SANE bug tracker <i><a rel="nofollow" href="http://www.sane-project.org/bugs.html">http://www.sane-project.org/bugs.html</a></i>.</p>
<h2>Authors</h2>
<p>Alex Belkin &lt;<i>abc [at] telekom.ru</i>&gt;.<br />
 Samsung SCX-4500W scan over network support by Alexander Kuznetsov &lt;<i>acca(at)cpan.org</i>&gt;.<br />
 Color scanning on Samsung M2870 model and Xerox Cognac 3215 &amp; 3225 models by Laxmeesh Onkar Markod &lt;<i>m.laxmeesh [at] samsung.com</i>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) </p>
